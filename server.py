import asyncio
from aiosmtpd.controller import Controller

class MySMTPServer:
    async def handle_DATA(self, server, session, envelope):
        message_data = envelope.content.decode('utf-8')
        sender = envelope.mail_from
        recipients = envelope.rcpt_tos
        print(f"Received email from {sender} to {recipients} with content:")
        print(message_data)

        # Here, you can further process the received email, save it to a database, etc.
        # For demonstration purposes, we're just printing the email content.

        return '250 OK'

async def main():
    controller = Controller(MySMTPServer(), hostname='localhost', port=1025)
    controller.start()

    # Keep the server running
    while True:
        await asyncio.sleep(3600)  # Sleep for 1 hour to keep the event loop running

# Run the main function to start the SMTP server
asyncio.run(main())
