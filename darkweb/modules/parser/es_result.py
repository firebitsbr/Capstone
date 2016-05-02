from datetime import datetime
from elasticsearch_dsl import DocType, String, Date, Integer
from elasticsearch_dsl.connections import connections
from elasticsearch import Elasticsearch, RequestsHttpConnection


    #http_auth=('user', 'secret'),
es = Elasticsearch(
    ['redteam.isamotherfucking.ninja'],
    port=9200,
    use_ssl=False,
    verify_certs=True,
    ca_certs='/path/to/cacert.pem',
    client_cert='/path/to/client_cert.pem',
    client_key='/path/to/client_key.pem',
)
connections.add_connection('default', es)

class es_result(DocType):
    source = String(analyzer='snowball')
    referrer = String(analyzer='snowball')
    data = String(analyzer='snowball')
    dataHash = String(analyzer='snowball')
    dataBytes = Integer(analyzer='snowball')
    regex_hit = Integer(analyzer='snowball')
    regex_hits = String(analyzer='snowball')
    searchterm_hit = Integer(analyzer='snowball')
    searchterm_hits = String(analyzer='snowball')
    timeStart = Date()
    timeEnd = Date()
    config_name = String(analyzer='snowball')
    config_location = String(analyzer='snowball')
    config_protocol = String(analyzer='snowball')
    config_speed = String(analyzer='snowball')
    config_depth = Integer(analyzer='snowball')
    config_maxDepth = Integer(analyzer='snowball')
    config_options = String(analyzer='snowball')

    class Meta:
        index = 'default'
    def save(self, ** kwargs):
        return super(ES_Result, self).save(** kwargs)
    def delete(self, ** kwargs):
        return super(ES_Result, self).delete(** kwargs)
