import time

from . import StartTime, get_readable_time, reply_id

DEFAULTUSER = "Yꪮꪶꪖꪀᦔ˼༒࿅"
CAT_IMG = "https://telegra.ph/file/b02c0afc76b7ae6cb111a.mp4"
CUSTOM_ALIVE_TEXT = "𓆩 𝙎𝙊𝙐𝙍𝘾𝞝-˹Yꪮꪶꪖꪀᦔ˼༒࿅ - 𝑫𝑬𝑽𝑬𝑳𝑶𝑷𝑬𝑹 𓆪"
EMOJI = "  𓄂† "


@bot.on(admin_cmd(outgoing=True, pattern="مرتضى$"))
@bot.on(sudo_cmd(pattern="مرتضى$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if CAT_IMG:
        cat_caption = f"**{CUSTOM_ALIVE_TEXT}**\n"
        cat_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧlandⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        cat_caption += f"**{EMOJI}** 𝑫𝑬𝑽 𝑼𝑺𝑬𝑹 ↬ @S_X_X_G ༗\n"
        cat_caption += f"**{EMOJI}** 𝑫𝑬𝑽 𝑰𝑫 ↬ 1566031059 ༗\n"
        cat_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧlandⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻"
        await alive.client.send_file(
            alive.chat_id, CAT_IMG, caption=cat_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n"
            f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧlandⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
            f"**{EMOJI}** 𝑫𝑬𝑽 𝑼𝑺𝑬𝑹 ↬ @S_X_X_G ༗\n"
            f"**{EMOJI}** 𝑫𝑬𝑽 𝑰𝑫 ↬ 1566031059 ༗\n"
            f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧlandⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻",
        )


def check_data_base_heal_th():
    # https://stackoverflow.com/a/41961968
    is_database_working = False
    output = "✾"
    if not Config.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION

    try:
        # to check database we will execute raw query
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "↫ "
        is_database_working = True
    return is_database_working, output
