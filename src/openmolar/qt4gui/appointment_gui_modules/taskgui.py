# -*- coding: utf-8 -*-
# Copyright (c) 2009 Neil Wallace. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# See the GNU General Public License for more details.

'''
a module housing all appointment functions that act on the gui
'''

import datetime

from PyQt4 import QtCore, QtGui

from openmolar.settings import localsettings
from openmolar.qt4gui.customwidgets import ui_taskwidget

class taskViewer(QtGui.QFrame):
    def __init__(self, parent=None):
        super(taskViewer, self).__init__(parent)
        
        self.setSizePolicy(QtGui.QSizePolicy(
        QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding))

        self.layout = QtGui.QVBoxLayout(self)

        self.ops = localsettings.allowed_logins
        self.ops.sort()
        self.taskWidgets = []
        
        self.setMinimumSize(self.minimumSizeHint())

    def minimumSizeHint(self):
        height = len(self.taskWidgets) * 120
        return QtCore.QSize(720, height)
        
    def layoutTasks(self):
        '''
        lay out some task widgets
        '''
        self.clear()
        alternateBase = False
        for op in self.ops:
            #--creates a widget
            iw = QtGui.QWidget(self)
            tw = ui_taskwidget.Ui_Form()
            tw.setupUi(iw)
            tw.label.setText(op)
            if op == "AH":
                tw.listWidget.addItems(["Sign your forms"])
            if op == "NW":
                tw.listWidget.addItems(["Fix the door handle X-ray room",
                "Refer to Buchanan", "order precision attachment"])
                
            self.taskWidgets.append(tw)
            if alternateBase:
                iw.setBackgroundRole(iw.palette().AlternateBase)
            else:
                alternateBase = True
            self.layout.insertWidget(-1, iw)
        
        self.setMinimumSize(self.minimumSizeHint())
        

    def clear(self):
        '''
        clears all taskWidgets
        '''
        while self.taskWidgets != []:
            widg = self.taskWidgets.pop()
            self.estimate_layout.removeWidget(widg.parent)
            widg.parent.setParent(None)


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)

    localsettings.initiate()
    print localsettings.allowed_logins
    form = taskViewer()
    form.layoutTasks()
    form.show()

    sys.exit(app.exec_())