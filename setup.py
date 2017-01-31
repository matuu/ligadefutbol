from ligafutbol import VERSION

from setuptools import setup, find_packages


setup(
    name='LigaFutbol',
    version=VERSION,
    description='Liga Sanrafaelina de Futbol',
    author='Matias Varela',
    author_email='matias@mava.com.ar',
    url='https://github.com/matuu/ligafutbol/',
    packages=find_packages(),
    scripts=['start_gui.py'],
    install_requires=[
        "PyQt5==5.7.1",
        "pygame==1.9.3",
        "SQLAlchemy==0.7.10"
    ],
)
