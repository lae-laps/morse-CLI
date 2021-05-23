c # SETUP
REFRESHTIME = 300
import amino
import re
import requests

funciones = ["say", "enviar_mensaje", "img", "get_timezone", "help"]


# ==================================================================
# Logg In
general = "03ee80fc-71b4-424e-a9cb-95b89f328a35"
chatID = "23e2ffc7-592a-45dd-a2d8-e54c187a5a2b"

creds = {
    'email':"lociro3228@ezeca.com",
    'password':"vivaelemperah"
}
client = amino.Client()
client.login(**creds)
print()
print("Logged in as ", client.profile.nickname)
print()
subclient = amino.SubClient(comId="234960818", profile=client.profile)

# =======================================================================
# Funciones


# Envía un mensaje solo si es ejecutada por el código en si
def enviar_mensaje(mensaje, chatID=chatID):
    try:
        SubClient.send_message(message=mensaje, chatId=chatID)
    except Exception:
        print("Ocurrió un ERROR. El mensaje no pudo ser enviado")

# Manda un mensaje con lo que se le pida por un usuario
def say(mensaje):
    enviar_mensaje(mensaje=mensaje)

# Devuelve una imagen a partir de su referencia
def img(ref):
    global img_ref
    if ref in img_ref:
        for x in img_ref:
            if x == ref:
                return x
            else:
                continue
    else:
        enviar_mensaje("Referencia no encontrada")
        print("Referencia no encontrada")

def get_timezone(pais):
    global paises
    global iniciales
    pais = pais.lower()
    for x in paises:
        if pais == x:
            i = paises.index(x)
            inicial = iniciales[i]
            url = "http://api.timezonedb.com/v2.1/list-time-zone?key=6NDWSGIY5BCN&format=json&country="
            url = url + inicial
            response = requests.get(url)
            print(response.status_code)
            print(response.json())
            break
        else:
            continue
    if pais not in paises:
        enviar_mensaje("zona horaria no encontrada")


# Hace operaciones matemáticas con mensajes enviados
def sumar(inn):
    x = inn.split()
    if "+" in x:
        out = int(x)
        sum(out)
        enviar_mensaje(out)

# Devuelve un mensaje con información acerca de las demás funciones del bot
def help():
    try:
        help = open("get_help.txt", "r")
        if help.mode == "r":
            help = help.read()
            enviar_mensaje(mensaje=help)
        else:
            print("No se pudo abrir correctamente el fichero")
    finally:
        help.close()

# Sabe si un mensaje enviado que empieze con "//" corresponde a alguna función
def check_conditions(mensaje):
    global funciones
    for check in funciones:
        if mensaje == check:
            funcion = check
            return funcion
        else:
            continue
    if check not in funciones:
        print("La función no fué encontrada")
        return "La función no fué encontrada"

# Aplica la funcion que corresponde
def apply_conditions(funcion):
    contrast1 = "^//get_timezone"
    contrast2 = "^//say"
    contrast3 = "//img"

    result = re.match(contrast1, funcion)
    if result:
        pais = funcion[+16:]
        get_timezone(pais)
    else:
        pass

    result = re.match(contrast2, funcion)
    if result:
        to_say = say[+7:]
        say(to_say)
    else:
        pass

    result = re.match(contrast3, funcion)
    if result:
        img = result[+7:]
        img()

    if funcion == "//help":
        help()

# ====================================================================
# Recoge mensajes externos

@client.callbacks.event('on_text_message')
def on_text_message(data):
    incoming = data.message.content
    print(incoming)
    if incoming[0] != "/":
        return
    else:
        condition = check_conditions(incoming)
        apply_conditions(condition)


    #msg.update(chatId=data.message.chatId)
    #enviar_mensaje(data.comId, msg)

#@client.callbacks.event('on_group_member_join')
#def on_group_member_join(data):
 #   message = f"Bienvenid@ al chat, <$@{data.message.author.nickname}$>."
  #  msg = {
   #     'message': sanitize(message),
    #    'chatId': data.message.chatId,
     #   'mentionUserIds': [data.message.author.userId]
    #}
    #send_message(data.comId, msg)
