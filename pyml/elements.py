import warnings


class Element(object):

    def __init__(self, tag_name, is_empty=False, **attributes):
        self.tag_name = tag_name
        self.attributes = attributes
        self.is_empty = is_empty

    def __call__(self, *args, **kwargs):
        if kwargs:
            return Element(self.tag_name, self.is_empty, **kwargs)
        else:
            return '{opening_tag}{contents}{closing_tag}'.format(
                opening_tag=self.opening_tag,
                contents=self._render_contents(*args),
                closing_tag=self.closing_tag,
            )

    @property
    def opening_tag(self):
        return '<{tag}{attributes}>'.format(
            tag=self.tag_name,
            attributes=self._render_attributes(),
        )

    @property
    def closing_tag(self):
        if self.is_empty:
            return ''
        return '</{}>'.format(self.tag_name)

    def _render_attributes(self):
        if not self.attributes:
            return ''

        kv_pairs = (
            '{}="{}"'.format(_fix_attribute_name(k), v)
            for k, v in self.attributes.items()
        )
        return ' ' + ' '.join(kv_pairs)

    def _render_contents(self, *contents):
        if self.is_empty:
            if contents:
                warnings.warn(
                    "Attempting to add contents to an empty element",
                    UserWarning
                )
            return ''
        return ''.join(contents)


def _fix_attribute_name(name):
    if name.startswith('_'):
        return name[1:]
    elif '_' in name:
        return name.replace('_', '-')
    else:
        return name
