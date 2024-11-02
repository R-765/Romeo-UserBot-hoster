from os import getenv

API_ID = int(getenv("API_ID", "13146123"))
API_HASH = getenv("API_HASH", "53e10a257baaddea9c413a0c4249e731")
BOT_TOKEN = getenv("BOT_TOKEN", "6207250772:AAG6ILTYP82ajhHJEGpiP87-OT7xbwOBgQc")
OWNER_ID = int(getenv("OWNER_ID", "5378060239"))
STRING_SESSION = getenv("STRING_SESSION", "BQEiZi4AuFRdcuUrR_eBV42Mv5h3u61GyFWOPqXIf1bEaW-AyO15pxTtYeDcW3JqJKH92uiIiTr4kRnd6_is_sdZRcUughaQQFhx-mUbbOF5RB8crrXvhWyU65GWhfQNjw9xtoyKLMWdq0dau5-bBq1-zTjTsheSrkHKKwvbobPHWMC8sZu6WQg39QQIT0E4F6LOkxjMndz2VwY2d3RNBQoFspA_uplLznDT5Jx77_UX0YHSvAeEQa3Qa_1dJZX5suQj20nnybYbc2oTNXjRZpKtuA7I5t_LahVhHvgSS5JsGGgZ7WoRQA6mc4y2ncJ8K7Mhzb26wL7DycLd9dz0zXslKLkDbQAAAAFAjq_PAA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5378060239").split()))
ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/a62b9c7d9848afde0569e.jpg")
REPO_URL = getenv("REPO_URL", "https://github.com/RRomeo-RJ/Romeo-UserBot")
BRANCH = getenv("BRANCH", "main")
