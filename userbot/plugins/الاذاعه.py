from userbot import CMD_HELP
from userbot import Sonic
from ..Config import Config

LGROUP_CMD = Config.LGROUP_CMD or "للكروبات"
LPRIV_CMD = Config.LPRIV_CMD or "للخاص"
GCAST_BLACKLIST = [
    -1001571410362,
    -1001571410362,
    ]
#

@Sonic.on(admin_cmd(pattern=f"{LGROUP_CMD}(?: |$)(.*)"))
async def gcast(event):
    Sonic = event.pattern_match.group(1)
    if Sonic:
        msg = Sonic
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await eor(event, "**-يجب الرد على رسالو او وسائط او كتابه النص مع الامر**")
        return
    roz = await edit_or_reply(event, "⌔∮ يتم الاذاعة في الخاص انتظر لحضه")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if chat not in GCAST_BLACKLIST:
                    await event.client.send_message(chat, msg)
                    done += 1
            except BaseException:
                er += 1
    await roz.edit(
        f"**- تم بنجاح الأذاعة الى ** `{done}` **من الدردشات ، خطأ في ارسال الى ** `{er}` **من الدردشات**"
    )
    
@Sonic.on(admin_cmd(pattern=f"{LPRIV_CMD}(?: |$)(.*)"))
async def gucast(event):
    Sonic = event.pattern_match.group(1)
    if Sonic:
        msg = Sonic
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await eor(event, "**-يجب الرد على رسالو او وسائط او كتابه النص مع الامر**")
        return
    roz = await edit_or_reply(event, "⌔∮ يتم الاذاعة في الخاص انتظر لحضه")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await event.client.send_message(chat, msg)
            except BaseException:
                er += 1
    await roz.edit(
        f"**- تم بنجاح الأذاعة الى ** `{done}` **من الدردشات ، خطأ في ارسال الى ** `{er}` **من الدردشات**"
    )
    
    
