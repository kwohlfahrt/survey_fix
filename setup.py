#!/usr/bin/env python

from setuptools import setup

setup(
    name="Survey Fix",
    version="0.0.2",
    description="A program to assign labels as values to points",
    python_requires=">=3.6",
    install_requires=['ezdxf>=0.8.6', 'click'],
    py_modules=['survey_fix'],
    entry_points={'console_scripts': ['survey_fix=survey_fix:main']},
)
