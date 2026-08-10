import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
)
from supabase import create_client, Client

# ==================== CONFIGURATION ====================
TELEGRAM_BOT_TOKEN = '8968388349:AAESPUXmaQbIaD6K1FRN5TU0jnmP5rvmgNU'
ADMIN_CHAT_ID = 6971757276
SUPABASE_URL = 'https://wvvmcrurtiyrzxhbdkyk.supabase.co'
SUPABASE_KEY = 'sb_publishable_UcLHxAmiKiPrlf532m3llw_2JuIj6ND'
CHANNEL_ID = -1003612039766
PHOTO_URL = 'https://ibb.co/x87fvV19'
QR_CODE_URL = 'https://ibb.co/HpfXKM2L'  # আপনার QR কোডের লিংক

# চ্যানেল থেকে যে যে মেসেজ ID ইউজার পাবে
VIDEO_MESSAGE_IDS = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# ========================================================

# Supabase Initialization
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- DB Helper Functions ---
def check_user_access(user_id: int) -> bool:
    try:
        response = supabase.table('users').select('has_access').eq('user_id', user_id).execute()
        if response.data and len(response.data) > 0:
            return response.data[0].get('has_access', False)
    except Exception as e:
        print(f"DB Error: {e}")
    return False

def set_user_access(user_id: int, status: bool):
    try:
        # upsert এর মাধ্যমে ইউজার আইডি থাকলে আপডেট হবে, না থাকলে নতুন তৈরি হবে
        supabase.table('users').upsert({'user_id': user_id, 'has_access': status}).execute()
        print(f"User {user_id} access set to {status}")
    except Exception as e:
        print(f"DB Error: {e}")

# --- Command & Event Handlers ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    has_access = check_user_access(user_id)
    
    caption = """
🚫𝐍𝐎 𝐏𝐔𝐁𝐋𝐈𝐂 𝐂𝐎𝐍𝐓𝐄𝐍𝐓 ❌
🟢𝐔𝐋𝐓𝐑𝐀 𝐔𝐍𝐒𝐄𝐄𝐍 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐓𝐇𝐈𝐍𝐆𝐒 

🎥  𝐑𝐚𝐫𝐞 𝐕𝐢𝐝𝐞𝐨𝐬 𝐂𝐨𝐥𝐥𝐞𝐜𝐭𝐢𝐨𝐧
🔥𝐃𝐚𝐢𝐥𝐲 500+ 𝐍𝐞𝐰 𝐕𝐢𝐫𝐚𝐥 𝐕𝐢𝐝𝐞𝐨𝐬 𝐀𝐝𝐝𝐞𝐝
✅ 𝐒𝐚𝐯𝐞 & 𝐅𝐨𝐫𝐰𝐚𝐫𝐝 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞
━━━━━━━━━━━━━━━━━━━━
💎𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐜𝐚𝐭𝐞𝐠𝐨𝐫𝐢𝐞𝐬 
Bro sleep sis 😻
Full hd long videos 
Pink maal long videos 
𝐎𝐧𝐥𝐲𝐟𝐚𝐧𝐬 𝐄𝐗𝐂𝐋𝐔𝐒𝐈𝐕𝐄𝐒 
𝐅𝐚𝐦𝐢𝐥𝐲 𝐈𝐍𝐂𝐄𝐒𝐓
𝐇𝐚𝐜𝐤𝐞𝐝 𝐜𝐜𝐭𝐯
𝐅𝐚𝐦𝐢𝐥𝐲 𝐬𝐩𝐲 
𝐃𝐔 𝐔𝐧𝐢𝐯𝐞𝐫𝐬𝐢𝐭𝐲 𝐋𝐄𝐀𝐊𝐒 
𝐁𝐃𝐒𝐌
𝐇𝐢𝐝𝐝𝐞𝐧 𝐜𝐚𝐦𝐬
𝐎𝐲𝐨 𝐥𝐞𝐚𝐤𝐞𝐝
𝐃𝐚𝐫𝐤 𝐰𝐨𝐫𝐥𝐝
𝐒𝐭𝐮𝐝𝐞𝐧𝐭 & 𝐭𝐞𝐚𝐜𝐡𝐞𝐫
𝐒𝐜𝐡𝐨𝐨𝐥 𝐠𝐢𝐫𝐥
𝐈𝐧𝐟𝐥𝐮𝐞𝐧𝐜𝐞𝐫/𝐚𝐜𝐭𝐫𝐞𝐬𝐬
𝐌𝐚𝐥𝐥𝐮/𝐭𝐞𝐥𝐚𝐠𝐮/𝐭𝐚𝐦𝐢𝐥/𝐛𝐞𝐧𝐠𝐚𝐥𝐢
𝐌𝐮𝐬𝐥𝐢𝐦 𝐇𝐈𝐉𝐀🇧🇮
𝐇𝐨𝐬𝐩𝐢𝐭𝐚𝐥 𝐥𝐞𝐤𝐚𝐬
𝐖𝐢𝐟𝐞 𝐚𝐟𝐟𝐚𝐢𝐫 𝐋𝐄𝐀𝐊𝐒
𝐑𝐞𝐚𝐥 𝐦𝐨𝐦&𝐬𝐨𝐧
𝐉𝐚𝐩𝐚𝐧𝐞𝐬𝐞/𝐤𝐨𝐫𝐞𝐚𝐧
𝐒𝐭𝐞𝐩𝐟𝐚𝐦𝐢𝐥𝐲
𝐏𝐚𝐤𝐢𝐬𝐭𝐚𝐧𝐢🇵🇰𝐦𝐚𝐚𝐥
𝐍𝐨𝐭𝐭𝐲 𝐀𝐦𝐞𝐫𝐢𝐜𝐚
𝐑𝐞𝐚𝐥 𝐛𝐫𝐨 & 𝐬𝐢𝐬

✅₹99only /-🇴🇳🇱🇾
"""
    
    if has_access:
        keyboard = [[InlineKeyboardButton("🎬 SEE VIDEOES", callback_data='view_videos')]]
    else:
        keyboard = [[InlineKeyboardButton("🛒 Buy Premium", callback_data='buy_course')]]
        
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    try:
        await update.message.reply_photo(
            photo=PHOTO_URL, 
            caption=caption,
            reply_markup=reply_markup
        )
    except Exception as e:
        print(f"Photo sending failed, falling back to text: {e}")
        await update.message.reply_text(
            text=caption, 
            reply_markup=reply_markup
        )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    if query.data == 'buy_course':
        msg = (
            "⚡ <b>PAYMENT GATEWAY</b>\n\n"
            "📛 <b>Access:</b> Lifetime VIP\n"
            "💵 <b>Amount:</b> ₹99\n"
            "🏦 <b>UPI ID:</b> <code>Q55147437@ybl</code>\n\n"
            "1️⃣ Scan QR Code\n"
            "2️⃣ Pay using UPI\n"
            "3️⃣ Click button below"
        )
        
        payment_keyboard = [
            [InlineKeyboardButton("✅ I HAVE PAID", callback_data='i_have_paid')],
            [InlineKeyboardButton("❌ CANCEL ORDER", callback_data='cancel_order')]
        ]
        reply_markup = InlineKeyboardMarkup(payment_keyboard)

        try:
            await query.message.reply_photo(
                photo=QR_CODE_URL,
                caption=msg,
                parse_mode='HTML',
                reply_markup=reply_markup
            )
        except Exception as e:
            print(f"Error sending QR Photo: {e}")
            await query.message.reply_text(text=msg, parse_mode='HTML', reply_markup=reply_markup)

    elif query.data == 'i_have_paid':
        await query.message.reply_text(
            "📸 <b>SEND SCREENSHOT NOW</b>\nUpload Payment Proof for 99",
            parse_mode='HTML'
        )

    elif query.data == 'cancel_order':
        await query.edit_message_caption(
            caption="❌ <b>Order Cancelled.</b>\n\nType /start to try again.",
            parse_mode='HTML'
        )

    elif query.data == 'view_videos':
        if check_user_access(user_id):
            await query.message.reply_text("...")
            for msg_id in VIDEO_MESSAGE_IDS:
                try:
                    await context.bot.copy_message(
                        chat_id=user_id, 
                        from_chat_id=CHANNEL_ID, 
                        message_id=msg_id, 
                        protect_content=True
                    )
                except Exception as e:
                    print(f"Error forwarding msg {msg_id}: {e}")
        else:
            await query.message.reply_text("Sorry, Your Access has not been approved")

