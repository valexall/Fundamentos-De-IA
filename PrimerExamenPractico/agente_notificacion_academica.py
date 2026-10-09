
import smtplib
import re
from datetime import datetime, timedelta
from email.mime.text import MIMEText

# Datos del estudiante
estudiante_nombre = 'Valentin Arenaza'
estudiante_correo = '231155@unamba.edu.pe'

# Datos del profesor
profesor_nombre = 'ing. Yonatan'
profesor_correo = 'ajua@gmail.com'

# Datos del evento academico
evento_titulo      = 'SIMBIG'
evento_tipo        = 'congreso'
evento_fecha       = datetime.now() + timedelta(days=10)
evento_modalidad   = 'presencial'
evento_prioridad   = 'alta'
evento_descripcion = 'Presentacion de ponencias de investigacion cientifica.'


def correo_valido(correo: str) -> bool:
    """Verifica que el correo tenga un formato valido."""
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$', correo))


def evento_valido(tipo: str, fecha: datetime, prioridad: str):
    """
    Verifica que el evento sea de un tipo conocido,
    que aun no haya ocurrido y que tenga una prioridad valida.
    Retorna (bool, str).
    """
    tipos_ok       = ['congreso', 'seminario', 'tesis', 'publicacion', 'beca']
    prioridades_ok = ['alta', 'media', 'baja']

    if tipo not in tipos_ok:
        return False, f'Tipo de evento invalido: {tipo}'
    if fecha < datetime.now():
        return False, 'El evento ya ocurrio'
    if prioridad not in prioridades_ok:
        return False, f'Prioridad invalida: {prioridad}'
    return True, 'OK'


errores = []

if not correo_valido(estudiante_correo):
    errores.append(f'Correo del estudiante invalido: {estudiante_correo}')

if not correo_valido(profesor_correo):
    errores.append(f'Correo del profesor invalido: {profesor_correo}')

ok_evento, msg_evento = evento_valido(evento_tipo, evento_fecha, evento_prioridad)
if not ok_evento:
    errores.append(msg_evento)

dias_restantes = (evento_fecha - datetime.now()).days

print('=== PERCEPCION ===')
print(f'Correo estudiante valido : {correo_valido(estudiante_correo)}')
print(f'Correo profesor valido   : {correo_valido(profesor_correo)}')
print(f'Evento valido            : {ok_evento}')
print(f'Dias para el evento      : {dias_restantes}')
if errores:
    print(f'Errores encontrados      : {errores}')


# Reglas de anticipacion minima segun prioridad
anticipacion_minima = {'alta': 1, 'media': 3, 'baja': 7}

# Reglas de destinatarios segun tipo de evento
destinatarios_por_tipo = {
    'congreso':    ['estudiante', 'profesor'],
    'seminario':   ['estudiante', 'profesor'],
    'tesis':       ['estudiante', 'profesor'],
    'publicacion': ['profesor'],
    'beca':        ['estudiante'],
}

# Tomar decision
notificar     = False
razon         = ''
destinatarios = []

if errores:
    razon = 'Datos invalidos: ' + ', '.join(errores)

elif dias_restantes < anticipacion_minima[evento_prioridad]:
    razon = (
        f'El evento es en {dias_restantes} dia(s), '
        f'pero prioridad {evento_prioridad!r} requiere '
        f'{anticipacion_minima[evento_prioridad]} dia(s) minimo.'
    )

else:
    notificar = True
    razon = f'Evento valido. {dias_restantes} dia(s) restantes. Prioridad: {evento_prioridad.upper()}.'
    roles = destinatarios_por_tipo[evento_tipo]
    if 'estudiante' in roles:
        destinatarios.append((estudiante_nombre, estudiante_correo))
    if 'profesor' in roles:
        destinatarios.append((profesor_nombre, profesor_correo))

print('\n=== RAZONAMIENTO ===')
print(f'Decision      : {"NOTIFICAR" if notificar else "NO NOTIFICAR"}')
print(f'Razon         : {razon}')
if destinatarios:
    for nombre, correo in destinatarios:
        print(f'  Destinatario: {nombre} ({correo})')



def generar_correo(nombre_dest: str):
    """
    Genera el asunto y cuerpo del correo para un destinatario dado.
    Retorna (asunto: str, cuerpo: str).
    """
    fecha_str = evento_fecha.strftime('%d/%m/%Y %H:%M')
    asunto = f'[UNAMBA] {evento_tipo.capitalize()}: {evento_titulo}'
    cuerpo = (
        f'Estimado/a {nombre_dest},\n\n'
        f'Le informamos sobre el siguiente evento academico:\n\n'
        f'  Titulo      : {evento_titulo}\n'
        f'  Tipo        : {evento_tipo.capitalize()}\n'
        f'  Fecha       : {fecha_str}\n'
        f'  Modalidad   : {evento_modalidad.capitalize()}\n'
        f'  Prioridad   : {evento_prioridad.upper()}\n'
        f'  Dias rest.  : {dias_restantes}\n'
        f'  Descripcion : {evento_descripcion}\n\n'
        f'Participantes:\n'
        f'  Estudiante  : {estudiante_nombre} ({estudiante_correo})\n'
        f'  Profesor    : {profesor_nombre} ({profesor_correo})\n\n'
        f'Atentamente,\n'
        f'Agente de Notificaciones Academicas - UNAMBA\n'
    )
    return asunto, cuerpo


if notificar:
    asunto_ejemplo, cuerpo_ejemplo = generar_correo('(nombre del destinatario)')
    print('\n=== VISTA PREVIA DEL CORREO ===')
    print(f'Asunto: {asunto_ejemplo}')
    print('---')
    print(cuerpo_ejemplo)



enviar_correo = True  

if notificar and enviar_correo:
    remitente = 'telloleonricardo@gmail.com'
    password  = 'kkwg dnth gfhu yflt'  

    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login(remitente, password)

    for nombre, correo in destinatarios:
        asunto, cuerpo = generar_correo(nombre)
        msg = MIMEText(cuerpo, 'plain', 'utf-8')
        msg['From']    = remitente
        msg['To']      = correo
        msg['Subject'] = asunto
        servidor.sendmail(remitente, correo, msg.as_string())
        print(f'Correo enviado a: {nombre} ({correo})')

    servidor.quit()
    print('Todos los correos fueron enviados.')

elif not notificar:
    print('No se envia: el agente decidio no notificar.')

else:
    print('enviar_correo = False. Activa la variable para enviar.')
