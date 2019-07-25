from modifyuserinput import *
from api import *


a = ModifyUserInput()
b = ApiWiki()
c = ApiGoogleMap

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

    def mock_get(url,parameters):
        return MockResponse
    monkeypatch.setattr(requests, "get", mock_get)
    result = b.get_info("http://toto", PARAMETERS)
    assert result["lat"] == "00"


class MockResponse1:
    @staticmethod
    def json():
        return {'batchcomplete': '', 'query': {'normalized': [{'from': 'paris', 'to': 'Paris'}], 'pages': {'681159': {'pageid': 681159, 'ns': 0, 'title': 'Paris',
                'coordinates': [{'lat': 48.856578, 'lon': 2.351828, 'primary': '', 'globe': 'earth'}],
                'description': 'capitale de la France', 'descriptionsource': 'central'}}}}


def test_wiki_comm(monkeypatch):

    def mock_get(url, parameters):
        return MockResponse1
    monkeypatch.setattr(requests, "get", mock_get)
    result = b.wiki_comm("test")
    b.get_info_from_json()
    assert b.lon == "2.351828"
    assert b.lat == "48.856578"
    assert b.description == "capitale de la France"