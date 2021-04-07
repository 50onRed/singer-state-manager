#!/usr/bin/env python
from setuptools import setup

setup(
    name="singer-state-manager",
    version="0.1.0",
    description="Singer.io tool for persisting state immediately",
    author="Red Spark",
    url="https://github.com/50onRed/singer-state-manager",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["singer_state_manager"],
    install_requires=[
        "singer-python==5.12.1",
    ],
    entry_points="""
    [console_scripts]
    singer-state-manager=singer_state_manager:main
    """,
    packages=["singer_state_manager"],
)
