import socks
import socket
import io
import stem.process
from stem.util import term

class manageTor:
    temp=None
    def open(self):
            tor_process = stem.process.launch_tor_with_config(
                    config = {
                            'SocksPort': str(9150),
                    },
                    timeout=None
            )
            print("Tor Started")
            return tor_process

    def close(self,tor_process):
            tor_process.kill()
            socket.socket = self.temp
            print("Tor Closed")

    def create_connection_fix(self, address, timeout=None, source_address=None):
            sock = socks.socksocket()
            sock.connect(address)
            return sock

    def torProxy(self):
            socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9150, True)
            self.temp = socket.socket
            socket.socket = socks.socksocket
            socket.create_connection = self.create_connection_fix
