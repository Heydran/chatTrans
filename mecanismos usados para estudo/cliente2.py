from socket import *
class Cliente(object):
	def __init__(self, host, port):
		self.cliente = socket(AF_INET, SOCK_STREAM)
		self.cliente.connect((host, port))

cliente = Cliente("localhost", 33335)