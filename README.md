== Dark Web Recon ==

Contributors: Jacob Dresdale, Joey Fitzpatrick, Edward Mead, Aaron Pinzer,
Jimmy Trimer, and Bill Stackpole
Version: 1.0  
License: GPLv2  
License URI: http://www.gnu.org/licenses/gpl-2.0.html  

Dark Web Recon is a tool designed to have a web front end where a user can direct a search term towards a input resource, such as a web address or IRC channel and parameters for which they would like to search. The searches run through modules tied to the selected protocol and sent to a preconfigured, already in-place Elasticsearch Database.

== Description ==  

Dark Web Recon was designed at Rochester Institute of Technology as a way to search for information on the Dark Web. We
have developed with extensibility in mind and provide the ability to add new
crawling modules. Using the *parent classes* a developer can easily create their
own unique crawler modules to work with the developed parser.

The following components are included in version 1.0: The
Parser, the Web Front End, A Web/TOR Crawler, and an IRC Crawler. A server
needs to be configured with an ELK stack in place (Elasticsearch, Logstash, and
Kibana) which will act as the database that will store all successful search queries.

To use the program, once properly configured a user will
enter a query in the user friendly web interface, which will be sent to the
appropriate crawling module automatically. The crawler will send the results to
the parser which will check for keyword matches. All matches, stored in the Elasticsearch database, can be retrieved at a later time. The web interface for Kibana lets a user view any queries made and use the data as
they see fit. Kibana can be configured to render graphs and pie charts of
results found. Component breakdowns are included below:

== Web Front End ==

Dark Web Recon’s Web Front end is designed to communicate
with the back end components. The user provides a
domain, and search terms and instructs the search to run. For *web* and *TOR* domain searches, the query must
model ‘*http://[url]/*’. This ensures
the web site queried will return possible results. The user can continue to add
searches, each of which are threaded and will execute as quickly as the
hardware platform allows. The web front-end can be stylized by editing the CSS
file as desired by a user.

== ELK ==

ELK (Elasticsearch, Logstash, and Kibana) is used as the
database for Dark Web Recon. ELK is free, open source, and extremely scaleable.
Elasticsearch is used to search through the database, Logstash takes in and
reads log data, and Kibana is the visual front end to the database. ELK allows
Dark Web Recon to use a database and be searched in real time. The only limitations are hardware resources, add more resources as the need arises.

== Web/Tor Crawler ==

The *Web/Tor Crawler Class* is called by the web front end. 
Dark Web Recon has the capability to crawl any site. By default, it
honors Robots.txt but allows for a manual override of this setting in the web
interface. Any use of this feature is the sole responsibility of the user and
any legal action taken against the user is the responsibility of the user and
not of any developers on this project. If the web interface has the *tor*
flag enabled, then a proxy is opened for command line access to TOR allowing
the site to be crawled. The proxy is closed when the crawler has completed. All
crawls have a *max depth* setting which limits searches from going on
indefinitely. The larger the depth, the longer the search will take. As long as
hardware resources are adequate; deeper searches are likely to take longer. 
All data will be sent to the *results class* which sends the
crawled information to the Parser.

== IRC Crawler ==

Dark Web Recon has IRC capabilities. If the IRC module is
chosen in the web front end, then one o rmore channel names will need to be provided by the
user. Dark Web Recon can join as many channels as desired, and each channel
will run in a new thread. All activity will be monitored for a duration
provided by the user. A time interval is specified in the web front end,
providing a total search time and an interval at which to send data to be
parsed. 

== Parser ==

Dark Web Recon’s Parser accepts data from any Crawler
modules, and processes any new data received on its own thread. Search terms
and regular expressions set in the Web front end will be used by the parser to
match data that will then be sent to the ELK database. Each Crawler sends data
to the Parser via a *send_result* function call which is defined in the
*Crawler Super Class*. Search terms or regular expressions are added directly to
the *search class* via *add_searchterm* or *add_regexterm*. *ES_Result class* is created and pushed directly into Elasticsearch using the *Elasticsearch_DSL*
library.

== ELK System Requirements ==

