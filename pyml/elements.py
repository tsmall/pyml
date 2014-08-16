class Element(object):

    def __init__(self, tag_name, **attributes):
        self.tag_name = tag_name
        self.attributes = attributes

    def __call__(self, *args, **kwargs):
        if kwargs:
            return Element(self.tag_name, **kwargs)
        else:
            return '<{tag}{attributes}>{contents}</{tag}>'.format(
                tag=self.tag_name,
                attributes=self._render_attributes(),
                contents=''.join(args)
            )

    def _render_attributes(self):
        if not self.attributes:
            return ''

        kv_pairs = ('{}="{}"'.format(k, v) for k, v in self.attributes.items())
        return ' ' + ' '.join(kv_pairs)

