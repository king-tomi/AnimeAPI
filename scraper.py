from typing import List, Union
import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup


class Scraper:

    """
    Scraper class that allows the user scrape a web page and get desired values
    website of target is https://anime-planet.com

    paramters:
            url (str) -> the url of the site

            extras (str) -> any extra page that may accompany the url
    """

    BASE_SITE = 'https://anime-planet.com'

    AVAILABLE_CONTAINERS = (
        "class",
        "id"
    )

    def __init__(self, extra: str = None) -> None:
        self.response = self.get_page(Scraper.BASE_SITE, extra)

    @staticmethod
    def get_page(url: str, extras: str = None) -> requests.Response:
        """
        gets a webpage and returns the response if not None

        @param: url -> the url for the page
        @param: extras -> any extra string that accompanies the url

        @returns: a requests.Response object
        """
        if extras is not None:
            try:
                response = requests.get(url + extras)
                if response is not None:
                    return response
            except HTTPError as e:
                print(f"error occurred {e}")
            else:
                return None
        else:
            try:
                response = requests.get(url)
                if response is not None:
                    return response
            except HTTPError as e:
                print(f"error occurred {e}")
            else:
                return None


    def sieve_anime_reviews(self) -> List[str]:
        """
        sieves the page and returns the reviews for the specified anime
        """
        soup = BeautifulSoup(self.response.content, "html.parser")
        result = soup.find_all("div", class_="reviewScores pure-1-5")
        return [item.text.strip() for item in result]

    def sieve_anime_ratings(self) -> List[str]:
        """
        sieves the page and returns the ratings for the specified anime
        """ 
        soup = BeautifulSoup(self.response.content, "html.parser")
        result = soup.find_all("span", class_="slCount")
        return [item.text.strip() for item in result]

    def sieve_info(self) -> Union[List[str], int]:
        """
        sieves the page and returns the number of episodes for the specified anime
        """
        soup = BeautifulSoup(self.response.content, "html.parser")
        result = soup.find_all("div", class_="pure-1 md-1-5")
        
        if len(result) == 1:
            return int(result[0])
        else:
            return [item.text.strip() for item in result]

    def sieve_manga_reviews(self) -> List[str]:
        """
        sieves the page and returns the reviews for the specified manga
        """
        soup = BeautifulSoup(self.response.content, "html.parser")
        result = soup.find_all("div", class_="reviewScores pure-1-4")
        return [item.text.strip() for item in result]

    def sieve_manga_ratings(self) -> List[str]:
        """
        sieves the page and returns the ratings for the specified manga
        """ 
        soup = BeautifulSoup(self.response.content, "html.parser")
        result = soup.find_all("span", class_="slCount")
        return [item.text.strip() for item in result]

    def sieve_characters(self) -> List[str]:
        """sieves the page and returns the character name for the specified anime/manga"""
        soup = BeautifulSoup(self.response.content, "html.parser")
        result = soup.find_all("a", class_="name")
        return [item.text.strip() for item in result]



if __name__ == "__main__":
    scraper = Scraper("/manga/naruto")
    char = scraper.sieve_info()
    print(char)