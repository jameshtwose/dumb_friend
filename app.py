from flask import Flask, render_template, request
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = Flask(__name__)

model_name = "microsoft/DialoGPT-small"
# model_name = "microsoft/deberta-v3-xsmall"
# model_name = "facebook/blenderbot_small-90M"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    
    # Let's chat for 10 lines
    for step in range(10):
        # encode the new user input, add the eos_token and return a tensor in Pytorch
        new_user_input_ids = tokenizer.encode(userText + tokenizer.eos_token, return_tensors='pt')

        # append the new user input tokens to the chat history
        bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

        # generated a response while limiting the total chat history to 1000 tokens, 
        chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
        
        return str(tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True))


if __name__ == "__main__":
    app.run(debug=False, port=5000, host="0.0.0.0")


