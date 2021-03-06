# Copyright  By  @Sonic  © 2021
# WRITE BY  @RR9R7 - @GGGNE

import asyncio
import logging
import os
import time
from datetime import datetime

from userbot import Sonic
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.utils import sudo_cmd
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import media_type, progress
from ..helpers.functions import convert_toimage, convert_tosticker, vid_to_gif
from ..helpers.utils import _cattools, _catutils, reply_id

plugin_category = "misc"


if not os.path.isdir("./temp"):
    os.makedirs("./temp")


LOGS = logging.getLogger(__name__)
PATH = os.path.join("./temp", "temp_vid.mp4")

thumb_loc = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")

# Copyright  By  @Sonic  © 2021
# WRITE BY  @RR7PP


@Sonic.ar_cmd(
    pattern="تحويل صورة$",
    command=("تحويل صورة", plugin_category),
    info={
        "header": "رد على هذا الأمر إلى ملصق للحصول على صورة.",
        "description": "هذا أيضا يحول كل الوسائط إلى صورة. هذا إذا كان الفيديو ثم يستخرج الصورة من ذلك الصوت ثم يستخرج التمب.",
        "usage": "{tr}stoi",
    },
)
async def _(event):
    "Sticker to image Conversion."
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if not reply:
        return await edit_delete(
            event, "⌯︙يجـب عليـك الرد عـلى الملصق لتحويـله الـى صورة ⚠️"
        )
    output = await _cattools.media_to_pic(event, reply)
    if output[1] is None:
        return await edit_delete(
            output[0], "⌯︙غـير قـادر على تحويل الملصق إلى صورة من هـذا الـرد ⚠️"
        )
    meme_file = convert_toimage(output[1])
    await event.client.send_file(
        event.chat_id, meme_file, reply_to=reply_to_id, force_document=False
    )
    await output[0].delete()


@Sonic.ar_cmd(
    pattern="تحويل ملصق$",
    command=("تحويل ملصق", plugin_category),
    info={
        "header": "رد على هذا الأمر للصورة للحصول على ملصق.",
        "description": "هذا أيضا يحول كل الوسائط إلى ملصق. هذا إذا كان الفيديو ثم يستخرج الملصق من ذلك  الصوت ثم يستخرج التمب.",
        "usage": "{tr}itos",
    },
)
async def _(event):
    "Image to Sticker Conversion."
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if not reply:
        return await edit_delete(
            event, "⌯︙يجـب عليـك الرد عـلى الصـورة لتحويـلها الـى مـلصق ⚠️"
        )
    output = await _cattools.media_to_pic(event, reply)
    if output[1] is None:
        return await edit_delete(
            output[0], "⌯︙غـير قـادر على استـخراج الـملصق من هـذا الـرد ⚠️"
        )
    meme_file = convert_tosticker(output[1])
    await event.client.send_file(
        event.chat_id, meme_file, reply_to=reply_to_id, force_document=False
    )
    await output[0].delete()


@Sonic.ar_cmd(
    pattern="تحويل (mp3|voice)$",
    command=("تحويل", plugin_category),
    info={
        "header": "يحول ملف الوسائط المطلوب إلى ملف صوتي أو ملف mp3.",
        "usage": [
            "{tr}تحويل بصمة",
            "{tr}تحويل بصمة",
        ],
    },
)
async def _(event):
    "يحول ملف الوسائط المطلوب إلى ملف صوتي أو ملف mp3."
    if not event.reply_to_msg_id:
        await edit_or_reply(event, "**⌯︙يـجب الـرد على اي مـلف اولا ⚠️**")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await edit_or_reply(event, "**⌯︙يـجب الـرد على اي مـلف اولا ⚠️**")
        return
    input_str = event.pattern_match.group(1)
    event = await edit_or_reply(event, "⌯︙يتـم التـحويل انتـظر قليـلا ⏱")
    try:
        start = datetime.now()
        c_time = time.time()
        downloaded_file_name = await event.client.download_media(
            reply_message,
            Config.TMP_DOWNLOAD_DIRECTORY,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, event, c_time, "يتم التحميل")
            ),
        )
    except Exception as e:
        await event.edit(str(e))
    else:
        end = datetime.now()
        ms = (end - start).seconds
        await event.edit(
            "⌯︙التحـميل الى `{}` في {} من الثواني ⏱".format(downloaded_file_name, ms)
        )
        new_required_file_name = ""
        new_required_file_caption = ""
        command_to_run = []
        voice_note = False
        supports_streaming = False
        if input_str == "voice":
            new_required_file_caption = "voice_" + str(round(time.time())) + ".opus"
            new_required_file_name = (
                Config.TMP_DOWNLOAD_DIRECTORY + "/" + new_required_file_caption
            )
            command_to_run = [
                "ffmpeg",
                "-i",
                downloaded_file_name,
                "-map",
                "0:a",
                "-codec:a",
                "libopus",
                "-b:a",
                "100k",
                "-vbr",
                "on",
                new_required_file_name,
            ]
            voice_note = True
            supports_streaming = True
        elif input_str == "mp3":
            new_required_file_caption = "mp3_" + str(round(time.time())) + ".mp3"
            new_required_file_name = (
                Config.TMP_DOWNLOAD_DIRECTORY + "/" + new_required_file_caption
            )
            command_to_run = [
                "ffmpeg",
                "-i",
                downloaded_file_name,
                "-vn",
                new_required_file_name,
            ]
            voice_note = False
            supports_streaming = True
        else:
            await event.edit("⌯︙غـير مدعوم ❕")
            os.remove(downloaded_file_name)
            return
        process = await asyncio.create_subprocess_exec(
            *command_to_run,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
        os.remove(downloaded_file_name)
        if os.path.exists(new_required_file_name):
            force_document = False
            await event.client.send_file(
                entity=event.chat_id,
                file=new_required_file_name,
                allow_cache=False,
                silent=True,
                force_document=force_document,
                voice_note=voice_note,
                supports_streaming=supports_streaming,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, event, c_time, "يتم الرفع")
                ),
            )
            os.remove(new_required_file_name)
            await event.delete()



@Sonic.on(admin_cmd(pattern="تحويل متحركة (?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_message.media:
        return await edit_or_reply(
            event, "يستخدم الامر بالرد على فيديو بـ  `.تحويل متحركة`"
        )
    chat = "@VideoToGifConverterBot"
    rzevent = await edit_or_reply(event, "**- جـارِ التحـويا انتـظر ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1125181695)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await rzevent.edit(
                "**- تحـقق من انـك لم تقـم بحظر البوت @VideoToGifConverterBot .. ثم اعـد استخدام الامـر ..**"
            )
            return
        if response.text.startswith("لا استطيع ايجاده"):
            await rzevent.edit("**-**")
        else:
            await rzevent.delete()
            await event.client.send_message(event.chat_id, response.message)
        
