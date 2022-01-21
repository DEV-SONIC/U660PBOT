# @Sonic - < https://t.me/Sonic >
# Copyright (C) 2021 - Sonic-AR
# All rights reserved.
#
# This file is a part of < https://github.com/Sonic-AR/JM-THON >
# Please read the GNU Affero General Public License in;
# < https://github.com/Sonic-AR/JM-THON/blob/master/LICENSE
# ===============================================================

import random
from Sonic.razan.resources.strings import *
from userbot import Sonic, CMD_HELP
from userbot import Sonic
from ..core.managers import edit_or_reply
from ..helpers import get_user_from_event


@Sonic.on(admin_cmd(pattern="رفع بقلبي(?: |$)(.*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه بقلبك 🖤 "
    )


@Sonic.on(admin_cmd(pattern="رفع جوزي(?: |$)(.*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \nتـم رفعه جوزك  روحوا اعملو واحد 🤤😂",
    )


@Sonic.on(admin_cmd(pattern="رفع حمار(?: |$)(.*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1890819157:
        return await edit_or_reply(mention, f"**- احا دا هذا المطور **")
   
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفـعه حمار هـنا "
    )


@Sonic.on(admin_cmd(pattern="رفع مراتي(?: |$)(.*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1890819157:
        return await edit_or_reply(mention, f"**- احا دا هذا المطور**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه مراتك روح نيكها 😹🤤",
    )


@Sonic.on(admin_cmd(pattern="رفع كلب(?: |$)(.*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1890819157:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")

    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه كلب خليه خله  ياخد عضمة 😂🐶",
    )


@Sonic.on(admin_cmd(pattern="كت(?: |$)(.*)"))
async def mention(mention):
    reza = random.choice(kttwerz)
    await edit_or_reply(mention, f"**- {reza}**")


@Sonic.on(admin_cmd(pattern="هينه(?: |$)(.*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1890819157:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(hena)
    await edit_or_reply(mention, f"{sos} .")


@Sonic.on(admin_cmd(pattern="نسبة الحب(?: |$)(.*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rza = random.choice(roz)
    await edit_or_reply(
        mention, f"نـسـبتكم انـت و [{muh}](tg://user?id={user.id}) هـي {rza} 😔🖤"
    )


@Sonic.on(admin_cmd(pattern="نسبة الانوثة(?: |$)(.*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1890819157:
        return await edit_or_reply(mention, f"**- احا  دا المطور سيد الرجالة وعلى راسك**")
    
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(rr7)
    await edit_or_reply(
        mention, f"- نسبة الانوثة لـ [{muh}](tg://user?id={user.id}) هـي {sos} 🥵🖤"
    )


@Sonic.on(admin_cmd(pattern="نسبة الغباء(?: |$)(.*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rzona = random.choice(rr7)
    await edit_or_reply(
        mention, f"نسبة الغباء لـ [{muh}](tg://user?id={user.id}) هـي {rzona} 😂💔"
    )


@Sonic.on(admin_cmd(pattern="رفع ملك(?: |$)(.*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه ملك 👑🔥"
    )


@Sonic.on(admin_cmd(pattern="رفع قرد(?: |$)(.*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1890819157:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه قرد واعطائه موزة 🐒🍌",
    )


@Sonic.on(admin_cmd(pattern="اوصف(?: |$)(.*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rzona = random.choice(osfroz)
    await edit_or_reply(mention, f"{rzona}")

@Sonic.on(admin_cmd(pattern="شغله(?: |$)(.*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rezw = random.choice(rzwhat)
    await edit_or_reply(
        mention, f"- المستخدم [{muh}](tg://user?id={user.id}) شغله هو {rezw}"
    )
