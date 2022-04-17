"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID", None) or "19217751"
        self.API_HASH: str = os.environ.get("API_HASH", None) or "65031483c1e0a9d18b1f3f54bb4114d8"
        self.SESSION: str = os.environ.get("PYROGRAM_SESSION", None) or "1BVtsOIkBu2_VbuixqHTgpAXL3qyCD_MubrklHaLAcn1wpGD0F4bdRHj6n7ZakC5ri5bWeUZLvYE1P-xmvNTOYUoOyM8LFgKeLYJ5fqOfbcTsW1esS_rv_Yh3hTLBUOkozsFbLS3Z0MJgxZuCs72tzJcAUUNnGU50jw7hUSgVMRa9Nfkcpgq-3yxBEOp2D9wvoEgl7lu3hRkev_aHm5fgeV4WZxOPGCAdPFLHxXw8_jmfG8CwRXKdr72RV_o5EXFVnqoKhMaUHZOK5fYQgxqGzudxFcJyOnfC5aVmEIwoX8CTXqDDnYzsyKxp8yYHYEL4ZXo0BSxZZkDYhyE3SU9oGik0qQ1fCd0="
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", "5238676811").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("Error: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.CUSTOM_QUALITY: str = os.environ.get("CUSTOM_QUALITY", "high").lower()


config = Config()
