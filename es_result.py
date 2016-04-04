from datetime import datetime
from elasticsearch_dsl import DocType, String, Date, Integer
from elasticsearch_dsl.connections import connections
from elasticsearch import Elasticsearch, RequestsHttpConnection

connections.add_connection('default', es)

class ES_Result(DocType):
    source = String(analyzer='snowball')
    referrer = String(analyzer='snowball')
    data = String(analyzer='snowball')
    datahash = String(analyzer='snowball')
    regex_hit = Integer(analyzer='snowball')
    regex_hits = String(analyzer='snowball')
    searchterm_hit = Integer(analyzer='snowball')
    searchterm_hits = String(analyzer='snowball')
    timestart = Date()
    timeend = Date()
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
