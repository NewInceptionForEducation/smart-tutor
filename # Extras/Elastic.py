from elasticsearch import Elasticsearch

es = Elasticsearch()
es = Elasticsearch(["localhost:9200"], sniff_on_start=True)