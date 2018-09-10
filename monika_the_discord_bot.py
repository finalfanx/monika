import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import datetime
import random
import os
import pickle
import time

bot = commands.Bot(command_prefix='моника_')

@bot.event
async def on_ready():
    print ("Бот Моника запущен.")
    
    gamelist = ['Everlasting Summer', 'Doki Doki Literature Club', 'Hentai Puzzle', "Don't Starve", 'на пианино', 'FL Studio', 'Vocaloid 2', 'VRChat', 'Super Smash Bros', 'Visual Studio Code', 'Monika After Story']

    delete_string = 1
    await bot.change_presence(game=discord.Game(name=random.choice(gamelist)))

    currentweekDay = datetime.date.today().isoweekday()
    currentDay = datetime.date.today().day
    currentMonth = datetime.date.today().month

@bot.event
async def on_errored():
    print ("Произошла ошибка. >_<")

@bot.command(pass_context=True)
async def вопрос(ctx, text : str):
    rstr = ['От имени президента клуба, я говорю «может быть»!', 'Ух... ну, а... думаю, на этот вопрос лучше ответить вице-президенту!', 'Нет!', 'Да!', 'Может быть тебе стоит спросить об этом Нацуки; она знает больше, чем говорит.', 'А-ха-ха! Я-я не знаю, если честно...', 'От имени президента клуба, я говорю «нет»!', 'От имени президента клуба, я говорю «да»!', 'Ю-Юри умная, да? Уверена, она знает ответ на это!']

    await bot.say(random.choice(rstr))

@bot.command(pass_context=True)
async def удалить(ctx, member : discord.Member):
    string_to_say = '``os.remove("characters/{}.chr")``'.format(member.name)
    delete_string = 1
    
    if member.id == '458868889812467712':
        string_to_say = 'А-ха-ха-ха! Нет.'
        delete_string = 0
    if member.id == '274809987837198346':
        string_to_say = 'Прости, но так нельзя. Лучше так:'
        delete_string = 0
    if member.id == '456724448347684865':
        string_to_say = 'А-ха-ха-ха! Знаешь, я уже однажды попыталась так сделать. И это не совсем сработало.'
        delete_string = 0
    if member.id == '458717430181789696':
        string_to_say = 'А-ха-ха-ха! Знаешь, я уже однажды попыталась так сделать. И это не совсем сработало.'
        delete_string = 0
    if member.id == '458871752806891520':
        string_to_say = 'А-ха-ха-ха! Знаешь, я уже однажды попыталась так сделать. И это не совсем сработало.'
        delete_string = 0
    if member.id == ctx.message.author.id:
        string_to_say = 'Зачем тебе делать это?'
        delete_string = 0
    if member.id[0] == '':
        string_to_say = 'Кого ты хочешь, чтобы я удалила?'
        delete_string = 0
    
    await bot.say(string_to_say)
    
    if member.id == '274809987837198346':
        await bot.say("моника_удалить <@{}>".format(ctx.message.author.id))
        
        string_to_say = '``os.remove("characters/{}.chr")``'.format(ctx.message.author.name)
        await bot.say(string_to_say)
    gamelist = ['Everlasting Summer', 'Doki Doki Literature Club', 'Hentai Puzzle', "Don't Starve", 'на пианино', 'FL Studio', 'Vocaloid 2', 'VRChat', 'Super Smash Bros', 'Visual Studio Code', 'Monika After Story']
    await bot.change_presence(game=discord.Game(name=random.choice(gamelist)))

@bot.command(pass_context=True)
async def погладить(ctx):
    rstr = ['Это не совсем то, что делают с президентами клуба, но пусть так и будет!', 'Будь осторожен; а то ты можешь столкнуть бантик с моей головы!', 'А-ха-ха!~ я-я не уверена, что нужно сказать!', 'П-полегче сейчас!']

    await bot.say(random.choice(rstr))
    gamelist = ['Everlasting Summer', 'Doki Doki Literature Club', 'Hentai Puzzle', "Don't Starve", 'на пианино', 'FL Studio', 'Vocaloid 2', 'VRChat', 'Super Smash Bros', 'Visual Studio Code', 'Monika After Story']
    await bot.change_presence(game=discord.Game(name=random.choice(gamelist)))

