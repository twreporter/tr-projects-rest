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
    print heroImage
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

def before_returning_posts(response):
    items = response['_items']
    for item in items:
        if 'brief' in item:
            del item['brief']['draft']
            del item['brief']['html']
        if 'content' in item:
            del item['content']['draft']
            del item['content']['html']
        if 'heroImage' in item:
            if item['heroImage'] is not None:
                item['heroImage'] = filter_hero_image(item['heroImage'])
        if 'leading_video' in item:
            if item['leading_video'] is not None:
                item['leading_video'] = filter_hero_image(item['leading_video'])
    return response

#app = Eve(auth=RolesAuth)
app = Eve()

app.on_replace_article += lambda item, original: remove_extra_fields(item)
app.on_insert_article += lambda items: remove_extra_fields(items[0])
app.on_insert_accounts += add_token
app.on_fetched_resource_meta += before_returning_meta
app.on_fetched_resource_posts += before_returning_posts

def remove_extra_fields(item):
  accepted_fields = schema.keys()
  for field in item.keys():
    if field not in accepted_fields and field != '_id':
      del item[field]

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, threaded=True, debug=True)
