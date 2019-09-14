from constant import *
import random


class ModifyUserInput:
    """ check user input to found data to exploit"""
    def __init__(self):
        self.input_to_search = None
        self.response_from_papybot = None

    def clean_punctuation(self, user_input):
        """deleting punctuations from user_input"""
        user_input_without_punct = str()
        for char in user_input:
            if char not in PUNCTUATION:
                user_input_without_punct = user_input_without_punct + str(char)
            else:
                user_input_without_punct = user_input_without_punct + " "
        return user_input_without_punct

    def split_text(self, user_input):
        """string to list"""
        user_input_split = user_input.split()
        return user_input_split

    def clean_text(self, user_input_split):
        """clean text of stop words"""
        list_input_user_cleaned = []
        for word in user_input_split:
            if word not in STOP_WORDS:
                list_input_user_cleaned.append(word)
        return list_input_user_cleaned

    def format_text_to_search(self, list_input_cleaned):
        """format text for wikipedia API"""
        list_input_cleaned_and_format = []
        for word in list_input_cleaned:
            list_input_cleaned_and_format.append(word)
        self.input_to_search = " ".join(list_input_cleaned_and_format)

    def modification_process(self, raw_user_input):
        """use all method in this class to format user input"""
        step_1 = self.clean_punctuation(raw_user_input)
        step_2 = self.split_text(step_1)
        step_3 = self.clean_text(step_2)
        self.format_text_to_search(step_3)

    def get_random_response_from_papybot(self):
        """Build the grandpy response"""
        self.response_from_papybot = random.choice(GRANDPY_BOT_ANSWERS)