The ELK hardware requirements really depend upon how much data is being managed. Another main hardware factor is whether the ELK
stack will be hosted on a single machine or if it will be spread across multiple.
The following recommendations are taken from [elastic](https://elastic.co/)[.](https://elastic.co/)[co](https://elastic.co/) and are noted as guidance, actual performance may vary.

**Memory:**

16GB and 32GB RAM are a common starting point for ELK stacks with upwards of 64GB RAM being the sweet spot for large amounts of data
processing.

**CPU’s:**

With memory being the first bottleneck, there is no “right” CPU to use. Generally speaking, one should choose a modern processor
with multiple cores ranging from two to eight. More cores will only improve performance. 

**Disks:**

Disk space depends directly upon how much (in GB) of logs you are pulling in or to be processed. Multiple TB HDDs will do just fine but SSD are obviously the best choice if they fit into the budget of the project add substantially greater performance.

**Network:**

If you are going to split up the stack, crawlers, parser,
etc. then latency can become an issue if t

Latency may become an issue should the stack, crawler, parser, etc. be separated. Modern data-center networking
of Gigabit or better should be suffificient for the majority of cluster applications.

[https](https://www.elastic.co/guide/en/elasticsearch/guide/current/hardware.html)[://](https://www.elastic.co/guide/en/elasticsearch/guide/current/hardware.html)[www](https://www.elastic.co/guide/en/elasticsearch/guide/current/hardware.html)[.](https://www.elastic.co/guide/en/elasticsearch/guide/current/hardware.html)[elastic](https://www.elastic.co/guide/en/elasticsearch/guide/current/hardware.html)[.](https://www.elastic.co/guide/en/elasticsearch/guide/current/hardware.html)[co](https://www.elastic.co/guide/en/elasticsearch/guide/current/hardware.html)[/](https://www.elastic.co/guide/en/elasticsearch/guide/current/hardware.html)[guide](https://www.elastic.co/guide/en/elasticsearch/guide/current/hardware.html)[/](https://www.elastic.co/guide/en/elasticsearch/guide/current/hardware.html)[en](https://www.elastic.co/guide/en/elasticsearch/guide/current/hardware.html)[/](https://www.elastic.co/guide/en/elasticsearch/guide/current/hardware.html)[elasticsearch](https://www.elastic.co/guide/en/elasticsearch/guide/current/hardware.html)[/](https://www.elastic.co/guide/en/elasticsearch/guide/current/hardware.html)[guide](https://www.elastic.co/guide/en/elasticsearch/guide/current/hardware.html)[/](https://www.elastic.co/guide/en/elasticsearch/guide/current/hardware.html)[current](https://www.elastic.co/guide/en/elasticsearch/guide/current/hardware.html)[/](https://www.elastic.co/guide/en/elasticsearch/guide/current/hardware.html)[hardware](https://www.elastic.co/guide/en/elasticsearch/guide/current/hardware.html)[.](https://www.elastic.co/guide/en/elasticsearch/guide/current/hardware.html)[html](https://www.elastic.co/guide/en/elasticsearch/guide/current/hardware.html)

== ELK Installation ==  
  
The following should be run from the command line on the
server that will run ELK

1.   
Install

>_   
sudo apt-get install
openjdk-7-jre-headless_

2.   
Verify the Java Installation

>_   
java -version_

3.   
Update Linux packages

>_   
sudo apt-get update && sudo
apt-get upgrade_

4.   
To begin the process of installing
Elasticsearch, add the following repository key:

>_a.   
 wget -O - http://packages.elastic.co/GPG-KEY-elasticsearch | apt-key add_

5.   
Add the following Elasticsearch list to the key:

>_   
echo "deb
http://packages.elastic.co/elasticsearch/2.x/debian stable main" | sudo
tee -a /etc/apt/sources.list.d/elasticsearch-2.x.list_

>_   
sudo apt-get update_

6.   
Install Elasticsearch:

>_   
sudo apt-get install -y elasticsearch_

7.   
Elasticsearch is now installed. The following
command will open the configuration for editing:

>_   
sudo vi
/etc/elasticsearch/elasticsearch.yml_

8.   
Now, we will want to restrict access to our
Elasticsearch instance (port 9200). With the .yml open, find the network.host
line, uncomment it, and replace its value with "localhost"

>_   
network.host: localhost_

9.   
Start service:

>_   
sudo service elasticsearch start_

10. 
Test the service

>_   
curl localhost:9200_

11. 
The run the following command to start
Elasticsearch on boot up:

>_   
sudo update-rc.d elasticsearch defaults
95 10_

== Installing Logstash ==

1.   
The Logstash package is available from the same
repository as Elasticsearch. The public key has already been installed, so it’s
time to create a Logstash source list:

>_   
echo 'deb http://packages.elastic.co/logstash/2.2/debian
stable main' | sudo tee /etc/apt/sources.list.d/logstash-2.2.x.list_

2.   
Update your apt package database:

>_   
sudo apt-get update_

3.   
Install Logstash

>_   
sudo apt-get install logstash_

4.   
Ensure that logstash will autoboot on start:

>_   
sudo update-rc.d logstash defaults 97 8_

5.   
Start logstash:

>_   
sudo service logstash start_

6.   
Redirect the System logs to Logstash:

7.   
Create the file "logstash-syslog.conf"
with the command:

>_   
touch /etc/logstash/conf.d/logstash-syslog.conf_

8.   
Copy and paste the following code into the .conf
file:

>input {_

>>file {_

>>path =&gt; [
"/var/log/*.log", "/var/log/messages",
"/var/log/syslog" ]_

>>_type =&gt;
"syslog"_

>>_}_

>>_}_

>>_output {_

>>_elasticsearch {
host =&gt; localhost }_

>>_stdout { codec
=&gt; rubydebug }_

>_}_

9.   
The configuration above tells Logstash to
collect all files with .log extention in /var/log, /var/log/messages and
/var/log/syslog.

9.   
Next, we will create a filter to prevent
Elasticsearch to store logs in the message field and simplify the analysis.

>_filter {_

>>_if [type] == "syslog"
{_

>>_grok {_

>>>_match =&gt; {
"message" =&gt; "%{SYSLOGTIMESTAMP:syslog_timestamp}
%{SYSLOGHOST:syslog_hostname} %{DATA:syslog_program}(?:\[%{POSINT:syslog_pid}\])?:
%{GREEDYDATA:syslog_message}" }_

>>>_add_field
=&gt; [ "received_at", "%{@timestamp}" ]_

>>>_add_field
=&gt; [ "received_from", "%{host}" ]_

>>>_}_

>>>_syslog_pri { }_

>>>_date {_

>>>_match =&gt; [
"syslog_timestamp", "MMM 
d HH:mm:ss", "MMM dd HH:mm:ss" ]_

>>>_}_

>>_}_

>_}_

10. 
Next, point logstash to the correct config file:

>   
cd /opt/logstash_

>   
bin/logstash -f
/etc/logstash/conf.d/logstash-syslog.conf_

11. 
Finally, restart logstash

>   
sudo service logstash restart_

== Installing Kibana ==

1.   
Create the Kibana source list:

>_   
echo "deb
http://packages.elastic.co/kibana/4.4/debian stable main" | sudo tee -a
/etc/apt/sources.list.d/kibana-4.4.x.list_

2.   
Update your apt package database:

>_   
sudo apt-get update_

3.   
Install Kibana

>_   
sudo apt-get install -y kibana_

4.   
Go to /opt/kibana/config

>_   
cd /opt/kibana/config_

5.   
Edit the configuration file and make the
appropriate changes:

>_   
_Example:_
>>_server.port: 6501_

ii.server.host "localhost"

6.   
Auto start:

>_   
sudo update-rc.d kibana defaults 96 9_

== Parse and Module Dependencies ==

The dependencies outlined below are for the parse and modules. A full list of dependencies is available in the requirements.txt file.
All dependencies should install with the command ‘_pip install -r requirements.txt_’. The following dependencies should be verified manually.

1.   
python2

2.   
jsonpickle

3.   
simplejson

4.   
pysocks

5.   
stem

6.   
beautifulsoup

7.   
tor

== Parser and Module Installation Installation ==  

To install the parser and other modules, all that is required is to fork a copy of the repo from Github onto the server intended to run the parser and other modules (provided the dependencies are already installed).
