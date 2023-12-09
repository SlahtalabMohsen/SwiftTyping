import time

def SwiftTyping():
    prompt = "The quick brown fox jumps over the lazy dog"
    print("Type this following text as fast as you can: ")
    print(prompt)
    input("Press the enter when you are ready to start...")
    startTime = time.time()
    userInput = input("Type your text: ")
    endTime = time.time()
    elapsedTime = endTime - startTime
    wordsTyped = len(userInput.split())
    speed = wordsTyped / (elapsedTime / 60)
    print(f"You typed the text in {elapsedTime:.2f} seconds.")
    print(f"Your speed is {speed:.2f} words per minute!")
SwiftTyping()

# download the source code and give me a star in github/SlahtalabMohsen