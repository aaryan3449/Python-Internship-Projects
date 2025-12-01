
---

## 📄 README 3 – Chat Application (`3_Chat_Application/README.md`)

```markdown
# Simple Chat Application (Console Based)

This is a basic console-based chat application built using Python sockets.  
Multiple clients can connect to a single server and exchange messages in real time.

## How It Works

- `chat_server.py` runs on the host machine and listens for incoming connections.
- `chat_client.py` is used by each user to connect to the server.
- Each client enters a name, and messages are broadcast to all other connected clients.

## Files

- `chat_server.py` – Server script that handles multiple clients.
- `chat_client.py` – Client script to send and receive messages.

## Technologies Used

- Python 3
- `socket` module
- `threading` module

## How to Run

### 1. Start the Server

1. Open a terminal.
2. Go to the project folder:

   ```bash
   cd 3_Chat_Application
