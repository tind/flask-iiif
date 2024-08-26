#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2014-2020 CERN.
# Copyright (C) 2022 Graz University of Technology.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

# Quit on errors
set -o errexit

# Quit on unbound symbols
set -o nounset

# TODO: We've temporarily removed the -W flag because of unresolvable warnings
# https://github.com/inveniosoftware/flask-iiif/commit/cd88709eaa0272435c7cbb54ba6df675d8b623a3
python -m sphinx.cmd.build -qnN docs docs/_build/html
python -m pytest
tests_exit_code=$?
exit "$tests_exit_code"
