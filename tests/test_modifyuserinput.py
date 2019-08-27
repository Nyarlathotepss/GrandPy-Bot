from modifyuserinput import ModifyUserInput
from views import Control
from constant import GRANDPY_BOT_QUESTION_EMPTY, GRANDPY_BOT_DONT_UNDERSTAND
import requests


def test_clean_text():
    """check if sentence is cleaned about stop words"""
    test = ModifyUserInput()
    test.user_input = "bonjour as tu des infos sur  marseille"
    test.modification_process(test.user_input)
    assert test.input_to_search == "marseille"


def test_clean_punctuation():
    """check if sentence is cleaned about punctuation"""
    test = ModifyUserInput()
    test.user_input = "notre-,dame-de-paris?!"
    test.modification_process(test.user_input)
    assert test.input_to_search == "notre dame paris"


def test_sentence_empty():
    """simulate an empty user_input and check if the user response is correct """
    object_control = Control()
    object_control.user_question = ""
    object_control.control_if_empty()
    assert object_control.user_interaction.response_from_papybot == GRANDPY_BOT_QUESTION_EMPTY


class MockResponse:
    """mock the json method with an empty json"""
    @staticmethod
    def json():
        return {'status': 'ZERO_RESULTS'}


def test_no_sense(monkeypatch):
    """check if the user questions has non sense that program return an answer to user """
    object_control = Control()
    object_control.user_question = "sdfsdfsdfds"
    """simulate a non sense user_input, for example the input user could be : blablablabla """
    def mock_get(*args):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)
    result = object_control.object_gmap.get_info("www.fake_api_google.com", {"fake": "parameter"})
    object_control.object_gmap.googlemap_json = result
    assert result['status'] == 'ZERO_RESULTS'
    object_control.control_if_google_found_place()
    assert object_control.user_interaction.response_from_papybot == GRANDPY_BOT_DONT_UNDERSTAND
