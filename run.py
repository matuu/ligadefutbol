#!/usr/bin/env python3
import os
import sys

from PyQt5.QtWidgets import QApplication

from ligafutbol.app import LSFMainWindow, LigaDeFutbolApp


if __name__ == '__main__':
    if not os.path.exists("media"):
        os.makedirs("media")
    app = QApplication(sys.argv)
    # localization
    # qt_translator = QTranslator()
    # if qt_translator.load("qt_" + QLocale.system().name(), QLibraryInfo.location(QLibraryInfo.TranslationsPath)):
    #     app.installTranslator(qt_translator)

    MainWindow = LSFMainWindow()
    liga_app = LigaDeFutbolApp(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
