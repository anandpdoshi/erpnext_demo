from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='erpnext_demo',
    version=version,
    description='Demo Builder',
    author='Web Notes Technlogies',
    author_email='info@erpnext.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("webnotes",),
)
