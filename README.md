# Simply_Switch_Steam_Profile_Picture
Author: AdamWHY2K

                                      Not expected, extremely appreciated:
* BTC: bc1qfgj4tk2a7hzyxmmrgx4mvumef5f6yfey737xsj    BCH: qzrqu0yecxka0p7sxr2g3fvpfcpg9x0awq3tf2m5ny   
                      <img src="https://user-images.githubusercontent.com/68286215/130465610-63a93f21-4c79-4de4-a1ee-2aeb6ed17a9a.png">                                                                    <img src="https://user-images.githubusercontent.com/68286215/130466304-f6b50ae3-2bf4-40df-bf6d-3adf95f2ec67.png">
* XMR: 47tW7pPZTW9LWxsB3KkWSgQgK9B5RH8yr9hPZ7jRofu8jTtPPxhpRVYjJvkK2EsYDsfpbMGBBQp5wNRrk4h6pPhG2rH1q8s
                                                  <img src="https://user-images.githubusercontent.com/68286215/130466563-1ad94060-fd62-4c87-ad3b-728858f8dcea.png">

## Description
A program that iterates through pictures in a folder, changing your Steam profile picture every ~30 seconds

Can be used for animation, albeit rather slow animation. Steam limits profile picture changes to one every 30 - 40 seconds.


# Requirements
* Steam
* Internet connection

# Installation
* Download a [release](https://github.com/AdamWHY2K/Simply_Switch_Steam_Profile_Picture/releases).
* Extract.
* Place your profile pictures into the `images` folder.
* Open `settings.inc`.
* Find your Steam64ID [here](https://www.steamidfinder.com/) and enter it into `settings.inc`.
* Ensure you are logged into steam on your browser.
* Find your SessionID and Cookie by going to: [https://steamcommunity.com/actions/FileUploader?type=player_avatar_image&sId=**YOURSTEAM64IDHERE**](https://steamcommunity.com/actions/FileUploader?type=player_avatar_image&sId=YOURSTEAM64IDHERE)
* Press F12 or right click -> Inspect
* Go to the "Application" tab
* Double click the second column for `steamLoginSecure`, copy the value, and enter it into `settings.inc`.
* Double click the second column for "sessionid", copy the value, and enter it into `settings.inc`.
* Run `SSS_PFP.exe` or `SSS_PFP.pyw`

# If you have any issues please first check `SSS_PFP.log`, then ensure the values in `settings.inc` are correct, then open an [issue](https://github.com/AdamWHY2K/Simply_Switch_Steam_Profile_Picture/issues/new).
