# MONGO DATABASE SETTINGS
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = ''

# ALLOW ACTIONS
DEBUG = False
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE'] if DEBUG else ['GET']

schema = {
  'subtitle': {
    'type': 'string',
  },
  'availability': {
    'type': 'integer',
  },
  'byline': {
    'type': 'string',
  },
  'title': {
    'type': 'string',
  },
  'firstImage': {
    'type': 'string',
  },
  'excerpt': {
    'type': 'string',
  },
  'preset_tags': {
    'type': 'list',
  },
  'thumbnail': {
    'type': 'string',
  },
  'metadata': {
    'type': 'dict',
    'schema': {
      'metadata_text_key_name': {
        'type': 'string',
      },
    }
  },
  'lastUpdate': {
    'type': 'string',
  },
  'tags': {
    'type': 'list',
  },
  'author_display': {
    'type': 'string',
  },
  'slug': {
    'type': 'string',
  },
  'story_type': {
    'type': 'string',
  },
  'created': {
    'type': 'string',
  },
  'published': {
    'type': 'string',
  },
  'story_link': {
    'type': 'string',
  },
  'twitter_text': {
    'type': 'string',
  },
  'author_id': {
    'type': 'string',
  },
  'author_list': {
    'type': 'list',
  },
  'lastPublish': {
    'type': 'string',
  },
  'user_id': {
    'type': 'string',
  },
  'square_image': {
    'type': 'string',
  },
  'price_credits': {
    'type': 'string',
  },
  'createdBy': {
    'type': 'string',
  },
  'isPublishedVersion': {
    'type': 'boolean',
  },
  'facebook_text': {
    'type': 'string',
  },
  'id': {
    'type': 'integer',
  },
  'atavist_id': {
    'type': 'integer',
  },
  'status': {
    'type': 'string',
  },
  'pub_date': {
    'type': 'string',
  },
  'category_id': {
    'type': 'string',
  },
  'lastUpdateBy': {
    'type': 'string',
  },
  'url': {
    'type': 'string',
  },
  'protected_tags': {
    'type': 'list',
  },
  'preview_image': {
    'type': 'string',
  }
}

article = {
    'item_title': 'article',
    'additional_lookup': {
        'url': 'regex("[\d]+")',
        'field': 'id'
    },
    'datasource': {
      'filter': { 'isPublishedVersion': True}
    },
    'resource_methods': ['GET', 'POST'],
    'cache_control': 'max-age=300,must-revalidate',
    'cache_expires': 300,
    'allow_unknown': True,
    'schema': schema
}

DOMAIN = {'article': article}

XML = False
IF_MATCH = False
X_DOMAINS = '*'
PAGINATION_DEFAULT = 10
