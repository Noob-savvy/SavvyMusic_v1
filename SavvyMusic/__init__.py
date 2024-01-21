from SavvyMusic.core.bot import Savvy
from SavvyMusic.core.dir import dirr
from SavvyMusic.core.git import git
from SavvyMusic.core.userbot import Userbot
from SavvyMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Savvy()
getme = await app.get_me()
    BOT_ID = getme.id

userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
