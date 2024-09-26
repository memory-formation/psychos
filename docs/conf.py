# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import pkg_resources

sys.path.append(os.path.abspath(".."))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

try:
    release = pkg_resources.get_distribution("psychos").version
except pkg_resources.DistributionNotFound:
    print(
        "To build the documentation, the distribution information of "
        "psychos has to be available. Either install the package "
        'into your development environment or run "setup.py develop" '
        "to setup the metadata. A virtualenv is recommended. "
    )
    sys.exit(1)

project = "psychos"
copyright = "2024, DMF Group, University of Barcelona"
author = "Dynamics of Memory Formation Group (DMF)"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
]


exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "autosummary/psychos.*.*.*.rst",  # 3 levels of depth
    "autosummary/psychos.*.rst",
]

# Add mappings
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "pyglet": ("https://pyglet.readthedocs.io/en/latest/", None),
}
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "inherited-members": False,
    "show-inheritance": False,
}
autosummary_generate = True


language = "en"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_favicon = "assets/psychos-icon.svg"
html_logo = "assets/psychos.svg"
html_logo_dark = "assets/psychos-dark.svg"
html_logo_compact = "assets/psychos-compact.svg"
html_logo_dark_compact = "assets/psychos-dark-compact.svg"
html_theme_options = {
    "github_url": "https://github.com/memory-formation/psychos",
    "logo": {
        "text": "psychos",
    },
    "icon_links": [
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/psychos",
            "icon": "fab fa-python",
        },
        {
            "name": "DMF",
            "url": "https://brainvitge.org/groups/memory_formation/",
            "icon": "https://brainvitge.org/website/wp-content/themes/brainvitge/library/images/brainvitge-logo-45x40.png",
            "type": "url",
        },
    ],
    "logo": {
        "image_light": html_logo_compact,
        "image_dark": html_logo_dark_compact,
    },
}
html_context = {
    "github_user": "memory-formation",
    "github_repo": "psychos",
    "github_version": "main",
    "doc_path": "docs",
}

html_sidebars = {"content/license": []}
