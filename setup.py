# -*- coding: utf-8 -*-
#
# This file is part of Flask-IIIF
# Copyright (C) 2014, 2015, 2016, 2017 CERN.
# Copyright (C) 2020 data-futures.
# Copyright (C) 2022 Graz University of Technology.
#
# Flask-IIIF is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""Flask-IIIF extension provides easy IIIF API standard integration."""

import os

from setuptools import setup

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('flask_iiif', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

tests_require = [
    'pytest',
    'mock',
    'flask-testing',
    'coverage',
    'isort',
    'pytest-cache',
    'pytest-cov',
    'itsdangerous',
    'sphinx',
    'redis',
    'werkzeug<3.0'
]

install_requires = [
    'Flask',
    'Flask-RESTful',
    'blinker',
    'six',
    'pillow',
    'cachelib',
    'funcsigs'
]

extra_require = {
    'docs': [
        'sphinx',
    ],
    'tests': tests_require,
}

extra_require['all'] = []
for reqs in extra_require.values():
    extra_require['all'].extend(reqs)

setup(
    name='Flask-IIIF',
    version=version,
    url='http://github.com/inveniosoftware/flask-iiif/',
    license='BSD',
    author='Invenio collaboration',
    author_email='info@inveniosoftware.org',
    description=__doc__,
    long_description=open('README.rst').read(),
    packages=['flask_iiif'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=install_requires,
    extras_require=extra_require,
    tests_require=tests_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Flask',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 5 - Production/Stable',
    ],
)
