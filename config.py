import re
import os
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "10284859"))
API_HASH = getenv("API_HASH", "b0ad58eb8b845ba0003e0d9ce5fc2196")
# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6009759960:AAGPgxmfzfpTfUDGT3POlpraTnZiqtxr0GE")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://monivps5:monivps5@cluster0.kmbq8we.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 16000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002066328009"))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002066328009"))

# Get this value from  on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID","6900132473"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "newcute")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "HRKU-fc1b7aea-b37a-4015-9877-8c3967ee97bc")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/THE-VIP-BOY-OP/VIP-MUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TeamHyperNetworks")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Team_Hypers_Networks")

# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))

# MaximuM limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "2500"))
# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = False

#Auto Gcast/Broadcast Handler (True = broadcast on , False = broadcast off During Hosting, Dont Do anything here.)
AUTO_GCAST = os.getenv("AUTO_GCAST","True")

#Auto Broadcast Message That You Want Use In Auto Broadcast In All Groups.
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", None)

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "409e31d3ddd64af08cfcc3b0f064fcbe")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 2500))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 904857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 973741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes

# Time after which bot will suggest random chats about bot commands.
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "3")
)  # Remember to give value in Seconds

# Set it True if you want to bot to suggest about bot commands to random chats of your bots.
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "True")
# Cleanmode time after which bot will delete its old messages from chats
CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5")
)  # Remember to give value in Seconds

# Get your pyrogram v2 session from @VIP_STRING_ROBOT on Telegram
STRING1 = getenv("STRING_SESSION", "BQE9p8oAHK2EhvZYJF_Nq8-Cj0PlqY6vs_REMoHtxEVP7Fuotd-JdlPs_4CQgxYEEQZ4hztyzbqKe6enTVtKuWAGqZyvwhrGKQrnzg4B6eCZT4XVQcJin1xIdAShEQsSCniPljZiFf0D5CyeRR2GkOymHNX5iK-6WBHhtA2zIemxlQrdvX1lKbZSGG8AlaIkRlalYOVtBpF76J74FpsRhwfRA7N8m5yzyK_12w8EJIL5QLbkgt-rhjBa9_CU-g8LG69hhrQ2iwenh4RZmn1-SLW6VtsMwh8wV-FYSq9x_lqYnMMaeJRte_fXoHHH6MY_GdvF8J7AUEeKihRJDlhDXHkWs8MqwQAAAAGEyHmmAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


#    __      _______ _____    ___  __ _    _  _____ _____ _____   _____   ____ _______ 
#    \ \    / /_   _|  __ \   |  \/  | |  | |/ ____|_   _/ ____|  |  _ \ / __ \__   __|
#     \ \  / /  | | | |__) |  | \  / | |  | | (___   | || |       | |_) | |  | | | |   
#      \ \/ /   | | |  ___/   | |\/| | |  | |\___ \  | || |       |  _ <| |  | | | |   
#       \  /   _| |_| |       | |  | | |__| |____) |_| || |____   | |_) | |__| | | |   
#        \/   |_____|_|       |_|  |_|\____/|_____/|_____\_____|  |____/ \____/  |_|   




BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/01626a4a06b561efdd8dc.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/01626a4a06b561efdd8dc.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/01626a4a06b561efdd8dc.jpg"
STATS_IMG_URL = "https://telegra.ph/file/01626a4a06b561efdd8dc.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/01626a4a06b561efdd8dc.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/01626a4a06b561efdd8dc.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/01626a4a06b561efdd8dc.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/01626a4a06b561efdd8dc.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/01626a4a06b561efdd8dc.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/01626a4a06b561efdd8dc.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/01626a4a06b561efdd8dc.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/01626a4a06b561efdd8dc.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
