from eve import Eve
from flask import redirect, request
from settings import schema
import json, os

app = Eve()
app.on_replace_article += lambda item, original: remove_extra_fields(item)
app.on_insert_article += lambda items: remove_extra_fields(items[0])

@app.route("/tag/<name>", methods=['GET'])
def tagSearch(name):
  return redirect('/article/?where={"tags":{"$in":["%s"]}}' % name, code=302)

@app.route("/tags/", methods=['POST'])
def tagBulkSearch():
  data = json.loads(request.data)
  results = []
  tc = app.test_client()
  for tag in data['tags']:
    resp = tc.get('article/?sort=-lastPublish&where={"tags":{"$in":["%s"]}}' % tag)
    results.append(json.loads(resp.data))
  return json.dumps({'results':results})

@app.route("/rss2.xml")
def getRssFromPerl():
  return os.popen('perl script/rss.pl').read()

def remove_extra_fields(item):
  accepted_fields = schema.keys()
  for field in item.keys():
    if field not in accepted_fields and field != '_id':
      del item[field]

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, threaded=True, debug=True)
