django-i18nize-templates
=================

This is a working version for Django 3.0
A tool to automatically add i18n markup to Django and handlebars
templates.

The original tools worked for Jinja2 and Handlebars. But given the similitary
with Django templates, this repo contains a version that works with Django.

For more information, check out the original tool at
[csilvers/i18nize_templates](https://github.com/csilvers/i18nize_templates).

This is part of a process to make a non-i18n-aware jinja2 or
handlebars file i18n-aware.  i18n-ness support is mostly a matter of
marking natural-language text in the file that needs to be translated.
While some complicated natural language constructs (like plurals)
require a bit more work, the simple case is very simple: replace

    <p>Hello <b>world</b></p>

with

    <p>{% trans "Hello <b>world</b>" %}</p>

This script helps with that process.


Use
---

    i18nize-templates <file> ...

OR

    i18nize-templates [--handlebars] < <infile> > <outfile>

In the first use-case, the files are modified in-place.  In the second
use-case, infile is assumed to be a Django template unless
--handlebars is specified.

### What it does ###

This script will replace runs of natural language text with a
'translation marker'.  Most template libraries have built in support
for some translation markers, notably `{% trans %}` and `_(...)`.  We
use *only* the first form; we never use `{% trans %}`.
