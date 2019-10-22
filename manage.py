#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_bot.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)







if __name__ == '__main__':
    # main()
    import os

    import discord
    from dotenv import load_dotenv
    from django.conf import settings
    from bot.google import search

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chat_bot.settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(['python manage.py runserver'])

    from bot.db_connect import create_history, check_history

    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')

    client = discord.Client()


    @client.event
    async def on_ready():
        print(f'{client.user.name} has connected to Discord!')


    @client.event
    async def on_member_join(member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Hi {member.name}, welcome to my Discord server!'
        )


    @client.event
    async def on_message(message):

        if message.author == client.user:
            return

        if message.content == 'hay':
            await message.channel.send('hi')

        elif message.content[:7] == '!google':

            res = search(message.content[8:])
            create_history(message.content[8:])
            await message.channel.send('\n'.join([f'key: {item[1]} and link : {item[0]}' for item in res[:5]]))

        elif message.content[:7] == '!recent':

            res = check_history(message.content[8:])
            await message.channel.send('\n'.join([obj.key for obj in res]))


    client.run(token)