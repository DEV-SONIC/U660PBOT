import glob
import os
import sys
from asyncio.exceptions import CancelledError
from datetime import timedelta
from pathlib import Path

import requests
from telethon import Button, functions, types, utils
from telethon.tl.functions.channels import JoinChannelRequest

from userbot import BOTLOG, BOTLOG_CHATID, PM_LOGGER_GROUP_ID
from userbot import Sonic

from ..Config import Config
from ..core.logger import logging
from ..core.session import Sonic
from ..helpers.utils import install_pip
from ..sql_helper.global_collection import (
    del_keyword_collectionlist,
    get_item_collectionlist,
)
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from .pluginmanager import load_module
from .tools import create_supergroup

LOGS = logging.getLogger("Sonic")
cmdhr = Config.COMMAND_HAND_LER


async def setup_bot():
    """
    To set up bot for userbot
    """
    try:
        await Sonic.connect()
        config = await Sonic(functions.help.GetConfigRequest())
        for option in config.dc_options:
            if option.ip_address == Sonic.session.server_address:
                if Sonic.session.dc_id != option.id:
                    LOGS.warning(
                        f"⌯︙معرف ثابت في الجلسة من {Sonic.session.dc_id}"
                        f"⌯︙لـ  {option.id}"
                    )
                Sonic.session.set_dc(option.id, option.ip_address, option.port)
                Sonic.session.save()
                break
        bot_details = await Sonic.tgbot.get_me()
        Config.TG_BOT_USERNAME = f"@{bot_details.username}"
        # await Sonic.start(bot_token=Config.TG_BOT_USERNAME)
        Sonic.me = await Sonic.get_me()
        Sonic.uid = Sonic.tgbot.uid = utils.get_peer_id(Sonic.me)
        if Config.OWNER_ID == 0:
            Config.OWNER_ID = utils.get_peer_id(Sonic.me)
    except Exception as e:
        LOGS.error(f"كـود تيرمكس - {str(e)}")
        sys.exit()


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            Config.CATUBLOGO = await Sonic.tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/e9cd63140ffaba419db6b.jpg",
                caption="⌯︙**بــوت سونيك يـعـمـل بـنـجـاح**  ✅ \n⌯︙**قـنـاة الـسـورس**  : @u660p ",
                buttons=[(Button.url("جروب سونيك", "https://t.me/u660p"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
    try:
        msg_details = list(get_item_collectionlist("restart_update"))
        if msg_details:
            msg_details = msg_details[0]
    except Exception as e:
        LOGS.error(e)
        return None
    try:
        if msg_details:
            await Sonic.check_testcases()
            message = await Sonic.get_messages(msg_details[0], ids=msg_details[1])
            text = (
                message.text
                + "\n\n**⌯︙اهلا وسهلا لقد قمت باعاده تشغيل بـوت سونيك تمت بنجاح**"
            )
            await Sonic.edit_message(msg_details[0], msg_details[1], text)
            if gvarstatus("restartupdate") is not None:
                await Sonic.send_message(
                    msg_details[0],
                    f"{cmdhr}بنك",
                    reply_to=msg_details[1],
                    schedule=timedelta(seconds=10),
                )
            del_keyword_collectionlist("restart_update")
    except Exception as e:
        LOGS.error(e)
        return None


async def ipchange():
    """
    Just to check if ip change or not
    """
    newip = (requests.get("https://httpbin.org/ip").json())["origin"]
    if gvarstatus("ipaddress") is None:
        addgvar("ipaddress", newip)
        return None
    oldip = gvarstatus("ipaddress")
    if oldip != newip:
        delgvar("ipaddress")
        LOGS.info("Ip Change detected")
        try:
            await Sonic.disconnect()
        except (ConnectionError, CancelledError):
            pass
        return "ip change"


async def add_bot_to_logger_group(chat_id):
    """
    To add bot to logger groups
    """
    bot_details = await Sonic.tgbot.get_me()
    try:
        await Sonic(
            functions.messages.AddChatUserRequest(
                chat_id=chat_id,
                user_id=bot_details.username,
                fwd_limit=1000000,
            )
        )
    except BaseException:
        try:
            await Sonic(
                functions.channels.InviteToChannelRequest(
                    channel=chat_id,
                    users=[bot_details.username],
                )
            )
        except Exception as e:
            LOGS.error(str(e))


async def load_plugins(folder):
    """
    To load plugins from the mentioned folder
    """
    path = f"userbot/{folder}/*.py"
    files = glob.glob(path)
    files.sort()
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            try:
                if shortname.replace(".py", "") not in Config.NO_LOAD:
                    flag = True
                    check = 0
                    while flag:
                        try:
                            load_module(
                                shortname.replace(".py", ""),
                                plugin_path=f"userbot/{folder}",
                            )
                            break
                        except ModuleNotFoundError as e:
                            install_pip(e.name)
                            check += 1
                            if check > 5:
                                break
                else:
                    os.remove(Path(f"userbot/{folder}/{shortname}.py"))
            except Exception as e:
                os.remove(Path(f"userbot/{folder}/{shortname}.py"))
                LOGS.info(
                    f"⌯︙غير قادر على التحميل {shortname} يوجد هناك خطا بسبب : {e}"
                )


async def autojo():
    try:
        await Sonic(JoinChannelRequest("@u660p"))
        if gvar("AUTOEO") is False:
            return
        else:
            try:
                await Sonic(JoinChannelRequest("@u660p"))
            except BaseException:
                pass
            try:
                await Sonic(JoinChannelRequest("@RR7PP"))
            except BaseException:
                pass
    except BaseException:
        pass


async def autozs():
    try:
        await Sonic(JoinChannelRequest("@GROUPSonic"))
        if gvar("AUTOZS") is False:
            return
        else:
            try:
                await Sonic(JoinChannelRequest("@u660p"))
            except BaseException:
                pass
            try:
                await Sonic(JoinChannelRequest("@u660p"))
            except BaseException:
                pass
    except BaseException:
        pass


async def verifyLoggerGroup():
    """
    Will verify the both loggers group
    """
    flag = False
    if BOTLOG:
        try:
            entity = await Sonic.get_entity(BOTLOG_CHATID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        "⌯︙الفار الأذونات مفقودة لإرسال رسائل لـ PRIVATE_GROUP_BOT_API_ID المحدد."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "⌯︙الفار الأذونات مفقودة لإرسال رسائل لـ PRIVATE_GROUP_BOT_API_ID المحدد."
                    )
        except ValueError:
            LOGS.error("⌯︙تـأكد من فـار المجـموعة  PRIVATE_GROUP_BOT_API_ID.")
        except TypeError:
            LOGS.error(
                "⌯︙لا يمكـن العثور على فار المجموعه PRIVATE_GROUP_BOT_API_ID. تأكد من صحتها."
            )
        except Exception as e:
            LOGS.error(
                "⌯︙حدث استثناء عند محاولة التحقق من PRIVATE_GROUP_BOT_API_ID.\n"
                + str(e)
            )
    else:
        descript = "- عزيزي المستخدم هذه هي مجموعه الاشعارات يرجى عدم حذفها  - @u660p"
        photobt = await Sonic.upload_file(file="Sonic/razan/resources/start/Sonicp.jpg")
        _, groupid = await create_supergroup(
            "مجموعة اشعارات سونيك ", Sonic, Config.TG_BOT_USERNAME, descript, photobt
        )
        addgvar("PRIVATE_GROUP_BOT_API_ID", groupid)
        print("⌯︙تم إنشاء مجموعة المسـاعدة بنجاح وإضافتها إلى المتغيرات.")
        flag = True
    if PM_LOGGER_GROUP_ID != -100:
        try:
            entity = await Sonic.get_entity(PM_LOGGER_GROUP_ID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        "⌯︙الأذونات مفقودة لإرسال رسائل لـ PM_LOGGER_GROUP_ID المحدد."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "⌯︙الأذونات مفقودة للمستخدمين الإضافيين لـ PM_LOGGER_GROUP_ID المحدد."
                    )
        except ValueError:
            LOGS.error("⌯︙لا يمكن العثور على فار  PM_LOGGER_GROUP_ID. تأكد من صحتها.")
        except TypeError:
            LOGS.error("⌯︙PM_LOGGER_GROUP_ID غير مدعوم. تأكد من صحتها.")
        except Exception as e:
            LOGS.error(
                "⌯︙حدث استثناء عند محاولة التحقق من PM_LOGGER_GROUP_ID.\n" + str(e)
            )
    else:
        descript = "⌯︙ وظيفه الجروب يحفظ رسائل الخاص اذا ما تريد الامر احذف الجروب نهائي \n  - @u660p"
        photobt = await Sonic.upload_file(file="Sonic/razan/resources/start/Sonicp.jpg")
        _, groupid = await create_supergroup(
            "مجموعة التخزين", Sonic, Config.TG_BOT_USERNAME, descript, photobt
        )
        addgvar("PM_LOGGER_GROUP_ID", groupid)
        print("تـم عمـل الجروب التخزين بنـجاح واضافة الـفارات الـيه.")
        flag = True
    if flag:
        executable = sys.executable.replace(" ", "\\ ")
        args = [executable, "-m", "userbot"]
        os.execle(executable, *args, os.environ)
        sys.exit(0)
