from setuptools import setuptools, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gnome-extension-sync", 
    version="0.1.0",
    author="JJO",
    author_email="jjo@yahoo.com",
    description="Automate installation of gnome extensions for your linux environment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jeteokeeffe/gnome-extension-sync",
    packages=find_packages(exclude=["tests.*", "tests"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "gnome-extension-sync=gnomeextensionsync.app:main"
        ]
    },
    python_requires='>=3.6',
    install_requires=['PyYAML']
)
