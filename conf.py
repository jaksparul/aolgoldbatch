# conf.py

import os
import sys
sys.path.insert(0, os.path.abspath('.'))


# Project information
project = 'Official Guide: Download AOL Desktop Gold for Existing Member Without Re-Purchasing'
author = 'Documentation Team'


# -- General configuration ---------------------------------------------------


extensions = [
'myst_parser', # Markdown support
]


source_suffix = {
'.rst': 'restructuredtext',
'.md': 'markdown',
}


master_doc = 'index'


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------


html_theme = 'furo'