from dotenv import load_dotenv
from os import getenv

import lightbulb

load_dotenv()

karmaBot = lightbulb.BotApp(getenv("TOKEN"))

if __name__ == "__main__":
    karmaBot.run()
