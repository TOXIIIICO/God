import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["توكسي"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/4a1e93b4660b7de2130c5.jpg",
        caption=f"""╭──── • ◈ • ────╮
么 [َ𝚂𝙾𝚞𝚁𝚂 𝚃𝙾𝚇𝙸𝙲 (t.me/CMG_5S)
么 [ᯓ 𝙳𝙴𝚅 𝚃𝙾𝚇𝙸𝙲](t.me/T_O_X4)
么 [َ ᥉υρρ᥆ᖇƚ ](t.me/O_A_H2)
╰──── • ◈ • ────╯
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "‹ ᯓ 𝙳𝙴𝚅 𝚃𝙾𝚇𝙸𝙲 𝅘𝅥𝅯 . 🕷 › ", url=f"https://t.me/T_O_X4"),
                ],[
                    InlineKeyboardButton(
                        "‹ ᯓ 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𖠛›", url=f"https://t.me/CMG_5S"), 
                    InlineKeyboardButton(
                        "‹ ᯓ 𝚂𝚞𝙿𝙿𝙾𝚁𝚃 𖠛›", url=f"https://t.me/O_A_H2"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف البوت لمجموعتك ›", url=f"https://t.me/A_Rn_obot?startgroup=true"),
            ]
        ]
         ),
     )
  
@app.on_message(
    command(["سورس","‹ السورس ›","جودز","السورس", "جودزيلا"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/8c6b3160f70e64270e880.jpg",
        caption=f"""╭──── • ◈ • ────╮
么 [َ𝚂𝙾𝚄𝚁𝙲𝙴 𝙶𝙾𝙳𝚉𝙸𝙻𝙻𝙰 (t.me/El_Godzy)
么 [ᯓ 𝙳𝙴𝚅 𝙶𝙾𝙳𝚉𝙸𝙻𝙻𝙰](t.me/G1_d_U)
么 [َ ᥉υρρ᥆ᖇƚ ](t.me/GOoOdzill_1)
╰──── • ◈ • ────╯
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "‹ ᯓ 𝙳𝙴𝚅 𝙶𝙾𝙳𝚉𝙸𝙻𝙻𝙰 𝅘𝅥𝅯 . 🕷 › ", url=f"https://t.me/@G1_d_U"),
                ],[
                    InlineKeyboardButton(
                        "‹ ᯓ 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𖠛›", url=f"https://t.me/El_Godzy"), 
                    InlineKeyboardButton(
                        "‹ ᯓ 𝚂𝚞𝙿𝙿𝙾𝚁𝚃 𖠛›", url=f"https://t.me/GOoOdzill_1"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف البوت لمجموعتك ›", url=f"https://t.me/A_Rn_obot?startgroup=true"),
            ]
        ]
         ),
     )