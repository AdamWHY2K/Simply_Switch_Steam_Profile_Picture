import requests
import re
from os import listdir, mkdir
from os.path import exists
from time import sleep
import logging
from tkinter import messagebox

class App:

    def __init__(self):
        logging.basicConfig(
            filename='SSS_PFP.log',
            encoding='utf-8',
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p',
            filemode = 'w')
        logging.info("STARTING SSS_PFP")
        self.cookie = ""
        self.steam_64_id = ""
        self.session_id = ""

    def get_cookie(self) -> str:
        return self.cookie

    def get_steam_64_id(self) -> str:
        return self.steam_64_id

    def get_session_id(self) -> str:
        return self.session_id

    def images_in_folder(self) -> bool:
        for i in listdir("images"):
            if i.endswith(("jpg", "jpeg", "png")):
                return True

    def check_file_space(self):
        logging.info("Checking file space")
        if not exists("settings.inc"):
            logging.error("settings.inc not found!\nExiting.")
            messagebox.showerror("SSS_PFP Error:", "settings.inc not found!")
            raise SystemExit
        elif not exists("images\\"):
            mkdir("images")
            logging.error("No files found in images folder!\nExiting.")
            messagebox.showerror("SSS_PFP Error:", "No files found in images folder!")
            raise SystemExit
        elif not self.images_in_folder():
            logging.error("No images found in images folder: .png, .jpg, and .jpeg allowed.\nExiting.")
            messagebox.showerror("SSS_PFP Error:", "No images found in images folder: .png, .jpg, and .jpeg allowed.")
            raise SystemExit

    def read_settings(self):
        logging.info("Reading settings.inc")
        with open("settings.inc", "r") as f:
            logging.info("File opened successfully")
            for i in f.readlines():
                current_line = i
                if current_line.startswith("//"):
                    pass
                    #Skip lines that are comments
                elif current_line.startswith("Cookie"):
                    self.cookie = re.split("Cookie=", current_line)[1].strip()
                    #Split the string so that the actual data is seperated, strip any whitespace the user may have added
                elif current_line.startswith("Steam64ID"):
                    self.steam_64_id = re.split("Steam64ID=", current_line)[1].strip()
                elif current_line.startswith("SessionID"):
                    self.session_id = re.split("SessionID=", current_line)[1].strip()

    def send_post(self):
        url = "https://steamcommunity.com/actions/FileUploader"
        cookies = {
            "steamLoginSecure": self.get_cookie(),
            "sessionid": self.get_session_id()
        }
        data = {
            "MAX_FILE_SIZE": "1048576",
            "type": "player_avatar_image",
            "sId": self.get_steam_64_id(),
            "sessionid": self.get_session_id(),
            "doSub": "1"
        }
        while True:
            logging.info("Start of main loop")
            for i in listdir("images"):
                if i.endswith(("jpg", "jpeg", "png")):
                    logging.debug("Changing profile picture to " + i)
                    try:
                        with open("images\\" + i, "rb") as picture:
                            try:
                                r = requests.post(
                                    url=url,
                                    params={"type": "player_avatar_image","sId": self.get_steam_64_id()},
                                    files={"avatar": picture},
                                    data=data,
                                    cookies=cookies)
                                if "Failed to set avatar. Please try again." in r.text:
                                    sleep(5)
                                    logging.warning("Failed to set avatar")
                                    r = requests.post(
                                        url=url,
                                        params={"type": "player_avatar_image","sId": self.get_steam_64_id()},
                                        files={"avatar": picture},
                                        data=data,
                                        cookies=cookies)
                                elif "There was an error processing the image. Please ensure that it is no larger than 3072x3072 pixels" in r.text:
                                    logging.error("File " + i + " is too large")
                                elif "The server timed out while waiting for the browser's request." in r.text:
                                    logging.error("Server timeout")
                                elif "#Error_BadOrMissingSteamID" in r.text:
                                    logging.error("Incorrect information in settings.inc")
                                    messagebox.showerror("SSS_PFP Error:", "Incorrect information in settings.inc!")
                                    raise SystemExit
                            except SystemExit:
                                raise SystemExit
                            except:
                                logging.error("Failed to establish connection")
                            logging.info("Sleeping")
                            sleep(35)
                    except FileNotFoundError:
                        logging.error("File: " + i + " not found")


if __name__ == "__main__":
    myApp = App()
    myApp.check_file_space()
    myApp.read_settings()
    myApp.send_post()