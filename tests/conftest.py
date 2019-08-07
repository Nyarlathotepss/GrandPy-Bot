import pytest
from modifyuserinput import ModifyUserInput
from constant import *

@pytest.fixture()
def simulate_empty_input_user():
    object_modify_user_input = ModifyUserInput()
    user_input = None
    if not user_input:                                        # if input is empty
        object_modify_user_input.response_from_papybot = grandpy_bot_question_empty
    return object_modify_user_input.response_from_papybot

@pytest.fixture()
def simulate_nonsense_input_user():
    object_modify_user_input = ModifyUserInput()
    return_from_googlemap = {'status': 'ZERO_RESULTS'}         # the json return by googlemap
    if return_from_googlemap['status'] == 'ZERO_RESULTS':
        object_modify_user_input.response_from_papybot = grandpy_bot_dont_understand
    return object_modify_user_input.response_from_papybot
