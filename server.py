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

def before_returning_posts(response):
    items = response['_items']
    new_response_array = []
    content_type = request.args.get('content_type')
    content = request.args.get('content')
    if (content and content == 'meta'):
        for item in items:
            del item['content']['extended']
            new_response_array.append(item)
        response['_items'] = new_response_array
    elif content_type: # check if we need to add the filter
        paragraph = ['brief', 'extended']
        content_type_array = content_type.split(',')
        for item in items:
            new_item = {}
            for type_seq in paragraph:
                if (type_seq in item['content'].keys()):
                    new_item[type_seq] = {}
                    for data_type in content_type_array:
                        if data_type in item['content'][type_seq].keys():
                            new_item[type_seq][data_type] = item['content'][type_seq][data_type]
            item['content'] = new_item
            new_response_array.append(item)
        response['_items'] = new_response_array

    return response

#app = Eve(auth=RolesAuth)
app = Eve()
app.on_replace_article += lambda item, original: remove_extra_fields(item)
app.on_insert_article += lambda items: remove_extra_fields(items[0])
app.on_insert_accounts += add_token
app.on_fetched_resource_posts += before_returning_posts

def remove_extra_fields(item):
  accepted_fields = schema.keys()
  for field in item.keys():
    if field not in accepted_fields and field != '_id':
      del item[field]

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, threaded=True, debug=True)
