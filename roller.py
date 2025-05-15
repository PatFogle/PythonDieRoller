#----------------------------------------------------#
#| Roller 1.0                                       |#
#| Dice roller add-in for any rpg                   |#
#|                                                  |#
#|                                                  |#
#| © 2025 Lost Cause Solutuions                     |#
#| Written and designed by Patrick Fogle            |#
#----------------------------------------------------#


# This Python file uses the following encoding: utf-8
import sys
import random

from PySide6.QtWidgets import QApplication, QWidget


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_roller import Ui_Roller

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Roller()
        self.ui.setupUi(self)
        self.setWindowTitle("Roller 1.0")
        self.ui.quitButton.released.connect(self.quit_pressed)
        self.ui.rollButton.released.connect(self.roll)
        self.ui.resetButton.released.connect(self.reset)
        self.welcomeMsg="Die Roller 1.0\n\nChoose number of dice, sides, and rolls.\nThen click roll."
        self.ui.resultBox.insertPlainText(self.welcomeMsg)

    def quit_pressed(self):
        sys.exit()

    def roll(self):
        self.ui.resultBox.clear()
        rolls = self.ui.numRolls.text()
        dice = self.ui.numDice.text()
        sides = self.ui.numSides.text()
        for roll in range(int(rolls)):
            self.ui.resultBox.insertPlainText(f"Roll: {roll+1}\n")
            for die in range(int(dice)):
                result = random.randint(0, int(sides))
                self.ui.resultBox.insertPlainText(f"Die: {die+1}, Result: {result}\n")

    def reset(self):
        self.ui.resultBox.clear()
        self.ui.resultBox.insertPlainText(self.welcomeMsg)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
