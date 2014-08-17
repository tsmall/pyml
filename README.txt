====
PyML
====

PyML (Python Markup Language) lets you generate your HTML using the
full power of Python instead of being limited to the subset available
in template libraries. I know it's not what you're probably used to,
but try it. I think you'll really like it.

There are a number of reasons this is a better way to create HTML.

* It's more concise.
* You don't have to learn something completely new.
* You're not arbitrarily limited to the supported template tags.
* Variable interpolation is easy: just use variables!
* Your code and template creation logic is in one place.
* It's more DRY.


Setting Up Your Dev Environment
-------------------------------

This project uses `Vagrant <http://www.vagrantup.com/>`_, so getting
set up should be a snap. Just make sure you have Vagrant installed and
then run this command::

  $ vagrant up


Running the Unit Tests
----------------------

Once your dev environment is up and running, these commands will run
the full test suite::

  $ vagrant ssh
  $ cd /vagrant
  $ nosetests
