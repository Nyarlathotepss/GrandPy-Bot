from modifyuserinput import ModifyUserInput
from constant import grandpy_bot_question_empty, grandpy_bot_dont_understand


def test_clean_text():
    test = ModifyUserInput()
    test.user_input = "bonjour as tu des infos sur  marseille"
    test.modification_process(test.user_input)
    assert test.input_to_search == "marseille"


def test_clean_punctuation():
    test = ModifyUserInput()
    test.user_input = "notre-,dame-de-paris?!"
    test.modification_process(test.user_input)
    assert test.input_to_search == "notre dame paris"


def test_sentence_empty(simulate_empty_input_user):
    """simulate an empty user_input """
    assert simulate_empty_input_user == grandpy_bot_question_empty


def test_no_sense(simulate_nonsense_input_user):
    """simulate an non sense user_input, for example the input user could be : blablablabla """
    assert simulate_nonsense_input_user == grandpy_bot_dont_understand
