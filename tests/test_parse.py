from src.parse import Parser
from bs4 import BeautifulSoup

SAMPLE_DATA = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>HTML 5 Boilerplate</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
	<script src="index.js"></script>
    <div class="cardContainerInfo">Testy Test</div>
    <h2 class="testClass">test1</h2>
    <h2 class="testClass">test2</h2>
    <h2 class="testClass">test3</h2>
  </body>
</html>
"""


def test_parser_find():
    soup = BeautifulSoup(SAMPLE_DATA, "html.parser")
    soup_parser = Parser(soup=soup)
    assert soup_parser.parse_soup("div", "cardContainerInfo", "find") == "Testy Test"


def test_parser_find_all():
    soup = BeautifulSoup(SAMPLE_DATA, "html.parser")
    soup_parser = Parser(soup=soup)
    assert [x.text for x in soup_parser.parse_soup("h2", "testClass", "find_all")] == [
        "test1",
        "test2",
        "test3",
    ]


def test_parser_find_none():
    soup = BeautifulSoup(SAMPLE_DATA, "html.parser")
    soup_parser = Parser(soup=soup)
    assert soup_parser.parse_soup("h2", "noodleHat", "find") == None


def test_parser_find_all_none():
    soup = BeautifulSoup(SAMPLE_DATA, "html.parser")
    soup_parser = Parser(soup=soup)
    assert soup_parser.parse_soup("h2", "noodleHat", "find_all") == []
