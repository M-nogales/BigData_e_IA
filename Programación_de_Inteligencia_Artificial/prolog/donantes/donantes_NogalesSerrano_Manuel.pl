% ---------------------
% Hechos: donante(Persona, Grupo, Rh)
% ---------------------

donante(persona(juan, campos, ruiz), a, positivo).
donante(persona(ana, lara, silva), ab, negativo).
donante(persona(luis, luna, pachecho), ab, negativo).
donante(persona(carla, rodriguez, mora), o, positivo).
donante(persona(pedro, garcia, lopez), o, negativo).

% ---------------------
% Reglas de compatibilidad sanguínea
% ---------------------

% Factores RH
compatible_rh(negativo, negativo).
compatible_rh(positivo, positivo).
compatible_rh(negativo, positivo).  % negativo puede donar a positivo

% Grupos sanguíneos
compatible_grupo(o, _).
compatible_grupo(a, a).
compatible_grupo(a, ab).
compatible_grupo(b, b).
compatible_grupo(b, ab).
compatible_grupo(ab, ab).

% Regla general: ¿Puede X donar a Y?
puede_donar_a(donante(_, Grupo1, Rh1), donante(_, Grupo2, Rh2)) :-
    compatible_grupo(Grupo1, Grupo2),
    compatible_rh(Rh1, Rh2).

% ---------------------
% Contar donantes por grupo y RH
% ---------------------

contar_por_grupo_y_factor(Grupo, Rh, N) :-
    findall(1, donante(_, Grupo, Rh), Lista),
    length(Lista, N).

% ---------------------
% Escribir donantes a fichero por grupo y RH
% ---------------------

exportar_donantes(Grupo, Rh, NombreArchivo) :-
    open(NombreArchivo, write, Stream),
    forall(donante(persona(Nombre, Ap1, Ap2), Grupo, Rh),
        (
            format(Stream, '~w ~w ~w~n', [Nombre, Ap1, Ap2])
        )),
    close(Stream),
    format("Donantes exportados a ~w correctamente.~n", [NombreArchivo]).

% ---------------------
% Regla que interactúa con el usuario
% ---------------------

solicitar_y_exportar :-
    write('Introduce grupo sanguineo (a, b, ab, o): '),
    read(Grupo),
    write('Introduce factor RH (positivo o negativo): '),
    read(Rh),
    write('Introduce el nombre del archivo (con extensión): '),
    read(NombreArchivo),
    exportar_donantes(Grupo, Rh, NombreArchivo).
