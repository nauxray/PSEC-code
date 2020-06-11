import socket

logins = {}

# reading logins.txt, creating logins dictionary with login credentials
with open("logins.txt", newline="") as f:
    for line in f:
        (user, passwd) = line.split()
        logins[user] = passwd

# function to process connection
def processConn():
    cmd = conn.recv(255)
    creds = cmd.decode()
    # checking that the correct command is sent by server
    if creds[0:11] == "login_check":
        username = creds[11:]
        # checking username
        if username in logins.keys():
            print(f'{"Username found": ^40}')
            print(f'{"":-^40}')
            conn.send(b'true')
            passwdBytes = conn.recv(255)
            passwd = passwdBytes.decode()
            # checking password
            if passwd == logins[username]:
                print(f'{"Password found": ^40}')
                print(f'{"":-^40}')
                conn.send(b'success')
                # close connection
                conn.close()
                return False
            else:
                print(f'{"Password not found": ^40}')
                print(f'{"":-^40}')
                conn.send(b'false')
        else: 
            print(f'{"Username not found": ^40}')
            print(f'{"":-^40}')
            conn.send(b'false')

while True:
    loginsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    loginsocket.bind(('0.0.0.0', 9000))
    loginsocket.listen(5)
    print(f'{"":-^40}')
    print(f'{"Listening for connections...": ^40}')
    print(f'{"":-^40}')
    # accept connection from server
    conn, address = loginsocket.accept()
    ip, port = address
    print(f'Listening from {ip}:{port}')
    print(f'{"":-^40}')
    # once the correct username and password has been entered, close connection
    if processConn() == False:
        break
    else:
        continue
    
print(f'{"Connection closed": ^40}')
print(f'{"":-^40}')

