import subprocess
import ssl
import socket
import socketserver
import jsonpickle

class parser(socketserver.BaseRequestHandler):
    cert_file="<insert cert file>"
    key_file="<insert cert file>"

    def __init__(self,search):
        self.search = search

    def setup(self):
        self.context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        self.context.load_cert_chain(certfile=self.cert_file, keyfile=self.key_file)

    def handle(self):
        print("New connection from " + str(self.client_address))
        connstream = self.context.wrap_socket(self.request, server_side=True)
        print("Connection unwraped from " + str(connstream.getpeername()))
        try:
            data = connstream.recv()
            concat=data.decode('utf-8')
            while self.parse_beacon(connstream, self.decode(concat)):
                data = connstream.recv()
                concat+=data.decode('utf-8')
        finally:
            connstream.shutdown(socket.SHUT_RDWR)
            connstream.close()

    def decode(self,data):
        try:
            resp=jsonpickle.decode(data)
            print("Response decoded to: " + type(resp).__name__, end="")
            return resp
        except:
            print("Failed to decode... probably still receiving. Data:\n" + str(data))
            return None

    def parse_result(self, connstream, r):
        if r != None and type(r).__name__ == "Result":
            if r.data:
                print("Source:\n" + r.source + "\nData:\n" + str(r.data))
                searchhits, regexhits = search.apply_terms(r.data)
                print("Searchhits: " + str(searchhits))
                print("Regexhits: " + str(regexhits))
            return True
        return False

    def search_result(self, r):
        if r != None and type(r).__name__ == "Result":


if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 443
    server = socketserver.TCPServer((HOST, PORT), server)
    server.serve_forever()
