import amino
import random
from time import sleep

chat_bots = "23e2ffc7-592a-45dd-a2d8-e54c187a5a2b"
chat_general_hacking = '03ee80fc-71b4-424e-a9cb-95b89f328a35'
chat_general_jardin = 'ffeb3972-5c21-4925-a383-e1c84869f690'
chat_lobby_erajurasica = '69688ab3-20cc-4b24-948d-532806c805cc'
chat_isla_tartaros = '64ce2b86-e4a1-42c8-bc7e-95a1e976199e'
libros_nhul = 'f0fbc677-d167-44e3-ab0c-e0d9472db41d'
chat_general_nahul = 'd9dfdf17-f4ec-48b1-8c67-f3b9a108fcec'


creds = {
    'email':"cifehij223@geekale.com",
    'password':"thothbotG36"
}

print()
print('=========')
print('THOTH-BOT')
print('=========')

client = amino.Client()
client.login(**creds)
print()
print("Logged in as", client.profile.nickname)
print()
comunidad = int(input('Comunidad: 1 = Hackig Utils / 2 = Jardin / 3 = Nahul / 4 = Era jurasica -->> '))
if comunidad == 1:
    comid = '234960818'
elif comunidad == 2:
    comid = '229260151'
elif comunidad == 3:
    comid = '25618756'
elif comunidad == 4:
    comid = '260391359'

subclient = amino.SubClient(comId=comid, profile=client.profile)

print()
print('Loged into comunity')

#FUNCIONES
#===============================================================================================
def enviando_mensaje():
    print('Enviando mensaje...')

def enviar_mensaje(mensaje, tipo):
    subclient.send_message(message=mensaje, messageType=tipo, chatId=chat_general_hacking)

def echo(split_mensaje):
    tipo = split_mensaje[-1]
    print(tipo)

    if tipo == '0':
        del split_mensaje[0]
        del split_mensaje[-1]
        print(split_mensaje)
        string_env = ' '.join(split_mensaje)
        print(string_env)
        enviando_mensaje()
        enviar_mensaje(string_env, 0)

    elif tipo == '109':
        del split_mensaje[0]
        del split_mensaje[-1]
        string_env = ' '.join(split_mensaje)
        enviando_mensaje()
        enviar_mensaje(string_env, 109)
    else:
        del split_mensaje[0]
        string_env = ' '.join(split_mensaje)
        enviando_mensaje()
        enviar_mensaje(string_env, 0)

def get_help():
    try:
        help = open('help.txt', 'r')
        help = help.read()
        enviando_mensaje()
        enviar_mensaje(help, 0)
        help.close()
    except:
        help.close()

def give_user_info(userId):
    pass
    #print(get_user_info(self, u))

def check_functions(mensaje):
    mensaje = mensaje[2:]

    split_mensaje = mensaje.split()
    if split_mensaje[0] == 'echo':
        echo(split_mensaje)

    elif split_mensaje[0] == 'ping':
        enviar_mensaje('pong', 0)

    elif split_mensaje[0] == 'active':
        enviar_mensaje('active = True', 0)

    elif split_mensaje[0] == 'help':
        get_help()

    elif split_mensaje[0] == ' ':
        pass

    elif split_mensaje[0] == 'creador':

        enviar_mensaje('Mi creador es unen', 0)
    else:
        enviar_mensaje('El comando no fue reconocido -> //help para una lista de los comandos', 0)

#MAIN
#===============================================================================================

enviar_mensaje('thothbot conected to chat', 109)

@client.event('on_text_message')
def on_text_message(data):
    print(f'{data.message.author.nickname}: {data.message.content}')
    if data.message.content[:2] == '//':
        check_functions(data.message.content)
    else:
        return


@client.event('on_group_member_join')
def on_group_member_join(data):
    enviando_mensaje()
    enviar_mensaje(f'bienvenid@, <$@{data.message.author.nickname}$>.', 0)



#ComID ---> client.search_community('aminoID').comId[0]
#ComID's --->> Hacking Utils: 234960818  //  Jardín : 229260151  //  Era Jurásica : 260391359 // FundacionNHUL : 25618756
