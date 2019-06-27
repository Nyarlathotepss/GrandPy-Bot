from main import ModifyUserInput
from api import ApiParameters
import pytest, requests
from pytest import p
a = ModifyUserInput()
b = ApiParameters()
a.user_input = "bonjour marseille"


def test_modification_process():
    a.modification_process()
    assert a.input_to_search == "marseille"


def test_generate_parameters_wiki():
    b.generate_parameters_wiki(a.input_to_search)
    assert b.PARAMETERS == {"action": "query",
                            "format": "json",
                            "titles": a.input_to_search,
                            "prop": "coordinates|description"}


def test_generate_gmaps():
    b.generate_parameters_gmaps(b.lat, b.lon)
    assert b.PARAMETERS == {"location": (b.lat, b.lon),
                            "key": b.googlemap_key}


class MockResponse:
    @staticmethod
    def json():
        return {"lat": "00"}


def test_get_info(monkeypatch):
    PARAMETERS = {"lat": "00"}

    def mock_get():
        return MockResponse
    monkeypatch.setattr(requests, "get", mock_get)
    result = b.get_info("https://test", PARAMETERS)
    assert result["lat"] == "00"

"""
class FakeRequestsLibrary(object):

    def get(self, url):
        self.url = url
        return self
    def json(self):
        return self.data
def test_google():
    fake = FakeRequestsLibrary()
    fake.data = {"lat": "00", "lon": "00"}
    with patch('requests.get', fake.get):
        coordinates = b.get_info_from_json()

    assert coordinates == {"lat": "00", "lon": "00"}
"""