async def handle_payment_screenshot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    photo = update.message.photo[-1]
    
    admin_keyboard = [
        [
            InlineKeyboardButton("✅ Approve", callback_data=f"approve_{user.id}"),
            InlineKeyboardButton("❌ Reject", callback_data=f"reject_{user.id}")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(admin_keyboard)
    
    admin_caption = (
        f"📩 <b>নতুন পেমেন্ট প্রুফ জমা পড়েছে!</b>\n\n"
        f"👤 <b>ইউজার:</b> {user.first_name} (@{user.username})\n"
        f"🆔 <b>User ID:</b> <code>{user.id}</code>"
    )
    
    await context.bot.send_photo(
        chat_id=ADMIN_CHAT_ID,
        photo=photo.file_id,
        caption=admin_caption,
        parse_mode='HTML',
        reply_markup=reply_markup
    )
    
    await update.message.reply_text("Your ScreenShot Has Send To Verify. Please Wait")

async def admin_action_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    data = query.data
    if data.startswith("approve_"):
        target_user_id = int(data.split("_")[1])
        
        # ডাটাবেসে এক্সেস গ্রান্ট করা হচ্ছে
        set_user_access(target_user_id, True)
        
        await query.edit_message_caption(caption=f"{query.message.caption}\n\n✅ <b>Status: Approved</b>", parse_mode='HTML')
        
        try:
            keyboard = [[InlineKeyboardButton("🎬 SEE VIDEOES", callback_data='view_videos')]]
            await context.bot.send_message(
                chat_id=target_user_id,
                text="🎉 Your Payment Has been Approved. Click Here To See Videoes",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
        except Exception as e:
            print(f"Failed to notify user: {e}")

    elif data.startswith("reject_"):
        target_user_id = int(data.split("_")[1])
        set_user_access(target_user_id, False)
        
        await query.edit_message_caption(caption=f"{query.message.caption}\n\n❌ <b>Status: Rejected</b>", parse_mode='HTML')
        
        try:
            await context.bot.send_message(
                chat_id=target_user_id,
                text="❌ Your Payment ScreenShot Hasbeen Rejected Please Send Right ScreenShot"
            )
        except Exception as e:
            print(f"Failed to notify user: {e}")

# --- Main App Execution ---
if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(admin_action_handler, pattern="^(approve_|reject_)"))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.PHOTO & ~filters.COMMAND, handle_payment_screenshot))
    
    print("Bot is running...")
    app.run_polling()