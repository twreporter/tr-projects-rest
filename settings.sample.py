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
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'contacts',
            'field': '_id',
            'embeddable': True
        },
    },
  },
  'author_display': {
    'type': 'string',
  },
  'slug': {
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
  'published': {
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
  'author_list': {
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
  'facebook_enable': {
    'type': 'integer',
  },
  'facebook_image': {
    'type': 'string',
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
          'post': {
            'type': 'objectid',
            'data_relation': {
              'resource': 'posts',
              'field': '_id',
              'embeddable': True
            },
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

posts = {
    'item_title': 'post',
    'additional_lookup': {
        'url': 'regex("[\d]+")',
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

DOMAIN = {
    'posts': posts,
    'drafts': drafts,
    'users': users,
    'members': members,
    'contacts': contacts,
    'tags': tags,
    'postcategories': postcategories,
    }

XML = False
IF_MATCH = False
X_DOMAINS = '*'
X_HEADERS = ['Content-Type']
PAGINATION_DEFAULT = 10
