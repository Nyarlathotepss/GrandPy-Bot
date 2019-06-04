from constant import *


class ModifyUserInput:
    """ check user input to found data to exploit"""

    def __init__(self):
        self.user_input = str
        self.user_input_split = None
        self.list_input_user_cleaned = []
        self.input_to_search = None

    def split_text(self, user_input):
        """string to list"""
        self.user_input_split = user_input.split()

    def clean_text(self, user_input_split):
        """clean text of stop words"""
        for word in user_input_split:
            if word not in stop_words:
                    self.list_input_user_cleaned.append(word)

    def format_text_to_search(self, list_input_cleaned):
        """format text for wikipedia API"""
        list_input_cleaned_and_format = []
        for word in list_input_cleaned:
            list_input_cleaned_and_format.append(word.capitalize())
        self.input_to_search = " ".join(list_input_cleaned_and_format)

    def modification_process(self):
        self.split_text(self.user_input)
        self.clean_text(self.user_input_split)
        self.format_text_to_search(self.list_input_user_cleaned)

