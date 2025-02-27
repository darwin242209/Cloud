#!/usr/bin/env python3
# This is bot coded by Abhijith N T and used for educational purposes only
# https://github.com/abhint
# Copyright ABHIJITH N T
# Thank you https://github.com/pyrogram/pyrogram

import logging
from .env import get_env
from logging.handlers import RotatingFileHandler

API_ID = get_env('5293972')
API_HASH = get_env('fc7377be14fb556b2fe43945e1910e51')
BOT_TOKEN = get_env('6036016901:AAHRwWJ75lxFThjVgzqOqNysOWTZq2ISyqk')


# Messages

SOURCE = "\n\nSource: [TelegramFilestoCloud](https://github.com/abhint/TelegramFilestoCloud)"
START = "\n\n**~~This bot uploads telegram files to a third-party server~~**.\n\nAdmin: __[Abhijith](" \
        "tg://user?id=429320566)__"
ERROR = "something is went wrong\n{error} \ncontact admin __[Abhijith](tg://user?id=429320566)__"
HELP = "\n\nUsage: **Send any file or bot. Then select the third-party Cloud you want to upload to.**"


# LOGGER

LOGGER_FILE_NAME = "filetocloud_log.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOGGER_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler()
    ])
logging.getLogger('pyrogram').setLevel(logging.WARNING)


def LOGGER(log: str) -> logging.Logger:
    """Logger function"""
    return logging.getLogger(log)


# import os
# import logging

# logging.basicConfig(level=logging.INFO,
#                     handlers=[logging.FileHandler(
#                         'log.txt'), logging.StreamHandler()],
#                     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
#                     )
# LOGGER = logging.getLogger(__name__)
# logging.getLogger("pyrogram").setLevel(logging.WARNING)

# ENV = bool(os.environ.get('ENV', False))
# try:
#     if ENV:
#         AUTH_USER = []
#         BOT_TOKEN = os.environ.get('BOT_TOKEN')
#         APP_ID = os.environ.get('APP_ID')
#         API_HASH = os.environ.get('API_HASH')
#         BOT_USE = bool(os.environ.get('BOT_USE', False))
#         GET_AUTH_USER = os.environ.get('AUTH_USER')
#         for i in GET_AUTH_USER.split(','):
#             AUTH_USER.append(int(i))
#     else:
#         from sample_config import Config

#         BOT_TOKEN = Config.BOT_TOKEN
#         APP_ID = Config.APP_ID
#         API_HASH = Config.API_HASH
#         BOT_USE = Config.BOT_USE
#         AUTH_USER = Config.AUTH_USERS
# except KeyError:
#     LOGGER.error('One or more configuration values are missing exiting now.')
#     exit(1)


# class Msg:
#     source = "\nsource: https://github.com/AbhijithNT/TelegramFiletoCloud"
#     start = "\n<b>This bot uploads telegram files to MixDrop.co,File.io.\nAdmin: @thankappan369</b>"
#     error = "something is went wrong\n{error} \ncontact admin @thankappan369"
#     help = "Usage: <b>Send any file and the bot will upload it to MixDrop.co,File.io</b>"
