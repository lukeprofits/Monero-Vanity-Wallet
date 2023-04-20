# monero-vanity-wallet
![Version 1.0](https://img.shields.io/badge/Version-1.0-orange.svg)
![Python 3.10.9+](https://img.shields.io/badge/Python-3.10.9+-3776ab.svg)

monero-vanity-wallet is simple tool to add custom text to the end of your Monero wallet.

Why the end and not the beginning? Because the first character of a Monero wallet is always a "4" usually followed by a number or an "A". Characters don't get truly random until a few characters into the wallet address, so adding the custom text to the end makes the most sense.


# How To Use:
* Make sure you have [Python 3.10.9](https://www.python.org/downloads/) or newer installed
* Download the files in this repo and put them in a folder
* Download the [Monero CLI Wallet](https://www.getmonero.org/downloads/#cli), extract the files from the .zip and put them in the same folder
* Double click the "START_VANITY_GENERATOR.bat" file, or open your console and enter the command: `python monero_vanity_wallet.py`
* When prompted, enter the custom text that you would like to have at the end of your wallet address
* That's it!


# Donate
If you use this, throw me some XMR (even if it's just a few cents)

XMR: `4At3X5rvVypTofgmueN9s9QtrzdRe5BueFrskAZi17BoYbhzysozzoMFB6zWnTKdGC6AxEAbEE5czFR3hbEEJbsm4hCeX2S`


# Generation Speed
Monero uses Base58, so there are 58 possibilities for each character, two of which are correct ("A" or "a"). 
If we assume 30 wallets/min are generated:

* 1 custom character  = 2 minutes to generate
* 2 custom characters =   2 hours to generate
* 3 custom characters =    4 days to generate
* 4 custom characters =  7 months to generate
* 5 custom characters =  35 years to generate

This vanity wallet generate is not the fastest (it uses the [Monero CLI Wallet](https://www.getmonero.org/downloads/#cli)), but it is great for generating wallets if you just want a few custom characters at the end (for example: XMR).


## Features
* Lets you type in custom text and generates a Monero wallet with the custom text at the end
* Convenient .bat launcher
* Cool Monero color scheme & ASCII Art


## Requirements
* [Python 3.10.9](https://www.python.org/downloads/) or above
* [Monero CLI Wallet](https://www.getmonero.org/downloads/#cli)


## License
[MIT](https://github.com/Equim-chan/vanity-monero/blob/master/LICENSE)
