from eve import Eve
from eve.auth import TokenAuth
from flask import redirect, request, Response
from settings import posts, users
import json
import random
import string

class RolesAuth(TokenAuth):
    def check_auth(self, token,  allowed_roles, resource, method):
    # use Eve's own db driver; no additional connections/resources are used
        accounts = app.data.driver.db['accounts']
        lookup = {'token': token}
        if allowed_roles:
            # only retrieve a user if his roles match ``allowed_roles``
            lookup['roles'] = {'$in': allowed_roles}
        account = accounts.find_one(lookup)
        return account

def add_token(documents):
    for document in documents:
        document["token"] = (''.join(random.choice(string.ascii_uppercase)
                                    for x in range(10)))

def filter_hero_image(heroImage):
    if 'image' in heroImage: 
        image = filter_gcs_info(heroImage['image'])
        heroImage['image'] = image
    return heroImage

def filter_leading_video(leadingVideo):
    if 'video' in leadingVideo: 
        video = filter_gcs_info(leadingVideo['video'])
        leadingVideo['video'] = video
    return leadingVideo

def filter_gcs_info(gcsObj):
    if 'gcsDir' in gcsObj:
      del gcsObj['gcsDir']
    if 'gcsBucket' in gcsObj:
      del gcsObj['gcsBucket']
    if 'filename' in gcsObj:
      del gcsObj['filename']
    return gcsObj 

def get_relateds(item, key):
    if key in item and item[key]:
        headers = dict(request.headers)
        tc = app.test_client()
        all_relateds =  ",".join(map(lambda x: '"' + str(x) + '"',item[key]))
        resp = tc.get('meta?where={"_id":{"$in":[' + all_relateds + ']}}', headers=headers)
        resp_data = json.loads(resp.data)
        result = []
        for i in item[key]: 
            for j in resp_data['_items']:
                if j['_id'] == str(i):
                    result.append(j)
                    continue
        item[key] = result
        # item[key] = resp_data['_items']
    return item

def before_returning_meta(response):
    items = response['_items']
    for item in items:
        if 'brief' in item:
            del item['brief']['draft']
            del item['brief']['html']
        if 'heroImage' in item:
            if item['heroImage'] is not None:
                item['heroImage'] = filter_hero_image(item['heroImage'])
    return response

def get_topic(topic_id):
  headers = dict(request.headers)
  tc = app.test_client()
  resp = tc.get('topics/' + str(topic_id) , headers=headers)
  resp_data = json.loads(resp.data)
  return resp_data

def filter_post(item):
  if 'brief' in item:
    del item['brief']['draft']
    del item['brief']['html']
  if 'content' in item:
    del item['content']['draft']
    del item['content']['html']
  if 'heroImage' in item:
    if type(item['heroImage']) is dict:
      item['heroImage'] = filter_hero_image(item['heroImage'])
  if 'leading_video' in item:
    if type(item['leading_video'] is dict):
      item['leading_video'] = filter_leading_video(item['leading_video'])
  return item

def before_returning_posts(response):
    items = response['_items']
    for item in items:
      item = before_returning_post(item)
    return items

def before_returning_post(response):
  item = filter_post(response)
  # check if topic object is to be embedded
  topics = str(request.args.get('embedded')).find('topics')

  if topics > -1 and 'topics' in item: 
    item['topics'] = get_topic(item['topics'])
  return item

def filter_topics(items):
    for item in items:
        item = filter_topic(item)
    return items

def filter_topic(item): 
    if 'description' in item:
      del item['description']['draft']
      del item['description']['apiData']
    if 'team_description' in item:
      del item['team_description']['draft']
      del item['team_description']['apiData']
    if 'leading_image' in item:
      if type(item['leading_image']) is dict:
        item['leading_image'] = filter_hero_image(item['leading_image'])
    if 'leading_image_portrait' in item:
      if type(item['leading_image_portrait']) is dict:
        item['leading_image_portrait'] = filter_hero_image(item['leading_image_portrait'])
    if 'leading_video' in item:
      if type(item['leading_video']) is dict:
        item['leading_video'] = filter_leading_video(item['leading_video'])
    return item

def before_returing_topics(response): 
    items = response['_items']
    for item in items:
        item = before_returning_topic(item)
    return response

def before_returning_topic(response):
    item = filter_topic(response)
    item = get_relateds(item, 'relateds')
    return item

#app = Eve(auth=RolesAuth)
app = Eve()
app.on_fetched_resource_meta += before_returning_meta
app.on_fetched_resource_posts += before_returning_posts
app.on_fetched_item_posts += before_returning_post
app.on_fetched_resource_topics += before_returing_topics
app.on_fetched_item_topics += before_returning_topic

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, threaded=True, debug=True)
