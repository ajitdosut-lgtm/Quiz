import telebot
import time
import random  # Options ko shuffle (aage-piche) karne ke liye
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "8583246985:AAGkJEtjyVPFtzSCUhIwJIDglvkB_NvYNRY"
# ⚠️ Yahan apne group ka asli username likhna (@ ke sath)
CHAT_ID = "@targetbihardarogagroupimport telebot
import time  # Do sawalon ke bich me thoda gap (rest) dene ke liye

BOT_TOKEN = "8583246985:AAGkJEtjyVPFtzSCUhIwJIDglvkB_NvYNRY"

# ⚠️ Yahan apne group ka asli username likhna (@ ke sath)
CHAT_ID = "@Aapke_Group_Ka_Username"

bot = telebot.TeleBot(BOT_TOKEN)

# --- SAARE SAWALON KI LIST ---
# Yahan aap jitne chahein utne sawal {} ke andar comma (,) lagakar jod sakte hain
quiz_list = [
    {
        "sawaal": "1857 के विद्रोह में बिहार का नेतृत्व किसने किया था?",
        "options": ["मंगल पांडे", "कुंवर सिंह", "नाना साहेब", "तात्या तोपे"],
        "sahi_index": 1,  # कुंवर सिंह (Dusra option)
    },
    {
        "sawaal": "बिहार दिवस प्रतिवर्ष कब मनाया जाता है?",
        "options": ["22 जनवरी", "22 मार्च", "22 अप्रैल", "22 अगस्त"],
        "sahi_index": 1,  # 22 मार्च (Dusra option)
    },
    {
        "sawaal": "पाटलिपुत्र नगर के संस्थापक कौन थे?",
        "options": ["उदयिन", "अशोक", "बिम्बिसार", "महापद्मनंद"],
        "sahi_index": 0,  # उदयिन (Pehla option)
    },
]


print("Bulk Quiz bhejna shuru ho raha hai...\n")

# Ek-ek karke saare sawal bhejne ke liye loop
for ek_sawaal in quiz_list:
    try:
        bot.send_poll(
            chat_id=CHAT_ID,
            question=ek_sawaal["sawaal"],
            options=ek_sawaal["options"],
            type="quiz",
            correct_option_id=ek_sawaal["sahi_index"],
            is_anonymous=True,
        )
        print(f"Sawaal bhej diya: {ek_sawaal['sawaal'][:20]}...")

        # ⚠️ Sabse Zaroori: Do sawal ke bich me 3 second ka gap
        # Agar gap nahi denge toh Telegram bot ko 'Spam' samajhkar block kar dega
        time.sleep(3)

    except Exception as e:
        print(f"Is sawal me koi galti hui: {e}")

print("\n🎉 Mubarak ho! Saare quizzes ek sath group me chale gaye hain.")"

bot = telebot.TeleBot(BOT_TOKEN)

# --- SAARE SAWALON KA DATA ---
quiz_list = [
    {
        "tag": "इतिहास (History)",
        "sawaal": "1857 के विद्रोह में बिहार का नेतृत्व किसने किया था?",
        "options": ["मंगल पांडे", "कुंवर सिंह", "नाना साहेब", "तात्या तोपे"],
        "sahi_jawab": "कुंवर सिंह", # Yahan index ke bajaye seedhe naam likhein
        "explanation": "💡 कुंवर सिंह जगदीशपुर के जमींदार थे, जिन्होंने 80 वर्ष की उम्र में विद्रोह का नेतृत्व किया था।"
    },
    {
        "tag": "इतिहास (History)",
        "sawaal": "बिहार दिवस प्रतिवर्ष कब मनाया जाता है?",
        "options": ["22 जनवरी", "22 मार्च", "22 अप्रैल", "22 अगस्त"],
        "sahi_jawab": "22 मार्च",
        "explanation": "💡 22 मार्च 1912 को बिहार, बंगाल से अलग होकर एक नया राज्य बना था।"
    },
    {
        "tag": "भूगोल (Geography)",
        "sawaal": "बिहार का शोक किस नदी को कहा जाता है?",
        "options": ["गंगा नदी", "सोन नदी", "कोसी नदी", "गंडक नदी"],
        "sahi_jawab": "कोसी नदी",
        "explanation": "💡 कोसी नदी उत्तर बिहार में भीषण बाढ़ लाने ke karan 'बिहार का शोक' कहलाती है।"
    }
]

try:
    print("🚀 Ultra-Pro Test Series Shuru Ho Rahi Hai...")

    # --- 1. INTRO BANNER WITH BUTTONS ---
    intro_text = (
        "🔥 *BIHAR DAROGA PREMIUM TEST SERIES* 🔥\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "📝 *Total Questions:* 3\n"
        "⏱️ *Time per Question:* 30 Seconds\n"
        "🎯 *Target:* 3/3 Correct Answers\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "👇 _Behtareen taiyari ke liye niche judein!_"
    )
    
    # Inline Buttons banana
    markup_intro = InlineKeyboardMarkup()
    markup_intro.add(InlineKeyboardButton("📢 Join YouTube Channel", url="https://youtube.com"))
    markup_intro.add(InlineKeyboardButton("🔗 Share This Group", url="https://t.me/share/url?url=" + CHAT_ID))
    
    bot.send_message(CHAT_ID, intro_text, parse_mode="Markdown", reply_markup=markup_intro)
    time.sleep(3) # Intro message ke 3 second baad quiz shuru hoga

    # --- 2. QUIZ LOOP WITH TIMER & SHUFFLE ---
    for index, ek_sawaal in enumerate(quiz_list, start=1):
        
        # Pro Feature: Options ko automatic shuffle karna taaki cheating na ho
        shuffled_options = ek_sawaal["options"].copy()
        random.shuffle(shuffled_options)
        # Naya sahi index pata karna shuffling ke baad
        sahi_index_naya = shuffled_options.index(ek_sawaal["sahi_jawab"])

        # Design formatting
        formatted_question = (
            f"🏆 *LIVE TEST* | *[Q {index}/{len(quiz_list)}]*\n"
            f"📌 *विषय:* {ek_sawaal['tag']}\n"
            f"⏳ *समय सीमा:* 30 Seconds\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"❓ *{ek_sawaal['sawaal']}*"
        )

        bot.send_poll(
            chat_id=CHAT_ID,
            question=formatted_question,
            options=shuffled_options,
            type="quiz",
            correct_option_id=sahi_index_naya,
            explanation=ek_sawaal["explanation"],
            open_period=30, # ⏱️ AUTOMATIC TIMER: 30 Seconds me poll apne aap close ho jayega
            is_anonymous=True,
            parse_mode="Markdown"
        )
        print(f"✅ प्रश्न {index} Group me bhej diya gaya hai!")
        
        # Kyunki timer 30s ka hai, hum 35 second rukenge taaki agla sawal tabhi aaye jab purana close ho jaye
        time.sleep(35)

    # --- 3. OUTRO BANNER (TEST KHATAM) ---
    outro_text = (
        "🏁 *TEST COMPLETED! (टेस्ट समाप्त)* 🏁\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "Aapne aaj ka mock test poora kar liya hai. Apna score upar diye gaye questions me check karein.\n\n"
        "📢 *Agla Mega Test kal isi samay hoga!*"
    )
    bot.send_message(CHAT_ID, outro_text, parse_mode="Markdown")
    print("\n🎉🎯 SAARE ULTRA-PRO QUIZZES LIVE GROUP ME CHALE GAYE!")

except Exception as e:
    print(f"❌ Koi galti hui: {e}")
