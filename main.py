from constant import stop_words


class ModifyUserInput:
    """ check user input to found data to exploit"""

    def __init__(self):
        self.user_input = input("enter:")
        self.user_select = None
        self.list_user_input = []

    def split_text(self):
        self.user_select = self.user_input.split()

    def clean_text(self):
        """clean text and transform to list"""
        for word in self.user_select:
            if word not in stop_words:
                    self.list_user_input.append(word)


nico = AnalysisData()
nico.split_text()
print(nico.user_select)
nico.clean_text()
print(nico.list_user_input)
