import smtpd
import asyncore
import requests

class CustomSMTPServer(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data):
        print(f"Receiving message from: {mailfrom}")
        print(f"Recipients: {rcpttos}")
        print("Message data:")
        print(data)

        # Make a POST request to the API endpoint to store the received email
        # api_endpoint = "https://bengalinstiute.online/receive_mail/"
        # payload = {
        #     "sender": mailfrom,
        #     "recipients": rcpttos,
        #     "message": data
        # }

        # try:
        #     response = requests.post(api_endpoint, json=payload)
        #     if response.status_code == 200:
        #         print("Email stored successfully")
        #     else:
        #         print("Failed to store email. Status code:", response.status_code)
        # except Exception as e:
        #     print("Error storing email:", e)

# Start the custom SMTP server
server = CustomSMTPServer(('0.0.0.0', 25), None)
print("SMTP server started")

# Run the asyncore event loop
asyncore.loop()
