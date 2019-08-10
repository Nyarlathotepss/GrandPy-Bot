import pytest
from modifyuserinput import ModifyUserInput
from constant import *


@pytest.fixture()
def simulate_empty_input_user():
    object_modify_user_input = ModifyUserInput()
    user_input = None
    if not user_input:                                        # if input is empty
        object_modify_user_input.response_from_papybot = GRANDPY_BOT_QUESTION_EMPTY
    return object_modify_user_input.response_from_papybot

