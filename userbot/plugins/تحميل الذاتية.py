
from userbot import *
from userbot import Sonic
from ..Config import Config

Sonic_CMD = Config.SCPIC_CMD or "جلب الصورة"

@Sonic.on(admin_cmd(pattern=f"{Sonic_CMD}"))
async def dato(event):
    if not event.is_reply:
        return await event.edit("..")
    rr9r7 = await event.get_reply_message()
    pic = await rr9r7.download_media()
    await bot.send_file(
        "me",
        pic,
        caption=f"""
-تـم جـلب الصـورة بنجـاح ✅
- Dev: @u660p
  """,
    )
    await event.edit("احاا")
