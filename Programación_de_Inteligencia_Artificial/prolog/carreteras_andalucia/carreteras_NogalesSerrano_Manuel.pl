% -----------------------
% Datos: carretera(Origen, Destino, Kilometros)
% -----------------------

carretera(sevilla, dos_hermanas, 15).
carretera(sevilla, utrera, 31).
carretera(sevilla, cordoba, 140).
carretera(sevilla, cadiz, 122).
carretera(sevilla, jerez_de_la_frontera, 90).
carretera(sevilla, huelva, 94).
carretera(sevilla, malaga, 205).
carretera(dos_hermanas, jerez_de_la_frontera, 85).
carretera(cordoba, granada, 166).
carretera(cordoba, jaen, 110).
carretera(cordoba, malaga, 165).
carretera(jerez_de_la_frontera, cadiz, 35).
carretera(jerez_de_la_frontera, san_fernando, 45).
carretera(cadiz, san_fernando, 15).
carretera(cadiz, chiclana_de_la_frontera, 24).
carretera(san_fernando, chiclana_de_la_frontera, 15).
carretera(jerez_de_la_frontera, la_linea_de_la_concepcion, 110).
carretera(la_linea_de_la_concepcion, algeciras, 20).
carretera(almeria, el_ejido, 31).
carretera(almeria, roquetas_de_mar, 26).
carretera(el_ejido, roquetas_de_mar, 19).
carretera(granada, motril, 65).
carretera(granada, jaen, 97).
carretera(jaen, linares, 34).
carretera(malaga, marbella, 60).
carretera(marbella, mijas, 30).
carretera(malaga, velez_malaga, 35).
carretera(sanlucar_de_barrameda, jerez_de_la_frontera, 26).
carretera(utrera, sanlucar_de_barrameda, 70).
carretera(huelva, sanlucar_de_barrameda, 75).

% -----------------------
% Regla para conexión bidireccional
% -----------------------
conectado(X, Y, D) :- carretera(X, Y, D).
conectado(X, Y, D) :- carretera(Y, X, D).

% -----------------------
% Ruta con acumulación de distancia
% -----------------------

ruta(Inicio, Fin, Ruta, DistTotal) :-
    ruta_aux(Inicio, Fin, [Inicio], RutaInvertida, 0, DistTotal),
    reverse(RutaInvertida, Ruta).

% Caso base: hemos llegado al destino
ruta_aux(Fin, Fin, Ruta, Ruta, Dist, Dist).

% Recursivo: explora caminos evitando ciclos
ruta_aux(Actual, Fin, Visitados, RutaFinal, DistAcum, DistTotal) :-
    conectado(Actual, Siguiente, Distancia),
    \+ member(Siguiente, Visitados),
    NuevoDist is DistAcum + Distancia,
    ruta_aux(Siguiente, Fin, [Siguiente|Visitados], RutaFinal, NuevoDist, DistTotal).
