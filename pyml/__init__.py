from pyml.elements import Element


NONEMPTY_ELEMENTS = [
    'a',
    'body',
    'button',
    'div',
    'em',
    'footer',
    'h1',
    'h2',
    'h3',
    'h4',
    'h5',
    'head',
    'header',
    'html',
    'li',
    'nav',
    'ol',
    'p',
    'script',
    'section',
    'span',
    'strong',
    'title',
    'ul',
]


__all__ = NONEMPTY_ELEMENTS


locals().update({tag_name: Element(tag_name) for tag_name in NONEMPTY_ELEMENTS})
