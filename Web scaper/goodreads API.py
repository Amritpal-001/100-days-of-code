import goodreads
from goodreads import client
gc = client.GoodreadsClient(<api_key>, <api_secret>)
gc.authenticate(<access_token>, <access_token_secret>)

book = gc.book(1)
book.title
authors = book.authors
authors[0].name

book.average_rating


author = gc.author(2617)
author.name
author.works_count
author.books

'''

>>> import goodreads_api_client as gr
>>> client = gr.Client(developer_key='<YOUR_DEVELOPER_KEY>')
>>> book = client.Book.show('1128434')
>>> keys_wanted = ['id', 'title', 'isbn']
>>> reduced_book = {k:v for k, v in book.items() if k in keys_wanted}
>>> reduced_book
{'id': '1128434', 'title': 'The Last Wish (The Witcher, #1)', 'isbn': '0575077832'}


'''

