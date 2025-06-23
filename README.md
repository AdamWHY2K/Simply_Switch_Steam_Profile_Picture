# Simply_Switch_Steam_Profile_Picture
Author: AdamWHY2K

## Description
A program that iterates through pictures in a folder, automatically changing your Steam profile picture every ~40 seconds. 

Iteration can be done randomly or linearly, random will choose any image in the folder as long as it isn't the current profile picture, whereas linear allows for—admittedly rather slow—animation.

https://user-images.githubusercontent.com/68286215/160739726-1f9f3a6c-69f4-4f80-a499-9cad8677f0c9.mp4


# Requirements
* Steam
* Internet connection
* The .pyw *should*—mostly—run on either Windows or Linux, assuming you have python and `requirements.txt` installed; I haven't tested it on anything but Windows though, so open an [issue](https://github.com/AdamWHY2K/Simply_Switch_Steam_Profile_Picture/issues/new) if it doesn't.
* I'd recommend just using the .exe if you're on Windows.

# Installation
* Download a [release](https://github.com/AdamWHY2K/Simply_Switch_Steam_Profile_Picture/releases).
* Extract.
* Place your profile pictures into the `images` folder.
* Open `settings.inc`.
* Find your Steam64ID [here](https://www.steamidfinder.com/) and enter it into `settings.inc`.
* Ensure you are logged into steam on your browser.
* Run `SSS_PFP.exe` or `SSS_PFP.pyw`.

# If you have any issues please first check `SSS_PFP.log`, then ensure the values in `settings.inc` are correct and that you are logged in to Steam via your browser, then open an [issue](https://github.com/AdamWHY2K/Simply_Switch_Steam_Profile_Picture/issues/new).
