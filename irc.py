# IRC Crawler
# Jimmy Trimer

import socket
import time
import datetime
import threading
from crawler import Crawler
from results import *
from crawlerconfig import * 

class IRC(Crawler):
    def __init__(self, server, nickname):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = server
        self.nickname = nickname
        self.channel = ""

    def connect(self):
        print("Connecting to server... %s" % self.server)
        self.irc.connect((self.server, 6667))
        self.irc.send("USER " + self.nickname + " " + self.nickname + " " + self.nickname + " :" + self.nickname
                      + " \n")
        self.irc.send("NICK " + self.nickname + "\n")
        while(True):
            temp = self.irc.recv(2048)
            if(temp == "" or temp == None or temp == "-1"):
                break
            if("End of /MOTD" in temp):
                break  
        print("Connected to %s!" % self.server)
        return 

    def joinChannel(self, channel):
        self.channel = channel
        self.irc.send("JOIN " + self.channel + "\n")
        return 

    def get_text(self):
        text = self.irc.recv(2048)

        if text.find('PING') != -1:
            self.irc.send('PONG ' + text.split()[1] + "\r\n")
            return ""
        return text

    def getChannels(self):
        print("Getting Channels..."),
        self.irc.send("LIST\n")
        data = ""
        while(True):
            d = self.irc.recv(2048)
            data += d 
            if(d == "" or d == None or d == "-1"):
                break
            if("End of /LIST" in d):
                break
	    #print("Still Getting Channels...")
        
        #print("GOT LIST!")
        channels = []
        data_split = data.split("\n")
        for line in data_split:
              #print("***" + line + "+++")  
              if "322" in line:
                channel = line.split(" ")[3]
                #print("Channel = %s" % channel)
                channels.append(channel)
        return channels
        
def doCrawl(irc, mins_interval, total_mins, crawler_config, channel):
    session_text = ""
    finished = False
    i = 0

    irc.joinChannel(channel) # source = (server, channel)
    print("Starting to listen... %s" % channel)
    start_time_total = time.time()
    start_time = time.time()
    cur_time = time.time() 
    while(not finished):
        #print("cur_time: %d total_time: %d"  % ((cur_time - start_time), (cur_time - start_time_total)))
        text = irc.get_text()
        if text != "": 
            #print(session_text)
            session_text += (text+"\n")
        cur_time = time.time()
        if((cur_time - start_time) >= mins_interval*60):
            #print("="*80)
            #print(session_text)
            utc_start_time = datetime.datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')
            utc_cur_time = datetime.datetime.fromtimestamp(cur_time).strftime('%Y-%m-%d %H:%M:%S')
            print("Start time: %s End time: %s %s" % (utc_start_time, utc_cur_time, channel))
            res = Results(crawler_config, utc_start_time, utc_cur_time, (irc.server, channel), "", session_text)
            results_list.append(res)
            session_text = ""
            start_time = time.time()
            if((cur_time - start_time_total) >= total_mins*60):
                finished = True
    return 

if __name__ == "__main__":
    #CrawlerConfig = location, protocol, speed(interval), maxDepth(duration), name
    config = CrawlerConfig("irc.freenode.net", "IRC", 1, 2,"name")
    channel = "#linux" # where does channel fit into CrawlerConfig?
    source = (config.get_location(), channel)
    nickname = "tnasty1"
    mins_interval = config.get_speed() # how often to get data
    total_mins = config.get_maxDepth() # how long to run (total time)

    irc = IRC(source[0], nickname)
    irc.connect()
    channels = irc.getChannels()
    #print(channels)
    print(len(channels))
    global results_list
    results_list = []

    for i in range(0,2):
        t = threading.Thread(target=doCrawl, args=(irc, mins_interval, total_mins, config, channels[i], ))
        results_list.append(t.start())
    
    sleep(total_mins + 1)

    # results_list = listen(irc, mins_interval, total_mins, config, cha)
    print(results_list)
    print(len(results_list))
    print("Done")


