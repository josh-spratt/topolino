from config import Config
from payload import PayloadBuilder
from request import Requester
from parse import Parser

import logging
from bs4 import BeautifulSoup
import re
from tabulate import tabulate


def main():
    logging.basicConfig(
        format="%(asctime)s %(levelname)-8s %(message)s",
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    payload = PayloadBuilder()
    logging.info("Collecting booking parameters...")
    payload.collect_parameter("checkInDate")
    payload.collect_parameter("checkOutDate")
    payload.collect_parameter("numberOfAdults")
    payload.collect_parameter("numberOfChildren")
    payload.collect_parameter("kid1")
    payload.collect_parameter("kid2")
    payload.collect_parameter("numberOfRooms")

    logging.info("Adding static parameters...")
    payload.add_static_parameter("accessible", 0)
    payload.add_static_parameter("resort", False)
    payload.add_static_parameter("roomTypeId", False)
    payload.add_static_parameter("components", "")
    payload.add_static_parameter("cartId", "")
    payload.add_static_parameter("cartItemId", "")

    logging.info("Configuring collected parameters...")
    cookie = payload.manipulate_payload()

    logging.info("Making HTTP request...")
    request_manager = Requester(url=Config.URL, headers=Config.HEADERS, cookies=cookie)
    status_code, html_text = request_manager.make_get_request()
    logging.info("HTTP request status code: %s", status_code)

    logging.info("Parsing HTML result...")
    soup = BeautifulSoup(html_text, "html.parser")
    soup_parser = Parser(soup=soup)
    resort_card_containers = soup_parser.parse_soup(
        tag="div", class_name="cardContainerInfo", find_option="find_all"
    )

    result = []
    for container in resort_card_containers:
        container_parser = Parser(soup=container)
        record = [
            container_parser.parse_soup("h2", "cardName", "find"),
            container_parser.parse_soup("div", "experienceLocation", "find"),
            re.sub(
                r"\s+",
                " ",
                container_parser.parse_soup("div", "transportation", "find").replace(
                    "Transportation Options: ", ""
                ),
            ),
            container_parser.parse_soup("div", "booked", "find"),
            container_parser.parse_soup("span", "accessibleText", "find"),
        ]
        result.append(record)
    print(tabulate(result, tablefmt="rounded_grid"))


if __name__ == "__main__":
    main()
