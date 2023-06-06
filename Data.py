from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [
        InlineKeyboardButton("🌝بدء استخراج الجلسه🌝", callback_data="generate")
    ]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="العوده الى صفحه الرئيسه ♨️", callback_data="home")],
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton(
                "سورس تيبثون", url="https://t.me/E9N99"
            )
        ],
        [
            InlineKeyboardButton("كيفية استخدام البوت ؟", callback_data="help"),
            InlineKeyboardButton("حـول  🧑‍🔧", callback_data="about"),
        ],
        [InlineKeyboardButton("المطور", url="https://t.me/nunuu")],
    ]

    START = """
اهلا وسهلا حب
هذا البوت مخصص لاستخراج الجلسات
مثل: - البايروجرام ، التيرمكس
من خلال إرسال الأيبي ايدي والأيبي هاش ورقم هاتفك والكود والتحقق بخطوتين إذا كنت مفعله
المطور : @nunuu
    """

    HELP = """
 **الأوامر المتاحة**

/about - حول البوت
/help - لمساعدتك
/start - لبدء البوت 
/repo - لإعطاء ريبو البوت
/generate - استخراج الجلسات 
/cancel - الغاء الاستخراج 
/restart - ترسيت اليوت
"""

    # About Message
    ABOUT = """
**حول البوت** 

هذا هو بوت استخراج كود تيرمكس وبايروجرام مقدم من @nunuu
قناه السورس : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/E9N99)
المطور : @nunuu
    """

    # Repo Message
    REPO = """
💥 أنا مشغل لكي أقوم باستخراج الجلسات 
   """
