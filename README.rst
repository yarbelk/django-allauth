==========================
Welcome to django-allauth!
==========================

.. image:: https://badge.fury.io/py/django-allauth.png
   :target: http://badge.fury.io/py/django-allauth

.. image:: https://travis-ci.org/pennersr/django-allauth.png
   :target: http://travis-ci.org/pennersr/django-allauth

.. image:: https://img.shields.io/pypi/v/django-allauth.svg
   :target: https://pypi.python.org/pypi/django-allauth

.. image:: https://coveralls.io/repos/pennersr/django-allauth/badge.png?branch=master
   :alt: Coverage Status
   :target: https://coveralls.io/r/pennersr/django-allauth

.. image:: https://pennersr.github.io/img/bitcoin-badge.svg
   :target: https://blockchain.info/address/1AJXuBMPHkaDCNX2rwAy34bGgs7hmrePEr

.. caution::
   This is rather application specific at the moment.  It is *really recomened* you use the main line
   `django-allauth` by pennersr unless you want to spend a lot of time tinkering in this code base.
   
   
This is a fork of https://github.com/pennersr/django-allauth that
is focused on supporting multiple `SocialApp`'s of the same type.
I.E, allow you to authenticate against multiple Facebook Pages as well
as multiple types of authenticators (providers - IE. G+, Facebook & Twitter).


It also adds basic swappable models for SocialApp.

Integrated set of Django applications addressing authentication,
registration, account management as well as 3rd party (social) account
authentication.

Home page
  http://www.intenct.nl/projects/django-allauth/

Source code
  http://github.com/pennersr/django-allauth

Mailinglist
  http://groups.google.com/group/django-allauth

Documentation
  http://django-allauth.readthedocs.org/en/latest/

Stack Overflow
  http://stackoverflow.com/questions/tagged/django-allauth

Rationale
=========

Most existing Django apps that address the problem of social
authentication focus on just that. You typically need to integrate
another app in order to support authentication via a local
account.

This approach separates the worlds of local and social
authentication. However, there are common scenarios to be dealt with
in both worlds. For example, an e-mail address passed along by an
OpenID provider is not guaranteed to be verified. So, before hooking
an OpenID account up to a local account the e-mail address must be
verified. So, e-mail verification needs to be present in both worlds.

Integrating both worlds is quite a tedious process. It is definitely
not a matter of simply adding one social authentication app, and one
local account registration app to your `INSTALLED_APPS` list.

This is the reason this project got started -- to offer a fully
integrated authentication app that allows for both local and social
authentication, with flows that just work.


Commercial Support
==================
This Version Isn't
------------------

This project is based off of https://github.com/pennersr/django-allauth
They have an option for commercial support of that version.  If you are 
interested in that, please go there and enquire
