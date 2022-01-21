# speech to text module for catuserbot by uniborg (@spechide)
import os
from datetime import datetime

import requests

from userbot import Sonic

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import media_type

plugin_category = "utils"


@Sonic.ar_cmd(
    pattern="stt$",
    command=("stt", plugin_category),
    info={
        "header": "speech to text module.",
        "usage": "{tr}stt",
    },
)
async def _(event):
    "speech to text."
    if Config.IBM_WATSON_CRED_URL is None or Config.IBM_WATSON_CRED_PASSWORD is None:
        return await edit_delete(
            event,
            "`You need to set the required ENV variables for this module. \nModule stopping`",
        )
    start = datetime.now()
    lan = "en"
    if not os.path.isdir(Config.TEMP_DIR):
        os.makedirs(Config.TEMP_DIR)
    reply = await event.get_reply_message()
    mediatype = media_type(reply)
    if not reply or (mediatype and mediatype not in ["Voice", "Audio"]):
        return await edit_delete(
            event,
            "`قم بالرد على رسالة صوتية أو ملف صوتي للحصول على النص ذي الصلة.`",
        )
    catevent = await edit_or_reply(event, "`تحميل على الموقع المحلي ، للتحليل  🙇`")
    required_file_name = await event.client.download_media(reply, Config.TEMP_DIR)
    await catevent.edit("`بدء التحيل لاستخراج النص`")
    headers = {
        "Content-Type": reply.media.document.mime_type,
    }
    data = open(required_file_name, "rb").read()
    response = requests.post(
        Config.IBM_WATSON_CRED_URL + "/v1/recognize",
        headers=headers,
        data=data,
        auth=("apikey", Config.IBM_WATSON_CRED_PASSWORD),
    )
    r = response.json()
    if "results" not in r:
        return await catevent.edit(r["خطـأ"])
    # process the json to appropriate string format
    results = r["results"]
    transcript_response = ""
    transcript_confidence = ""
    for alternative in results:
        alternatives = alternative["alternatives"][0]
        transcript_response += " " + str(alternatives["transcript"])
        transcript_confidence += " " + str(alternatives["confidence"])
    end = datetime.now()
    ms = (end - start).seconds
    if transcript_response == "":
        string_to_show = "**اللغه : **`{}`\n**الوقت المستغرق : **`{} الثواني`\n**لم اجد نتائج**".format(
            lan, ms
        )
    else:
        string_to_show = "**اللغه : **`{}`\n**نسخة طبق الأصل : **`{}`\n**الوقت المستغرق : **`{} الثواني`\n**الثقة : **`{}`".format(
            lan, transcript_response, ms, transcript_confidence
        )
    await catevent.edit(string_to_show)
    # now, remove the temporary file
    os.remove(required_file_name)
