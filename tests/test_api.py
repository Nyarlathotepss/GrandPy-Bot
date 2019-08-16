from api import *
from views import Control
import requests


class MockResponse:

    def __init__(self, json=None):
        if json is None:
            self.fake_json = {}
        else:
            self.fake_json = json

    def json(self):
        return self.fake_json


def test_api_google_with_empty_json(monkeypatch):

    form =
    object_mock = MockResponse()
    object_control = Control()
    object_gmap = ApiGoogleMap()

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)
    result = object_gmap.get_info("www.fake_api_google.com", {"fake": "parameter"})
    assert result == {}


"""
def test_api_wiki_with_empty_json(monkeypatch):


 
def test_api_wiki_with_no_result_found(monkeypatch):
"""
json = MockResponse()
json.fake_json = {}
