import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wptools",
    version="0.0.1",
    author="Matthew Larsen",
    author_email="utegrad@gmail.com",
    description="A small package of tools for administration of WordPress installations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/utegrad/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)