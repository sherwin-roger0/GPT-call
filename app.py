from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

account_sid = 'AC800aca2064e968ee465ec1563691636f'
auth_token = 'b8130ba09974aeba4c1ad72ef29bd7c1'
client = Client(account_sid, auth_token)

def generate_twiml():
    response = VoiceResponse()
    response.say("Hello! This is your phone call bot speaking.")
    response.say("How can I assist you today?")
    # Add more TwiML instructions as needed
    return str(response)

def make_phone_call():
    call = client.calls.create(
        url="https://5dc2-27-5-162-233.ngrok-free.app/bot",
        to='+919962779708',
        from_='+12292673002'
    )
    print("Call SID:", call.sid)

if __name__ == '__main__':
    make_phone_call()



