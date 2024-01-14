import random
import discord
import json
import time
from discord.ext import commands

intents = discord.Intents(messages=True, guilds=True)
bot = commands.Bot('/', intents=intents)

config = {
    'token': 'сюды токен',
    'prefix': '/',
    'job': "Нафармить 13.5 стаков обсидиана. Для передачи обсидиана обратиться к главе или хелперу.",
    'admins': [636626607557312532, 529699280060022814, 555036117011791912],
    'channels': ''
}

ping = False


@bot.event
async def on_message(ctx, *arg):
    print(ctx.author.name + ": " + ctx.content)


@bot.command()
async def job(ctx, *arg):
    await ctx.reply(config['job'])


@bot.command()
async def change_job(ctx, *args):
    if ctx.author.id in config['admins']:
        if args:
            config['job'] = ' '.join(args)
            await ctx.reply("Текст задания успешно изменён! Используйте /job")
        else:
            await ctx.reply("Используйте /change_job <текст задания>")
    else:
        await ctx.reply("У вас недостаточно прав, для выполнения данной команды.")


@bot.command()
async def ahelp(ctx, *arg):
    await ctx.reply("/job - узнать задание для вступления в клан\n\n"
                    "/change_job <текст задания> - сменить задание для новичков (доступно лишь доверенным лицам)\n\n"
                    "/ping_bomb <человек, на которого идёт атака> <количество пингов> <сообщение (необязательный параметр)> - пинг атака на определённого человека (доступно лишь доверенным лицам). ВНИМАНИЕ! Может пинговать именно определённого человека!\n\n"
                    "/ping_stop - останавливает пинг атаку")


@bot.command()
async def ping_bomb(ctx, member: discord.Member = None, *args):
    if ctx.author.id in config['admins']:
        if member and args:
            global ping
            ping = True
            await ctx.reply("Начинаю пинг атаку!")
            await ctx.send("Атака через 3...")
            time.sleep(1)
            await ctx.send("Атака через 2...")
            time.sleep(1)
            await ctx.send("Атака через 1...")
            time.sleep(1)
            for i in range(int(args[0])):
                if ping:
                    await ctx.send(f"{member.mention} {' '.join(args[1:])}")
                else:
                    break
        else:
            await ctx.reply("Используйте /ping_bomb <человек, на которого идёт атака> <количество пингов> <сообщение (необязательный параметр)>")
    else:
        await ctx.reply("У вас недостаточно прав, для выполнения данной команды.")


@bot.command()
async def ping_stop(ctx, *arg):
    if ctx.author.id in config['admins']:
        global ping
        ping = False
        await ctx.reply("Пинг атака завершена!")
    else:
        await ctx.reply("У вас недостаточно прав, для выполнения данной команды.")

bot.run(config['token'])
