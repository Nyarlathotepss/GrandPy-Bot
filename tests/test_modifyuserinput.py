from modifyuserinput import ModifyUserInput
from views1 import Control
from constant import GRANDPY_BOT_QUESTION_EMPTY, GRANDPY_BOT_DONT_UNDERSTAND
import requests


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


def test_sentence_empty():
    """simulate an empty user_input """
    object_control = Control()
    input_user = ""
    object_control.control_if_empty(input_user)
    assert object_control.user_interaction.response_from_papybot == GRANDPY_BOT_QUESTION_EMPTY


class MockResponse:

    @staticmethod
    def json():
        return {'status': 'ZERO_RESULTS'}


def test_no_sense(monkeypatch):
    object_control = Control()
    """simulate a non sense user_input, for example the input user could be : blablablabla """
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)
    result = object_control.object_gmap.get_info("www.fake_api_google.com", {"fake": "parameter"})
    assert result['status'] == 'ZERO_RESULTS'
    assert object_control.user_interaction.response_from_papybot == GRANDPY_BOT_DONT_UNDERSTAND
