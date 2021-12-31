import socket
import sys
def CreateSever(host, port): 
	Sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	Sever.bind((host,port))
	Sever.listen(5)
	return Sever

def ReadRequest(Client):
	re = ""
	Client.settimeout(1)
	try:
		re = Client.recv(1024).decode()
		while (re):
			re = re + Client.recv(1024).decode()
	except socket.timeout: 
		if not re:
			print("Didn't receive data! [Timeout]")
	finally:
		return re


def ReadHTTPRequest(Sever): 
	re = ""
	while (re == ""):
		Client, address = Sever.accept()
		print("Client: ", address," da ket noi toi sever")
		re = ReadRequest(Client)
	return Client, re

def SendFileIndex(Client): 
	f = open ("index.html", "rb")
	L = f.read()
	header ="""HTTP/1.1 200 OK
Content-Length: %d

"""%len(L)
	print("-----------------HTTP respone  Index.html: ")
	print(header)
	header += L.decode()
	Client.send(bytes(header, 'utf-8'))

def MovePageIndex(Client):
	header = """HTTP/1.1 301 Moved Permanently
Location: http://127.0.0.1:81/index.html

"""
	print("---------------HTTP respone move Index.html: ")
	print(header)
	Client.send(bytes(header,'utf-8'))
	Server.close()


def MoveToHomePage(Sever, Client, Request):
	if "GET /index.html HTTP/1.1" in Request: 
		SendFileIndex(Client)
		Sever.close()
		return True
	if "GET / HTTP/1.1" in Request:
		MovePageIndex(Client)
		Sever.close()
		Sever = CreateSever("localhost", 81)
		Client, Request = ReadHTTPRequest(Sever)
		print("------------------HTTP request: ")
		print(Request)
		MoveToHomePage(Sever, Client, Request)
		return True
	


def CheckPassword(Request): 
	if "POST / HTTP/1.1" not in Request:
		return False
	if "Username=admin&Password=admin" in Request: 
		return True
	else: 
		return False

def Redirector():
	if "POST / HTTP/1.1" not in Request:
		return False
	else: 
		return False


def MoveTo404(Sever, Client): 
	header = """HTTP/1.1 301 Moved Permanently
Location: http://127.0.0.1:82/404.html

"""
	print("HTTP respone: ")
	print(header)
	Client.send(bytes(header,"utf-8"))
	Sever.close()

def SendFile404(Client): 
	f = open ("404.html", "rb")
	L = f.read()
	header ="""HTTP/1.1 404 Not Found
Content-Type: text/html; charset=UTF-8
Content-Encoding: UTF-8
Content-Length: %d

"""%len(L) 
	print("HTTP respone file 404.html: ")
	print(header)
	header += L.decode()
	Client.send(bytes(header, 'utf-8'))

def Send404(Sever, Client): 
	Sever = CreateSever("localhost", 82)
	Client, Request = ReadHTTPRequest(Sever)
	print("HTTP Request: ")
	print(Request)
	if "GET /404.html HTTP/1.1" in Request:
		SendFile404(Client)
	Sever.close()

def MoveToInfo(Sever, Client):
	header = """HTTP/1.1 301 Moved Permanently
Location: http://127.0.0.1:82/info.html

"""
	print("HTTP respone: ")
	print(header)
	Client.send(bytes(header,"utf-8"))
	Sever.close()


def SendImg(Client, NameImg):
	with open(NameImg, 'rb') as f:
		L = f.read()
		header ="""HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Content-Encoding: UTF-8
Content-Length: %d

"""%len(L)
		print("-----------------HTTP respone: ")
		print(header)
		header =  bytes(header,'utf-8') + L
		Client.send(header)	


def SendFileInfo(Client): 
	f = open ("info.html", "rb")
	L = f.read()
	header ="""HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Content-Encoding: UTF-8
Content-Length: %d

"""%len(L)
	print("-----------------HTTP respone  Info.html: ")
	print(header)
	header += L.decode()
	Client.send(bytes(header, 'utf-8'))


def SendInfo(Sever, Client):
	Sever = CreateSever("localhost", 82)
	Client, Request = ReadHTTPRequest(Sever)
	print("HTTP Request: ")
	print(Request)
	if "GET /info.html HTTP/1.1" in Request:
		SendFileInfo(Client)
	Sever.close()
	Sever = CreateSever("localhost", 82)
	Client, Request = ReadHTTPRequest(Sever)
	print("HTTP Request: ")
	print(Request)
	if "GET /header.jpg HTTP/1.1" in Request:
		SendImg(Client, "header.jpg")
	if "GET /avtT.jpg HTTP/1.1" in Request:
		SendImg(Client, "avtT.jpg")
	if "GET /avtK.jpg HTTP/1.1" in Request:
		SendImg(Client, "avtK.jpg")
	
	Client, Request = ReadHTTPRequest(Sever)
	print("HTTP Request: ")
	print(Request)
	if "GET /header.jpg HTTP/1.1" in Request:
		SendImg(Client, "header.jpg")
	if "GET /avtT.jpg HTTP/1.1" in Request:
		SendImg(Client, "avtT.jpg")
	if "GET /avtK.jpg HTTP/1.1" in Request:
		SendImg(Client, "avtK.jpg")

	Client, Request = ReadHTTPRequest(Sever)
	print("HTTP Request: ")
	print(Request)
	if "GET /header.jpg HTTP/1.1" in Request:
		SendImg(Client, "header.jpg")
	if "GET /avtT.jpg HTTP/1.1" in Request:
		SendImg(Client, "avtT.jpg")
	if "GET /avtK.jpg HTTP/1.1" in Request:
		SendImg(Client, "avtK.jpg")
	Sever.close()

def SendToFileHtml(Sever,Client):
	Sever = CreateSever("localhost", 83)
	Client, Request = ReadHTTPRequest(Sever)
	if "GET /file.html HTTP/1.1" in Request:
		SendFile(Client,"file.html")
	Sever.close()

def SendFile(Client,filename):
	f = open (filename, "rb")
	L = f.read()
	header ="""HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Content-Encoding: UTF-8
Transfer-Encoding: chunked

"""%len(L)
	print("-----------------HTTP respone  file.html: ")
	print(header)
	header += L.decode()
	Client.send(bytes(header, 'utf-8'))

def MoveToFileHtml(Sever, Client):
	header = """HTTP/1.1 301 Moved Permanently
Location: http://127.0.0.1:83/file.html

"""
	print("HTTP respone: ")
	print(header)
	Client.send(bytes(header,"utf-8"))
	Sever.close()





if __name__ == "__main__":
	while True:	
		print("Chuyen toi index.html")
		Server = CreateSever("localhost",81)
		Client, Request = ReadHTTPRequest(Server)
		#print("----------------HTTP requset: " )
		#print(Request)
		MoveToHomePage(Server, Client, Request)
		Server = CreateSever("localhost",10000)
		Client, Request = ReadHTTPRequest(Server)
		#print("----------------HTTP requset: " )
		#print(Request)
		if CheckPassword(Request) == True: 
			print("Chuyen toi info.html")
			MoveToInfo(Server, Client)
			SendInfo(Server, Client)
			Server = CreateSever("localhost",9000)
			Client, Request = ReadHTTPRequest(Server)
			print("----------------HTTP requset: " )
			print(Request)
			print("Chuyen toi file.html")
			MoveToFileHtml(Server,Client)
			SendToFileHtml(Server,Client)
		else:
			MoveTo404(Server,Client)
			Send404(Server,Client)
