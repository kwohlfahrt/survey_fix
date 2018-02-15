#!/usr/bin/env python

from setuptools import setup

setup(
    name="Survey Fix",
    version="0.0.1",
    description="A program to assign labels as values to points",
    install_requires=['ezdxf', 'click'],
    packages=['survey_fix'],
    entry_points={'console_scripts': ['survey_fix=survey_fix:main']},
)
