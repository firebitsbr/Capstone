import socks
import socket
import io
import stem.process
from stem.util import term

def open():
	tor_process = stem.process.launch_tor_with_config(
		config = {
			'SocksPort': str(9150),
		},
	)
	print("Tor Started")
	return tor_process

def close(tor_process):
	tor_process.kill()
	print("Tor Closed")

def create_connection_fix(address, timeout=None, source_address=None):
	sock = socks.socksocket()
	sock.connect(address)
	return sock

def torProxy():
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9150, True)
	socket.socket = socks.socksocket
	socket.create_connection = create_connection_fix
