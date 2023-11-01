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

    # Original webpage of articles
    hrefs = [article.a['href'].split('?')[0] for article in soup.find_all('div', 'lc ld le lf lg l')]

    # Minutes for reading
    min_read = [int(span.text.split()[0]) for article in soup.find_all('div', 'jg jh ji jj jk ab q') for span in article.findAll('span') if 'read' in span.contents[0]]

    # Published date
    date = [span.text for article in soup.find_all('div', 'jg jh ji jj jk ab q') for span in article.children if ' read' not in span.text and len(span.text)> 2]

    data = {
        'titles' : titles,
        'texts' : texts,
        'pictures' : pictures,
        'authors' : authors,
        'photos' : photos,
        'hrefs': hrefs,
        'min_read': min_read,
        'date': date
    }

    return data