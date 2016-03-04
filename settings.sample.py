# MONGO DATABASE SETTINGS
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'keystone-test'

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
  'authors': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'contacts',
            'field': '_id',
            'embeddable': True
        },
    },
  },
  'publishedDate': {
    'type': 'string',
  },
  'image': {
    'type': 'string',
  },
  'categories': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'postcategories',
            'field': '_id',
            'embeddable': True
         },
     },
  },
  'tags': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'tags',
            'field': '_id',
            'embeddable': True
         },
     },
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
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'posts',
            'field': '_id',
            'embeddable': True
         },
     }, 
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
    'allow_unknown': False,
    'schema': post_schema
}

users = {
    'item_title': 'user',
    'additional_lookup': {
        'url': 'regex(".+")',
        'field': 'name'
    },
    'resource_methods': ['GET', 'POST'],
    'cache_control': 'max-age=300,must-revalidate',
    'cache_expires': 300,
    'allow_unknown': False,
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

tags = {
    'item_title': 'tag',
    'additional_lookup': {
        'url': 'regex(".+")',
        'field': 'name'
    },
    'resource_methods': ['GET', 'POST'],
    'cache_control': 'max-age=300,must-revalidate',
    'cache_expires': 300,
    'allow_unknown': True,
    'schema': {
      'name': {
        'type': 'string',
      }
    }
}

postcategories = {
    'item_title': 'postcategory',
    'additional_lookup': {
        'url': 'regex(".+")',
        'field': 'name'
    },
    'resource_methods': ['GET', 'POST'],
    'cache_control': 'max-age=300,must-revalidate',
    'cache_expires': 300,
    'allow_unknown': True,
    'schema': {
      'name': {
        'type': 'string',
      }
    }
}

DOMAIN = {
    'posts': posts,
    'users': users,
    'contacts': contacts,
    'tags': tags,
    'postcategories': postcategories,
    }

XML = False
IF_MATCH = False
X_DOMAINS = '*'
X_HEADERS = ['Content-Type']
PAGINATION_DEFAULT = 10
