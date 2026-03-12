from resources.utils import extract_title_from_writeup


def test_extract_title_from_formatted_writeup():
    writeup = """======================
Writeup:

Title:
Example vulnerability title
Severity: High
======================"""

    assert extract_title_from_writeup(writeup) == "Example vulnerability title"


def test_extract_title_from_writeup_missing_title():
    assert extract_title_from_writeup("no title here") == ""
