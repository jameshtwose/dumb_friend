#%%
import chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import pymongo
from dotenv import load_dotenv, find_dotenv
import os
# %%
_ = load_dotenv(find_dotenv())
user=os.environ["user"]
pwd=os.environ["pwd"]
mongo_db_string=f"mongodb+srv://{user}:{pwd}@cluster0.yf82syg.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(mongo_db_string)
db = client.test
# %%
db

# %%
# Create a chatbot instance and name it
chatbot = ChatBot('dumb friend', 
                  storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
                #   logic_adapters=['chatterbot.logic.BestMatch'],
                database="cluster0",
                  database_uri=mongo_db_string)

#%%
# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")
#%%
# Get a response to an input statement
chatbot.get_response("Hello, how are you today?").text

# %%
