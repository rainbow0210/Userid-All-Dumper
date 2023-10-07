# Discord bot import
import discord
from discord import app_commands
from discord import ui
import os
from dotenv import load_dotenv
import glob
import csv
import pprint


# Discordボットのプログラム部分
load_dotenv()

intents = discord.Intents.default()#適当に。
intents.typing = False  # typingを受け取らないように
intents.members = True  # membersを受け取る
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


# bot start
@client.event
async def on_ready():
    print("接続しました！")
    #await client.change_presence(activity=discord.Game(name="All user id data view"))
    await tree.sync()#スラッシュコマンドを同期
    print("グローバルコマンド同期完了！")

# /member_dump
@tree.command(name="member_dump",description="Members name and id write file dump.")
async def id_member(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=True)

    file_path = "./" + str(interaction.guild.id) + ".csv"
    #output = ""
    member_info = interaction.guild.members

    print(len(member_info))
    #print(user.id)
    #print(len(client.guilds))

    with open(file_path, 'w', newline='', encoding='cp932') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "id"])
        for i in range(0, len(member_info)):
            #user = member_info[i]

            #print(type(user))

            writer.writerow([str(member_info[i]), member_info[i].id])
            #output = output + str(member_info[i]) + "," + str(user.id) + "\n"
            #print(i)

    #print(output)
    await interaction.followup.send(file=discord.File(file_path))
    os.remove(file_path)

# /user_dump
@tree.command(name="user_dump",description="Users name and id write file dump.")
async def id_user(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=True)

    file_path = "./" + str(interaction.guild.id) + ".csv"
    #output = ""
    member_info = interaction.guild.members

    print(len(member_info))
    #print(user.id)
    #print(len(client.guilds))

    with open(file_path, 'w', newline='', encoding='cp932') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "id"])

        for i in range(0, len(member_info)):
            if not member_info[i].bot:
                user = member_info[i]

                #print(type(user))

                writer.writerow([str(member_info[i]), member_info[i].id])
                #output = output + str(member_info[i]) + "," + str(user.id) + "\n"
                #print(i)

    #print(output)
    await interaction.followup.send(file=discord.File(file_path))
    os.remove(file_path)

client.run(os.environ['token'])