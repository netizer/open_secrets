import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="open_secrets",
    version="1.0.3",
    description="Use local counterparts of Google Could Secret Manager entries.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/netizer/open_secrets",
    author="Krzysiek Herod",
    author_email="krzysiek.herod@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(exclude=("tests")),
    include_package_data=True,
    install_requires=["google.cloud"]
)
