# GuessThePinBruteForce
https://www.guessthepin.com/ brute force python script. Going through all the pins for 0000 to 9999 looking to find the correct pin.

A very basic introduction to brute forcing, which is forcing to find the correct combination without using a wordlist of possible passwords. It proves to be a very ineffective and time-consuming method of breaking into devices, as a simple prevention is time-outs after a set amount of fails.

## Install
Open up a cmd prompt to clone the repo

`git clone https://github.com/Connor12858/GTPBF.git`

Move into the directory

`cd GTPBF`

Create a virtual environment (optional) 

1. `python3 -m venv venv`
2. `.\venv\Scripts\activate`

Install the needed packages

`pip install -r requirements.txt`

Run the script

`python3 main.py`