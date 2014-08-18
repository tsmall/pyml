from unittest import TestCase
import warnings

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
        """Should be able to render with contents."""
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

    def test_attributes_reserved_words(self):
        """Should be able to avoid reserved words with leading `_`."""
        self.assertEqual(
            div(_class='test')(),
            '<div class="test"></div>'
        )

    def test_attributes_hyphenated(self):
        """Should be able to generate hyphenated attributes."""
        self.assertEqual(
            div(data_id="1")("Test"),
            '<div data-id="1">Test</div>'
        )


class EmptyElementTests(TestCase):

    """Tests for the empty elements."""

    def test_no_attributes(self):
        """Should be able to render an element without attributes."""
        self.assertEqual(
            br(),
            '<br>'
        )

    def test_attributes(self):
        """Empty elements should support attributes."""
        self.assertEqual(
            meta(charset='utf-8')(),
            '<meta charset="utf-8">'
        )

    def test_warning_on_contents(self):
        """Empty elements can't have contents, so trying causes a warning."""
        with warnings.catch_warnings(record=True) as w:
            br('Hi!')
            self.assertEqual(len(w), 1)
            self.assertTrue(issubclass(w[0].category, UserWarning))

    def test_no_warning_if_no_contents(self):
        """Shouldn't issue a warning if there are no contents."""
        with warnings.catch_warnings(record=True) as w:
            br()
            self.assertEqual(len(w), 0)