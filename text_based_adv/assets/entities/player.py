"""
File docs here, when they're ready!
"""
# Created by Aaron Delaney, see README.md for more information.

class Player(object):
    def __init__(self, controller):
        self.name = controller.string_prompt(
            prompt = 'What is your name: ',
            word_limit = 1
        )
        self.gender = controller.option_prompt(
            prompt = 'Are you male, or female: ',
            options = ['male', 'female']
        )
        self.hp = 100
