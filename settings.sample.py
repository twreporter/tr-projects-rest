# MONGO DATABASE SETTINGS
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = ''

# ALLOW ACTIONS
DEBUG = False
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE'] if DEBUG else ['GET']

post_schema = {
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

user_schema = {
  'name': {
    'type': 'string',
  },
  'email': {
    'type': 'string',
  },
  'role': {
    'type': 'string',
  },
  'company': {
    'type': 'string',
  },
  'address': {
    'type': 'string',
  }
}

contact_schema = {
  'name': {
    'type': 'string',
  },
  'email': {
    'type': 'string',
  },
  'homepage': {
    'type': 'string',
  },
  'facebook': {
    'type': 'string',
  },
  'twitter': {
    'type': 'string',
  },
  'instantgram': {
    'type': 'string',
  },
  'bio': {
    'type': 'string',
  }
}

posts = {
    'item_title': 'post',
    'additional_lookup': {
        'url': 'regex("[\d]+")',
        'field': 'slug'
    },
    'resource_methods': ['GET', 'POST'],
    'cache_control': 'max-age=300,must-revalidate',
    'cache_expires': 300,
    'allow_unknown': True,
    'schema': post_schema
}

users = {
    'item_title': 'user',
    'additional_lookup': {
        'url': 'regex("[\d]+")',
        'field': 'name'
    },
    'resource_methods': ['GET', 'POST'],
    'cache_control': 'max-age=300,must-revalidate',
    'cache_expires': 300,
    'allow_unknown': True,
    'schema': user_schema
}

contacts = {
    'item_title': 'contact',
    'additional_lookup': {
        'url': 'regex(".+")',
        'field': 'name'
    },
    'resource_methods': ['GET', 'POST'],
    'cache_control': 'max-age=300,must-revalidate',
    'cache_expires': 300,
    'allow_unknown': True,
    'schema': contact_schema
}

DOMAIN = {
    'posts': posts,
    'users': users,
    'contacts': contacts,
    }

XML = False
IF_MATCH = False
X_DOMAINS = '*'
X_HEADERS = ['Content-Type']
PAGINATION_DEFAULT = 10
