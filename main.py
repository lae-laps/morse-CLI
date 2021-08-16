import amino
import curses
from os import listdir, _exit
from re import match
from getpass import getpass
from menu import menu
from curses.textpad import rectangle

class Pos:
    def __init__(self, stdscr):
        self.y, self.x = stdscr.getmaxyx()
        self.y -= 1
        self.x -= 1
        self.ceny = self.y//2
        self.cenx = self.x//2


def lambdas(x, a):
    return lambda: x(*a)

def logout():
    client.logout()
    curses.endwin()
    _exit(0)

def joincom(stdscr):
    stdscr.move(8,0);stdscr.clrtobot()
    while True:
        stdscr.addstr(max.ceny-3, max.cenx-34//2, "Ingresa el aminoId de la comunidad")
        stdscr.move(max.ceny-2, 0);stdscr.clrtobot()
        rectangle(stdscr, max.ceny, (max.cenx-34//2)-5, max.ceny+2, (max.cenx-24//2)+28)
        stdscr.addstr(max.ceny+6, max.cenx-58//2, "Pista: Si escribes 'exit' volverás a la pantalla anterior.")
        cid = stdscr.getstr(max.ceny+1, (max.cenx-34//2)-4, 32).decode().strip()
        if cid == "exit": break
        try:
            x=client.search_community(cid).comId[0]
        except Exception:
            stdscr.addstr(max.ceny-1, (max.cenx-34//2)-5, "Comunidad no encontrado")
            stdscr.addstr(max.y,0,"Presiona una tecla para continuar...")
            stdscr.getch()
            continue
        client.join_community(x)
        stdscr.addstr(max.ceny+4, (max.cenx-24//2)-5, f"Hecho!")
        stdscr.addstr(max.y, 0, "Presiona una tecla para continuar...")
        stdscr.getch()
        break

def chid(stdscr):
    stdscr.move(8,0);stdscr.clrtobot()
    while True:
        stdscr.addstr(max.ceny-3, max.cenx-24//2, "Ingresa el link del chat")
        stdscr.move(max.ceny-2, 0);stdscr.clrtobot()
        rectangle(stdscr, max.ceny, (max.cenx-24//2)-5, max.ceny+2, (max.cenx-24//2)+28)
        cid = stdscr.getstr(max.ceny+1, (max.cenx-24//2)-4, 32).decode().strip()
        if not cid.startswith("http://aminoapps.com/p/"):
            stdscr.addstr(max.ceny-1, (max.cenx-24//2)-5, "Link inválido.")
            stdscr.addstr(max.y,0,"Presiona una tecla para continuar...")
            stdscr.getch()
            continue
        stdscr.addstr(max.ceny+4, (max.cenx-24//2)-5, f"chatId: {client.get_from_code(cid).objectId}")
        stdscr.addstr(max.y, 0, "Presiona una tecla para continuar...")
        stdscr.getch()
        break

def com(stdscr, com):
    stdscr.move(7,0);stdscr.clrtobot()
    subclient = amino.SubClient(com, profile=client.profile)
    stdscr.addstr(6,max.cenx-len(subclient.community.name)//2, subclient.community.name, curses.A_UNDERLINE)
    stdscr.addstr(7, 0, f"comId: {subclient.comId}")
    while True:
        stdscr.clear()
        stdscr.addstr(2,max.cenx-len("amino id finder")//2,"Amino ID Finder", curses.color_pair(196))
        stdscr.addstr(4,max.cenx-len("by: darth venom")//2,"By: Darth Venom", curses.color_pair(34))
        stdscr.addstr(6,max.cenx-len(subclient.community.name)//2, subclient.community.name, curses.A_UNDERLINE)
        stdscr.addstr(6,0,f"perfil: {client.profile.nickname}")
        stdscr.addstr(7, 0, f"comId: {subclient.comId}")
        x = menu(stdscr, max.ceny, max.cenx-10, {"Obtener chatId": lambda: chid(stdscr), "Volver": lambda: 1})
        if x:
            return

def comupd(stdscr, coms):
    coms.clear()
    subs = client.sub_clients()
    for i in range(len(subs.name)):
        coms[subs.name[i]] = lambdas(com, (stdscr, subs.comId[i]))
    coms["Unirse a una comunidad"] = lambda: joincom(stdscr)
    coms["Actualizar lista"] = lambda: comupd(stdscr,coms)
    coms["Cerrar sesión"] = logout

def main(stdscr):
    global max
    max = Pos(stdscr)
    curses.use_default_colors()
    curses.init_pair(196, 196, -1)
    curses.init_pair(34, 34, -1)
    curses.echo()
    stdscr.addstr(2,max.cenx-len("amino id finder")//2,"Amino ID Finder", curses.color_pair(196))
    stdscr.addstr(4,max.cenx-len("by: darth venom")//2,"By: Darth Venom", curses.color_pair(34))
    stdscr.addstr(6,max.cenx-len("inicia sesion")//2,"Inicia sesión", curses.A_UNDERLINE)
        
    while True:
        stdscr.addstr(9, max.x//4,"Email: ")
        email = stdscr.getstr().decode()
        if not match(r'[a-zA-Z0-9\.]+@[a-zA-Z]+\.[a-z]+', email):
            stdscr.move(8,0);stdscr.clrtoeol()
            stdscr.addstr(8, max.x//4, "Email inválido", curses.color_pair(196))
            stdscr.clrtobot()
            continue
        curses.noecho()
        stdscr.addstr(10,max.x//4,"Contraseña: ")
        passw = stdscr.getstr().decode()
        if not passw or len(passw) < 6:
            stdscr.move(8,0);stdscr.clrtoeol()
            stdscr.addstr(8, max.x//4, "La contraseña es inválida", curses.color_pair(196))
            stdscr.clrtobot()
            continue
        curses.echo()
        try:
            client.login(email, passw)
        except amino.exceptions.InvalidAccountOrPassword:
            stdscr.move(8,0);stdscr.clrtoeol()
            stdscr.addstr(8, max.x//4, "Email o contraseña incorrectos", curses.color_pair(196))
            stdscr.clrtobot()
            continue
        break
    stdscr.move(5,0);stdscr.clrtobot()
    stdscr.addstr(6,0,f"perfil: {client.profile.nickname}")
    subs = client.sub_clients()
    coms = {}
    for i in range(len(subs.name)):
        coms[subs.name[i]] = lambdas(com, (stdscr, subs.comId[i]))
    coms["Unirse a una comunidad"] = lambda: joincom(stdscr)
    coms["Actualizar lista"] = lambda: comupd(stdscr,coms)
    coms["Cerrar sesión"] = logout
    while True:
        stdscr.clear()
        stdscr.addstr(2,max.cenx-len("amino id finder")//2,"Amino ID Finder", curses.color_pair(196))
        stdscr.addstr(4,max.cenx-len("by: darth venom")//2,"By: Darth Venom", curses.color_pair(34))
        stdscr.addstr(6,0,f"perfil: {client.profile.nickname}")
        menu(stdscr, max.ceny, max.cenx-10, coms)

client = amino.Client()
curses.wrapper(main)
