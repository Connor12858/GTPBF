# Import the packages needed
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Make a driver to access google
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Variables to access
guess = 0000


# Check if the guess was correct
def check_correct():
    # Get the label that contains the incorrect message
    inputLabel = driver.find_element(By.XPATH, '//*[@id="container"]/form/label')

    # Formulate what the incorrect message would say
    msg = "Sorry, " + str(guess).zfill(4) + " is not the PIN. Guess again?"

    # Check if they are the same, if so the guess was wrong
    if inputLabel.text == msg:
        return False
    else:
        return True


# Create a function to send the guess
def enter_number():
    # Find the input box
    inputBox = driver.find_element(By.NAME, "guess")

    # Type out the guess with leading zeros
    inputBox.send_keys(str(guess).zfill(4))

    # Send the input
    inputBox.submit()


if __name__ == '__main__':
    # Access the site and initialize
    driver.get("https://www.guessthepin.com/")

    # Make the first guess
    enter_number()

    # Repeat while we get the not correct message
    while not check_correct():
        guess += 1
        enter_number()

    print("The pin is: " + str(guess))
