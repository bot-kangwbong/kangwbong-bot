import discord
from discord.ext import commands
import os
import asyncio

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# 🌈 tên fancy bạn yêu cầu
base_name = "𝑲𝒂𝒏𝒈 𝑾 𝑩𝒐𝒏𝒈 ♡"

# 🌈 hiệu ứng màu
names = [
    f"💜 {base_name}",
    f"💙 {base_name}",
    f"💚 {base_name}",
    f"💛 {base_name}",
    f"🌈 {base_name}",
    f"✨ {base_name}",
]

# ✨ hiệu ứng bay
def flying_text(text):
    frames = []
    for i in range(6):
        frames.append(" " * i + text)
    return frames

@bot.event
async def on_ready():
    print(f"✅ Đã đăng nhập: {bot.user}")

    channel_id = 1490673130824401016
    channel = bot.get_channel(channel_id)

    if channel:
        try:
            vc = await channel.connect()
            await vc.guild.change_voice_state(
                channel=channel,
                self_mute=True,
                self_deaf=True
            )
            print("🎧 Đã vào voice + tắt mic, loa")
        except Exception as e:
            print("❌ Lỗi voice:", e)

    guild = bot.guilds[0]
    me = guild.me

    fly_frames = flying_text(base_name)

    while True:
        try:
            # 🌈 đổi màu
            for name in names:
                await me.edit(nick=name)
                await asyncio.sleep(2)

            # ✨ bay bổng
            for frame in fly_frames:
                await me.edit(nick=frame)
                await asyncio.sleep(1)

        except Exception as e:
            print("❌ Lỗi đổi tên:", e)
            await asyncio.sleep(5)

if not TOKEN:
    print("❌ Không tìm thấy TOKEN")
else:
    print("🚀 Bot đang chạy...")
    bot.run(TOKEN)
