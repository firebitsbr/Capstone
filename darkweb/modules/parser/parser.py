import subprocess
import ssl
import socket
import SocketServer
#import socketserver
import jsonpickle
import base64
from darkweb.modules.base.result import Result
from search import search
from es_result import es_result

class parser(SocketServer.BaseRequestHandler):
    cert_file="rsa.crt"
    key_file="rsa.key"
    #st=["dad"]
    #re=["dad"]
    #search = Search(st,re)

    def setup(self):
        #self.context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        #self.context.load_cert_chain(certfile=self.cert_file, keyfile=self.key_file)
        print("parser.py - setup start")
        es_result.init();
        print("parser.py - setup end")

    def handle(self):
        print("New connection from " + str(self.client_address))
        #connstream = self.context.wrap_socket(self.request, server_side=True)
        connstream = self.request
        print("Connection unwraped from " + str(connstream.getpeername()))
        connstream.setblocking(0)
        try:
            data = connstream.recv(1024)
            concat=data.decode('utf-8')
            while len(data) > 0:
                data = connstream.recv(1024)
                concat+=data.decode('utf-8')
            #print(concat)
            if self.parse_result(connstream, self.decode(concat)):
                print("Recieve/Decode Successful.")
            else:
                print("Recieve/Decode Failure.")
        finally:
            connstream.shutdown(socket.SHUT_RDWR)
            connstream.close()

    def decode(self,data):
        try:
            resp=jsonpickle.decode(data)
            print("Response decoded to: " + type(resp).__name__)
            return resp
        except:
            print("Failed to decode... probably still receiving. Data:\n" + str(data))
            return None

    def parse_result(self, connstream, r):
        if r != None and isinstance(r,Result):
            if r.data:
                #print("Source:\n" + r.source + "\nData:\n" + str(r.data))
                searchhits, regexhits = search().apply_terms(r.data)
                print("Searchhits: " + str(searchhits))
                print("Regexhits: " + str(regexhits))
                esr = es_result()
                esr.source = r.source
                esr.referrer = r.referrer
                esr.dataHash = r.dataHash
                esr.dataBytes = r.dataBytes

                if len(regexhits) > 0:
                    esr.regex_hit = 1
                    esr.regex_hits = "\n".join(regexhits)
                else:
                    esr.regex_hit = 0
                if len(searchhits) > 0:
                    esr.searchterm_hit = 1
                    esr.searchterm_hits = "\n".join(searchhits)
                else:
                    esr.searchterm_hit = 0

                if esr.searchterm_hit or esr.regex_hit:
                    esr.data = base64.b64encode(r.data)
                else:
                    esr.data = ""

                esr.timeStart = r.timeStart
                esr.timeEnd = r.timeEnd
                c = r.crawlerConfig
                esr.config_name = c.name
                esr.config_location = c.location
                esr.config_protocol = c.protocol
                esr.config_speed = c.speed
                esr.config_depth = c.depth
                esr.config_maxDepth = c.maxDepth
                esr.config_options = c.options
                print("Saving to elasticsearch.")
                esr.save()
                print("Save complete.")
            return True
        return False

    #def run(self, port):
    #    HOST, PORT = "0.0.0.0", port
    #    parser = socketserver.TCPServer((HOST, PORT), parser)
    #    parser.serve_forever()
