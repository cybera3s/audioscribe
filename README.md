# Audioscribe

<p>
<b>Audioscribe</b> can turn any incoming or outgoing voice messages in telegram to its text
with the help of speach recognition in python


- Utilize <b>telethon</b> for automating telegram account
- Utilize <b>speachrecognition</b> as voice to text tool
- Utilize <b>ffmpeg-python</b> as format converter

## Prerequisites
Debian/Ubuntu
```
sudo apt install ffmpeg
```

# Usage
1- Clone the repo
```
git clone https://github.com/cybera3s/audioscribe.git
```

2- change directory to project root
```
cd app
```

3- create virtual environment and activate it
```
python -m virtualenv venv
source venv/bin/activate
```

4- install required packages
```
pip install -r requirements.txt
```


5- Create a .env file in django root folder
```
touch app/.env
```

6- Fill the .env file like the provided env sample

```
# Telegram
API_ID=api id from my.telegram.org
API_HASH=api hash from my.telegram.org
SESSION_NAME=session name

# Logging
STDOUT_LOG_PATH=stdout log path
STDERR_LOG_PATH=stderr log path
LOG_LEVEL=info

# Translation
LANG=speacking language

ROOT_MEDIA=root media folder
```

7- run the project
```
python run.py
```

enjoy!
# Contact
Email: cybera.3s@gmail.com<br>
Telegram: <a href="https://t.me/ario_3s">ario3s</a>
</p>