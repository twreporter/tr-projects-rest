#! /usr/bin/python

import json
import urllib2
import subprocess
from sys import argv

if __name__ == '__main__':
  if len(argv) < 3:
    print 'usage: %s [host] [port] [url] [key]' % argv[0]
    exit()

  if len(argv) == 3:
    host = 'localhost'
    port = '80'
    url = argv[1]
    key = argv[2]
  else:
    host = argv[1]
    port = argv[2]
    url = argv[3]
    key = argv[4]
  data = json.load(urllib2.urlopen(url))[key]

  for record in data:
    _id = str(record['id'])
    pre = '0' * (24 - len(_id)) # used as mongo _id
    cmd = '''
    curl -d '%s' -X PUT -H 'Content-Type: application/json' http://%s:%s/article/%s
    ''' % (json.dumps(record), host, port, pre+_id)
    subprocess.Popen(cmd, shell=True)
