% =============================================================================
% Base de conocimiento para diagnóstico médico
% =============================================================================
% Fuentes:
%   - OMS (Organización Mundial de la Salud): https://www.who.int/es/news-room/fact-sheets
%   - CDC (Centers for Disease Control and Prevention): https://www.cdc.gov/
%   - Mayo Clinic: https://www.mayoclinic.org/
%   - PAHO (Organización Panamericana de la Salud): https://www.paho.org/
%
% AVISO: Este sistema es solo un simulador con fines educativos.
%        No reemplaza el diagnóstico de un profesional médico.
% =============================================================================

% --- ENFERMEDADES RESPIRATORIAS ---

% Resfriado común
% Fuente: CDC - https://www.cdc.gov/common-cold/
% Síntomas: congestión/goteo nasal, estornudos, dolor de garganta, tos leve,
%           malestar general, fiebre leve, dolor de cabeza leve.
enfermedad(resfriado_comun, [
    congestion_nasal,
    estornudos,
    dolor_garganta,
    tos_leve,
    malestar_general,
    fiebre_baja,
    dolor_cabeza_leve
]).

% Gripe (Influenza estacional)
% Fuente: OMS - https://www.who.int/es/news-room/fact-sheets/detail/influenza-(seasonal)
% Síntomas: inicio súbito de fiebre alta, tos, dolor de garganta, dolores
%           musculares/corporales, fatiga intensa, escalofríos, dolor de cabeza.
enfermedad(gripe_influenza, [
    fiebre_alta,
    tos,
    dolor_garganta,
    dolor_muscular,
    fatiga_intensa,
    escalofrios,
    dolor_cabeza
]).

% Neumonía
% Fuente: CDC - https://www.cdc.gov/pneumonia/
% Síntomas: fiebre alta, tos con flema/moco, dificultad para respirar,
%           dolor en el pecho al respirar, escalofríos, fatiga.
enfermedad(neumonia, [
    fiebre_alta,
    tos_con_flema,
    dificultad_respirar,
    dolor_pecho,
    escalofrios,
    fatiga_intensa
]).

% COVID-19
% Fuente: OMS - https://www.who.int/es/emergencies/diseases/novel-coronavirus-2019
%         CDC - https://www.cdc.gov/covid/
% Síntomas más comunes: fiebre, tos seca, pérdida de olfato, pérdida del gusto,
%                       dificultad respiratoria, fatiga, dolor muscular.
enfermedad(covid19, [
    fiebre_alta,
    tos_seca,
    perdida_olfato,
    perdida_gusto,
    dificultad_respirar,
    fatiga_intensa,
    dolor_muscular
]).

% --- ENFERMEDADES TRANSMITIDAS POR VECTORES ---

% Dengue
% Fuente: OMS - https://www.who.int/es/news-room/fact-sheets/detail/dengue-and-severe-dengue
%         PAHO - https://www.paho.org/es/temas/dengue
% Síntomas: fiebre alta repentina, dolor de cabeza intenso, dolor retroocular
%           (detrás de los ojos), dolores musculares y articulares, náuseas,
%           erupción cutánea (sarpullido).
enfermedad(dengue, [
    fiebre_alta,
    dolor_cabeza_intenso,
    dolor_retroocular,
    dolor_muscular,
    dolor_articular,
    nauseas,
    erupcion_cutanea
]).

% --- ENFERMEDADES INFECCIOSAS ---

% Tuberculosis (TB Pulmonar)
% Fuente: OMS - https://www.who.int/es/news-room/fact-sheets/detail/tuberculosis
% Síntomas de TB activa: tos persistente (>2 semanas), esputo con sangre,
%                        dolor torácico, debilidad/cansancio, pérdida de peso,
%                        fiebre, sudores nocturnos.
enfermedad(tuberculosis, [
    tos_persistente,
    esputo_con_sangre,
    dolor_pecho,
    debilidad,
    perdida_de_peso,
    fiebre_baja,
    sudores_nocturnos
]).

% Gastroenteritis (infección estomacal)
% Fuente: CDC - https://www.cdc.gov/norovirus/
%         Mayo Clinic - https://www.mayoclinic.org/diseases-conditions/viral-gastroenteritis/
% Síntomas: náuseas, vómitos, diarrea acuosa, dolor/cólicos abdominales,
%           fiebre leve, malestar general.
enfermedad(gastroenteritis, [
    nauseas,
    vomitos,
    diarrea,
    dolor_abdominal,
    fiebre_baja,
    malestar_general
]).

% --- ENFERMEDADES NEUROLÓGICAS ---

% Migraña
% Fuente: Mayo Clinic - https://www.mayoclinic.org/diseases-conditions/migraine-headache/
% Síntomas: dolor de cabeza intenso y pulsátil (generalmente un lado),
%           sensibilidad a la luz (fotofobia), sensibilidad al sonido (fonofobia),
%           náuseas, vómitos, visión borrosa o aura visual antes del dolor.
enfermedad(migrana, [
    dolor_cabeza_intenso,
    sensibilidad_luz,
    sensibilidad_ruido,
    nauseas,
    vomitos,
    vision_borrosa
]).

% --- ENFERMEDADES DE LA SANGRE Y CARDIOVASCULARES ---

% Anemia
% Fuente: Mayo Clinic - https://www.mayoclinic.org/diseases-conditions/anemia/
% Síntomas: fatiga, palidez, mareos, debilidad, dificultad para respirar
%           con el esfuerzo, palpitaciones, manos y pies fríos.
enfermedad(anemia, [
    fatiga_intensa,
    palidez,
    mareos,
    debilidad,
    dificultad_respirar,
    palpitaciones,
    extremidades_frias
]).

% Hipertensión arterial (presión alta)
% Fuente: OMS - https://www.who.int/es/news-room/fact-sheets/detail/hypertension
% Nota: La mayoría de veces es asintomática. Cuando hay síntomas pueden ser:
%       dolor de cabeza (nuca), visión borrosa, dolor en el pecho,
%       dificultad para respirar (en casos graves).
enfermedad(hipertension_arterial, [
    dolor_cabeza,
    vision_borrosa,
    dolor_pecho,
    dificultad_respirar,
    palpitaciones
]).

% =============================================================================
% REGLAS DEL MOTOR DE INFERENCIA
% =============================================================================

% Calcular cuántos síntomas del usuario coinciden con los de una enfermedad
contar_coincidencias([], _, 0).
contar_coincidencias([S|Resto], SintomasUsuario, N) :-
    member(S, SintomasUsuario),
    !,
    contar_coincidencias(Resto, SintomasUsuario, N1),
    N is N1 + 1.
contar_coincidencias([_|Resto], SintomasUsuario, N) :-
    contar_coincidencias(Resto, SintomasUsuario, N).

% Regla principal: diagnosticar basado en número de síntomas coincidentes.
% Devuelve la enfermedad y la cantidad de síntomas que coinciden.
diagnosticar(Enfermedad, SintomasUsuario, Coincidencias) :-
    enfermedad(Enfermedad, SintomasEnfermedad),
    contar_coincidencias(SintomasEnfermedad, SintomasUsuario, Coincidencias),
    Coincidencias > 0. % Al menos un síntoma debe coincidir

% Listar todos los síntomas posibles (para poblar la interfaz de usuario)
sintomas_posibles(Sintomas) :-
    findall(S, (enfermedad(_, L), member(S, L)), TodosSintomas),
    sort(TodosSintomas, Sintomas). % sort elimina duplicados y ordena alfabéticamente
