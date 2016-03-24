from eve import Eve
from flask import redirect, request, Response
from settings import posts, users
import json

def before_returning_posts(response):
    items = response['_items']
    new_response_array = []
    paragraph = ['brief', 'extended']
    content_type = request.args.get('content_type')
    if content_type: # check if we need to add the filter
        content_type_array = content_type.split(',')
        for item in items:
            new_item = {}
            for type_seq in paragraph:
                new_item[type_seq] = {}
                for data_type in content_type_array:
                    if data_type in item['content'][type_seq].keys():
                        new_item[type_seq][data_type] = item['content'][type_seq][data_type]
            item['content'] = new_item
            new_response_array.append(item)
        response['_items'] = new_response_array
    else: # there is no parameter for paragraph, so we won't add the filter for the content
        return response

app = Eve()
app.on_replace_article += lambda item, original: remove_extra_fields(item)
app.on_insert_article += lambda items: remove_extra_fields(items[0])
app.on_fetched_resource_posts += before_returning_posts

def remove_extra_fields(item):
  accepted_fields = schema.keys()
  for field in item.keys():
    if field not in accepted_fields and field != '_id':
      del item[field]

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, threaded=True, debug=True)
