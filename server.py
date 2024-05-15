import asyncio

class SMTPServer:
    def __init__(self, host='127.0.0.1', port=25):
        self.host = host
        self.port = port

    async def handle_client(self, reader, writer):
        client_address = writer.get_extra_info('peername')
        print(f"Connection from {client_address}")

        writer.write(b'220 Welcome to Python SMTP server\r\n')
        await writer.drain()

        while True:
            data = await reader.readline()
            if not data:
                break
            command = data.decode().strip()
            print(f"Received: {command}")

            if command.upper() == 'QUIT':
                writer.write(b'221 Bye\r\n')
                await writer.drain()
                break
            elif command.upper().startswith('HELO'):
                writer.write(b'250 Hello\r\n')
                await writer.drain()
            elif command.upper().startswith('MAIL FROM:'):
                writer.write(b'250 OK\r\n')
                await writer.drain()
            elif command.upper().startswith('RCPT TO:'):
                writer.write(b'250 OK\r\n')
                await writer.drain()
            elif command.upper() == 'DATA':
                writer.write(b'354 Start mail input; end with <CRLF>.<CRLF>\r\n')
                await writer.drain()
                while True:
                    line = await reader.readline()
                    if line.strip() == b'.':
                        break
                writer.write(b'250 OK\r\n')
                await writer.drain()
            else:
                writer.write(b'500 Error: command not recognized\r\n')
                await writer.drain()

        print(f"Connection with {client_address} closed")
        writer.close()

    async def start(self):
        server = await asyncio.start_server(
            self.handle_client, self.host, self.port
        )
        print(f"SMTP server started on {self.host}:{self.port}")
        async with server:
            await server.serve_forever()

if __name__ == "__main__":
    server = SMTPServer()
    asyncio.run(server.start())
