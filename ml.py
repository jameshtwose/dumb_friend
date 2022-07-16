#%%
# Import the chatterbot module
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# from chatterbot.trainers import ChatterBotCorpusTrainer
#%%
# read in the NLP model
# Create a chatbot instance and name it
# dumbbot = ChatBot('dumb friend', trainer="chatterbot.corpus.english")
dumbbot = ChatBot('Charlie')

trainer = ListTrainer(dumbbot)

trainer.train([
    "Hi, can I help you?",
    "Sure, I'd like to book a flight to Iceland.",
    "Your flight has been booked."
])

# %%
# dumbbot.get_response("I am sad")
# %%
