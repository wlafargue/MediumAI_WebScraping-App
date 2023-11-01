from bs4 import BeautifulSoup as bs
import requests

def scrape(url):
    """ Web scrapping with BeautifulSoup.

    Args:
        url (str): webpage url
    
    Returns:
        data (dict): dictionary containing lists of titles, texts, 
                     pictures, authors and authors' photo
    
    """
    response = requests.get(url)
    soup = bs(response.content, "lxml")

    # Titles
    titles = [title.text for title in soup.find_all('h2', 'be if ig ih ii ij ik il im in io ip gu gv iq ir gw is it iu iv iw ix iy iz ja jb gh gg hz ib id bj')]

    # Texts
    texts = [text.text for text in soup.find_all('h3')]

    # Pictures
    pictures = [img['src'] for img in soup.find_all('img', "bw lh")]

    # Authors
    authors = [author.text for author in soup.find_all('p', "be b gm z gh hy gg hz ia ib ic id bj")]

    # Authors' photo
    photos = [img['src'] for img in soup.find_all('img', "l hv bx hq hr ec")]

    data = {
        'titles' : titles,
        'texts' : texts,
        'pictures' : pictures,
        'authors' : authors,
        'photos' : photos,
    }

    return data