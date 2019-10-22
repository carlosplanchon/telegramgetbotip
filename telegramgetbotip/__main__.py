#!/usr/bin/env python3

from telegramgetbotip.telegramgetbotip import TelegramGetBotIp

from argparse import ArgumentParser
from pathlib import Path


def main():
    parser = ArgumentParser(
        description="Telegram Bot to get the public IP where the bot "
        "is hosted on."
        )
    # Argparse logic.
    parser.add_argument(
            "-v", "--verbose",
            help="Verbosity.",
            action="store_true",
            dest="verbose",
            default=False
        )
    parser.add_argument(
            "-t", "--tokenfile",
            type=str,
            help=f"Bot token file.",
            dest="tokenfile"
        )
    parser.add_argument(
            "-i", "--idsfile",
            type=str,
            help=f"Allowed Telegram IDs file.",
            dest="idsfile"
        )
    parser.add_argument(
            "-d", "--delta",
            type=int,
            help=f"Time between queries.",
            dest="delta",
            default=-1
        )

    args = parser.parse_args()

    bot = TelegramGetBotIp()
    if args.tokenfile and args.idsfile:
        bot.start_bot(
            bot_token_file=Path(args.tokenfile),
            allowed_telegram_ids_file=Path(args.idsfile),
            time_between_queries=args.delta,
            verbose=args.verbose
            )
