from bson.json_util import dumps
import bottle
from bottle import route, run, request, abort
#from pymongo import Connection
from pymongo import MongoClient

 
#connection = Connection('localhost', 27017)
connection = MongoClient()
db = connection.Capstone 

'''
@route('/rawdata', method='PUT')
def put_document():
    data = request.body.readline()
    if not data:
        abort(400, 'No data received')
    entity = json.loads(data)
    if not entity.has_key('_id'):
        abort(400, 'No _id specified')
    try:
        db['rawdata'].save(entity)
    except ValidationError as ve:
        abort(400, str(ve))
'''
     
@route('/rawdata/:id', method='GET')
def get_rawdata(id):
    entity = db['Rawdata'].find_one({'_id':id})
    if not entity:
        abort(404, 'No document with id %s' % id)
    return dumps(entity)

@route('/rawdata', method='GET')
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
    if not entity:
        abort(404, 'Failed')
    return dumps(entity)
 
run(host='0.0.0.0', port=8080)
