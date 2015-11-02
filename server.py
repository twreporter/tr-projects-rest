from eve import Eve
from flask import redirect

app = Eve()

@app.route("/tag/<name>", methods=['GET'])
def tagSearch(name):
  return redirect('/article/?where={"tags":{"$in":["%s"]}}' % name, code=302)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, threaded=True, debug=True)
