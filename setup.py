#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name="xbox-smartglass-auxiliary",
    version="0.9.1",
    author="OpenXbox",
    description="Title channel / AuxiliaryStream extension of the Xbox One SmartGlass protocol.",
    long_description=open('README.rst').read() + '\n\n' + open('HISTORY.rst').read(),
    license="GPL",
    keywords="xbox one auxiliary fallout title smartglass",
    url="https://github.com/OpenXbox/xbox-smartglass-auxiliary-python",
    packages=[
        'xbox.auxiliary',
        'xbox.auxiliary.scripts'
    ],
    namespace_packages=['xbox'],
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6"
    ],
    install_requires=[
        'xbox-smartglass-core'
    ],
    tests_require=[
        'pytest',
        'flake8',
        'tox'
    ],
    extras_require={
        'dev': [
            'bumpversion',
            'watchdog',
            'coverage',
            'Sphinx',
            'wheel',
            'twine'
        ]
    },
    test_suite="tests",
    entry_points={
        'console_scripts': [
            'xbox-fo4-relay=xbox.auxiliary.scripts.fo4:main'
        ]
    }
)
