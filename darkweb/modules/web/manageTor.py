import socks
import socket
import io
import stem.process
from stem.util import term
import time

# The manageTor class allows for the management of a TOR proxy on the localhost.

class manageTor:
	temp=None

	# The "open" function utilizes the stem library to launch tor with a specified configuration.
	# This launch returns a process that we can use to close later. It uses the SOCKS5 port 9150
	# for all of its communication. If a socket is created on the port (another crawl is using
	# a tor connection), the "open" function will wait for 10 seconds and retry the tor launch.
	# It will continue to do this until it gets control of the port.

	def open(self):
		try:
			tor_process = stem.process.launch_tor_with_config(
				config = {
                            		'SocksPort': str(9150),
                    		},
                    		timeout=None
            		)
		except:
			print "TOR Socket in use. Waiting 10 seconds to retry"
			time.sleep(10)
			tor_process = self.open()	
		print("Tor Started")
       		return tor_process

	# The "close" function takes the tor process created in the "open" function and closes the tor connection.
	# It also resets the socket function to allows for regular sockets to be used to communicate with the parser.

	def close(self,tor_process):
       		tor_process.kill()
        	socket.socket = self.temp
        	print("Tor Closed")

	# This function is a "fix" to the regular socket create_connection function in that is allows a SOCKS5 socket
	# to be used to connect to TOR. SOCKS5 is needed for a TOR connection.

	def create_connection_fix(self, address, timeout=None, source_address=None):
        	sock = socks.socksocket()
        	sock.connect(address)
        	return sock

	# This function tells the imported libraries (in "WebCrawler.py") what proxy to use to connect to TOR. It changes
	# the default socket and create_connection variables/functions to allows for a SOCKS5 connection to TOR.

	def torProxy(self):
        	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9150, True)
       		self.temp = socket.socket
        	socket.socket = socks.socksocket
        	socket.create_connection = self.create_connection_fix

