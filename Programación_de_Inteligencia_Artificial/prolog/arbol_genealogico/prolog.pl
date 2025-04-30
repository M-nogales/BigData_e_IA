% -------- Hechos --------

% Género
hombre(juan).
hombre(luis).
hombre(jorge).
hombre(ricardo).
hombre(carlos).
hombre(eduardo).
hombre(pedro).
hombre(alejandro).
hombre(sebastian).
hombre(daniel).

mujer(maria).
mujer(ana).
mujer(laura).
mujer(sofia).
mujer(clara).
mujer(lucia).
mujer(elena).
mujer(valentina).
mujer(paula).
mujer(isabel).

% Matrimonios
matrimonio(juan, maria).
matrimonio(luis, ana).
matrimonio(jorge, laura).
matrimonio(ricardo, sofia).
matrimonio(carlos, clara).
matrimonio(eduardo, lucia).
matrimonio(pedro, elena).

% Parentescos: padre/madre
padre(juan, luis).
padre(juan, jorge).
padre(juan, ricardo).
padre(luis, carlos).
padre(jorge, eduardo).
padre(ricardo, pedro).
padre(carlos, alejandro).
padre(eduardo, valentina).
padre(pedro, daniel).

madre(maria, luis).
madre(maria, jorge).
madre(maria, ricardo).
madre(ana, carlos).
madre(laura, eduardo).
madre(sofia, pedro).
madre(clara, alejandro).
madre(lucia, valentina).
madre(elena, daniel).

% -------- Reglas --------

% Esposos (bidireccional)
esposo(X, Y) :- matrimonio(X, Y).
esposo(X, Y) :- matrimonio(Y, X).

% Hijo/a
hijo(X, Y) :- padre(Y, X).
hijo(X, Y) :- madre(Y, X).

% Hermano/a
hermano(X, Y) :-
    padre(P, X), padre(P, Y),
    madre(M, X), madre(M, Y),
    X \= Y.

% Abuelo/a
abuelo(X, Y) :- padre(X, P), padre(P, Y).
abuelo(X, Y) :- padre(X, P), madre(P, Y).
abuela(X, Y) :- madre(X, P), padre(P, Y).
abuela(X, Y) :- madre(X, P), madre(P, Y).

% Nieto/a
nieto(X, Y) :- abuelo(Y, X).
nieta(X, Y) :- abuela(Y, X).

% Primo/a
primo(X, Y) :-
    padre(P1, X), padre(P2, Y),
    hermano(P1, P2),
    X \= Y.
primo(X, Y) :-
    madre(P1, X), madre(P2, Y),
    hermana(P1, P2),
    X \= Y.

% Hermana
hermana(X, Y) :-
    padre(P, X), padre(P, Y),
    madre(M, X), madre(M, Y),
    mujer(X), X \= Y.