import os


class Display():
    def __init__(self, number_of_persistent_lines=1):
        self.number_of_persistent_lines = number_of_persistent_lines
        self.reset()

    def print_display(self):
        os.system("clear")
        for line in self.lines:
            print(line)
        self.lines = self.lines[:self.number_of_persistent_lines]

    def set_display(self, message, position):
        if position >= self.number_of_persistent_lines:
            return
        self.lines[position] = message

    def add_messages(self, *args):
        for message in args:
            self.lines.append(message)

    def reset(self):
        self.lines = ["" for i in range(self.number_of_persistent_lines)]
