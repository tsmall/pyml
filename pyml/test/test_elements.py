from unittest import TestCase

from pyml import *


class FullPageTests(TestCase):

    def test_full_page(self):
        """Should be able to render a complex page."""
        output = html(lang='en')(
            head(
                title('Test Page'),
            ),
            body(
                header(
                    nav(
                        ul(
                            li(a(href='/')('Home')),
                            li(a(href='/about')('About')),
                        ),
                    ),
                ),
                h1('Test Page'),
                section(id='main')(
                    h2('About'),
                    p('This is the about page.'),
                ),
                footer('Copyright 2014'),
            ),
        )
        expected = ''.join([
            '<html lang="en">',
              '<head>',
                '<title>Test Page</title>',
              '</head>',
              '<body>',
                '<header>',
                  '<nav>',
                    '<ul>',
                      '<li><a href="/">Home</a></li>',
                      '<li><a href="/about">About</a></li>',
                    '</ul>',
                  '</nav>',
                '</header>',
                '<h1>Test Page</h1>',
                '<section id="main">',
                  '<h2>About</h2>',
                  '<p>This is the about page.</p>',
                '</section>',
                '<footer>Copyright 2014</footer>',
              '</body>',
            '</html>',
        ])
        self.assertEqual(output, expected)


class NonemptyElementTests(TestCase):

    """Tests for the non-empty elements."""

    def test_no_contents(self):
        """Should be able to render an element without contents."""
        self.assertEqual(
            p(),
            '<p></p>'
        )

    def test_contents(self):
        """Should be able to render with simple string contents."""
        self.assertEqual(
            p('Hello world.'),
            '<p>Hello world.</p>'
        )
        self.assertEqual(
            div(p('Goodbye, ', em('cruel'), ' world!')),
            '<div><p>Goodbye, <em>cruel</em> world!</p></div>'
        )

    def test_attributes(self):
        """Should be able to render with only attributes."""
        self.assertEqual(
            div(id='foo')(),
            '<div id="foo"></div>'
        )
