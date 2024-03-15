class Parser:
    def __init__(self, soup):
        self.soup = soup

    def parse_soup(self, tag, class_name, find_option):
        if find_option == "find":
            try:
                return self.soup.find(tag, {"class": class_name}).text.strip()
            except AttributeError:
                return None
        else:
            return self.soup.find_all(tag, {"class": class_name})
