import os
import sys

from PyQt5.QtWidgets import QApplication

from ligafutbol.utils import get_application_folder, exists_or_create_folder


def main():
    exists_or_create_folder(get_application_folder())
    exists_or_create_folder(get_application_folder("media"))
    exists_or_create_folder(get_application_folder("db"))

    app = QApplication(sys.argv)
    # importo acá, para estar seguro que existen las carpetas necesarias
    from ligafutbol.app import LSFMainWindow, LigaDeFutbolApp
    MainWindow = LSFMainWindow()
    liga_app = LigaDeFutbolApp(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()