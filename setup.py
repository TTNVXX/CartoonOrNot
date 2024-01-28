# setup.py

from setuptools import setup, find_packages

setup(
    name='cartoon-or-not',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow==8.2.0',
        'numpy==1.21.0',
        'tensorflow==2.5.0',
    ],
)