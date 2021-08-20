# parte do chatbot
from chatterbot.trainers import ListTrainer
from chatterbot import Chatbot

# Speech recognition
import speech_recognition as sr

# speech synthesis
import pyttsx3

bot= ChatBot('Bibo')

chats=['oi', 'ola', 'Como você está?', 'estou bem, obrigado']

bot.set_trainer(ListTrainer) #define o médoto de treinamento
bot.train(chats) #define a lista de conversa
