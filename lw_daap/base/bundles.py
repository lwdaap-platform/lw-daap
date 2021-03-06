# -*- coding: utf-8 -*-
#
# This file is part of Lifewatch DAAP.
# Copyright (C) 2015 Ana Yaiza Rodriguez Marrero.
#
# Lifewatch DAAP is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Lifewatch DAAP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Lifewatch DAAP. If not, see <http://www.gnu.org/licenses/>.
#

# This file is part of Zenodo.
# Copyright (C) 2014 CERN.
##
# Zenodo is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
##
# Zenodo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
##
# You should have received a copy of the GNU General Public License
# along with Zenodo. If not, see <http://www.gnu.org/licenses/>.
##
# In applying this licence, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

"""Zenodo base bundles."""

from invenio.base.bundles import styles as _s, jquery as _j, invenio as _i

#
# Site-wide CSS
#
_s.contents += [
    "css/custom.css",
    "css/spacer.css",
    "css/footer.css",
    "css/header.css",
    "css/buttons.css",
    "css/panels.css",
    "css/dlc.css",
    "css/pid_badge.css"
]

#
# Site-wide JS
#
_i.contents += [
    "js/zenodo/init.js",
    "vendors/leaflet/dist/leaflet.js",
]
_i.bower.update({
    "zeroclipboard": "~2.1.6",
    "leaflet": "latest"
})

# Remove MathJax (served from CDN instead).
# del _j.bower['MathJax']

#
# Site-wide styles
#
# _s.contents.remove("less/base.less")
# _s.contents.remove("less/footer.less")
_s.contents += [
    "vendors/leaflet/dist/leaflet.css",
]
