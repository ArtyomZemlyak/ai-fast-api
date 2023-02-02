"""
`ai-fast-api` - Common functionality for FastAPI realization.
https://github.com/ArtyomZemlyak/ai-fast-api
"""

import os.path

# Always prefer setuptools over distutils
from setuptools import setup, find_packages


def read_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


here = os.path.dirname(__file__)
# Get the long description from the README file
long_description = read_text(os.path.join(here, "README.md"))


def read_version_string(version_file):
    for line in read_text(version_file).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


version = read_version_string("ai_fast_api/__version__.py")

requirements = read_text(os.path.join(here, "requirements.txt")).splitlines()

setup(
    name="ai_fast_api",
    version=version,
    description="ai-fast-api - Common functionality for FastAPI realization.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # The project's main homepage.
    url="https://github.com/ArtyomZemlyak/ai-fast-api.git",
    author="Artem Zemliak",
    author_email="artyom.zemlyak@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: POSIX :: Linux",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="fastapi api generator generation",
    packages=find_packages(exclude=["contrib", "docs", "data", "examples", "tests"]),
    install_requires=requirements,
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    # entry_points={
    #     'console_scripts': [
    #       ' = .__main__:main',
    #     ],
    # },
)
