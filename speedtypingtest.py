import time
import random

def get_words():
    # Replace this list with a larger set of words if desired
    words = ["python", "programming", "challenge", "keyboard", "practice", "speed", "typing", "test"]
    return words

def display_words(words):
    print(" ".join(words))

def typing_test():
    words = get_words()
    display_words(words)

    input("Press Enter when you are ready to start typing.")
    start_time = time.time()

    user_input = input("Type the words above: ")
    end_time = time.time()

    user_words = user_input.split()
    correct_words = [user_word == actual_word for user_word, actual_word in zip(user_words, words)]

    accuracy = sum(correct_words) / len(correct_words) * 100
    words_per_minute = len(user_words) / ((end_time - start_time) / 60)

    print("\nTyping test results:")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Words per minute: {words_per_minute:.2f}")

if __name__ == "__main__":
    print("Welcome to the Speed Typing Test!")
    typing_test()

