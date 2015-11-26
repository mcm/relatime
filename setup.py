from setuptools import setup, find_packages

version = "1.0.0"

setup(
    name = "relatime",
    version = version,
    description = "Python parser for a simple relative time syntax",
    url = "https://github.com/mcm/relatime",
    author = "Steve McMaster",
    author_email = "mcmaster@hurricanelabs.com",
    package_dir = {"":"src"},
    packages = find_packages("src"),
    install_requires = ["pytz"],
)
