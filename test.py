import amino
import asyncio

async def main():
    client = amino.Client()
    await client.login(email="cirod56183@flmcat.com", password="sP620j786Hwz")
    subclient = await amino.SubClient(aminoId=client.search_community('ProgramacionDesde0').comId[0], profile=client.profile)

    await subclient.send_message(chatId="6dc520ba-bf55-41fe-849a-27d0cdce55fe", message="MESSAGE")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
