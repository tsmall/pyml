from pyml.elements import Element


NONEMPTY_ELEMENTS = [
    'a',
    'body',
    'button',
    'div',
    'em',
    'p',
    'script',
    'span',
    'strong',
]


__all__ = NONEMPTY_ELEMENTS


locals().update({tag_name: Element(tag_name) for tag_name in NONEMPTY_ELEMENTS})
