from pyml.elements import Element


EMPTY_ELEMENTS = [
    'br',
    'link',
    'meta',
    'input',
]


NONEMPTY_ELEMENTS = [
    'a',
    'abbr',
    'article',
    'aside',
    'blockquote',
    'body',
    'button',
    'code',
    'div',
    'em',
    'footer',
    'form',
    'h1',
    'h2',
    'h3',
    'h4',
    'h5',
    'head',
    'header',
    'html',
    'label',
    'li',
    'nav',
    'ol',
    'p',
    'script',
    'section',
    'span',
    'strong',
    'textarea',
    'title',
    'ul',
]


__all__ = EMPTY_ELEMENTS + NONEMPTY_ELEMENTS


locals().update({tag_name: Element(tag_name, is_empty=True) for tag_name in EMPTY_ELEMENTS})
locals().update({tag_name: Element(tag_name) for tag_name in NONEMPTY_ELEMENTS})
