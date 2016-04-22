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
        'type': 'dict',
        'schema': {
            "html": {
                "type": "string",
            },
        },
      },
      'extended': {
        'type': 'dict',
        'schema': {
            "html": {
                "type": "string",
            },
        },
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
    'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
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
    'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
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

member_schema = {
  'member_id': {
    'type': 'string',
    'required': True,
  },
  'email': {
    'type': 'string',
    'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
  },
  'password': {
    'type': 'string',
    'required': True,
  },
  'country': {
    'type': 'string',
  },
  'city': {
    'type': 'string',
  },
  'address': {
    'type': 'string',
  },
  'zip': {
    'type': 'interger',
  },
  'gender': {
    'type': 'string',
  },
  'state': {
      'type': 'dict',
      'schema': {
          'bookmark': {
            'type': 'list',
            'schema': {
              'type': 'objectid',
              'data_relation': {
                'resource': 'posts',
                'field': '_id',
                'embeddabole': True
              },
            },
          },
          'bookmark_count': {
            'type': 'integer',
          },
          'position': {
            'type': 'string',
          }
      },
  },
  'create_date': {
    'type': 'datetime',
  }
}

account_schema = {
    'username': {
       'type': 'string',
       'required': True,
       'unique': True,
    },
    'password': {
       'type': 'string',
       'required': True,
    },
    'roles': {
        'type': 'list',
        'allowed': ['user', 'superuser', 'admin'],
        'required': True,
    },
    'token': {
        'type': 'string',
        'required': True,
    }
}

posts = {
    'item_title': 'post',
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'slug'
    },
    'datasource': {
        'source': 'posts',
        'filter': {'state': 'published'},
    },
    'resource_methods': ['GET'],
    'cache_control': 'max-age=300,must-revalidate',
    'cache_expires': 300,
    'allow_unknown': False,
    'schema': post_schema
}

drafts = {
    'item_title': 'draft',
    'additional_lookup': {
        'url': 'regex("[\d]+")',
        'field': 'slug'
    },
    'datasource': {
        'source': 'posts',
        'filter': {'state': 'draft'},
    },
    'resource_methods': ['GET'],
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
    'resource_methods': ['GET'],
    'cache_control': 'max-age=300,must-revalidate',
    'cache_expires': 300,
    'allow_unknown': False,
    'schema': user_schema
}

members = {
    'item_title': 'member',
    'additional_lookup': {
        'url': 'regex("\w+")',
        'field': 'member_id'
    },
    'resource_methods': ['GET', 'POST'],
    'cache_control': 'max-age=300,must-revalidate',
    'cache_expires': 300,
    'allow_unknown': False,
    'schema': member_schema
}

contacts = {
    'item_title': 'contact',
    'additional_lookup': {
        'url': 'regex(".+")',
        'field': 'name'
    },
    'resource_methods': ['GET'],
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
    'resource_methods': ['GET'],
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
    'resource_methods': ['GET'],
    'cache_control': 'max-age=300,must-revalidate',
    'cache_expires': 300,
    'allow_unknown': True,
    'schema': {
      'name': {
        'type': 'string',
      }
    }
}

account = {
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'username',
    },
    'resource_methods': ['GET', 'POST'],
    'allowed_roles': ['superuser', 'admin'],
    'cache_control': '',
    'cache_expires': 0,
    'schema': account_schema,
}

DOMAIN = {
    'posts': posts,
    'drafts': drafts,
    'users': users,
    'members': members,
    'contacts': contacts,
    'tags': tags,
    'postcategories': postcategories,
    'account': account,
    }

XML = False
IF_MATCH = False
X_DOMAINS = '*'
X_HEADERS = ['Content-Type']
PAGINATION_DEFAULT = 10
