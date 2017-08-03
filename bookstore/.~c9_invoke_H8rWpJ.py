def create_bookstore(name):
    # dict(name = name)
    bookstore = { 'name' : name, 
                  'authors' : [], 
                  'books' : []
    }
    return bookstore
    
    #return dictionary
    #{name: "rmotr's bookstore"}

def add_author(bookstore, name, nationality):
    _id = id(name)
    author = {'name' : name, 
              'nationality' : nationality, 
              'id' : _id}
    bookstore['authors'].append(author)
    return author
    
#    'last_author_id': 0
#    'last_book_id': 0
#    bookstore['last_author_id'] += 1

def get_author_by_name(bookstore, name):
    authors = bookstore['authors']
    for author in authors:
        if author['name'] == name:
            break
    return author



def get_author_by_id(bookstore, author_id):
    authors = bookstore['authors']
    for author in authors:
        i_d = author['id']
        if author_id == author['id']:
            return author


def add_book(bookstore, title, isbn, author_id):
    book = {'title' : title, 
            'isbn' : isbn, 
            'id' : author_id}
    bookstore['books'].append(book)
    return book

def get_book_by_title(bookstore, title):
    books = bookstore['books']
        if book == name:
        if book == title:
            return book


def get_book_by_id(bookstore, book_id):
    pass


def get_books_by_author(bookstore, author_id):
    pass
