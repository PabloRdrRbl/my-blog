#!usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = 'Pablo Rodríguez Robles'
SITENAME = 'Escribo las cosas que no quiero olvidar'
SITEURL = ''

EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }

PATH = 'content'
STATIC_PATHS = ['images', 'images/blog', 'extra/CNAME',
                'extra/custom.css', 'extra/robots.txt']

# Tell pelican where it should copy that file to in your output folder
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
}

TIMEZONE = 'Europe/Madrid'

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

# Theming
THEME = 'pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'

# Tell the pelican-bootstrap-3 theme where to find the custom.css file in
# your output folder
CUSTOM_CSS = 'static/custom.css'

DISPLAY_CATEGORIES_ON_MENU = False

FAVICON = 'images/blog/favicon.jpg'

ABOUT_ME = """
           Mi nombre es Pablo Rodríguez Robles y estudio Ingeniería Aeroespacial
           """
AVATAR = 'images/blog/profile.jpg'

BANNER = 'images/blog/banner.png'

GITHUB_USER = 'pablordrrbl'

PYGMENTS_STYLE = 'solarizeddark'

# Plugins

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'pelican_youtube',
    'render_math',
    'read_more_link',
    'simple_footnotes',
    'summary'
]

# Different plugin settings

# Better figures and images
# [https://github.com/getpelican/pelican-plugins/
# tree/master/better_figures_and_images]
#

# Pelican Youtube
# [https://github.com/kura/pelican_youtube/
# tree/0b72fdaf9dbbf2800bc0a463fbedd372b87808cd]
#

# Render Math
# [https://github.com/getpelican/pelican-plugins/
# tree/master/render_math]
#

MATH_JAX = {'color': 'black', 'align': 'center'}

# Summary
# [https://github.com/getpelican/pelican-plugins/
# tree/master/summary]
#
