#! /usr/bin/python

# ########################################################################### #
# #                                                                         # #
# # Copyright (c) 2009-2016 Neil Wallace <neil@openmolar.com>               # #
# #                                                                         # #
# # This file is part of OpenMolar.                                         # #
# #                                                                         # #
# # OpenMolar is free software: you can redistribute it and/or modify       # #
# # it under the terms of the GNU General Public License as published by    # #
# # the Free Software Foundation, either version 3 of the License, or       # #
# # (at your option) any later version.                                     # #
# #                                                                         # #
# # OpenMolar is distributed in the hope that it will be useful,            # #
# # but WITHOUT ANY WARRANTY; without even the implied warranty of          # #
# # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           # #
# # GNU General Public License for more details.                            # #
# #                                                                         # #
# # You should have received a copy of the GNU General Public License       # #
# # along with OpenMolar.  If not, see <http://www.gnu.org/licenses/>.      # #
# #                                                                         # #
# ########################################################################### #

import datetime
import hashlib
import logging

from PyQt5 import QtWidgets

from openmolar.settings import localsettings
from openmolar.dbtools import db_settings
from openmolar.qt4gui.customwidgets.warning_label import WarningLabel
from openmolar.qt4gui.dialogs.base_dialogs import BaseDialog

LOGGER = logging.getLogger("openmolar")


def _hashed_input(input_):
    salted_input = "%s%s" % (input_, localsettings.SALT)
    return hashlib.sha1(salted_input.encode("utf8")).hexdigest()


class RaisePermissionsDialog(BaseDialog):

    def __init__(self, parent=None):
        BaseDialog.__init__(self, parent)
        self.setWindowTitle(_("Raise Permissions Dialog"))
        self.label = WarningLabel("%s<hr />%s" % (
            _("Supervisor privileges required to perform this action"),
            _("Please enter the supervisor password")))

        frame = QtWidgets.QFrame()
        self.form_layout = QtWidgets.QFormLayout(frame)
        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.form_layout.addRow(_("Supervisor Password"), self.line_edit)

        self.insertWidget(self.label)
        self.insertWidget(frame)
        self.enableApply()
        self.line_edit.setFocus(True)

    @property
    def correct_password(self):
        return _hashed_input(self.line_edit.text()) == \
            localsettings.SUPERVISOR

    def exec_(self):
        if not BaseDialog.exec_(self):
            return False
        if self.correct_password:
            localsettings.permissionsRaised = True
            resetExpireTime()
            return True
        else:
            QtWidgets.QMessageBox.information(
                self, _("whoops"),
                _("incorrect supervisor password"))
        return False


class ResetSupervisorPasswordDialog(RaisePermissionsDialog):

    def __init__(self, parent=None):
        RaisePermissionsDialog.__init__(self, parent)

        self.label.setText(_("Reset Supervisor Password"))
        self.new_password_line_edit = QtWidgets.QLineEdit()
        self.confirm_password_line_edit = QtWidgets.QLineEdit()

        self.new_password_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_password_line_edit.setEchoMode(
            QtWidgets.QLineEdit.Password)

        self.form_layout.addRow(_("New Password"), self.new_password_line_edit)
        self.form_layout.addRow(_("Confirm New Password"),
                                self.confirm_password_line_edit)

    @property
    def _new_password(self):
        return self.new_password_line_edit.text()

    def passwords_match(self):
        if self._new_password == \
                self.confirm_password_line_edit.text():
            return True
        QtWidgets.QMessageBox.warning(self, _("error"),
                                      _("new passwords didn't match"))

    def exec_(self):
        if not RaisePermissionsDialog.exec_(self):
            return False
        if self.passwords_match():
            localsettings.SUPERVISOR = _hashed_input(self._new_password)
            db_settings.updateData("supervisor_pword",
                                   localsettings.SUPERVISOR,
                                   localsettings.operator)
            message = _("password changed successfully")
        else:
            message = _("Password unchanged")
        QtWidgets.QMessageBox.information(self, _("information"), message)


def granted(parent=None):
    if localsettings.permissionsRaised:
        if localsettings.permissionExpire > datetime.datetime.now():
            resetExpireTime()
            return True
        else:
            localsettings.permissionsRaised = False

    dl = RaisePermissionsDialog(parent)
    return dl.exec_()


def resetExpireTime():
    diff = datetime.timedelta(minutes=5)
    localsettings.permissionExpire = datetime.datetime.now() + diff
