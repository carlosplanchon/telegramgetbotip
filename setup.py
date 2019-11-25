#!/usr/bin/env python3

from setuptools import setup
from pathlib import Path

readme = Path("README.md").read_text()


setup(
    name="telegramgetbotip",
    packages=["telegramgetbotip"],
    entry_points={
        "console_scripts": [
            "telegramgetbotip = telegramgetbotip.__main__:main"
        ]
    },
    version="0.1.4",
    license="GPL3",
    description="Python3 telegram bot to retrieve public IP "
    "of the Telegram bot's host machine.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Carlos A. Planchón",
    author_email="bubbledoloresuruguay2@gmail.com",
    url="https://github.com/carlosplanchon/telegramgetbotip",
    download_url="https://github.com/carlosplanchon/"
        "telegramgetbotip/archive/v0.1.4.tar.gz",
    keywords=["telegram", "bot", "ip", "networking"],
    install_requires=[
        "telepot"
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.8",
    ],
)
