from datetime import datetime
from elasticsearch_dsl import DocType, String, Date, Integer
from elasticsearch_dsl.connections import connections
from elasticsearch import Elasticsearch, RequestsHttpConnection


    #http_auth=('user', 'secret'),
    #verify_certs=True,
    #ca_certs='/path/to/cacert.pem',
    #client_cert='/path/to/client_cert.pem',
    #client_key='/path/to/client_key.pem',
es = Elasticsearch(
    ['localhost'],
    port=9200,
    use_ssl=False
)
connections.add_connection('default', es)

class es_result(DocType):
    source = String()
    referrer = String()
    data = String()
    dataHash = String()
    dataBytes = Integer()
    regex_hit = Integer()
    regex_hits = String()
    searchterm_hit = Integer()
    searchterm_hits = String()
    timeStart = Date()
    timeEnd = Date()
    config_name = String()
    config_location = String()
    config_protocol = String()
    config_speed = String()
    config_depth = Integer()
    config_maxDepth = Integer()
    config_options = String()

    class Meta:
        index = 'default'
    def save(self, ** kwargs):
        return super(es_result, self).save(** kwargs)
    def delete(self, ** kwargs):
        return super(es_result, self).delete(** kwargs)
