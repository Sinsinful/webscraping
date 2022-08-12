import requests
import bs4

# goal: get the title of every book with 2 stars

base_url = 'https://books.toscrape.com/catalogue/category/books_1/page-{}.html'

twostar_books = []

for n in range(1, 51):
    
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select('.product_pod')
    
    for book in books:
        
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            twostar_books.append(book_title)

print(twostar_books)