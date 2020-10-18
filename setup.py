from codecs import open
from os import path

from setuptools import find_packages, setup

with open("Readme.md", "r") as fh:
    long_description = fh.read()

setup(
    name="HCMUTRemoteSensing, # Replace with your own username
    version="demo",
    author="Long Tan Le",
    author_email="tanlong.ce@gmail.com",
    description="Satellite Images Processing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/longtanle/HCMUTRemoteSensing",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests',
        'tqdm',
        'click',
        'gdal',
        'numpy'
    ],
    include_package_data=True,
    zip_safe=False,
    entry_points="""
        [console_scripts]
        HCMUTRemoteSensing=HCMUTRemoteSensing.cli:cli
    """,
    
)