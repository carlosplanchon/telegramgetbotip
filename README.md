
Disclaimer: This is a fork of https://github.com/carlosplanchon/telegramgetbotip! I only added Docker support and extended the documentation. I do not intend to change the software itself (I'm not a Python programmer anyway...).

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
The Bot Token file must contain the bot ID in JSON format.
{
	"token": "token_string" (str)
}

The ids's file must contain the IDs in JSON format.
{
	"name": id (int)
}

You can get your Telegram ID from @userinfobot
You can register your Telegram Bot from @BotFather

From the interpreter:

```
help(telegramgetbotip)
```
### Receive your public IP address
Send "ip" to your bot - it will reply with your public IP address. Other texts are ignored.

## Docker

- List item
- Clone or download and unzip this repository and enter the directory.
- Modify the files "token" and "ids" and add your values in.
- Build the docker image:
```
docker build -t telegramgetbotip .
```
- Run a container:
```
docker run -d --name telegramgetbotip telegramgetbotip
```
