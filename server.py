from eve import Eve
from flask import redirect, request, Response
from settings import posts, users
import json

app = Eve()
app.on_replace_article += lambda item, original: remove_extra_fields(item)
app.on_insert_article += lambda items: remove_extra_fields(items[0])

@app.route("/tag/<name>", methods=['GET'])
def tagSearch(name):
  return redirect('/posts/?where={"tags":{"$in":["%s"]}}' % name, code=302)

# TODO
# [issue] /tags/ doesn't handle preflight requests
# [solve] redirect /tags/ to /article when the request's method is OPTIONS
# [note]  other url's preflight requests is now handled by eve
# [todo]  preflight requests should be handled in one place for all urls
@app.route("/tags/", methods=['OPTIONS'])
def handlePreflightRequests(name=None):
  headers = dict(request.headers)

  tc = app.test_client()
  resp = tc.get('article', headers = headers)

  headers = dict(resp.headers)
  del headers['Content-Length']

  resp = Response("", headers=headers)
  return resp

@app.route("/tags/", methods=['POST'])
def tagBulkSearch():
  data = json.loads(request.data)
  results = []

  headers = dict(request.headers)
  del headers['Content-Length']

  tc = app.test_client()
  for tag in data['tags']:
    resp = tc.get('article/?sort=-lastPublish&where={"tags":{"$in":["%s"]}}' % tag, headers=headers)
    results.append(json.loads(resp.data))

  headers = dict(resp.headers)
  del headers['Content-Length']

  resp = Response(json.dumps({'results':results}), headers=headers)
  return resp

def remove_extra_fields(item):
  accepted_fields = schema.keys()
  for field in item.keys():
    if field not in accepted_fields and field != '_id':
      del item[field]

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, threaded=True, debug=True)
