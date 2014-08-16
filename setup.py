from distutils.core import setup

setup(
    name='PyML',
    version='0.1.0',
    author='Tom Small III',
    author_email='tsmall@gmail.com',
    packages=['pyml', 'pyml.test'],
    url='http://github.com/tsmall/pyml',
    license='LICENSE.txt',
    description='Pure Python HTML generation.',
    long_description=open('README.txt').read(),
)
