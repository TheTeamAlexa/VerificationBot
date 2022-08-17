# TeamAlexa Verification Bot Property Of TeamAlexa
# Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# TeamAlexa © @Dr_Asad_Ali © TeamAlexa
# Owner Asad + Harshit

import random
import aiohttp
import asyncio
from configs import Config
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from TeamAlexa.markup_maker import MakeCaptchaMarkup
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message,
    CallbackQuery,
    ChatPermissions,
)

CaptchaBot = Client(
    session_name=Config.SESSION_NAME,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
)
CaptchaDB = {}


@CaptchaBot.on_message(filters.command("start"))
async def start_handler(_, event: Message):
    await event.reply_text(
        "**ʜᴇʟʟᴏ sᴡᴇᴇᴛ ʜᴇᴀʀᴛ ɪ ᴀᴍ ʀᴏᴄᴋs ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ʙᴏᴛ ᴛᴏ ᴠᴇʀɪғʏ ᴛʜᴇ ɴᴇᴡ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs ɪɴ ᴛᴇʟᴇɢʀᴀᴍ**👻\n\n**ɢɪᴠᴇ ᴍᴇ ʜᴇᴀʀᴛ** [ʟᴏᴠᴇ](https://t.me/Give_Me_Heart) [ᴊᴏɪɴ](t.me/Shayri_Music_Lovers) **ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ**.",
        disable_web_page_preview=True,
    )


@CaptchaBot.on_chat_member_updated()
async def welcome_handler(bot: Client, event: Message):
    if (event.chat.id != Config.GROUP_CHAT_ID) or (event.from_user.is_bot is True):
        return
    try:
        user_ = await bot.get_chat_member(event.chat.id, event.from_user.id)
        if (user_.is_member is False) and (
            CaptchaDB.get(event.from_user.id, None) is not None
        ):
            try:
                await bot.delete_messages(
                    chat_id=event.chat.id,
                    message_ids=CaptchaDB[event.from_user.id]["message_id"],
                )
            except:
                pass
            return
        elif (user_.is_member is False) and (
            CaptchaDB.get(event.from_user.id, None) is None
        ):
            return
    except UserNotParticipant:
        return
    try:
        if CaptchaDB.get(event.from_user.id, None) is not None:
            try:
                await bot.send_message(
                    chat_id=event.chat.id,
                    text=f"{event.from_user.mention} 🙄 **ᴏʏᴇ ɴᴏᴏʙ ʙɪɴᴀ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ɢʀᴏᴜᴘ ᴊᴏɪɴ ᴋɪʏᴀ**!\n\n"
                    f"😜 **ʜᴇ ᴄᴀɴ ᴛʀʏ ᴀɢᴀɪɴ ᴀғᴛᴇʀ 10ᴍ**.",
                    disable_web_page_preview=True,
                )
                await bot.restrict_chat_member(
                    chat_id=event.chat.id,
                    user_id=event.from_user.id,
                    permissions=ChatPermissions(can_send_messages=False),
                )
                await bot.delete_messages(
                    chat_id=event.chat.id,
                    message_ids=CaptchaDB[event.from_user.id]["message_id"],
                )
            except:
                pass
            await asyncio.sleep(600)
            del CaptchaDB[event.from_user.id]
        else:
            await bot.restrict_chat_member(
                chat_id=event.chat.id,
                user_id=event.from_user.id,
                permissions=ChatPermissions(can_send_messages=False),
            )
            await bot.send_message(
                chat_id=event.chat.id,
                text=f"{event.from_user.mention}, ❤️ **ʜᴏᴡ ᴀʀᴇ ʏᴏᴜ ᴛᴏ ᴄʜᴀᴛ ʜᴇʀᴇ ᴘʟᴇᴀsᴇ ᴠɪʀɪғʏ ᴛʜᴀᴛ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀ ʙᴏᴛ**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "ᴠᴇʀɪғʏ ɴᴏᴡ",
                                callback_data=f"startVerify_{str(event.from_user.id)}",
                            )
                        ]
                    ]
                ),
            )
    except:
        pass


