from setuptools import find_packages, setup

from freshdesk import __version__

setup(
    name="python-freshdesk",
    version=__version__,
    license="BSD",
    author="python-freshdesk Team",
    author_email="stefan.heitmueller@gmx.com",
    description="An API for the Freshdesk helpdesk",
    url="https://github.com/python-freshdesk/python-freshdesk",
    install_requires=["requests", "python-dateutil"],
    packages=find_packages(),
    python_requires='>3.6',
)
