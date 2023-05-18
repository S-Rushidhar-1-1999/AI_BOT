from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from config import *
import openai
openai.api_key = OPENAI_API

@Client.on_message(filters.private & filters.text)
async def answer(client, message):
    try : 
        user_id = message.from_user.id
        if user_id:
            try:
                message = message.text
                user_id = message.from_user.id
                response = openai.Completion.create(
                    model = "text-davinci-003",
                    prompt = message,
                    temperature = 0.5, 
                    max_tokens = 1000,
                    top_p=1,
                    frequency_penalty=0.1,
                    presence_penalty = 0.0,
                )
                btn=[
                        [InlineKeyboardButton(text=f"Updates Channel", url=f'https://telegram.me/{UPDATES_CHANNEL}')],
                        [InlineKeyboardButton(text=f"Owner", url=f'https://telegram.me/{OWNER}')]
                    ]
                reply_markup=InlineKeyboardMarkup(btn)
                footer_credit = f"Join My Updates Channel 🦋 @{UPDATES_CHANNEL} 🦋 \nOwner 🦋 @{OWNER} 🦋"
                response = response.choices[0].text 
                await client.send_message(AI_LOGS, text=f"⚡️⚡️#AI_Query \n\n• A user named **{message.from_user.mention}** with user id - `{user_id}`. Asked me this query...\n\n══❚█══Q   U   E   R   Y══█❚══\n\n\n[Q྿.]**{message}**\n\n👇Here is what i responded:\n:-`{response}`\n\n\n❚═USER ID═❚═• `{user_id}` \n❚═USER Name═❚═• `{message.from_user.mention}` \n\n🗃️" , reply_markup = reply_markup )
                await message.reply(f"{response}\n\n\n{footer_credit}")
            except Exception as error:
                print(error)
    except :
        return
