# @Sonic - < https://t.me/Sonic >
# Copyright (C) 2021 - Sonic-AR
# All rights reserved.
#
# This file is a part of < https://github.com/Sonic-AR/Sonic >
# Please read the GNU Affero General Public License in;
# < https://github.com/Sonic-AR/JM-THON/blob/master/LICENSE
# ===============================================================
import sys

from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession

from ..Config import Config
from .client import CatUserBotClient

__version__ = "2.10.6"

loop = None

if Config.STRING_SESSION:
    session = StringSession(str(Config.STRING_SESSION))
else:
    session = "Sonic"

try:
    Sonic = CatUserBotClient(
        session=session,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        loop=loop,
        app_version=__version__,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
except Exception as e:
    print(f"[STRING SESSION] - {str(e)}")
    sys.exit()


Sonic.tgbot = tgbot = CatUserBotClient(
    session="arTgbot",
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    loop=loop,
    app_version=__version__,
    connection=ConnectionTcpAbridged,
    auto_reconnect=True,
    connection_retries=None,
).start(bot_token=Config.TG_BOT_TOKEN)
