import setuptools

with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="UTF-8") as fh:
    require = fh.readlines()
require = [x.strip() for x in require]

setuptools.setup(
    name="shadok",
    version="1.2.0",
    author="pierre-sassoulas",
    author_email="pierre.sassoulas@gmail.com",
    description="Permit to unleash the full efficiency of shadok's logic in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pierre-Sassoulas/shadok",
    packages=setuptools.find_packages(),
    install_requires=require,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
