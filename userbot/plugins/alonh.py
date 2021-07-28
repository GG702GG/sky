from telethon import events, Button
from ..Config import Config
from . import SKY, K, mention


@admin_cmd("/repo|#repo")
async def dev(kimo):
    await kimo.reply(
        "⌔∮ SOURCE SKY - RePo 𓆪",
        buttons=[[Button.url("🔗 RePo 🔗", K)]]
    )
   

SKY_PIC = Config.ALIVE_PIC if Config.ALIVE_PIC else "https://telegra.ph/file/fc612de7a6554dfb5527b.jpg

if Config.TG_BOT_USERNAME is not None and tgbot is not None:
    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        me = await bot.get_me()
        if query.startswith("بوت") and event.query.user_id == bot.uid:
            buttons = [
                [
                    Button.url("الرابط 🔗", K),
                    Button.url("المطور ⚙️", "https://t.me/CXRCX"),
                ]
            ]
            if SKY_PIC and SKY_PIC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(
                    SKY_PIC,
                    text=SKY,
                    buttons=buttons,
                    link_preview=False
                )
            elif SKY_PIC:
                result = builder.document(
                    SKY_PIC,
                    title="SOURCE SKY",
                    text=SKY,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="SOURCE SKY",
                    text=SKY,
                    buttons=buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)

@bot.on(admin_cmd(outgoing=True, pattern="بوت"))
async def repo(event):
    if event.fwd_from:
        return
    KIM = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(KIM, "بوت")
    await response[0].click(event.chat_id)
    await event.delete()