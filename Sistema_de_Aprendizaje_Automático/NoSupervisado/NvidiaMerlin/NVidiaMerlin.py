

# 1. Generar datos sintéticos (usuarios, películas, calificaciones)
np.random.seed(42)
n_users = 1000
n_movies = 500
n_interactions = 10_000

user_ids = np.random.randint(1, n_users, n_interactions)
movie_ids = np.random.randint(1, n_movies, n_interactions)
ratings = np.random.randint(1, 6, n_interactions)  # Calificaciones de 1 a 5

df = cudf.DataFrame({
    "user_id": user_ids,
    "movie_id": movie_ids,
    "rating": ratings
})

# 2. Preprocesamiento con NVTabular
workflow = Workflow(
    cat_names=["user_id", "movie_id"],  # Variables categóricas
    cont_names=["rating"],              # Variables continuas
    label_name=None                     # Sin etiqueta (sistema no supervisado)
)

# Operaciones de preprocesamiento
workflow.add_preprocess(
    FillMissing(fill_val=0) >> Normalize()  # Normalizar ratings
)
workflow.add_preprocess(
    Categorify()  # Codificar user_id y movie_id
)

# Aplicar workflow y guardar datos procesados
workflow.fit(df)
processed_df = workflow.transform(df)
processed_df.to_parquet("processed_data.parquet")

# 3. Definir y entrenar modelo con HugeCTR
solver_config = solver_parser_helper(
    max_iter=1000,
    batchsize=2048,
    lr=0.001,
    snapshot=100,
    display=10
)

model_config = {
    "layers": [
        {
            "name": "input",
            "type": "Data",
            "source": "processed_data.parquet",
            "format": "Parquet",
            "num_samples": n_interactions,
            "label": {"top": "label"},
            "dense": {"top": "features_dense"},
            "sparse": [
                {"top": "user_id", "max_feature_num": n_users},
                {"top": "movie_id", "max_feature_num": n_movies}
            ]
        },
        {
            "name": "embedding",
            "type": "Embedding",
            "bottom": ["user_id", "movie_id"],
            "top": ["user_emb", "movie_emb"],
            "embedding_vec_size": 16
        },
        {
            "name": "interaction",
            "type": "Interaction",
            "bottom": ["user_emb", "movie_emb"],
            "top": "interaction"
        },
        {
            "name": "fc",
            "type": "InnerProduct",
            "bottom": "interaction",
            "top": "fc",
            "num_output": 1
        }
    ]
}

# Inicializar sesión y entrenar
sess = Session()
sess.init(solver_config, model_config)
sess.train()