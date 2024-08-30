# Comics publisher

The project is intended for the publication
of comics in the telegram channel

### How to install

Clone the repository

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```commandline
pip install -r requirements.txt
```

### Create a telegram bot

Save the token received when creating the bot. Add your bot to your telegram channel.
Give him administrator rights.

### Environment variables

Save environment variables to a `.env` file

```commandline
TG_TOKEN=your telegram token
TG_CHAT_ID=chat id of your channel
```

### Run

Run the script with the command
```python
python main.py
```

### Project Goals

The code is written for educational purposes on online-course
for web-developers [dvmn.org](https://dvmn.org/).