try:
    from html.parser import HTMLParseError
except ImportError:  # Python 3.5+
    class HTMLParseError(Exception):
        pass
