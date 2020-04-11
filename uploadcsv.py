import sys
import json
from pprint import pprint
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth


es = Elasticsearch(
    ['dad068e19c544838b1bdbdce3152c54f.ap-southeast-2.aws.found.io'],
    http_auth=('', ''),
    scheme="https",
    port=9243

)

MyFile = open("prodlogging-full-1.csv",'r').read()
ClearData = MyFile.splitlines(True)
i=0
json_str=""
docs ={}
for line in ClearData:
    line = ''.join(line.split())
    if line != "},":
        json_str = json_str+line
    else:
        docs[i]=json_str+"}"
        json_str=""
        print(docs[i])
        es.index(index='ie_log_full', doc_type='Log', id=i, body=docs[i])
        i=i+1
