from constant import stop_words


class ModifyUserInput:
    """ check user input to found data to exploit"""

    def __init__(self):
        self.user_input = None
        self.list_user_input = []

    def split_text(self, user_input):
        self.user_input = user_input.split()

    def clean_text(self, user_input_split):
        """clean text and transform to list"""
        for word in user_input_split:
            if word not in stop_words:
                    self.list_user_input.append(word)
