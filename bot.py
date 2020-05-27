from datetime import date

import sqlite3
from sqlite3 import Error

import discord
from discord.ext import commands

import random

client = commands.Bot(command_prefix='.')

# Comandos del bot
@client.event
async def on_ready():
    print('holaquehace bot')

@client.event
async def on_member_join(member):
    print(f'{member} se acaba de conectar')

@client.event
async def on_member_remove(member):
    print(f'{member} se ha ido')

# comandos
# nombrar funciones igual que el comando
@client.command()
async def hola(ctx):
    await ctx.send(f'hola que hace hola ')

@client.command()
async def onomastico(ctx):
    today = date.today()
    d = today.strftime("%d")
    m = today.strftime("%m")
    santo=getNombreSanto(conn,f'D{d}M{m}')
    await ctx.send(f'el santoral de hoy saluda a {santo}. Saludos a {santo} de Chile')

@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball','test'])
async def _8ball(ctx,*,question):
    responses=['clarines','más o menos','so so']
    await ctx.send(f'Tú pregunta es {question}\ny tu respuesta es {random.choice(responses)}')


# funciones base datos
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f'Conectado a sqlite3 v{sqlite3.version}')
        return conn
    except Error as e:
        print(e)
    
    return conn

def getDiaSanto(conn, nombreSanto):
    cur = conn.cursor()
    cur.execute("SELECT * FROM santos WHERE nombreSanto=?", (nombreSanto,))

    rows = cur.fetchall()

    return rows

def getNombreSanto(conn, diaSanto):
    cur = conn.cursor()
    cur.execute("SELECT santo FROM santos WHERE Codigo=?", (diaSanto,))

    rows = cur.fetchall()

    return rows[0][0]

conn=create_connection(r"./dbBot.db")
client.run('NzA5NTk0MDkxMDgzNjYxMzUy.XroLJg.VMWaz_JnfXshm8XQtTaS3OOOMDg')