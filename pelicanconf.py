#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'NeuroFedora'
SITENAME = 'The NeuroFedora Blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['tag_cloud', 'share_post']

# Theme
THEME = "theme-nice-blog"
THEME_COLOR = "green"
LOGO = "NeuroFedoraLogo01.png"
SIDEBAR_DISPLAY = ['about', 'categories', 'tags']
COPYRIGHT = '<a href="https://fedoraproject.org" target="_blank">Fedora project contributors</a>'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None

# Blogroll
MENUITEMS = (('News', '/blog_index.html'),
             ('Documentation', 'https://neuro.fedoraproject.org'),
             ('Fedora project', 'https://getfedora.org'),
             ('Archives', '/archives.html'),
             ('Tags', '/tags.html'),
             ('Categories', '/categories.html'),
             )

# Social widget
SOCIAL = (
    ('Mailing list', 'https://lists.fedoraproject.org/admin/lists/neuro-sig@lists.fedoraproject.org/'),
    ('IRC', 'https://webchat.freenode.net/?channels=#fedora-neuro'),
    ('Telegram', 'https://t.me/NeuroFedora'),
    ('Pagure', 'https://pagure.io/neuro-sig/NeuroFedora'),
    ('Github', 'https://github.com/neurofedora'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Static index page
INDEX_SAVE_AS = 'blog_index.html'

# Slugs for tags and so on
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

# Settings for article paths
ARTICLE_PATHS = ['']
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

ARCHIVES_SAVE_AS = 'archives.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'

TAG_CLOUD_STEPS = 6
TAG_CLOUD_MAX_ITEMS = 30
TAG_CLOUD_SORTING = 'random'

DELETE_OUTPUT_DIRECTORY = True