@CaptchaBot.on_callback_query()
async def buttons_handlers(bot: Client, cb: CallbackQuery):
    if cb.data.startswith("startVerify_"):
        __user = cb.data.split("_", 1)[-1]
        if cb.from_user.id != int(__user):
            await cb.answer(
                "🙄 𝗧𝗵𝗶𝘀 𝗠𝗲𝘀𝘀𝗮𝗴𝗲 𝗜𝘀 𝗡𝗼𝘁 𝗙𝗼𝗿 𝗬𝗼𝘂 𝗜𝘁𝘁𝘂 🤏 𝗦𝗲𝘆 𝗡𝗼𝗼𝗯!", show_alert=True
            )
            return
        await cb.message.edit("😏 **ɢᴇɴᴇʀᴀᴛɪɴɢ ᴄᴀᴘᴛᴄʜᴇ** ...")
        print("Fetching Captcha JSON Data ...")
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://api.abirhasan.wtf/captcha?token={Config.CAPTCHA_API_TOKEN}"
            ) as res:
                if res.status != 200:
                    try:
                        UserOnChat = await bot.get_chat_member(
                            user_id=cb.from_user.id, chat_id=cb.message.chat.id
                        )
                        if UserOnChat.restricted_by.id == (await bot.get_me()).id:
                            await bot.unban_chat_member(
                                chat_id=cb.message.chat.id, user_id=cb.from_user.id
                            )
                    except:
                        pass
                    await cb.message.edit("😢 𝗨𝗻𝗮𝗯𝗹𝗲 𝗧𝗼 𝗚𝗲𝘁 𝗖𝗮𝗽𝘁𝗰𝗵𝗲!")
                    return
                data = await res.json()
                print("Done!")
                markup = [[], [], []]
                __emojis = data["CaptchaAnswer"].split(": ", 1)[-1].split()
                print(__emojis)
                _emojis = [
                    "🐻",
                    "🐔",
                    "☁️",
                    "🔮",
                    "🌀",
                    "🌚",
                    "💎",
                    "🐶",
                    "🍩",
                    "🌏",
                    "🐸",
                    "🌕",
                    "🍏",
                    "🐵",
                    "🌙",
                    "🐧",
                    "🍎",
                    "😀",
                    "🐍",
                    "❄️",
                    "🥺",
                    "🐢",
                    "🌝",
                    "🍺",
                    "🍔",
                    "🍒",
                    "🍫",
                    "🍡",
                    "🌑",
                    "🍟",
                    "☕️",
                    "🍑",
                    "🍷",
                    "🍧",
                    "🍕",
                    "🍵",
                    "🐋",
                    "🐱",
                    "💄",
                    "👠",
                    "💰",
                    "💸",
                    "🎹",
                    "📦",
                    "📍",
                    "🐊",
                    "🦕",
                    "🐬",
                    "💋",
                    "🦎",
                    "🦈",
                    "🦷",
                    "🦖",
                    "🐠",
                    "🐟",
                    "💀",
                    "🎃",
                    "👮",
                    "⛑",
                    "👨‍🔧",
                    "🧶",
                    "🧵",
                    "😢",
                    "🧥",
                    "🥼",
                    "🥻",
                    "🤏",
                    "👑",
                    "🎒",
                    "🙊",
                    "🐗",
                    "🦋",
                    "🦐",
                    "🐀",
                    "🐿",
                    "🦔",
                    "🦦",
                    "💖",
                    "🦡",
                    "🦨",
                    "🐇",
                ]
                print("Cleaning Answer Emojis from Emojis List ...")
                for a in range(len(__emojis)):
                    if __emojis[a] in _emojis:
                        _emojis.remove(__emojis[a])
                show = __emojis
                print("Appending New Emoji List ...")
                for b in range(9):
                    show.append(_emojis[b])
                print("Randomizing ...")
                random.shuffle(show)
                count = 0
                print("Appending to ROW - 1")
                for _ in range(5):
                    markup[0].append(
                        InlineKeyboardButton(
                            f"{show[count]}",
                            callback_data=f"verify_{str(cb.from_user.id)}_{show[count]}",
                        )
                    )
                    count += 1
                print("Appending to ROW - 2")
                for _ in range(5):
                    markup[1].append(
                        InlineKeyboardButton(
                            f"{show[count]}",
                            callback_data=f"verify_{str(cb.from_user.id)}_{show[count]}",
                        )
                    )
                    count += 1
                print("Appending to ROW - 3")
                for _ in range(5):
                    markup[2].append(
                        InlineKeyboardButton(
                            f"{show[count]}",
                            callback_data=f"verify_{str(cb.from_user.id)}_{show[count]}",
                        )
                    )
                    count += 1
                print("Setting Up in Database ...")
                CaptchaDB[cb.from_user.id] = {
                    "emojis": data["CaptchaAnswer"].split(": ", 1)[-1].split(),
                    "mistakes": 0,
                    "group_id": cb.message.chat.id,
                    "message_id": None,
                }
                print("Sending Captcha ...")
                __message = await bot.send_photo(
                    chat_id=cb.message.chat.id,
                    photo=data["DownloadURL"],
                    caption=f"{cb.from_user.mention}, 😉 **sᴇʟᴇᴄᴛ ᴀʟʟ ᴛʜᴇ ᴇᴍᴏᴊɪᴇs ᴄᴀɴ sᴇᴇ ɪɴ ᴛʜɪs ᴘɪᴄᴛᴜʀᴇ**. "
                    f"🤗 **ʏᴏᴜ ᴀʀᴇ ᴀʟʟᴏᴡᴇᴅ ᴏɴʟʏ** (3) **ᴍɪsᴛᴀᴄᴋᴇs**.",
                    reply_markup=InlineKeyboardMarkup(markup),
                )
                CaptchaDB[cb.from_user.id]["message_id"] = __message.message_id
                await cb.message.delete(revoke=True)

    elif cb.data.startswith("verify_"):
        __emoji = cb.data.rsplit("_", 1)[-1]
        __user = cb.data.split("_")[1]
        if cb.from_user.id != int(__user):
            await cb.answer("😜 𝗨𝗹𝗼 𝗬𝗲 𝗠𝗲𝘀𝘀𝗮𝗴𝗲 𝗧𝗲𝗿𝗲 𝗟𝗶𝘆𝗲 𝗡𝗶 𝗛𝗮𝗶!", show_alert=True)
            return
        if cb.from_user.id not in CaptchaDB:
            await cb.answer("😉 𝗧𝗿𝘆 𝗔𝗴𝗮𝗶𝗻 𝗔𝗳𝘁𝗲𝗿 𝗥𝗲_𝗝𝗼𝗶𝗻𝗶𝗻𝗴!", show_alert=True)
        if __emoji not in CaptchaDB.get(cb.from_user.id).get("emojis"):
            CaptchaDB[cb.from_user.id]["mistakes"] += 1
            await cb.answer("🙄 𝗬𝗼𝘂 𝗣𝗿𝗲𝘀𝘀𝗲𝗱 𝗔 𝗪𝗿𝗼𝗻𝗴 𝗘𝗺𝗼𝗷𝗶!", show_alert=True)
            n = 3 - CaptchaDB[cb.from_user.id]["mistakes"]
            if n == 0:
                await cb.message.edit_caption(
                    f"{cb.from_user.mention}, **😢 **ʏᴏᴜ ғᴀɪʟᴇᴅ ᴛᴏ ᴘᴀss ᴛʜᴇ ᴄᴀᴘᴛᴄʜᴇ**!\n\n"
                    f"❤️ **ʏᴏᴜ ᴄᴀɴ ᴛʀʏ ᴀɢᴀɪɴ ᴀғᴛᴇʀ 10ᴍ ᴏʀ ᴄᴏɴᴛᴀᴄᴛ** @Dr_Asad_Ali.",
                    reply_markup=None,
                )
                await asyncio.sleep(600)
                del CaptchaDB[cb.from_user.id]
                return
            markup = await MakeCaptchaMarkup(
                cb.message["reply_markup"]["inline_keyboard"], __emoji, "❌"
            )
            await cb.message.edit_caption(
                caption=f"{cb.from_user.mention}, select all the emojis you can see in the picture. "
                f"😜  **ʏᴏᴜ ᴀʀᴇ ᴀʟʟᴏᴡᴇᴅ ᴏɴʟʏ** ({n}) **ᴍɪsᴛᴀᴄᴋᴇs**.",
                reply_markup=InlineKeyboardMarkup(markup),
            )
            return
        else:
            CaptchaDB.get(cb.from_user.id).get("emojis").remove(__emoji)
            markup = await MakeCaptchaMarkup(
                cb.message["reply_markup"]["inline_keyboard"], __emoji, "✅"
            )
            await cb.message.edit_reply_markup(
                reply_markup=InlineKeyboardMarkup(markup)
            )
            if not CaptchaDB.get(cb.from_user.id).get("emojis"):
                await cb.answer("❤️ 𝗬𝗼𝘂 𝗣𝗮𝘀𝘀𝗲𝗱 𝗧𝗵𝗲 𝗖𝗮𝗽𝘁𝗰𝗵𝗲", show_alert=True)
                del CaptchaDB[cb.from_user.id]
                try:
                    UserOnChat = await bot.get_chat_member(
                        user_id=cb.from_user.id, chat_id=cb.message.chat.id
                    )
                    if UserOnChat.restricted_by.id == (await bot.get_me()).id:
                        await bot.unban_chat_member(
                            chat_id=cb.message.chat.id, user_id=cb.from_user.id
                        )
                except:
                    pass
                await cb.message.delete(True)
            await cb.answer()


CaptchaBot.run()
