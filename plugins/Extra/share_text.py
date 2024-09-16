# Don't Remove Credit @AmRobots_Bots
# Subscribe YouTube Channel For Amazing Bot @AmRobotsTech
# Ask Doubt on telegram @Am_Robots


import os
from pyrogram import Client, filters
from urllib.parse import quote
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command(["share_text", "share", "sharetext"]))
async def share_text(client, message):
    amrobots = await client.ask(chat_id = message.from_user.id, text = "Now Send me your text.")
    if amrobots and (amrobots.text or amrobots.caption):
        input_text = amrobots.text or amrobots.caption
    else:
        await amrobots.reply_text(
            text=f"**Notice:**\n\n1. Send Any Text Messages.\n2. No Media Support\n\n**Any Question Join Support Chat**",               
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Updates Channel", url=f"https://t.me/Benzmovies")]])
            )                                                   
        return
    await amrobots.reply_text(
        text=f"**Here is Your Sharing Text 👇**\n\nhttps://t.me/share/url?url=" + quote(input_text),
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("♂️ Share", url=f"https://t.me/share/url?url={quote(input_text)}")]])       
    )
