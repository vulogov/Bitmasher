import os
from setuptools import setup, find_packages
try:
    # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:
    # for pip <= 9.0.3
    from pip.req import parse_requirements

name="bund"
version="0.0"
release="0.0.1"

def load_requirements(fname):
    reqs = parse_requirements(fname, session="test")
    return [str(ir.req) for ir in reqs]

setup(name=name,
    setup_requires=['pytest-runner'],
    version=release,
    description='BUND language interpreter library',
    url='https://github.com/vulogov/py-bund',
    author='Vladimir Ulogov',
    author_email='vulogov@linkedin.com',
    license='GPL3',
    install_requires=load_requirements("requirements.txt"),
    packages=find_packages())
