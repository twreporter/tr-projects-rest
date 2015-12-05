from eve import Eve
from flask import redirect, request
from settings import schema
import json

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
    resp = tc.get('article/?where={"tags":{"$in":["%s"]}}' % tag)
    results.append(json.loads(resp.data))
  return json.dumps({'results':results})

def remove_extra_fields(item):
  accepted_fields = schema.keys()
  for field in item.keys():
    if field not in accepted_fields and field != '_id':
      del item[field]

def filter_only_published(response):
  data = response
  if 'items' in data.keys():
    for item in data['items']:
      if not item['isPublishedVersion']:
        data['items'].remove(item)
  else:
    if 'isPublishedVersion' in data.keys():
      if not data['isPublishedVersion']:
        data = {}
  return data
app.on_fetched_item_article += filter_only_published

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, threaded=True, debug=True)
