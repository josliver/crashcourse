#from name_function import get_formatted_name  as gfn
from name_function import get_formatted_name as gfn

def test_first_last_name():
    formatted_name = gfn("janis","joplin")
    assert formatted_name == "Janis Joplin"

def test_first_last_middle_name():
    formatted = gfn("wolfang","mozart","amadeus")
    assert formatted == "Wolfang Amadeus Mozart"

print(gfn("Jon","Sliver"))