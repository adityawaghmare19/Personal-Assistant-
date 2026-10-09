# Personal Assistant

A Python-based voice-controlled personal assistant designed to help with everyday tasks using voice commands, web automation, and chat history tracking. It can fetch news, open commonly used apps and websites (such as YouTube or the camera), and save conversation history for later review.

Built with Python and a MongoDB-ready persistence layer, this project is ideal for creating a smart desktop assistant with a simple UI and voice-driven interactions.

## Features

- Voice activation and command processing
- Fetch latest news headlines
- Open applications and websites like YouTube, browser tabs, and system tools
- Launch camera and multimedia tools
- Save chat conversations and command history
- Lightweight web interface for interaction
- Extendable command engine for new features

## Tech Stack

- Python
- MongoDB / database persistence
- HTML, CSS, JavaScript
- Speech recognition and text-to-speech support
- Web automation / browser integration

## Project Structure

```bash
Personal-Assistant-
├── jarvis/
│   ├── engine/
│   │   ├── command.py
│   │   ├── config.py
│   │   ├── db.py
│   │   ├── features.py
│   │   ├── helper.py
│   │   └── saveChat.py
│   ├── www/
│   │   ├── assets/
│   │   ├── css/
│   │   ├── js/
│   │   └── index.html
│   ├── main.py
│   ├── run.py
│   ├── jarvis.db
│   ├── database.txt
│   ├── location.txt
│   ├── SnakeGame.py
│   └── test.py
├── README.md
└── LICENSE
```

## Prerequisites

Before running the project, make sure you have:

- Python 3.8+
- pip
- MongoDB server running locally or in the cloud
- A microphone and speaker for voice interaction
- Required Python packages installed

## Installation

1. Clone the repository

```bash
git clone https://github.com/adityawaghmare19/Personal-Assistant-.git
cd Personal-Assistant-
```

2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

If a `requirements.txt` file is not present, install the core packages manually:

```bash
pip install pymongo pyttsx3 SpeechRecognition playsound eel pywhatkit pyaudio pyautogui
```

4. Configure MongoDB

Update your database configuration in the project settings or in the relevant database module to connect to your MongoDB instance.

Example:

```python
MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "personal_assistant"
```

## Running the Assistant

From the project root:

```bash
cd jarvis
python run.py
```

This starts the assistant and initializes the voice-based command listener.

## Main Functionalities

### 1. Voice commands
The assistant listens for wake words and user commands such as:

- "Open YouTube"
- "Open Camera"
- "Play music"
- "What is the news today?"
- "Save this chat"

### 2. News fetching
The assistant can fetch trending or latest news updates and read them aloud.

### 3. App and website launching
It supports opening applications and websites like:

- YouTube
- Browser
- Camera
- System apps

### 4. Chat history storage
User conversations and assistant responses are saved to the database so that previous interactions can be reviewed later.

## Example Commands

```text
Open YouTube
Open camera
Tell me the latest news
Play a song
Save my chat
Who are my recent contacts?
```

## Database Design

The project can store data such as:

- user conversations
- command logs
- news history
- saved preferences
- app shortcuts and custom actions

Example collections could include:

- users
- chat_history
- system_commands
- web_commands
- preferences

## Future Improvements

- Add more natural language understanding
- Integrate weather and reminders
- Support multiple users with profiles
- Add secure login and user authentication
- Improve UI/UX for the web dashboard
- Add support for voice-based control of smart devices

## Contributing

Contributions are welcome. If you want to improve the assistant:

1. Fork the project
2. Create your feature branch
3. Commit your changes
4. Open a pull request

## License

This project is open source and available under the MIT License.

## Author

Created by Aditya Waghmare

## Acknowledgements

- Python community
- MongoDB
- Open-source speech and automation libraries
- Contributors and supporters of this project

---

If you want, I can also generate:

- a more minimal README
- a professional GitHub-style README with screenshots
- a README tailored specifically to the current codebase in this repository
- a version with badges and a demo section
