# telegramgetbotip
*Python3 telegram bot to retrieve public IP of the Telegram bot's host machine.*

## Rationale:
Sometimes a DynDNS is an overkill. This bot is designed to cover the use case where
you just need the IP of a network.

## Installation
### Install with pip
```
python3.8 -m pip install --user -U telegramgetbotip
```

## Usage
From shell:

```
$ python3.8 telegramgetbotip -h
usage: telegramgetbotip [-h] [-v] [-t TOKENFILE] [-i IDSFILE] [-d DELTA]

Telegram Bot to get the public IP where the bot is hosted on.

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Verbosity.
  -t TOKENFILE, --tokenfile TOKENFILE
                        Bot token file.
  -i IDSFILE, --idsfile IDSFILE
                        Allowed Telegram IDs file.
  -d DELTA, --delta DELTA
                        Time between queries.
```

From the interpreter:

```
help(telegramgetbotip)
```
