# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'MolSanitizer'
copyright = "2024, Carlsson's Lab, Uppsala University"
author = 'Phong Lam, Israel Cabeza de Vaca, Szymon Pach'

release = '0.1.0'
version = '0.1.3'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
