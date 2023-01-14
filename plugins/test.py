import os
import requests
import random
import asyncio
from pyrogram import Client, filters, idle
from pyrogram.types import Message 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

RKPICS = (environ.get('RKPICS', 'https://te.legra.ph/file/3c3b0f2213771a593191d.jpg https://te.legra.ph/file/f4673c1c4d0cb92a3a7f4.jpg')).split()
# S1 E100

RKCAP100 = """😇 **(--'𝐑adha𝐊rishn'--)-2018** ✨
•• | [Season 1 - Episode 100](https://t.me/rkrishnaa) | ••
_
#Dj 👌"""

RKBUTTON100 = InlineKeyboardMarkup([[InlineKeyboardButton('720p', url='https://telegram.me/RKrishnaBot?start=Z2V0LTE2OTM4NzA3NDgzNDI2ODQ'), InlineKeyboardButton('1080p', url='https://telegram.me/RKrishnaBot?start=Z2V0LTE2OTI4NjkwNTA2Nzk1NjA')], [InlineKeyboardButton('[ • 𝚄𝚙𝚍𝚊𝚝𝚎𝚜!! • ]', url='https://t.me/RkrishnaDj')]])

@Client.on_message(filters.regex("/rks1 E100")) 
async def rkepdj(_, message):
    if message.text in ['/rks1 E100']:
        dj = await message.reply_text(text = '<code>Checking DStore...</code>', reply_to_message_id=message.id, quote = True)
        await asyncio.sleep(1)
        await dj.edit_text("<code>Please wait...</code>")
        await asyncio.sleep(2)
        await dj.delete()
        idj = await message.reply_photo(photo=random.choice(RKPICS), caption=RKCAP100, reply_to_message_id=message.id, 
        reply_markup=RKBUTTON100)
        await asyncio.sleep(600)
        await idj.delete()
        await message.delete() 
