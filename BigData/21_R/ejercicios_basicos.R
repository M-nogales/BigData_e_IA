# =============================
# 🟢 Ejercicios Básicos
# =============================

# Calculadora simple
3 + 5 * 2
10^2
sqrt(144)
log(pi)

# Asignación de variables
a <- 100
print(a)
a <- a + 50
print(a)

# Vectores numéricos
v <- c(10, 20, 30, 40, 50)
length(v)
v * 2
v + 5

# Funciones elementales
mean(v)
sum(v)
min(v)
max(v)
sd(v)

# Insertar NA
v[3] <- NA
mean(v)
# [1] NA
mean(v, na.rm = TRUE)
# [1] 30

# Indexación básica
v <- c(10, 20, 30, 40, 50)
v[3]
v[2:4]

# Operaciones lógicas
w <- c(5, 15, 25, 35, 45)
sel <- w > 20
w[sel]
which(w == 25)

# Redondeo
round(pi, 0)
round(pi, 1)
round(pi, 3)

# Secuencias y repeticiones
seq(0, 1, by = 0.2)
rep(1:3, each = 4)

# Uso de paste
paste("Hola", "mundo")
paste0("Hola", "mundo")

# Primer histograma
v <- rnorm(100)
hist(v)

# =============================
# 🟡 Ejercicios Intermedios
# =============================

# Cuantiles y resumen
# quantile(v) y summary(v) indican los quartiles del vector 
# y metodos comunes
v <- rnorm(200)
quantile(v)
summary(v)

# Ordenación y rangos
w <- sample(1:20, 10)
sort(w)
sort(w, decreasing = TRUE)
order(w)
rank(w, ties.method = "min")

# Manejo de NA
u <- c(NA, 2, NA, 5, 8, NA)
sum(is.na(u))
u[!is.na(u)]

# Tablas y frecuencias
colores <- factor(c("rojo", "azul", "rojo", "verde", "azul"))
table(colores)

# Matrices y apply
m <- matrix(1:12, nrow = 3, byrow = TRUE)
apply(m, 1, sum)
apply(m, 2, mean)

# Listas
l <- list(nombre = "Ana", edades = c(20, 30, 40), activo = TRUE)
l$nombre
l$edades[2]

# Data frame simple
df <- data.frame(id = 1:5, score = rnorm(5))
df$passed <- df$score > 0
df

# Funciones propias
f <- function(x) x^2 + 2*x + 1
f(5)
sapply(1:10, f)

# Control de flujo
for (i in 1:10) {
  cat(i, ":", factorial(i), "\n")
}

i <- 1
f <- 1
while (f <= 1e5) {
  f <- factorial(i)
  cat(i, ":", f, "\n")
  i <- i + 1
}

# Factores ordenados
talla <- factor(c("S", "M", "L", "M", "S"), levels = c("S", "M", "L"), ordered = TRUE)
talla > "M"

# =============================
# 🔴 Ejercicios Avanzados
# =============================

# tapply en agrupaciones
df <- data.frame(grupo = rep(LETTERS[1:3], each = 5), valor = rnorm(15))
tapply(df$valor, df$grupo, mean)

# Funciones anónimas
sapply(1:5, function(x) ifelse(x %% 2 == 0, "par", "impar"))

# Expresiones regulares
text <- "Visita http://example.com y https://r-project.org"
gsub("http[s]?://[^ ]+", "", text)

# cut y cuantiles
v <- rnorm(100)
cut(v, breaks = quantile(v), labels = FALSE, include.lowest = TRUE)

# Fechas y horas
fecha <- as.Date("21/04/2025", "%d/%m/%Y")
fecha + 30
Sys.Date() - fecha

# Complejos y módulo
z <- 3 + 4i
Mod(z)
Arg(z)
plot(Re(z), Im(z), xlim = c(0,5), ylim = c(0,5), xlab = "Re", ylab = "Im", main = "Número complejo", pch = 19)

# Pila con Reference Class
Stack <- setRefClass("Stack",
                     fields = list(items = "list"),
                     methods = list(
                       initialize = function() items <<- list(),
                       put = function(x) items <<- c(items, list(x)),
                       pop = function() {
                         val <- tail(items, 1)[[1]]
                         items <<- items[-length(items)]
                         return(val)
                       },
                       size = function() length(items)
                     )
)

s <- Stack$new()
s$put(10)
s$put(20)
s$size()
s$pop()

# Histogramas avanzados
v <- rnorm(1000)
hist(v, breaks = 10, main = "10 bins")
hist(v, breaks = 50, main = "50 bins")

# Vectorización vs bucles
x <- 1:1e6

start <- Sys.time()
sapply(x, function(x) x^3 + x^2 + 1/(x + 10))
Sys.time() - start

start <- Sys.time()
res <- numeric(length(x))
for (i in seq_along(x)) {
  res[i] <- x[i]^3 + x[i]^2 + 1/(x[i] + 10)
}
Sys.time() - start

# Función de orden superior
dualize <- function(f) function(x) f(f(x))
d_sqrt <- dualize(sqrt)
d_sqrt(16)

d_log <- dualize(log)
d_log(10)
