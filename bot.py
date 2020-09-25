import discord
from discord.ext import commands
import random

jokes_words = ['300', 'зоо', 'триста', 'тристо']

# Префикс .help
client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('BOT connected')

@client.event
async def on_message(message):
    msg = message.conetent.lower()

    if msg in jokes_words:
        await message.channel.send('Отсоси у тракториста')

@client.command(pass_context = True)
async def hello (ctx):
    await ctx.send('Hello. I am a BOT for discord')

# Удаление сообщения
@client.command(pass_context = True)
# Разрешает удолять сообщения только администраторам сервера
@commands.has_permissions(administrator = True)
# Удаление сообщений из чата.
async def clear(ctx, amount = 100):
    await ctx.channel.purge(limit = amount)

# Kick пользователя с сервера
@client.command(pass_context = True)
# Разришение для алминистратора
@commands.has_permissions(administrator = True)
async def kick(ctx, member: discord.Member, *, reason = None):
    await ctx.channel.purge(limit = 1)
    await member.kick(reason = reason)
    await ctx.send(f'Kick user { member.mention }')

#Ban пользователя на сервере
@client.command(pass_context = True)
# Разришение для алминистратора
@commands.has_permissions(administrator = True)
async def ban(ctx, member: discord.Member, *, reason = None):
    await ctx.channel.purge(limit = 1)
    await member.ban(reason = reason)
    await ctx.send(f'Ban user { member.mention }')


# Меню для игры Камень Ножницы Бумага
@client.command(pass_context = True)
# Функция menu для для создание команды .menu для вывода меню
async def menu (ctx):
    # Удоление команды .menu из чата
    await ctx.channel.purge(limit=1)
    # Реализация меню
    await ctx.send('Игра. Камень Ножницы Бумага\n\n1. Камень\n2. Ножницы\n3. Бумага\n\n'
                   'Что-бы выбрать предмет нужно написать ".item " и выбранное число от "1" до "3",  ".item 1".\n')

# Игра Камень Ножницы Бумага
@client.command(pass_context = True)
# Функция item для создание команды .item
# Для игры в камень ножницы бумага с с индификатором id
async def item(ctx, id):
    # Удоление команды .item из чата
    await ctx.channel.purge(limit = 1)
    # Получаем рандомное число от 1 до 3
    AI = random.randint(1, 3)

    author = ctx.message.author

    # Периврди id из строки в целое число
    player = int(id)
    # Выводим надпись что выбрал пользователь
    if player == 1:
        await ctx.send(f'{ author.mention }. Вы, выбрали, Камень.')
    elif player == 2:
        await ctx.send(f'{ author.mention }. Вы, выбрали, Ножницы.')
    elif player == 3:
        await ctx.send(f'{ author.mention }. Вы, выбрали, Бумагу.')
    else:
        await ctx.send(f'{ author.mention }. Вы, ввели неверное значение. Введите число от 1 до 3.')


    # Логика игры

    # Логика Ничьй
    if AI == player:
        # Выыодит надпись Нечья если введённое число полизователем и рандомное число совпали
        await ctx.send(f'{ author.mention }, у вас НИЧЬЯ')
        # Выводим надпись что выбрал "комютер"
        if AI == 1:
            await ctx.send('Компьютер тоже выбрал, Камень.')
        elif AI == 2:
            await ctx.send('Компьютер тоже выбрал, Ножницы.')
        elif AI == 3:
            await ctx.send('Компьютер тоже выбрал, Бумагу.')

    # Логика Пороиграша
    elif AI == 1 and player == 2 or AI == 2 and player == 3 or AI == 3 and player == 1:
        await ctx.send(f'{ author.mention }. Вы, к сожалению ПРОИГРАЛИ.')
        # Выводим надпись что выбрал "комютер"
        if AI == 1:
            await ctx.send('Компьютер выбрал, Камень.')
        elif AI == 2:
            await ctx.send('Компьютер выбрал, Ножницы.')
        elif AI == 3:
            await ctx.send('Компьютер выбрал, Бумагу.')

    # Логика Выиграша
    elif AI == 2 and player == 1 or AI == 3 and player == 2 or AI == 1 and player ==3:
        await ctx.send(f'{ author.mention }. Вы, ВЫИГРАЛИ !!!')
        # Выводим надпись что выбрал "комютер"
        if AI == 1:
            await ctx.send('Компьютер выбрал, Камень.')
        elif AI == 2:
            await ctx.send('Компьютер выбрал, Ножницы.')
        elif AI == 3:
            await ctx.send('Компьютер выбрал, Бумагу.')

# Игра Таблица Умножения
@client.command(pass_context = True)
async def mult(ctx,):
    # Удоление команды .mult из чата
    await ctx.channel.purge(limit = 1)
    
    # Делаем переменные публичные
    global number1
    global number2
    # Получаем рандомные числа от 2 до 9
    number1 = random.randint(2,9)
    number2 = random.randint(2,9)
    
    # Переводим полученные цифры в строку
    numberOne = str(number1)
    numberTwe = str(number2)

    # Вывода ник перед командой
    author = ctx.message.author
    # Выводим полученные два числа чат
    await ctx.send(f'{ author.mention }. Сколько будит: ' + numberOne + ' * ' + numberTwe)
    
@client.command(pass_context = True)
# Создаём команда .ot для ввода ответа
async def ot(ctx, id):
    # Удоление команды .ot из чата
    await ctx.channel.purge(limit = 1)

    # Вывода ник перед командой
    author = ctx.message.author
    # Переводим переменную id из строки в целое число 
    id = int(id)
    # Проверяет введённое число с ответом
    if id == (number1 * number2):
        # Выводим надпись 'Правелно'
        await ctx.send(f'{ author.mention }. Правелно.')
    else:
        # Выводим надпись 'Не верно'
        await ctx.send(f'{ author.mention }. Не верно.')

# Коннект бота
token = open('token.txt', 'r').readline()
client.run(token)
