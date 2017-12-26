from setuptools import setup, find_packages

setup(
    name="usac",
    version="1",
    package_dir={"": "apps", "project": "./project"},
    packages=find_packages("apps") + ["project"],
)
