# MONGO DATABASE SETTINGS
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = ''

# ALLOW ACTIONS
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

schema = {
  'xorgAvailability': {
    'type': 'boolean',
  },
  'story_theme': {
    'type': 'string',
  },
  'manual_slug_set': {
    'type': 'boolean',
  },
  'subtitle': {
    'type': 'string',
  },
  'availability': {
    'type': 'integer',
  },
  'byline': {
    'type': 'string',
  },
  'suppress_toolbars': {
    'type': 'integer',
  },
  'title': {
    'type': 'string',
  },
  'wv_availability': {
    'type': 'integer',
  },
  'rev_of': {
    'type': 'string',
    'nullable': True,
  },
  'firstImage': {
    'type': 'string',
  },
  'title_page': {
    'type': 'string',
  },
  'minimum_version': {
    'type': 'string',
  },
  'disable_swipe_to_store': {
    'type': 'integer',
  },
  'suppress_jacket': {
    'type': 'integer',
  },
  'soundtrack_default_state': {
    'type': 'string',
  },
  'soundtrack_loop': {
    'type': 'integer',
  },
  'for_sale': {
    'type': 'string',
  },
  'publish_web': {
    'type': 'integer',
  },
  'weight': {
    'type': 'integer',
  },
  'excerpt': {
    'type': 'string',
  },
  'has_preview': {
    'type': 'integer',
  },
  'lastUpdateBy': {
    'type': 'string',
  },
  'has_1url': {
    'type': 'integer',
  },
  'preset_tags': {
    'type': 'list',
  },
  'story_template_prefix_pagination': {
    'type': 'string',
  },
  'story_template_prefix_hyphenate': {
    'type': 'string',
  },
  'last_cache': {
    'type': 'integer',
  },
  'facebook_image': {
    'type': 'string',
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
  'javascript': {
    'type': 'string',
  },
  'author_display': {
    'type': 'string',
  },
  'slug': {
    'type': 'string',
  },
  'preview_image': {
    'type': 'string',
  },
  'story_type': {
    'type': 'string',
  },
  'soundtrack': {
    'type': 'list',
  },
  'product_id': {
    'type': 'string',
  },
  'created': {
    'type': 'string',
  },
  'suppress_text_size': {
    'type': 'integer',
  },
  'story_template': {
    'type': 'string',
  },
  'cover_partial': {
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
  'options': {
    'type': 'dict',
    'schema': {
      'suppress_chapter_pointer': {
        'type': 'integer',
      },
      'story_theme': {
        'type': 'string',
      },
      'manual_slug_set': {
        'type': 'boolean',
      },
      'cms2': {
        'type': 'boolean',
      },
      'suppress_text_size': {
        'type': 'integer',
      },
      'story_template_prefix_drop_caps': {
        'type': 'string',
      },
      'story_template_prefix_hyphenate': {
        'type': 'string',
      },
      'publish_apps': {
        'type': 'integer',
      },
      'byline': {
        'type': 'string',
      },
      'suppress_toolbars': {
        'type': 'integer',
      },
      'story_template_prefix_pop-up_style': {
        'type': 'string',
      },
      'wv_availability': {
        'type': 'integer',
      },
      'story_template_prefix_pagination': {
        'type': 'string',
      },
      'last_cache': {
        'type': 'integer',
      },
      'metadata': {
        'type': 'dict',
        'schema': {
          'metadata_text_key_name': {
            'type': 'string',
          },
        }
      },
      'disable_swipe_to_store': {
        'type': 'integer',
      },
      'cover_type': {
        'type': 'string',
      },
      'story_template_prefix_map_style': {
        'type': 'string',
      },
      'suppress_jacket': {
        'type': 'integer',
      },
      'soundtrack_default_state': {
        'type': 'string',
      },
      'use_profile_for_byline': {
        'type': 'integer',
      },
      'soundtrack': {
        'type': 'list',
      },
      'soundtrack_loop': {
        'type': 'integer',
      },
      'commerce': {
        'type': 'integer',
      },
      'story_template_prefix_navigation_option': {
        'type': 'string',
      },
      'story_template_prefix_paragraph_spacing': {
        'type': 'string',
      },
      'story_template': {
        'type': 'string',
      },
      'cover_partial': {
        'type': 'string',
      },
      'suppress_slideoutnav': {
        'type': 'integer',
      },
      'publish_web': {
        'type': 'integer',
      },
      'suppress_chapter_number_display': {
        'type': 'integer',
      },
      'toc_icon': {
        'type': 'integer',
      },
    }
  },
  'isbn': {
    'type': 'string',
  },
  'cms2': {
    'type': 'boolean',
  },
  'author_list': {
    'type': 'list',
  },
  'story_template_prefix_drop_caps': {
    'type': 'string',
  },
  'publish_apps': {
    'type': 'integer',
  },
  'lastPublish': {
    'type': 'string',
  },
  'user_id': {
    'type': 'string',
  },
  'stylesheet': {
    'type': 'string',
  },
  'square_image': {
    'type': 'string',
  },
  'device_specific_options': {
    'type': 'string',
  },
  'cover_type': {
    'type': 'string',
  },
  'story_template_prefix_map_style': {
    'type': 'string',
  },
  'organization_id': {
    'type': 'string',
  },
  'price_credits': {
    'type': 'string',
  },
  'createdBy': {
    'type': 'string',
  },
  'commerce': {
    'type': 'integer',
  },
  'soundtrack_id': {
    'type': 'string',
  },
  'suppress_chapter_number_display': {
    'type': 'integer',
  },
  'toc_icon': {
    'type': 'integer',
  },
  'suppress_chapter_pointer': {
    'type': 'integer',
  },
  'isPublishedVersion': {
    'type': 'boolean',
  },
  'story_template_prefix_paragraph_spacing': {
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
  'story_template_prefix_pop-up_style': {
    'type': 'string',
  },
  'store_thumbnail': {
    'type': 'string',
  },
  'title_page_landscape': {
    'type': 'string',
  },
  'status': {
    'type': 'string',
  },
  'exclude_subscriptions': {
    'type': 'string',
  },
  'use_profile_for_byline': {
    'type': 'integer',
  },
  'suppress_slideoutnav': {
    'type': 'integer',
  },
  'device': {
    'type': 'string',
  },
  'pub_date': {
    'type': 'string',
  },
  'story_template_prefix_navigation_option': {
    'type': 'string',
  },
  'url': {
    'type': 'string',
  },
  'protected_tags': {
    'type': 'list',
  },
  'title_page_iphone': {
    'type': 'string',
  },
  'category_id': {
    'type': 'string',
  },
}

article = {
    'item_title': 'article',
    'additional_lookup': {
        'url': 'regex("[\d]+")',
        'field': 'id'
    },
    'resource_methods': ['GET', 'POST'],
    'cache_control': 'max-age=300,must-revalidate',
    'cache_expires': 300,
    'schema': schema
}

DOMAIN = {'article': article}

XML = False
IF_MATCH = False
