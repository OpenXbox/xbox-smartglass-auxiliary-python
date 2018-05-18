=========================
Xbox-Smartglass-Auxiliary
=========================

.. image:: https://pypip.in/version/xbox-smartglass-auxiliary/badge.svg
    :target: https://pypi.python.org/pypi/xbox-smartglass-auxiliary/
    :alt: Latest Version

.. image:: https://readthedocs.org/projects/xbox-smartglass-auxiliary-python/badge/?version=latest
    :target: http://xbox-smartglass-auxiliary-python.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://travis-ci.com/OpenXbox/xbox-smartglass-auxiliary-python.svg?branch=master
    :target: https://travis-ci.com/OpenXbox/xbox-smartglass-auxiliary-python

This library provides the title channel / auxiliary stream extension of the SmartGlass protocol.
Only title that is making use of it currently is Fallout 4.

For in-depth information, check out the documentation: (https://openxbox.github.io)

Dependencies
------------
* Python >= 3.6
* xbox-smartglass-core

Install
-------

Via pip:
::

    pip install xbox-smartglass-auxiliary


How to use
----------

Authenticate first (Authentication provided by xbox-webapi-python):
::

    xbox-authenticate

    # alternatively: ncurses terminal ui
    xbox-auth-tui

Now you can use the relay script (Fallout 4 PipBoy)
::

    xbox-fo4-relay


Credits
-------
Kudos to joelday_ for figuring out the AuxiliaryStream / TitleChannel communication first!
You can find the original implementation here: DarkId.SmartGlass_.

Known issues
------------
* Find, report and/or fix them ;)

Contribute
----------
* Report bugs/suggest features
* Add/update docs

Credits
-------
This package uses parts of Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _joelday: https://github.com/joelday
.. _DarkId.SmartGlass: https://github.com/joelday/DarkId.SmartGlass
