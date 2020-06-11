import socket,pickle
from datetime import date
import functions as func

# Initializations
today = date.today()
weekDay = today.weekday()
host = "localhost"
cartList = []
action = ''
end = 0

# get today's menu
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((host, 8089))
clientsocket.send(b'get_tdymenu')
menuBytes = clientsocket.recv(4096)
todaysMenu = []
todaysMenu = pickle.loads(menuBytes)
clientsocket.close()

# get whole menu
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((host,8089))
clientsocket.send(b'get_menu')
menuBytes = clientsocket.recv(4096)
menu = []
menu = pickle.loads(menuBytes)
clientsocket.close()

# Dictionary to call the different functions
actionFn = {
    "1": func.displayMenu, 
    "2": func.searchMenu, 
    "3": func.displayCart,
    "4": func.checkOut,
    "5": func.editCart
}

while end == 0:
    try:
        if action == "":
            action = func.showHome()
            if action.lower() == "q":
                end = 1
                break
            else:
                action = actionFn[action](todaysMenu, menu, cartList)
                pass
        elif action.isnumeric():
            if action == "4" or action == "5":
                action = actionFn[action](todaysMenu,menu,cartList)
                continue
            else:
                action = ''
                pass
            pass
        elif action.lower() == "q":
            end = 1
            break
    except (IndexError, KeyError):
        print(f'{"":-^38}')
        print(f'{"Invalid input. Please try again.": ^38}')
        print(f'{"":-^38}')
        action = ''
        continue
    continue

# Print thank you message when program ends
if end == 1:
    print(f'{"":=^38}')
    print(f'{"Thank you for using SPAM!": ^38}')
    print(f'{"See you again ʕ•ᴥ•ʔ": ^38}')
    print(f'{"":=^38}')
    # sending 'end' to server to close server socket as well
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((host,8089))
    clientsocket.send(b'end')
    clientsocket.close()
