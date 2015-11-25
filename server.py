from eve import Eve
from flask import redirect, request
from settings import schema
import json

app = Eve()

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

def remove_extra_fields(item, original):
  accepted_fields = schema.keys()
  for field in item.keys():
    if field not in accepted_fields:
      del item[field]

if __name__ == '__main__':
  app.on_replace_article += remove_extra_fields
  app.run(host='0.0.0.0', port=8080, threaded=True, debug=True)
