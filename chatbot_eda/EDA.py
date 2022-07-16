#%%
import chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
# %%
# Create a chatbot instance and name it
chatbot = ChatBot('dumb friend', 
                #   logic_adapters=[
        # {
        #     "import_path": "chatterbot.logic.BestMatch",
        #     "statement_comparison_function": chatterbot.comparisons.LevenshteinDistance,
        #     "response_selection_method": chatterbot.response_selection.get_first_response
        # }]
                  )

#%%
# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")
#%%
# Get a response to an input statement
chatbot.get_response("Hello, how are you today?").text
# %%