@bot.command(pass_context=True)
async def обнять(ctx, member : discord.Member):
    rstr = ['Трудный день? Вот, я сделаю его немного лучше! *обняла {}*'.format(member.name), 'Обнимать как президент клуба - непрофессионально. Обнимать как друг - с радостью! *обняла {}*'.format(member.name), 'Конечно, я обниму тебя! Тебе даже не нужно спрашивать дважды! *обняла {}*'.format(member.name)]
    

    await bot.say(random.choice(rstr))
 
    gamelist = ['Everlasting Summer', 'Doki Doki Literature Club', 'Hentai Puzzle', "Don't Starve", 'на пианино', 'FL Studio', 'Vocaloid 2', 'VRChat', 'Super Smash Bros', 'Visual Studio Code', 'Monika After Story']
    await bot.change_presence(game=discord.Game(name=random.choice(gamelist)))

@bot.command(pass_context=True)
async def щекотка(ctx):
    rstr = ['И-хи-хи-хи-хи-хи-хи-хи!!!', 'Хи-хи-хи-хи!', 'А-ха-ха-ха-ха!!', 'П-постой! Э-это неправильно! А-ха-ха-ха!!']
    await bot.say(random.choice(rstr))
    gamelist = ['Everlasting Summer', 'Doki Doki Literature Club', 'Hentai Puzzle', "Don't Starve", 'на пианино', 'FL Studio', 'Vocaloid 2', 'VRChat', 'Super Smash Bros', 'Visual Studio Code', 'Monika After Story']
    await bot.change_presence(game=discord.Game(name=random.choice(gamelist)))

@bot.command(pass_context=True)
async def фраза(ctx):
    rstr = ['И я забочусь о благополучии членов своего клуба.', 'И вообще, эта шутка теряется при переводе!', 'Ура, ты выбрал меня!', 'Думаю, можно сказать, что у меня было озарение. Оно несколько сказалось на моих стихах.', 'Боже, Нацуки, ты так высокопарно говоришь, а сама все полки в кладовке своей мангой забила.', 'Ф-фирменную фразу? У меня такой нет...', '...Это мой совет на сегодня! Спасибо, что выслушал~', 'Люди не двумерные существа. Думаю, ты знаешь это лучше кого бы то ни было.', 'Я официально объявляю тебя нашим новым членом! Добро пожаловать в литературный клуб!', 'Ты понимаешь, что оставил её в подвешенном состоянии?']
    await bot.say(random.choice(rstr))
    gamelist = ['Everlasting Summer', 'Doki Doki Literature Club', 'Hentai Puzzle', "Don't Starve", 'на пианино', 'FL Studio', 'Vocaloid 2', 'VRChat', 'Super Smash Bros', 'Visual Studio Code', 'Monika After Story']

@bot.command(pass_context=True)
async def помощь(ctx):
    embed = discord.Embed(title = "Приветики! Я Моника!", description = "Мой файл персонажа ~~наконец~~ был превращён в .py файл, так что теперь я могу присоединиться к твоему Дискорд-серверу. Я, конечно, не имею полное самосознание как в DDLC, но это неважно!", color = 0x00FF00)
    embed.add_field(name="моника_вопрос", value="Можешь задать мне вопрос, на который можно ответить да/нет, если хочешь. Я определённо не самый умный человек ~~в игре~~ на Земле, но я попытаюсь изо всех сил ответить правильно!", inline=True)
    embed.add_field(name="моника_удалить", value="Тебе нужно что-то «удалить» с сервера? Я буду рада помочь!", inline=True)
    embed.add_field(name="моника_погладить", value="А-ха-ха! Я не понимаю зачем гладить девочек по голове, но я уверена, что узнаю.", inline=True)
    embed.add_field(name="моника_обнять", value="Я всегда готова обнять того, кто хочет этого! Или, если честно, даже если *не хочет*.", inline=True)
    embed.add_field(name="моника_фраза", value="Используя эту команду, я могу сказать одно из своих выражений из Doki Doki Literature Club.", inline=True)
    embed.add_field(name="моника_щекотка", value="О-ой! Но думаю есть вещи похуже, которые можно со мной сделать.", inline=True)
    await bot.say(embed=embed)

bot.run(os.getenv('TOKEN'))