import os
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from config import *
import openai
openai.api_key = OPENAI_API

bot = Client("my_bot",api_id=api_id, api_hash=api_hash,bot_token=bot_token)  

# @bot.on_message(filters.command(["start"]))
# async def send_start(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
#     if str(message.chat.id).startswith("-100") and message.chat.id not in GROUP_ID:
#         return
#     elif message.chat.id not in GROUP_ID:
#         if UPDATES_CHANNEL != "None":
#             try:
#                 user = await bot.get_chat_member(UPDATES_CHANNEL, message.chat.id)
#                 if user.status == enums.ChatMemberStatus.BANNED:
#                     await bot.send_message(
#                         chat_id=message.chat.id,
#                         text=f"__Sorry, you are banned. Contact My [ Owner ](https://telegram.me/{OWNER_USERNAME})__",
#                         disable_web_page_preview=True
#                     )
#                     return
#             except UserNotParticipant:
#                  await bot.send_message(
#                     chat_id=message.chat.id,
#                     text="<i>🔐 Join Channel To Use Me 🔐</i>",
#                     reply_markup=InlineKeyboardMarkup(
#                         [
#                             [
#                                 InlineKeyboardButton("🔓 Join Now 🔓", url=f"https://t.me/{UPDATES_CHANNEL}")
#                             ]
#                         ]
#                     ),

#                 )
#                  return
#             except Exception:
#                 await bot.send_message(
#                     chat_id=message.chat.id,
#                     text=f"<i>Something went wrong</i> <b> <a href='https://telegram.me/{OWNER_USERNAME}'>CLICK HERE FOR SUPPORT </a></b>",

#                     disable_web_page_preview=True)
#                 return
#     await bot.send_message(message.chat.id, f"__👋 Hi **{message.from_user.mention}**, Special AI features including ChatBot, you don't believe me? ask me anything",
#                            reply_markup=InlineKeyboardMarkup([[ InlineKeyboardButton("❤️ Owner ❤️", url=f"https://telegram.me/{OWNER_USERNAME}")]]), reply_to_message_id=message.id)

@bot.on_message(filters.command(["start"]))
def send_start(bot, message):
    bot.send_message(message.chat.id, f"__👋 Hi **{message.from_user.mention}**, Special AI features including ChatBot, you don't believe me? ask me anything",
    reply_markup=InlineKeyboardMarkup([[ InlineKeyboardButton("❤️ Owner ❤️", url=f"https://telegram.me/{OWNER_USERNAME}")]]), reply_to_message_id=message.id)
    
@bot.on_message(filters.command(["ask"]))
async def answer(bot, message):
    lol = message.chat.id
    if True: 
        await bot.send_message(lol, f"entered true")
        user_id = message.chat.id
        if user_id:
            await bot.send_message(lol, f"entered userid {user_id}")
            try:
                await bot.send_message(lol, f"entered try")
                message = message.text.replace("/ask ","")
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
                footer_credit = f"Join My Updates Channel 🦋 @{UPDATES_CHANNEL} 🦋 \nOwner 🦋 @{OWNER_USERNAME} 🦋"
                response = response.choices[0].text 
                await bot.send_message(lol, f"response completed")
                await bot.send_message(AI_LOGS, text=f"⚡️⚡️#AI_Query \n\n• A user named **{message.from_user.mention}** with user id - `{user_id}`. Asked me this query...\n\n══❚█══Q   U   E   R   Y══█❚══\n\n\n[Q྿.]**{message}**\n\n👇Here is what i responded:\n:-`{response}`\n\n\n❚═USER ID═❚═• `{user_id}` \n❚═USER Name═❚═• `{message.from_user.mention}` \n\n🗃️")
                await bot.send_message(lol, f"{response}\n\n\n{footer_credit}")
            except Exception as error:
                print(error)
                bot.send_message(lol, f"entered error")
    else:
        bot.send_message(lol, f"entered else")
        return

print("Bot Starting")
bot.run()
