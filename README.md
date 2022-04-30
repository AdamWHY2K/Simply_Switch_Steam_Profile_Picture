# Simply_Switch_Steam_Profile_Picture
Author: AdamWHY2K

                                      Not expected, extremely appreciated:
* BTC: bc1qfgj4tk2a7hzyxmmrgx4mvumef5f6yfey737xsj    BCH: qzrqu0yecxka0p7sxr2g3fvpfcpg9x0awq3tf2m5ny   
                      <img src="https://user-images.githubusercontent.com/68286215/130465610-63a93f21-4c79-4de4-a1ee-2aeb6ed17a9a.png">                                                                    <img src="https://user-images.githubusercontent.com/68286215/130466304-f6b50ae3-2bf4-40df-bf6d-3adf95f2ec67.png">
* XMR: 47tW7pPZTW9LWxsB3KkWSgQgK9B5RH8yr9hPZ7jRofu8jTtPPxhpRVYjJvkK2EsYDsfpbMGBBQp5wNRrk4h6pPhG2rH1q8s
                                                  <img src="https://user-images.githubusercontent.com/68286215/130466563-1ad94060-fd62-4c87-ad3b-728858f8dcea.png">

## Description
A program that iterates through pictures in a folder, automatically changing your Steam profile picture every ~40 seconds. 

Iteration can be done randomly or linearly, random will choose any image in the folder as long as it isn't the current profile picture, whereas linear allows for—admittedly rather slow—animation.

https://user-images.githubusercontent.com/68286215/160739726-1f9f3a6c-69f4-4f80-a499-9cad8677f0c9.mp4


# Requirements
* Steam
* Internet connection
* The .pyw *should* run on either Windows or Linux, assuming you have python and `requirements.txt` installed; I haven't tested it on anything but Windows though, so open an [issue](https://github.com/AdamWHY2K/Simply_Switch_Steam_Profile_Picture/issues/new) if it doesn't.

# Installation
* Download a [release](https://github.com/AdamWHY2K/Simply_Switch_Steam_Profile_Picture/releases).
* Extract.
* Place your profile pictures into the `images` folder.
* Open `settings.inc`.
* Find your Steam64ID [here](https://www.steamidfinder.com/) and enter it into `settings.inc`.
* Ensure you are logged into steam on your browser.
* Find your SessionID and Cookie by going to: [https://steamcommunity.com/actions/FileUploader?type=player_avatar_image&sId=**YOURSTEAM64IDHERE**](https://steamcommunity.com/actions/FileUploader?type=player_avatar_image&sId=YOURSTEAM64IDHERE)
* Press F12 or right click -> Inspect.
* Go to the "Application" tab.
* Double click the second column for `steamLoginSecure`, copy the value, and enter it into `settings.inc`.
* Double click the second column for "sessionid", copy the value, and enter it into `settings.inc`.
* Run `SSS_PFP.exe` or `SSS_PFP.pyw`.
* (Optional) Add a shortcut to `SSS_PFP.exe` or `SSS_PFP.pyw` in `C:\Users\USERNAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup` to start with Windows.

# If you have any issues please first check `SSS_PFP.log`, then ensure the values in `settings.inc` are correct, then open an [issue](https://github.com/AdamWHY2K/Simply_Switch_Steam_Profile_Picture/issues/new).
