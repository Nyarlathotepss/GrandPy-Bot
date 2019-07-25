from modifyuserinput import ModifyUserInput

a = ModifyUserInput()
b = ApiParameters()
a.user_input = "bonjour marseille"


def test_modification_process():
    a.modification_process()
    assert a.input_to_search == "marseille", "pb de saisie"

