import os
from setuptools import setup, find_packages
try:
    # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:
    # for pip <= 9.0.3
    from pip.req import parse_requirements

name="Bitmasher"
version="0.0"
release="0.0.4"

def load_requirements(fname):
    reqs = parse_requirements(fname, session="test")
    return [str(ir.req) for ir in reqs]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name=name,
    description="Bit rotational encryption with steganography",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
        "Topic :: Security :: Cryptography"
    ],
    python_requires='>=3.6',
    version=release,
    url='https://github.com/vulogov/Bitmasher',
    author='Vladimir Ulogov',
    author_email='vladimir.ulogov@me.com',
    license='MPL+2.0',
    install_requires=load_requirements("requirements.txt"),
    packages=find_packages())
