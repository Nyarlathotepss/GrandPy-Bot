from main import ModifyUserInput
from api import ApiParameters

a = ModifyUserInput()
b = ApiParameters()
user_input = "la tour eiffel"

a.user_input = user_input
print(a.user_input)

a.modification_process()
print(a.input_to_search)

b.wiki_comm(a.input_to_search)
print(b.json)

b.get_info_from_json()
print(b.lat, b.lon, b.description)

