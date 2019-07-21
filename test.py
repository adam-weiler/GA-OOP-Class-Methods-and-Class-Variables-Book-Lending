from Book import *

print('Adding new books to the library:')
sister_outsider = Book.create('Sister Outsider', 'Audre Lorde', '9781515905431', 'Nonfiction')
aint_i = Book.create('Ain\'t I a Woman?', 'Bell Hooks', '9780896081307', 'Nonfiction')
if_they_come = Book.create('If They Come in the Morning', 'Angela Y. Davis', '0893880221', 'Nonfiction')
game_of_thrones = Book.create('Game of Thrones', 'George R.R. Martin', '0553588486', 'Fantasy')
book_1984 = Book.create('1984', 'George Orwell', '9780451524935', 'Fiction')
hitchikers_guide_to_the_galaxy = Book.create('The Hitchhiker\'s Guide to the Galaxy', 'Douglas Adams', '0345391802', 'Science-Fiction')
print()

print(Book.browse().title) # A random book title.
print(Book.browse().title)
print(len(Book.on_shelf)) # 6
print(len(Book.on_loan)) # 0
print()

print(sister_outsider.lent_out()) # False ; Book is not lent out.
sister_outsider.borrow() # True ; Book is now borrowed.
print(len(Book.on_shelf)) # 5
print(len(Book.on_loan)) # 1
print(sister_outsider.lent_out()) # True ; Book is lent out.
print()

sister_outsider.renew() #Renews the due_date by 2 weeks.
sister_outsider.borrow() # False ; You cannot borrow a book that is out.
print(sister_outsider.on_hold) # True ; Book is on hold.
sister_outsider.renew() #False ; You cannot renew a book that is on hold.
print()

print(sister_outsider.due_date) # 2019-08-04 23:59:59
print(len(Book.overdue_books())) # 0
sister_outsider.return_to_library() # True - Book is returned.
print(sister_outsider.lent_out()) # False ; Book is not lent out.
print()

print(len(Book.on_shelf)) # 6
print(len(Book.on_loan)) # 0
print(Book.browse().genre) # A random book genre.
print(Book.browse().genre)
print()

Book.search_books('the', 'Title') #Returns 2 books.
Book.search_books('George', 'Author') #Returns 2 books.
Book.search_books('Nonfiction', 'Genre') #Returns 3 books.
Book.search_books('978', 'ISBN') #Returns 3 books.