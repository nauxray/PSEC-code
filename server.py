import socket, csv, pickle
from datetime import date

# Initializations
today = date.today()
weekDay = today.weekday()
end = 0 
logins = {}

# function to process logging in
def processLogin():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.connect(('localhost',9000))
    serversocket.send(b'login_check')
    # send username for login program to check
    serversocket.send(username.encode())
    checkUser = serversocket.recv(255)
    # username is correct
    if checkUser.decode() == "true":
        # send password for login program to check
        serversocket.send(passwd.encode())
        checkPass = serversocket.recv(255)
        # password is correct, break out of while loop
        if checkPass.decode() == "success":
            print(f'{"":-^40}')
            print(f'{"Successfully logged in!": ^40}')
            return "break"
        else:
            print(f'{"Invalid password! Please try again": ^40}')
    else: 
        print(f'{"Invalid username! Please try again": ^40}')
    serversocket.close()

# Login prompt
while True:
    print(f'{"":-^40}')
    print(f'{"Welcome to SPAM!": ^40}')
    print(f'{"Please login before you start the server": ^40}')
    print(f'{"":-^40}')
    username = input(f'Please enter your username here:\n>> ')
    print(f'{"":-^40}')
    passwd = input (f'Please enter your password here:\n>> ')
    # only breaks if username and password is correct
    if processLogin() == "break":
        break

# Establishing serversocket for client to connect
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('0.0.0.0', 8089))
serversocket.listen(5)
print(f'{"":-^40}')
print(f'{"Waiting for connection...": ^40}')
print(f'{"":-^40}')

# function to process client connection
def processConn():
    cmd = conn.recv(255)
    if cmd.decode() == "get_tdymenu":
        # Opening csv file and reading content into todaysMenu
        with open("menu.csv", newline="") as csvfile:
            csvReader = csv.DictReader(csvfile)
            todaysMenu = []
            for i in csvReader:
                if str(i["Day"]) == str(weekDay):
                    todaysMenu.append(dict(i))
        menuSend = pickle.dumps(todaysMenu)
        conn.send(menuSend)
        print(f'{"":-^40}')
        print(f'{"MENU FOR TODAY SENT": ^40}')
        print(f'{"":-^40}')
    elif cmd.decode() == "get_menu":
        # Opening csv file and reading content into menu
        with open("menu.csv", newline="") as csvfile:
            csvReader = csv.DictReader(csvfile)
            menu = []
            for i in csvReader:
                menu.append(dict(i))
        menuSend = pickle.dumps(menu)
        conn.send(menuSend)
        print(f'{"MENU FOR EVERYDAY SENT": ^40}')
        print(f'{"":-^40}')
    elif cmd.decode() == 'end':
        print(f'{"Connection closed": ^40}')
        conn.close()
        global end
        end = 1

while end == 0:
    conn, address = serversocket.accept()
    ip, port = address
    print("Listening from {}:{}".format(ip,port))
    print(f'{"":-^40}')
    processConn()
    
if end == 1:
    print(f'{"":=^40}')
    print(f'{"Stopped listening... Server closed":-^40}')
    print(f'{"":=^40}')
