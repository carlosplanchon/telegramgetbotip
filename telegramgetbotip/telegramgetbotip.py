#!/usr/bin/env python3

from telepot.loop import MessageLoop

from requests import get
from telepot import Bot

from pathlib import Path
from pprint import pprint
from time import sleep, time

from typing import Any, Dict


class TelegramGetBotIp:
    """
    Telegram bot to retrieve public IP of
    the Telegram bot's host machine.
    """
    def __init__(self):
        self.queries_log = {}

    def message_handler(self, msg: Dict[Any, Any]) -> None:
        """
        This message handler get the public IP of the host if
        the ID of the message's sender is in allowed_telegram_ids.

        :param msg: Dict[Any, Any]: Message to be processed.

        """
        resp = None
        query_enabled = False
        chat_id = msg["chat"]["id"]
        if self.verbose:
            pprint(msg)
        if chat_id in self.allowed_telegram_ids:
            if self.time_between_queries == -1:
                query_enabled = True
            else:
                if chat_id not in self.queries_log:
                    query_enabled = True
                else:
                    if time() - self.queries_log[
                            chat_id] > self.time_between_queries:
                        query_enabled = True
                    else:
                        query_enabled = False
                        last_query = self.queries_log[chat_id]
                        time_since_last_query = time() - last_query
                        needs_to_wait = self.time_between_queries\
                            - time_since_last_query
                        resp = f"Wait {int(needs_to_wait)} second(s) "\
                            "to query again."

        if query_enabled:
            try:
                resp = get("http://ip.42.pl/short").text
                self.queries_log[chat_id] = time()
            except Exception:
                resp = "ERR"

        if resp:
            if self.verbose:
                pprint(f"Resp: {resp}")

            if msg["text"].lower() == "ip":
                self.bot.sendMessage(chat_id, resp)
        return None

    def start_bot(
        self,
        bot_token_file: Path,
        allowed_telegram_ids_file: Path,
        time_between_queries: int = -1,
        verbose: bool = False
            ):
        """
        Start bot and keep it running in its own thread.

        :param bot_token_file: Path: File where the bot token is located.
        :param allowed_telegram_ids_file: Path: Allowed IDs file.
        :param time_between_queries: int: Time between user queries
        to avoid spamming the service. -1 to disable it. (Default value = -1)
        :param verbose: bool: Verbosity. (Default value = False)

        """
        self.bot_token = Path(bot_token_file).read_text()
        self.allowed_telegram_ids = [int(i) for i in Path(
            allowed_telegram_ids_file).read_text().split("\n") if i.isnumeric()]

        self.time_between_queries = time_between_queries
        self.verbose = verbose

        self.bot = Bot(self.bot_token)
        MessageLoop(self.bot, self.message_handler).run_as_thread()
        while True:
            sleep(100000000)
