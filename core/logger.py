import pygame

class Logger:
    def __init__(self, filename):
        self.filename = filename

    # logs a message to the file
    def log(self, message):
        with open(self.filename, "a") as file:
            file.write(message + "\n")

    # clears the file
    def clear(self):
        with open(self.filename, "w") as file:
            file.write("")