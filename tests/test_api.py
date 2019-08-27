from views import Control
from constant import *
import api


class MockResponse:
    """class to mock the json response and create the json file"""

    def __init__(self, your_json=None):
        if your_json is None:
            self.fake_json = {}
        else:
            self.fake_json = your_json

    def json(self):
        """modify the return of json method"""
        return self.fake_json


def test_api_google_with_empty_json(monkeypatch):
    """test if api google return an empty json"""
    object_apigoogle = api.ApiGoogleMap()

    def mock_get(*args):
        return MockResponse()

    monkeypatch.setattr(api.requests, "get", mock_get)
    result = object_apigoogle.get_info("www.fake_api_google.com", {"fake": "parameter"})
    assert result == {}


def test_api_wiki_with_empty_json(monkeypatch):
    """test if api wikimedia return an empty json"""
    object_api_wiki = api.ApiWiki()
    object_control = Control()

    def mock_get(*args):
        return MockResponse()

    monkeypatch.setattr(api.requests, "get", mock_get)
    result = object_api_wiki.get_info("www.fake_api_wikimedia.com", {"fake": "parameter"})
    assert result == {}
    object_control.object_wiki.json_page_id = result
    object_control.object_wiki.json_description = result
    object_control.control_if_wiki_found_page_id()
    assert object_control.user_interaction.response_from_papybot == GRANDPY_BOT_DONT_UNDERSTAND


def test_api_wiki_with_no_result_found(monkeypatch):
    """test if api wikimedia return a different result than expected"""
    MockResponse({"result": "not found"})
    object_control = Control()
    object_api_wiki = api.ApiWiki()

    def mock_get(*args):
        return MockResponse()

    monkeypatch.setattr(api.requests, "get", mock_get)
    result = object_api_wiki.get_info("www.fake_api_wikimedia.com", {"fake": "parameter"})
    assert result == {"result": "not found"}
    object_control.object_wiki.json_page_id = result
    object_control.object_wiki.json_description = result
    object_control.control_if_wiki_found_page_id()
    assert object_control.user_interaction.response_from_papybot == GRANDPY_BOT_DONT_UNDERSTAND
