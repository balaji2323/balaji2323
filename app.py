from flask import Flask, request, jsonify
from flask_cors import CORS
from twilio.rest import Client

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Disaster Alert System is running!"

@app.route('/send_sms', methods=['POST'])
def send_sms():
    data = request.json
    number = data.get('number')
    message = data.get('message')

    if not number or not message:
        return jsonify({'status': 'error', 'message': 'Number and message are required'}), 400

    # Replace these with your actual Twilio credentials
    account_sid = 'AC73a45fe818f03d3f250e41fe4b23c7d4'
    auth_token = '593387236b986fb40c6e74329ef68f99'
    twilio_number = '+13098619411'

    client = Client(account_sid, auth_token)

    try:
        client.messages.create(
            body=message,
            from_=twilio_number,
            to=number
        )
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
