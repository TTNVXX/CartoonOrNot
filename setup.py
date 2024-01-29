# setup.py

from setuptools import setup, find_packages

setup(
    name='cartoon-or-not',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy==1.26.2',
        'Pillow==8.2.0',
        'tensorflow==2.15.0',
        'requests==2.26.0',  # Include the requests library
    ],
)
