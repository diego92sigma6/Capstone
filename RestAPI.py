from bson.json_util import dumps
import bottle
from bottle import route, run, request, abort, response
#from pymongo import Connection
from pymongo import MongoClient

 
#connection = Connection('localhost', 27017)
connection = MongoClient()
db = connection.Capstone 




# the decorator
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
    if not entity:
        abort(404, 'Failed')
    return dumps(entity)
 
run(host='0.0.0.0', port=8080)
