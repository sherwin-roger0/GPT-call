from twilio.twiml.voice_response import VoiceResponse
from flask import Flask, request, redirect
from llama_index import StorageContext, load_index_from_storage
import os
import openai



app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot_response():
    response = VoiceResponse()
    response.say("Is there any question regarding Saveetha Engineering college?")
    response.gather(input='speech', timeout=4, action='/get_result', method='POST')

    return str(response)

@app.route('/get_result', methods=['POST'])
def get_name():
    openai.api_key = ""
    os.environ["OPENAI_API_KEY"] = ""

    response = VoiceResponse()
    
    storage_context = StorageContext.from_defaults(persist_dir="myproject/AI")
    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine() 
    query = request.form['SpeechResult']
    answer = query_engine.query(query)

    response.say(answer.response)
    
    response.redirect("/bot")

    return str(response)

if __name__ == '__main__':
    app.run(debug=True)
