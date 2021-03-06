#!/usr/bin/env python

import random
import re

from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to


@respond_to('hi', re.IGNORECASE)
def sayhi(ws):
    ws.reply('Koman ou ye?')


@respond_to('(sak*.ap*.fet)', re.IGNORECASE)
def sakapfet(ws, message):
    ws.reply('nap boule!')


@respond_to('(koman*.ou*.ye)', re.IGNORECASE)
def komanwye(ws, message):
    repons = ['nou la wi, nap genbe', 'nap byen pase', 'nou anfom...']
    ws.reply(random.choice(repons))


@listen_to('^joined\s\#', re.IGNORECASE)
def bienvenue(ws):
    saliitasyon = ['Onè pou ou! Ak respè!', 'Bienvenue!', 'Welcome!', 'Bienvenido!']
    mesaj = random.choice(saliitasyon)
    mesaj += '\n\nWe are really happy you joined!'
    mesaj += '\n* Please add "What you do" (including the technologies you know) to your profile.'
    mesaj += '\n* Include your "[city]" right after your Display name (100% voluntary).'
    mesaj += '\n* Keep in mind, we like to use threads to keep conversations in context.'
    mesaj += '\n\nNou vrèman kontan ou la!'
    mesaj += '\n* Ajoute sou pwofil ou "Kisa ki angaje tanw" (teknoloji ou bon ladanl/ou renmen).'
    mesaj += '\n* Epi apre tinon''w sou Slack mete nan ki "[site/vil]" ou ye (siw vle).'
    mesaj += '\n* Toujou fè repons nan Thread (fil konvèsasyon) yo avan tou.'
    ws.reply(mesaj)


def main():
    Bot().run()


if __name__ == "__main__":
    main()
