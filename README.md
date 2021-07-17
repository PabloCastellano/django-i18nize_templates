django-i18nize-templates
=================

This is a working version for Django 3.0
A tool to automatically add i18n markup to Django and handlebars
templates.

The original tools worked for Jinja2 and Handlebars. But given the similitary
with Django templates, this repo contains a version that works with Django.

For more information, check out the original tool at
[csilvers/i18nize_templates](https://github.com/csilvers/i18nize_templates).

### What it does ###

This script will replace runs of natural language text with a
'translation marker'.  Most template libraries have built in support
for some translation markers, notably `{% trans %}` and `_(...)`.  We
use *only* the first form; we never use `{% trans %}`.
