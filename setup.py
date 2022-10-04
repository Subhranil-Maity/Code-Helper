from setuptools import setup, version, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.6'
DESCRIPTION = 'Improve your code environment'

setup(
    name="Code-Helper",
    version=VERSION,
    author="Subhranil Maity",
    packages=find_packages(),
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    entry_points={
        'console_scripts': [
            'ch = CodeHelper:app'
        ]
    },
    install_requires=[],
    keywords=['python', 'Code-Helper', 'good code environment', 'workspace'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
