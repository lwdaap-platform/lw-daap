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

from __future__ import absolute_import, print_function, unicode_literals

from invenio.ext.sqlalchemy import db
from invenio_accounts.models import Usergroup
#from lw_daap.modules.instruments.models import Instrument
#import lw_daap.modules.instruments.models
from lw_daap.modules.instruments.models import Instrument


class GroupInstrument(db.Model):
    __tablename__ = 'group_instrument'

    """ Fields """
    id = db.Column(db.Integer(255, unsigned=True),
                        nullable=False, primary_key=True,
                        )
    usergroup_id = db.Column(db.Integer(255, unsigned=True), db.ForeignKey(Usergroup.id),
                        nullable=False,
                        )

    instrument_id = db.Column(db.Integer(255, unsigned=True), db.ForeignKey(Instrument.id),
                              nullable=False,
                              )
