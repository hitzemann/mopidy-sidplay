****************************
Mopidy-Sidplay
****************************

.. image:: https://img.shields.io/pypi/v/Mopidy-Sidplay.svg?style=flat
    :target: https://pypi.python.org/pypi/Mopidy-Sidplay/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/travis/hitzemann/mopidy-sidplay/master.svg?style=flat
    :target: https://travis-ci.org/hitzemann/mopidy-sidplay
    :alt: Travis CI build status

.. image:: https://img.shields.io/coveralls/hitzemann/mopidy-sidplay/master.svg?style=flat
   :target: https://coveralls.io/r/hitzemann/mopidy-sidplay
   :alt: Test coverage

Mopidy backend extension for .sid files

Not going to happen soon. I would need to provide an own library and file scanner. Mupidy already relies on gstreamer and gstreamer has everything you need. If that bug from 2014 regarding mime types is finally fixed it would be a patch against audio/scan.py only.


Installation
============

Install by running::

    pip install Mopidy-Sidplay

Or, if available, install the Debian/Ubuntu package from `apt.mopidy.com
<http://apt.mopidy.com/>`_.


Configuration
=============

Before starting Mopidy, you must add configuration for
Mopidy-Sidplay to your Mopidy configuration file::

    [sidplay]
    # TODO: Add example of extension config


Project resources
=================

- `Source code <https://github.com/hitzemann/mopidy-sidplay>`_
- `Issue tracker <https://github.com/hitzemann/mopidy-sidplay/issues>`_


Credits
=======

- Original author: `Simon Hitzemann <https://github.com/hitzemann`__
- Current maintainer: `Simon Hitzemann <https://github.com/hitzemann`__
- `Contributors <https://github.com/hitzemann/mopidy-sidplay/graphs/contributors>`_


Changelog
=========

v0.0.1 (UNRELEASED)
----------------------------------------

- Initial release.
