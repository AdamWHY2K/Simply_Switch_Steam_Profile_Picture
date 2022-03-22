import requests
import re
from os import listdir, mkdir
from os.path import exists
from time import sleep
import logging
from tkinter import messagebox
from random import choice

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
        self.randomized = False
        self.last_choice = ""

    def get_cookie(self) -> str:
        return self.cookie

    def get_steam_64_id(self) -> str:
        return self.steam_64_id

    def get_session_id(self) -> str:
        return self.session_id
    
    def get_randomized(self) -> bool:
        return self.randomized

    def images_in_folder(self) -> bool:
        for i in listdir("images"):
            if i.endswith(("jpg", "jpeg", "png")):
                return True

    def get_last_choice(self) -> str:
        return self.last_choice

    def set_last_choice(self, new_last_choice):
        self.last_choice = new_last_choice

    def check_file_space(self):
        logging.info("Checking file space")
        if not exists("settings.inc"):
            logging.error("\t\t\tsettings.inc not found!\nExiting.")
            messagebox.showerror("SSS_PFP Error:", "settings.inc not found!")
            raise SystemExit
        elif not exists("images\\"):
            mkdir("images")
            logging.error("\t\t\tNo files found in images folder!\nExiting.")
            messagebox.showerror("SSS_PFP Error:", "No files found in images folder!")
            raise SystemExit
        elif not self.images_in_folder():
            logging.error("\t\t\tNo images found in images folder: .png, .jpg, and .jpeg allowed.\nExiting.")
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
                    logging.debug("Found cookie")
                elif current_line.startswith("Steam64ID"):
                    self.steam_64_id = re.split("Steam64ID=", current_line)[1].strip()
                    logging.debug("Found Steam64ID")
                elif current_line.startswith("SessionID"):
                    self.session_id = re.split("SessionID=", current_line)[1].strip()
                    logging.debug("Found SessionID")
                elif current_line.startswith("Randomized"):
                    if "True" in re.split("Randomized=", current_line)[1].strip():
                        self.randomized = True
    
    def initiate_post(self):
        first_run = True
        while True:
            logging.debug("\t\t\tStart of main loop")
            if self.get_randomized():
                logging.info("Randomized")
                i = choice(listdir("images"))
                if not first_run:
                        if i == self.get_last_choice():
                            i = "duplicate" #Flagging as duplicate so the next if statement will skip it
                            logging.debug("Skipping duplicate")
                if i.endswith(("jpg", "jpeg", "png")):
                    logging.info("Changing profile picture to " + i)
                    first_run = False
                    self.send_post(i)
                else:
                    logging.debug("Skipping non-image file: " + i)
            else:
                logging.info("Linear")
                for i in listdir("images"):
                    if i.endswith(("jpg", "jpeg", "png")):
                        logging.info("Changing profile picture to " + i)
                        self.send_post(i)

    def send_post(self, chosen_file):
        self.set_last_choice(chosen_file)
        try:
            with open("images\\" + chosen_file, "rb") as picture:
                try:
                    r = requests.post(
                        "https://steamcommunity.com/actions/FileUploader", params={"type": "player_avatar_image","sId": self.get_steam_64_id()},
                        files={"avatar": picture},
                        data={"MAX_FILE_SIZE": "1048576", "type": "player_avatar_image", "sId": self.get_steam_64_id(), "sessionid": self.get_session_id(), "doSub": "1"},
                        cookies={"steamLoginSecure": self.get_cookie(), "sessionid": self.get_session_id()})
                    if "Failed to set avatar. Please try again." in r.text:
                        logging.warning("Failed to set avatar")
                        sleep(20)
                        with open("images\\" + chosen_file, "rb") as retry_picture:
                            r = requests.post(
                                "https://steamcommunity.com/actions/FileUploader", params={"type": "player_avatar_image","sId": self.get_steam_64_id()},
                                files={"avatar": retry_picture},
                                data={"MAX_FILE_SIZE": "1048576", "type": "player_avatar_image", "sId": self.get_steam_64_id(), "sessionid": self.get_session_id(), "doSub": "1"},
                                cookies={"steamLoginSecure": self.get_cookie(), "sessionid": self.get_session_id()})
                            if "There was an error processing the image." in r.text:
                                logging.debug("Retry failed.")
                            else:
                                logging.debug("Retry successful")
                    elif "There was an error processing the image. Please ensure that it is no larger than 3072x3072 pixels" in r.text:
                        logging.error("\t\t\tFile " + chosen_file + " is too large")
                    elif "The server timed out while waiting for the browser's request." in r.text:
                        logging.error("\t\t\tServer timeout")

                    elif "#Error_BadOrMissingSteamID" in r.text:
                        logging.error("\t\t\tIncorrect information in settings.inc")
                        messagebox.showerror("SSS_PFP Error:", "Incorrect information in settings.inc!")
                        raise SystemExit
                except SystemExit:
                    raise SystemExit
                except:
                    logging.error("\t\t\tFailed to establish connection")
                logging.info("Sleeping\n")
                sleep(40)
        except FileNotFoundError:
            logging.error("\t\t\tFile: " + chosen_file + " not found")

if __name__ == "__main__":
    myApp = App()
    myApp.check_file_space()
    myApp.read_settings()
    myApp.initiate_post()
