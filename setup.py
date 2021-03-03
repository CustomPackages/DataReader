from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "numpy", "gdal"]

setup(
    name="paulSubha998",
    version="0.0.1",
    author="Subhajit Paul",
    author_email="paul.isro123@gmail.com",
    description="A package to read tif image",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/CustomPackages/DataReader",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
