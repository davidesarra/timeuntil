from setuptools import setup, find_packages

setup(
    name="timeuntil",
    version="0.1.0",
    include_package_data=True,
    packages=find_packages(exclude=["tests"]),
)
