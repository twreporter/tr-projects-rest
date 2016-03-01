# MONGO DATABASE SETTINGS
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = ''

# ALLOW ACTIONS
DEBUG = False
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE'] if DEBUG else ['GET']

schema = {
  'name': {
    'type': 'string',
  },
  'slug': {
    'type': 'string',
  },
  'title': {
    'type': 'string',
  },
  'subtitle': {
    'type': 'string',
  },
  'byline': {
    'type': 'string',
  },
  'state': {
    'type': 'string',
  },
  'author': {
    'type': 'list',
  },
  'publishedDate': {
    'type': 'string',
  },
  'image': {
    'type': 'string',
  },
  'categories': {
    'type': 'list',
  },
  'tags': {
    'type': 'list',
  },
  'style': {
    'type': 'string',
  },
  'content': {
    'type': 'dict',
    'schema': {
      'brief': {
        'type': 'string',
      },
      'extended': {
        'type': 'string',
      },
    }
  },
  'relateds': {
    'type': 'list',
  },
  'og_title': {
    'type': 'string',
  },
  'og_description': {
    'type': 'string',
  }
}

posts = {
    'item_title': 'post',
    'additional_lookup': {
        'url': 'regex("[\d]+")',
        'field': 'name'
    },
    'resource_methods': ['GET', 'POST'],
    'cache_control': 'max-age=300,must-revalidate',
    'cache_expires': 300,
    'allow_unknown': True,
    'schema': schema
}

DOMAIN = {'posts': posts}

XML = False
IF_MATCH = False
X_DOMAINS = '*'
X_HEADERS = ['Content-Type']
PAGINATION_DEFAULT = 10
