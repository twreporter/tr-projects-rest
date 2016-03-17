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

def remove_extra_fields(item):
  accepted_fields = schema.keys()
  for field in item.keys():
    if field not in accepted_fields and field != '_id':
      del item[field]

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, threaded=True, debug=True)
