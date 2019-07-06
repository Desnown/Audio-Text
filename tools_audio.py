#! -*- coding: utf-8 -*-

'''
Módulo responsável por reconhecimento de fala e logo após,
a tradução tradução para texto
'''

from os import sep
import speech_recognition as sr

def speek():
    r = sr.Recognizer()
    with sr.Microphone() as s:
        r.adjust_for_ambient_noise(s)
        while True:
            audio = r.listen(s)

            speech = r.recognize_google(audio, language='pt')
            print("Você disse: ", speech)


# speek()
                

def hoje():
    '''Mostrar a data no momento da gravação.
    '''

    from time import localtime, time

    ano, mes, dia, hora, minu, seg, weekday, jday, dst =  localtime(time())
    return f'{hora}:{minu}:{seg} -- {dia}/{mes}/{ano}'


# def save_info(path, file, content):
#     '''Salva as informações em um determinado arquivo.
#     '''

#     with open(path+sep+'data.json', 'r') as data:
#         pass


def read_info(path='/home/desnown/Desktop/Projetos/Audio-Text'):
    '''Lê os dados do arquivo json.
    '''

    with open(path+sep+'data.txt', 'r') as data:
        return data.readlines() 