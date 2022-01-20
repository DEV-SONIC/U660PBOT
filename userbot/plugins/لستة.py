# Copyright (C) 2021 JMTHON TEAM
# FILES WRITTEN BY  @RR7PP
import re

from telethon import Button

from ..Config import Config
from . import edit_delete, jmthon, reply_id

plugin_category = "tools"
BTN_URL_REGEX = re.compile(r"(\[([^\[]+?)\]\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)")


@jmthon.ar_cmd(
    pattern="لستة(?: |$)(.*)",
    command=("لستة", plugin_category),
    info={
        "header": "To create button posts via inline",
        "note": f"Markdown is Default to html",
        "options": "If you button to be in same row as other button then follow this <buttonurl:link:same> in 2nd button.",
        "usage": [
            "{tr}ibutton <text> [Name on button]<buttonurl:link you want to open>",
        ],
        "examples": "{tr}لستة قنواتي الرسمية [sonic]<buttonurl:t.me/u660p> [sonic]<buttonurl:t.me/revorb0t> ",
    },
)
async def _(event):
    "To create button posts via inline"
    reply_to_id = await reply_id(event)
    # soon will try to add media support
    reply_message = await event.get_reply_message()
    if reply_message:
        markdown_note = reply_message.text
    else:
        markdown_note = "".join(event.text.split(maxsplit=1)[1:])
    if not markdown_note:
        return await edit_delete(event, "⌯︙يجب عليك وضع مسافـة لاستخدامها مع الامر ")
    catinput = "Inline buttons " + markdown_note
    results = await event.client.inline_query(Config.TG_BOT_USERNAME, catinput)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


def build_keyboard(buttons):
    keyb = []
    for btn in buttons:
        if btn[2] and keyb:
            keyb[-1].append(Button.url(btn[0], btn[1]))
        else:
            keyb.append([Button.url(btn[0], btn[1])])
    return keyb
