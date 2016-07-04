#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Pablo Rodríguez Robles'
SITENAME = 'Escribo las cosas que no quiero olvidar.'
#SITEURL = 'pablorrobles.com'

EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

PATH = 'content'
STATIC_PATHS = ['images', 'extra/CNAME']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/PabloRdrRbl'),
          ('linkedin', 'https://es.linkedin.com/in/pablordrrbl'),
          ('github', 'http://github.com/PabloRdrRbl'))

DEFAULT_PAGINATION = 5

# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['render_math']

# Different plugin settings
MATH_JAX = {'color': 'blue', 'align': 'left'}

# Theming
THEME = 'pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'

DISPLAY_CATEGORIES_ON_MENU = False

FAVICON = 'images/blog/favicon.jpg'

ABOUT_ME = """
           Mi nombre es Pablo Rodríguez Robles y estudio Ingeniería Aeroespacial
           """
AVATAR = 'images/blog/profile.jpg'

BANNER = 'images/blog/banner.png'

GITHUB_USER = 'pablordrrbl'

PYGMENTS_STYLE = 'solarizeddark'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
