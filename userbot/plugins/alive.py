import time
from platform import python_version

from telethon import version

from . import alive_name, starttime, catversion, get_readable_time, mention, reply_id

defaultuser = alive_name or "cat"
cat_img = config.alive_pic or "https://telegra.ph/file/9af8c7015d398fdb9f368.jpg"
custom_alive_text = config.custom_alive_text or "s᥆ᥙℛᥴᥱ sky 𖣂"
emoji = config.custom_alive_emoji or " ☆:↫"


@bot.on(admin_cmd(outgoing=true, pattern="فحص$"))
@bot.on(sudo_cmd(pattern="فحص$", allow_sudo=true))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    uptime = await get_readable_time((time.time() - starttime))
    _, check_sgnirts = check_data_base_heal_th()
    if cat_img:
        cat_caption = f"**{custom_alive_text}**\n\n"
        cat_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧskyⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        cat_caption += f"**{emoji} قاعدة البيانات :** `{check_sgnirts}`\n"
        cat_caption += f"**{emoji} اصدار التليثون  :** `{version.__version__}\n`"
        cat_caption += f"**{emoji} اصدار سكاي :** `{catversion}`\n"
        cat_caption += f"**{emoji} اصدار البايثون :** `{python_version()}\n`"
        cat_caption += f"**{emoji} مدة التشغيل :** `{uptime}\n`"
        cat_caption += f"**{emoji} المستخدم:** {mention}\n"
        cat_caption += f"**{emoji}**  **[مطور السورس]**(t.me/eeeee1k)  𓆰 .\n"
        cat_caption += f"**{emoji}**  **[رابط التنصيب]**(http://t.me/CXRCX/342)  𓆰 .\n"
        cat_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧskyⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        await alive.client.send_file(
            alive.chat_id, cat_img, caption=cat_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{custom_alive_text}**\n\n"
            f"**{emoji} قاعدة البيانات :** `{check_sgnirts}`\n"
            f"**{emoji} اصدار التليثون :** `{version.__version__}\n`"
            f"**{emoji} اصدار سكاي :** `{catversion}`\n"
            f"**{emoji} اصدار البايثون :** `{python_version()}\n`"
            f"**{emoji} مدة التشغيل :** `{uptime}\n`"
            f"**{emoji} المستخدم:** {mention}\n",
        )


@bot.on(admin_cmd(outgoing=true, pattern="ialive$"))
@bot.on(sudo_cmd(pattern="ialive$", allow_sudo=true))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    tgbotusername = config.tg_bot_username
    reply_to_id = await reply_id(alive)
    cat_caption = f"**catuserbot is up and running**\n"
    cat_caption += f"**  -telethon version :** `{version.__version__}\n`"
    cat_caption += f"**  -catuserbot version :** `{catversion}`\n"
    cat_caption += f"**  -python version :** `{python_version()}\n`"
    cat_caption += f"**  -master:** {mention}\n"
    results = await bot.inline_query(tgbotusername, cat_caption)  # pylint:disable=e0602
    await results[0].click(alive.chat_id, reply_to=reply_to_id, hide_via=true)
    await alive.delete()


# uniborg telegram userbot
# copyright (c) 2020 @uniborg
# this code is licensed under
# the "you can't use this for anything - public or private,
# unless you know the two prime factors to the number below" license
# 543935563961418342898620676239017231876605452284544942043082635399903451854594062955
# വിവരണം അടിച്ചുമാറ്റിക്കൊണ്ട് പോകുന്നവർ
# ക്രെഡിറ്റ് വെച്ചാൽ സന്തോഷമേ ഉള്ളു..!
# uniborg


def check_data_base_heal_th():
    # https://stackoverflow.com/a/41961968
    is_database_working = false
    output = "لم يتم تعيين قاعدة بيانات"
    if not config.db_uri:
        return is_database_working, output
    from userbot.plugins.sql_helper import session

    try:
        # to check database we will execute raw query
        session.execute("select 1")
    except exception as e:
        output = f"❌ {str(e)}"
        is_database_working = false
    else:
        output = "تعمل بنجاح ✅"
        is_database_working = true
    return is_database_working, output


cmd_help.update(
    {
        "alive": "**plugin :** `alive`\
      \n\n  •  **syntax : **`.alive` \
      \n  •  **function : **__status of bot will be showed__\
      \n\n  •  **syntax : **`.ialive` \
      \n  •  **function : **__inline status of bot will be shown.__\
      \nset `alive_pic` var for media in alive message"
    }
)