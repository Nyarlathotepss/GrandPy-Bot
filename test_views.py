from main import ModifyUserInput
from api import ApiParameters

a = ModifyUserInput()
b = ApiParameters()
a.user_input = "bonjour marseille"


def test_modification_process():
    a.modification_process()
    assert a.input_to_search == str(a.input_to_search)


def test_generate_parameters_wiki():
    b.generate_parameters_wiki(a.input_to_search)
    assert b.PARAMETERS == {"action": "query",
                            "format": "json",
                            "titles": a.input_to_search,
                            "prop": "coordinates|description"}

