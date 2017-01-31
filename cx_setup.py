import os
import sys
from cx_Freeze import Executable, setup
from ligafutbol import VERSION


company_name = 'MAVA'
product_name = 'Liga Sanrafaelina de Futbol'

bdist_msi_options = {
    'initial_target_dir': r'[ProgramFilesFolder]\%s\%s' % (company_name, product_name),
    'add_to_path': False,
    'upgrade_code': '{77990F3A-DC3A-01E2-B341-002219E9B01E}',
    }

build_exe_options = {
    'packages': ['sys', 'os', 'pygame', 'random', 'string', 'base64', 'datetime', 'uuid',
                 # 'sqlite3', 'sqlalchemy.dialects.sqlite',
    ],
    'excludes': ['tkinter', 'PyQt5.QtSql'],
    'includes': ['atexit', ],
    'include_files': ['deps/sqlite3.dll',]
    }

# GUI applications require a different base on Windows
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

exe = Executable(
    script='start_gui.py', base=base,
    shortcutName="Liga Sanrafaelina de Futbol",
    shortcutDir="ProgramMenuFolder",
    icon='logo-lsf.ico',
    initScript=None,
    targetName="LigaFutbol.exe",
)

setup(
    name=product_name,
    version=VERSION,
    author = "MAVA",
    author_email = "matias@mava.com.ar",
    description=u'Gestión de jugadores y clubes. Impresión de credenciales',
    executables=[exe],
    options={
        'bdist_msi': bdist_msi_options,
        'build_exe': build_exe_options
    },
)