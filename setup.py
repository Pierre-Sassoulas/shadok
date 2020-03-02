import setuptools


def get_long_description():
    with open("README.md", "r", encoding="UTF-8") as readme:
        long_description = readme.read()
    return long_description


setuptools.setup(
    name="shadok",
    version="1.2.0",
    author="pierre-sassoulas",
    author_email="pierre.sassoulas@gmail.com",
    description="Permit to unleash the full efficiency of shadok's logic in Python.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/Pierre-Sassoulas/shadok",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
