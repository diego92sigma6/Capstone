from bson.json_util import dumps
import cv2
import base64
from bson import json_util
from json import dumps
from json import JSONEncoder
import numpy as np
import traceback
import bottle
from bottle import route, run, request, abort, response
#from pymongo import Connection
from pymongo import MongoClient
import gridfs
from bson.objectid import ObjectId
 
#connection = Connection('localhost', 27017)
connection = MongoClient()
db = connection.Capstone 
fs = gridfs.GridFS(db)


# the decorator
# allows requests from a place different than localhost to be made
def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if bottle.request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors


@route('/rawdata/:id', method='GET')
@enable_cors
def get_rawdata(id):
    entity = db['Rawdata'].find_one({'_id':id})
    if not entity:
        abort(404, 'No document with id %s' % id)
    return dumps(entity)

@route('/rawdata', method='GET')
@enable_cors
def get_rawdatas():
    pipeline = [
            {
                '$sort' : {
                    '_id' : -1
                }
            } , {
                '$limit': 100
            }]
    entity = db['Rawdata'].aggregate(pipeline)
    result = []
    for doc in entity:
        if doc['type'] == 'camera' or True:
            result.append(doc)
    if not entity:
        abort(500, 'Failed')
    json = dumps(result, ensure_ascii=False, default=str).encode('utf-8')
    return json

#Allows to retrieve a base 64 encoded image by mongo Object ID
@route('/image/:oid',method='GET')
@enable_cors
def get_image(oid):
    try:
        img = fs.get(ObjectId(oid)).read()
        response.set_header('Content-type', 'application/json')
        result = [{ 'img' : img }]
        return dumps(result, ensure_ascii=False, default=str).encode('utf-8')
    except:
        traceback.print_exc()
        return None

 
run(host='0.0.0.0', port=8080, debug=True)
