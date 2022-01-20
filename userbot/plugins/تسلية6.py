#  =============================
#  == JMTHON - QHR_1  -  RR7PP =
#  =============================


import asyncio
import os
import re

from userbot import jmthon

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id
from . import changemymind, deEmojify, kannagen, moditweet, reply_id, trumptweet, tweets

plugin_category = "fun"


@jmthon.ar_cmd(
    pattern="ترامب(?:\s|$)([\s\S]*)",
    command=("ترامب", plugin_category),
    info={
        "header": "ملصق تغريدة ترامب مع نص مخصص معين",
        "usage": "{tr}ترامب <text>",
        "examples": "{tr}trump Catuserbot هو أحد برامج المستخدم المشهورة",
    },
)
async def nekobot(cat):
    "ملصق تغريدة ترامب مع نص مخصص معين_"
    text = cat.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(cat)

    reply = await cat.get_reply_message()
    if not text:
        if cat.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(cat, "⌯︙يجب ان تكتب نص اولا", 5)
    cate = await edit_or_reply(cat, "⌯︙جار طلب تغريدة من ترامب...")
    text = deEmojify(text)
    await asyncio.sleep(2)
    catfile = await trumptweet(text)
    await cat.client.send_file(cat.chat_id, catfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(catfile):
        os.remove(catfile)


@jmthon.ar_cmd(
    pattern="سونيك(?:\s|$)([\s\S]*)",
    command=("سونيك", plugin_category),
    info={
        "header": "ملصق تغريدة سونيك بنص مخصص معين",
        "usage": "{tr}سونيك <نص>",
        "examples": "{tr}سونيك مالك السورس",
    },
)
async def nekobot(cat):
    "ملصق تغريدة سونيك بنص مخصص معين"
    text = cat.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(cat)

    reply = await cat.get_reply_message()
    if not text:
        if cat.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(cat, "**⌯︙يجـب كـتابة نـص اولا", 5)
    cate = await edit_or_reply(cat, "⌯︙جاري طلب تغريدة من مودي...")
    text = deEmojify(text)
    await asyncio.sleep(2)
    catfile = await moditweet(text)
    await cat.client.send_file(cat.chat_id, catfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(catfile):
        os.remove(catfile)


@jmthon.ar_cmd(
    pattern="بنر(?:\s|$)([\s\S]*)",
    command=("بنر", plugin_category),
    info={
        "header": "تغيير رأيي لافتة مع نص مخصص معين",
        "usage": "{tr}غير عقلي <text>",
        "examples": "{tr}غير عقلي هو أحد برامج المستخدم المشهورة",
    },
)
async def nekobot(cat):
    text = cat.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(cat)

    reply = await cat.get_reply_message()
    if not text:
        if cat.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(cat, "⌯︙اعـطيني نص اولا", 5)
    cate = await edit_or_reply(cat, "⌯︙يتـم عـمل البـنر انتـظر...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    catfile = await changemymind(text)
    await cat.client.send_file(cat.chat_id, catfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(catfile):
        os.remove(catfile)


@jmthon.ar_cmd(
    pattern="كانا(?:\s|$)([\s\S]*)",
    command=("كانا", plugin_category),
    info={
        "header": "ملصق كانا تشان مع نص مخصص معين",
        "usage": "{tr}كانا text",
        "examples": "{tr}kanna Catuserbot أحد برامج المستخدم المشهورة",
    },
)
async def nekobot(cat):
    "kanna chan ملصق مع نص مخصص معين"
    text = cat.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(cat)

    reply = await cat.get_reply_message()
    if not text:
        if cat.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(cat, "⌯︙اوني شان ما ذا تريد ان اكتب", 5)
    cate = await edit_or_reply(cat, "⌯︙كانا تشان تكتب نصك...")
    text = deEmojify(text)
    await asyncio.sleep(2)
    catfile = await kannagen(text)
    await cat.client.send_file(cat.chat_id, catfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(catfile):
        os.remove(catfile)


@jmthon.ar_cmd(
    pattern="تويت(?:\s|$)([\s\S]*)",
    command=("تويت", plugin_category),
    info={
        "header": "الشخص المطلوب غرد الملصق بنص مخصص معين",
        "usage": "{tr}تويت <username> ; <text>",
        "examples": "{tr}tweet iamsrk ; هو من اشهر البوتات الموجودة",
    },
)
async def nekobot(cat):
    "The desired person tweet sticker with given custom text"
    text = cat.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(cat)

    reply = await cat.get_reply_message()
    if not text:
        if cat.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(
                cat,
                "⌯︙**يجـب كتـابة الامـر بشكـل صحـيح**\n `.تويت المعرف ; النص` ",
                5,
            )
    if ";" in text:
        username, text = text.split(";")
    else:
        await edit_delete(
            cat,
            "⌯︙**يجـب كتـابة الامـر بشكـل صحـيح**\n`.تويت المعرف ; النص`",
            5,
        )
        return
    cate = await edit_or_reply(cat, f"⌯︙جار الطلب من {username} للتغريد...")
    text = deEmojify(text)
    await asyncio.sleep(2)
    catfile = await tweets(text, username)
    await cat.client.send_file(cat.chat_id, catfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(catfile):
        os.remove(catfile)
