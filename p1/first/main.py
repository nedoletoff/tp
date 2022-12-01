from PyQt6 import QtWidgets
import sys
from MyException import *

import first  # Это конвертированный файл дизайна


class ExampleApp(QtWidgets.QMainWindow, first.Ui_MainWindow):
    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.changeButton.clicked.connect(self.change)

    def check_name(self):
        if self.nameEditor.text_label().isdigit():
            raise MyException("Name contains number")
        if len(self.nameEditor.text_label()) == 0:
            raise MyException("Name is empty")
        if not self.nameEditor.text_label().isalpha():
            raise MyException("Name contains not supported symbols")

    def check_surname(self):
        if self.surnameEditor.text_label().isdigit():
            raise MyException("Surname contains number")
        if len(self.surnameEditor.text_label()) == 0:
            raise MyException("Surname is empty")
        if not self.surnameEditor.text_label().isalpha():
            raise MyException("Surname contains not supported symbols")

    def writeUnicode(self):
        min_len = min(len(self.nameEditor.text_label()), len(self.surnameEditor.text_label()))
        max_len = max(len(self.nameEditor.text_label()), len(self.surnameEditor.text_label()))
        rest_len = max_len - min_len
        unicode_name = self.nameEditor.text_label()[:min_len]
        unicode_name = unicode_name.encode("utf-8")
        unicode_surname = self.surnameEditor.text_label()[:min_len]
        unicode_surname = unicode_surname.encode("utf-8")
        if rest_len == 0:
            rest = ""
        elif max_len == len(self.nameEditor.text_label()):
            rest = self.nameEditor.text_label()[-rest_len:]
        else:
            rest = self.surnameEditor.text_label()[-rest_len:]

        res = bytearray()
        un = ""
        for x in unicode_name:
            un += hex(x)
            res.append(x)
            un += " "

        us = ""
        i = 0
        for x in unicode_surname:
            us += hex(x)
            res[i] ^= x
            i += 1
            us += " "

        self.nameUnicode.setText(un)
        self.surnameUnicode.setText(us)
        self.rest.setText(rest)

        self.result.setText(res.decode("utf-8"))

    def change(self):
        try:
            self.check_name()
            self.check_surname()
            self.errorLabel.setText("")
            self.writeUnicode()
        except MyException as e:
            self.errorLabel.setText(e.message)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
