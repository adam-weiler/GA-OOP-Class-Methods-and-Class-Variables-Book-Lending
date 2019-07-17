from datetime import datetime
import random

# options = [15,20,34923,31,3,5,86,1]
# print(random.choice(options))
# print(random.choice(options))
# print(random.choice(options))
# print(random.choice(options))
# print(random.choice(options))




# now = datetime.now()
# print(now) # datetime.datetime(2018, 12, 14, 17, 7, 5, 190626) <--- the current date and time
# print(now.timestamp()) # 1544825225.190626 <--- the current date and time represented as the number of seconds that have passed since January 1st 1970 at midnight UTC time (that's when they started counting!)
# one_hour = 60 * 60 # 60 seconds times 60 minutes
# print(now.timestamp() + one_hour) # 1544828825.190626 <---- an hour from now (as a "timestamp")
# hour_from_now = now.timestamp() + one_hour
# print(datetime.fromtimestamp(hour_from_now)) # datetime.datetime(2018, 12, 14, 18, 7, 5, 190626) <--- an hour from now (as a datetime obj)



class Book():
    #These are class variables.
    on_shelf = []
    on_loan = []


    #These are instance methods.
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN

    def borrow(self):
        pass

    def return_to_library(self):
        pass

    def lent_out(self):
        # print(self.on_shelf)

        print(self)

        for book in self.on_shelf: #Iterates through all books on_shelf
            # print(book.title)
            if (book == self): #If current iteration book is the same as the one triggering the instance method.
                return False #The book has not been taken out.
            return True #Else, the book has been taken out.
            



    #These are class methods.
    @classmethod
    def create(cls, title, author, ISBN):
        new_book = Book(title, author, ISBN)
        cls.on_shelf.append(new_book)
        return new_book

    def current_due_date(cls):
        pass

    def overdue_books(cls):
        pass

    def browse(cls):
        pass
        # print('hey')
        # return random.choice(options)




sister_outsider = Book.create("Sister Outsider", "Audre Lorde", "9781515905431")
aint_i = Book.create("Ain't I a Woman?", "Bell Hooks", "9780896081307")
if_they_come = Book.create("If They Come in the Morning", "Angela Y. Davis", "0893880221")
# print(Book.browse().title) # "Sister Outsider" (this value may be different for you)
# print(Book.browse().title) # "Ain't I a Woman?" (this value may be different for you)
print(len(Book.on_shelf)) # 3
print(len(Book.on_loan)) # 0
print(sister_outsider.lent_out()) # False
print(sister_outsider.borrow()) # True
print(len(Book.on_shelf)) # 2
print(len(Book.on_loan)) # 1
print(sister_outsider.lent_out()) # True
print(sister_outsider.borrow()) # False
# print(sister_outsider.due_date) # 2017-02-25 20:52:20 -0500 (this value will be different for you)
# print(len(Book.overdue())) # 0
# print(sister_outsider.return_to_library()) # True
print(sister_outsider.lent_out()) # False
print(len(Book.on_shelf)) # 2
print(len(Book.on_loan)) # 0