#!/usr/bin/env python
"""Setup script for Cosmic Dungeon Quest."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cosmic-dungeon-quest",
    version="1.0.0",
    author="LAYLsec",
    author_email="kaifsidratul@gmail.com",
    description="The Ultimate Procedural Dungeon Crawler RPG built in pure Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LAYLsec/python-game",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Games/Entertainment :: Role-Playing",
        "Topic :: Terminals",
    ],
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black>=22.0",
            "pylint>=2.12",
            "sphinx>=4.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "cosmic-dungeon-quest=cosmic_dungeon_quest:main",
        ],
    },
    project_urls={
        "Bug Tracker": "https://github.com/LAYLsec/python-game/issues",
        "Changelog": "https://github.com/LAYLsec/python-game/blob/main/CHANGELOG.md",
        "Documentation": "https://github.com/LAYLsec/python-game#readme",
    },
)
