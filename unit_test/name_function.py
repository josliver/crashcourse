"""
    create environment: python -m venv .env
    activate it       : source .env/bin/activate
    update pip        : pip install --upgrade pip
    install pytest    : pip install pytest
    run pytest        : pytest [TEST_FOLDER]
"""

def get_formatted_name(first: str, last: str, middle:str = "") -> str:
    return f"{first.title()} {last.title()}" if not middle else f"{first.title()} {middle.title()} {last.title()}" 