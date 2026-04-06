import discord
from discord.ext import commands
import os
import asyncio
import nest_asyncio

nest_asyncio.apply()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# 🌈 chữ gốc
base_text = "𝑲𝒂𝒏𝒈 𝑾 𝑩𝒐𝒏𝒈 ♡"

# 🌈 màu giả bằng emoji
colors = ["🔴","🟠","🟡","🟢","🔵","🟣"]

# 🌈 tạo hiệu ứng cầu vồng từng chữ
def rainbow_text(text):
    frames = []
    for shift in range(len(colors)):
        result = ""
        for i, char in enumerate(text):
            if char != " ":
                color = colors[(i + shift) % len(colors)]
                result += f"{color}{char}"
            else:
                result += " "
        frames.append(result)
    return frames

@bot.event
async def on_ready():
    print(f"✅ Đã đăng nhập: {bot.user}")

    await asyncio.sleep(5)  # 🔥 chống lỗi voice

    channel_id = 1490673130824401016
    channel = bot.get_channel(channel_id)

    # 🎧 vào voice (retry)
    if channel:
        while True:
            try:
                vc = await channel.connect(timeout=60, reconnect=True)

                await vc.guild.change_voice_state(
                    channel=channel,
                    self_mute=True,
                    self_deaf=True
                )

                print("🎧 Đã vào voice")
                break
            except Exception as e:
                print("❌ Lỗi voice:", e)
                await asyncio.sleep(5)

    guild = bot.guilds[0]
    me = guild.me

    # 🌈 tạo animation
    frames = rainbow_text(base_text)

    while True:
        try:
            for frame in frames:
                await me.edit(nick=frame)
                await asyncio.sleep(0.5)
        except Exception as e:
            print("❌ Lỗi đổi tên:", e)
            await asyncio.sleep(5)

# 🔥 chống crash Railway
while True:
    try:
        if not TOKEN:
            print("❌ Không có TOKEN")
        else:
            print("🚀 Bot đang chạy...")
            bot.run(TOKEN)
    except Exception as e:
        print("💥 Bot crash, restart:", e)
