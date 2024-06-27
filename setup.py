from setuptools import setup, find_packages

VERSION = '1.3'
DESCRIPTION = 'A package for making turtle art'

with open("README.md", "r") as file:
    long_description = file.read()

URL = 'https://github.com/FrickTzy/Turtle-Art'

setup(
    name="turtle_art_manager",
    version=VERSION,
    author="FrickTzy (Kurt Arnoco)",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    url=URL,
    keywords=['python', 'turtle', 'python turtle', 'python art'],
)