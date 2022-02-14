# -*- coding: utf-8 -*-
# You need to use Python 3.7.9
# =============================================================================
# Created By (this is my github)  : https://github.com/thegoldencheesecake
# Created Date: Thursday February 18 20:17:00 GST 2022
# =============================================================================

# =============================================================================
# Packages
# pip install chatterbot chatterbot-corpus colorama art
# =============================================================================

"""
# Initializing the ChatBot using the chatterbot library
"""

# Imports the chatbot class from the chatterbot library
from chatterbot import ChatBot

# Makes a variable to store the name of the bot
name = "bot"
# Initializes the chatbot class and gives it a few arguments
bot = ChatBot(
    name,
    # Filters are an efficient way to create queries that can be passed to ChatterBot’s storage adapters. Filters
    # will reduce the number of statements that a chatbot has to process when it is selecting a response.
    filters=[
        "filters.get_recent_repeated_responses"
    ],
    # Allows the chatbot to utilize this storage adapter this allows ChatterBot to connect to different storage
    # technologies
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    # Allows the chatbot to utilize some logic adapters which determine the logic for how ChatterBot selects a
    # response to a given input statement
    logic_adapter=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter",
        "chatterbot.logic.BestMatch",
        {
            # Adds a few parameters for the BestMatch logic adapter
            "import-path": "chatterbot.logic.BestMatch",
            # Sets the default response as this
            "default_response": "I am sorry, I don't understand you.",
            # Sets the maximum similarity threshold to 0.90 to print to the screen
            "maximum_similarity_threshold": 0.90,
        },
    ],
    database_uri="sqlite:///database.sqlite3",
)

# Informs that the chatbot has been created and displays the name
print(f"Initialized chatbot with name {name}")

"""
# Making the trainers and training the bot using ready made data
"""

import re

# Imports the built-in chatterbot trainers
from chatterbot.trainers import (ChatterBotCorpusTrainer, ListTrainer,
                                 UbuntuCorpusTrainer)

# Makes a variable to initialize the list trainer class
trainer = ListTrainer(bot)
# Makes a variable to initialize the corpus trainer
trainerCorpus = ChatterBotCorpusTrainer(bot)
# Makes variable to initialize the ubuntu corpus trainer (2 gigabytes and 26 million conversations)
trainerUbuntuCorpus = UbuntuCorpusTrainer(bot)

# f = open("human_conversations.txt", "r")
# training_data = []

# for line in f:
# m = re.search('(Q:|A:)?(.+)', line)
# if m:
# training_data.append(m.groups()[1])

# Calls the train function from the respective classes that were initialized earlier in the form of variables

# trainer.train(training_data)
# trainerCorpus.train("chatterbot.corpus.english")
trainerUbuntuCorpus.train()

"""
# The Main Program
"""

import os, time

import art
from colorama import Fore, Style, init

# Initializes colorama
init()

# Prints the ascii art at the start of the program
print(art.text2art("The ChatBot!", font="starwars"))

# Asks the user for their name and stores in the uname variable
uname = input("What is your name? ")
# Asks the user for the name of their bot and stores it in the bname variable
bname = input("What would you like to name the bot? ")
print("")

# Starts the main loop
while True:
    # Checks whether the user's terminal supports color formatting
    if os.system("color") == 1:
        query = input(f"{Fore.LIGHTBLUE_EX}{uname}>{Style.RESET_ALL} ").lower()
    # If it doesn't then it just prints without the color formatting
    else:
        query = input(f"{uname}> ").lower()

    # Checks whether the user query is exit or quit on which it exits the program
    if query.lower() == "exit" or query.lower() == "quit":
        print("Exiting...\n")
        break
    # Checks whether the query is help on which it shows the available commands and explains their role
    elif query.lower() == "help":
        with open("commands.txt", "r") as f:
            fcontents = f.read()
            print(fcontents)
            f.close()
    elif query.lower() == "time":
        print(time.ctime(time.time()))

    # Calls the get_response function from the bot made earlier and gets the response to the query
    answer = bot.get_response(query)
    # Checks whether the user's terminal supports color formatting
    if os.system("color") == 1:
        print(f"{Fore.LIGHTYELLOW_EX}{bname}>{Style.RESET_ALL}", answer)
    # If it doesn't then it just prints without the color formatting
    else:
        print(f"{bname}>", answer)
