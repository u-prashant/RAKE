import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rake-keyword",
    version="0.0.1",
    author="Prashant Upadhyay",
    author_email="prashant.u@hotmail.com",
    description="Implementation of RAKE - Rapid Automatic Keyword Extraction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/u-prashant/RAKE",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)