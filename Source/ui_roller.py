# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'roller.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFrame, QHBoxLayout,
    QLabel, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Roller(object):
    def setupUi(self, Roller):
        if not Roller.objectName():
            Roller.setObjectName(u"Roller")
        Roller.resize(320, 400)
        Roller.setStyleSheet(u"background: #192428; color: #ff8503\n"
"\n"
"")
        self.verticalLayout_2 = QVBoxLayout(Roller)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.resultBox = QPlainTextEdit(Roller)
        self.resultBox.setObjectName(u"resultBox")
        self.resultBox.setStyleSheet(u"")
        self.resultBox.setFrameShape(QFrame.Shape.Box)
        self.resultBox.setFrameShadow(QFrame.Shadow.Plain)

        self.horizontalLayout_2.addWidget(self.resultBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalFrame = QFrame(Roller)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setFrameShape(QFrame.Shape.Box)
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.horizontalFrame)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.label_2 = QLabel(self.horizontalFrame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.label_3 = QLabel(self.horizontalFrame)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.numDice = QSpinBox(self.horizontalFrame)
        self.numDice.setObjectName(u"numDice")
        self.numDice.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.numDice.setValue(1)

        self.verticalLayout_5.addWidget(self.numDice)

        self.numSides = QSpinBox(self.horizontalFrame)
        self.numSides.setObjectName(u"numSides")
        self.numSides.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.numSides.setValue(6)

        self.verticalLayout_5.addWidget(self.numSides)

        self.numRolls = QSpinBox(self.horizontalFrame)
        self.numRolls.setObjectName(u"numRolls")
        self.numRolls.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.numRolls.setValue(1)

        self.verticalLayout_5.addWidget(self.numRolls)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.resetButton = QPushButton(self.horizontalFrame)
        self.resetButton.setObjectName(u"resetButton")

        self.verticalLayout.addWidget(self.resetButton)

        self.rollButton = QPushButton(self.horizontalFrame)
        self.rollButton.setObjectName(u"rollButton")

        self.verticalLayout.addWidget(self.rollButton)

        self.quitButton = QPushButton(self.horizontalFrame)
        self.quitButton.setObjectName(u"quitButton")

        self.verticalLayout.addWidget(self.quitButton)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addWidget(self.horizontalFrame)


        self.retranslateUi(Roller)

        QMetaObject.connectSlotsByName(Roller)
    # setupUi

    def retranslateUi(self, Roller):
        Roller.setWindowTitle(QCoreApplication.translate("Roller", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Roller", u"Number of dice:", None))
        self.label_2.setText(QCoreApplication.translate("Roller", u"Number of sides:", None))
        self.label_3.setText(QCoreApplication.translate("Roller", u"Number of rolls:", None))
        self.resetButton.setText(QCoreApplication.translate("Roller", u"Reset", None))
        self.rollButton.setText(QCoreApplication.translate("Roller", u"Roll", None))
        self.quitButton.setText(QCoreApplication.translate("Roller", u"Quit", None))
    # retranslateUi

