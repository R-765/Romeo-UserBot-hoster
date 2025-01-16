from random import choice
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import Message
from Romeo.helper.gm import *
from Romeo.helper.nw import *
from Romeo import spam_chats, SUDO_USER

@Client.on_message(filters.command(["gmorning", "ggm", "gg"], [".", "?", "/"]) & (filters.me | filters.user(SUDO_USER)))
async def ggm(client: Client, message: Message):
    chat_id = message.chat.id
    await message.delete()
    spam_chats.append(chat_id)
    tagged_users = []
    async for usr in client.get_chat_members(chat_id):
        if chat_id not in spam_chats:
            break
        tagged_users.append(f"[{usr.user.first_name}](tg://user?id={usr.user.id})")
        if len(tagged_users) == 4:
            S = choice(GGM)
            p = f"ㅤ"
            usrtxt = ", ".join(tagged_users)
            txt = f"{p}\n{usrtxt}\n{p}"
            await client.send_video(chat_id, video=S, caption=txt)
            await sleep(3)
            tagged_users = []
    try:
        spam_chats.remove(chat_id)
    except ValueError:
        pass


@Client.on_message(filters.command(["sgmorning", "sggm", "sgg"], [".", "?", "/"]) & (filters.me | filters.user(SUDO_USER)))
async def sggm(client: Client, message: Message):
    chat_id = message.chat.id
    await message.delete()
    spam_chats.append(chat_id)
    tagged_users = set()
    async for usr in client.get_chat_members(chat_id):
        if chat_id not in spam_chats:
            break
        if usr.user.id not in tagged_users:
            tagged_users.add(usr.user.id)
            txt = f"[{usr.user.first_name}](tg://user?id={usr.user.id})"
            if len(tagged_users) == 1:
                R = choice(GGM)
                q = f"ㅤ"
                txt = f"{q}\n{txt}\n{q}"
                await client.send_video(chat_id, video=R, caption=txt)
                await sleep(3)
                tagged_users.clear()  # Clear the set for the next round
    try:
        spam_chats.remove(chat_id)
    except ValueError:
        pass
        

@Client.on_message(filters.command(["morning", "gm", "g"], [".", "?", "/"]) & (filters.me | filters.user(SUDO_USER)))
async def gm(client: Client, message: Message):
    chat_id = message.chat.id
    await message.delete()
    spam_chats.append(chat_id)
    tagged_users = []
    async for usr in client.get_chat_members(chat_id):
        if chat_id not in spam_chats:
            break
        tagged_users.append(f"[{usr.user.first_name}](tg://user?id={usr.user.id})")
        if len(tagged_users) == 4:
            a = choice(GM)
            usrtxt = ", ".join(tagged_users)
            txt = f"{a}\n\n{usrtxt}"
            await client.send_message(chat_id, txt)
            await sleep(3)
            tagged_users = []
    try:
        spam_chats.remove(chat_id)
    except ValueError:
        pass

@Client.on_message(filters.command(["smorning", "sgm", "sg"], [".", "?", "/"]) & (filters.me | filters.user(SUDO_USER)))
async def sgm(client: Client, message: Message):
    chat_id = message.chat.id
    await message.delete()
    spam_chats.append(chat_id)
    tagged_users = set()
    async for usr in client.get_chat_members(chat_id):
        if chat_id not in spam_chats:
            break
        if usr.user.id not in tagged_users:
            tagged_users.add(usr.user.id)
            usrtxt = f"[{usr.user.first_name}](tg://user?id={usr.user.id})"
            if len(tagged_users) == 1:
                b = choice(GM)
                txt = f"{b}\n\n{usrtxt}"
                await client.send_message(chat_id, txt)
                await sleep(3)
                tagged_users.clear()
    try:
        spam_chats.remove(chat_id)
    except ValueError:
        pass
