#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'NeuroFedora'
SITENAME = 'NeuroFedora: Blog'
DESCRIPTION = "Free Software for Free Neuroscience"
SITESUBTITLE = "Free Software for Free Neuroscience"
SITEURL = ''

PATH = 'content'

# Let it use UTC
#  TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['tag_cloud', 'share_post']

# Theme
THEME = "theme-alchemy/alchemy"
SITEIMAGE = "/NeuroFedoraLogo01-title.png"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None

# Blogroll
LINKS = (('Posts', '/blog_index.html'),
         ('Documentation', 'https://neuro.fedoraproject.org'),
         )

# Social widget
ICONS = (
    ('fas fa-mail-bulk',
     'https://lists.fedoraproject.org/admin/lists/neuro-sig@lists.fedoraproject.org/',
     'Mailing list'),
    ('fas fa-comments', 'https://webchat.freenode.net/?channels=#fedora-neuro',
     "Chat"),
    ('fab fa-telegram', 'https://t.me/NeuroFedora',
     "Telegram"),
    ('fas fa-code-branch', 'https://pagure.io/neuro-sig/NeuroFedora',
     "Tickets"),
    ('fab fa-github', 'https://github.com/neurofedora',
     "Github"),
    ('fas fa-bug',
     'https://tinyurl.com/neurofedora-bugs',
     "Bugs"),
    ('fab fa-fedora', 'https://getfedora.org',
     "Get Fedora!"),
    ('fas fa-rss', '/feeds/all.atom.xml',
     "RSS feeds"),
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

# Favicon etc.
STATIC_PATHS = [
    'images',
    'extra',
]

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/NeuroFedoraLogo01-title.png': {'path': 'NeuroFedoraLogo01-title.png'}
}
