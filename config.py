# Copyright (c) 2022 Itz-fork

import os

class Config(object):
    # Mandotory
    APP_ID = int(os.environ.get("24903318"))
    API_HASH = os.environ.get("266a897e11f3872392f16a43e226c902")
    BOT_TOKEN = os.environ.get("7127174644:AAGQRwjKi0ebH1pmPzt4QDsTNRroYRYoSZY")
    LOGS_CHANNEL = int(os.environ.get("-1002008251110"))
    BOT_OWNER = int(os.environ.get("6575679459"))
    MONGODB_URL = os.environ.get("mongodb+srv://mrnoobx:DAZCdTczVWyECi04@cluster0.sedgwxy.mongodb.net/?retryWrites=true&w=majority")
    GOFILE_TOKEN = os.environ.get("TkZ5esrB1tGHn4DwOX95vG9qSwyIy1uU")
    # Optional
    MAX_DOWNLOAD_SIZE = int(os.environ.get("MAX_DOWNLOAD_SIZE")) if os.environ.get("MAX_DOWNLOAD_SIZE") else 10737418240
    # Constents
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/NexaBots"
    TG_MAX_SIZE = 2040108421
    CHUNK_SIZE = 1024 * 6
