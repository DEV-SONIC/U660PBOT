from . import *
from ..helpers.utils import reply_id as rd
from userbot import CMD_HELP

@bot.on(admin_cmd(pattern="المتحركات"))
@bot.on(sudo_cmd(pattern="المتحركات", allow_sudo=True))
async def gifrz(Sonic):
    await edit_or_reply(Sonic, B)

@bot.on(admin_cmd(pattern="متحركات ولد"))
@bot.on(sudo_cmd(pattern="متحركات ولد", allow_sudo=True))
async def gifrz(Sonic):
    await edit_or_reply(Sonic, ROZG)

@bot.on(admin_cmd(outgoing=True, pattern="و1$"))
@bot.on(sudo_cmd(pattern="و1$", allow_sudo=True))
async def GIFANIME(Sonic):
    if Sonic.fwd_from:
        return
    roz = await rd(Sonic)
    if gifrz_1:
        Sonic_c = f"**-**\n"
        await Sonic.client.send_file(Sonic.chat_id, gifrz_1, caption=Sonic_c, reply_to=roz)

@bot.on(admin_cmd(outgoing=True, pattern="و2$"))
@bot.on(sudo_cmd(pattern="و2$", allow_sudo=True))
async def GIFANIME(Sonic):
    if Sonic.fwd_from:
        return
    roz = await rd(Sonic)
    if gifrz_2:
        Sonic_c = f"**-**\n"
        await Sonic.client.send_file(Sonic.chat_id, gifrz_2, caption=Sonic_c, reply_to=roz)

@bot.on(admin_cmd(outgoing=True, pattern="و3$"))
@bot.on(sudo_cmd(pattern="و3$", allow_sudo=True))
async def GIFANIME(Sonic):
    if Sonic.fwd_from:
        return
    roz = await rd(Sonic)
    if gifrz_3:
        Sonic_c = f"**-**\n"
        await Sonic.client.send_file(Sonic.chat_id, gifrz_3, caption=Sonic_c, reply_to=roz)

@bot.on(admin_cmd(outgoing=True, pattern="و4$"))
@bot.on(sudo_cmd(pattern="و4$", allow_sudo=True))
async def GIFANIME(Sonic):
    if Sonic.fwd_from:
        return
    roz = await rd(Sonic)
    if gifrz_4:
        Sonic_c = f"**-**\n"
        await Sonic.client.send_file(Sonic.chat_id, gifrz_4, caption=Sonic_c, reply_to=roz)

@bot.on(admin_cmd(outgoing=True, pattern="و5$"))
@bot.on(sudo_cmd(pattern="و5$", allow_sudo=True))
async def GIFANIME(Sonic):
    if Sonic.fwd_from:
        return
    roz = await rd(Sonic)
    if gifrz_5:
        Sonic_c = f"**-**\n"
        await Sonic.client.send_file(Sonic.chat_id, gifrz_5, caption=Sonic_c, reply_to=roz)

@bot.on(admin_cmd(outgoing=True, pattern="و6$"))
@bot.on(sudo_cmd(pattern="و6$", allow_sudo=True))
async def GIFANIME(Sonic):
    if Sonic.fwd_from:
        return
    roz = await rd(Sonic)
    if gifrz_6:
        Sonic_c = f"**-**\n"
        await Sonic.client.send_file(Sonic.chat_id, gifrz_6, caption=Sonic_c, reply_to=roz)

@bot.on(admin_cmd(outgoing=True, pattern="و7$"))
@bot.on(sudo_cmd(pattern="و7$", allow_sudo=True))
async def GIFANIME(Sonic):
    if Sonic.fwd_from:
        return
    roz = await rd(Sonic)
    if gifrz_7:
        Sonic_c = f"**-**\n"
        await Sonic.client.send_file(Sonic.chat_id, gifrz_7, caption=Sonic_c, reply_to=roz)

@bot.on(admin_cmd(outgoing=True, pattern="و8$"))
@bot.on(sudo_cmd(pattern="و8$", allow_sudo=True))
async def GIFANIME(Sonic):
    if Sonic.fwd_from:
        return
    roz = await rd(Sonic)
    if gifrz_8:
        Sonic_c = f"**-**\n"
        await Sonic.client.send_file(Sonic.chat_id, gifrz_8, caption=Sonic_c, reply_to=roz)

@bot.on(admin_cmd(outgoing=True, pattern="و9$"))
@bot.on(sudo_cmd(pattern="و9$", allow_sudo=True))
async def GIFANIME(Sonic):
    if Sonic.fwd_from:
        return
    roz = await rd(Sonic)
    if gifrz_9:
        Sonic_c = f"**-**\n"
        await Sonic.client.send_file(Sonic.chat_id, gifrz_9, caption=Sonic_c, reply_to=roz)

@bot.on(admin_cmd(outgoing=True, pattern="و10$"))
@bot.on(sudo_cmd(pattern="و10$", allow_sudo=True))
async def GIFANIME(Sonic):
    if Sonic.fwd_from:
        return
    roz = await rd(Sonic)
    if gifrz_10:
        Sonic_c = f"**-**\n"
        await Sonic.client.send_file(Sonic.chat_id, gifrz_10, caption=Sonic_c, reply_to=roz)

@bot.on(admin_cmd(outgoing=True, pattern="و11$"))
@bot.on(sudo_cmd(pattern="و11$", allow_sudo=True))
async def GIFANIME(Sonic):
    if Sonic.fwd_from:
        return
    roz = await rd(Sonic)
    if gifrz_11:
        Sonic_c = f"**-**\n"
        await Sonic.client.send_file(Sonic.chat_id, gifrz_11, caption=Sonic_c, reply_to=roz)

@bot.on(admin_cmd(outgoing=True, pattern="و12$"))
@bot.on(sudo_cmd(pattern="و12$", allow_sudo=True))
async def GIFANIME(Sonic):
    if Sonic.fwd_from:
        return
    roz = await rd(Sonic)
    if gifrz_12:
        Sonic_c = f"**-**\n"
        await Sonic.client.send_file(Sonic.chat_id, gifrz_12, caption=Sonic_c, reply_to=roz)

CMD_HELP.update(
    {
        "متحركات":" ارسل  .المتحركات لعرض اوامر المتحركات"
    }
)
