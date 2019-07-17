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
        if (self.lent_out()): #The book is already lent out.
            return False
        #Else, the book is not lent out.
        self.due_date = self.current_due_date() #Sets the book's due_date to the current_due_date.
        
        self.on_loan.append(self)
        # self.on_loan.append(self.on_shelf.remove(self)) #Removes the book from on_shelf and appends it to on_loan.
        self.on_shelf.remove(self)

        # print('there')
        # print(self.on_loan)
        # print(self.on_shelf)

        return True


    def return_to_library(self):
        # print('here')
        if (self.lent_out()): #If lent_out is true.

            self.on_shelf.append(self)
            self.on_loan.remove(self)

            # print(self.on_loan)
            # print(self.on_shelf)
            # self.on_shelf.append(self.on_loan.remove(self)) #Removes the book from on_shelf and appends it to on_loan.

            print('The book was returned.')
            return True

        #Else, lent_out is false.
        print('The book wasn\'t on loan in the first place.')
        return False



    def lent_out(self):
        # print(self.on_shelf)

        # print(self)

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

    @classmethod
    def current_due_date(cls):
        now = datetime.now()
        two_weeks = 60 * 60 * 24 * 14 # two weeks expressed in seconds  
        future_timestamp = now.timestamp() + two_weeks
        return datetime.fromtimestamp(future_timestamp)

    @classmethod
    def overdue_books(cls):
        # print('\n Overdue book')
        # print(cls.on_loan[0].due_date)

        overdue_list = []
        
        for book in cls.on_loan: #Iterates through each book in the on_loan list.
            if (book.due_date < datetime.now()): #If current book's due_date happened before this moment.
                print('THAT"S OVERDUEE!')
                overdue_list.append(book)

        # print('Overdue book \n')

        return overdue_list


    @classmethod
    def browse(cls): #Returns a random book from the on_shelf list.
        return random.choice(cls.on_shelf)


sister_outsider = Book.create("Sister Outsider", "Audre Lorde", "9781515905431")
aint_i = Book.create("Ain't I a Woman?", "Bell Hooks", "9780896081307")
if_they_come = Book.create("If They Come in the Morning", "Angela Y. Davis", "0893880221")
print(Book.browse().title) # "Sister Outsider" (this value may be different for you)
print(Book.browse().title) # "Ain't I a Woman?" (this value may be different for you)
print(len(Book.on_shelf)) # 3
print(len(Book.on_loan)) # 0
print(sister_outsider.lent_out()) # False
print(sister_outsider.borrow()) # True
print(len(Book.on_shelf)) # 2
print(len(Book.on_loan)) # 1
print(sister_outsider.lent_out()) # True
print(sister_outsider.borrow()) # False
print(sister_outsider.due_date) # 2017-02-25 20:52:20 -0500 (this value will be different for you)
print(len(Book.overdue_books())) # 0
print(sister_outsider.return_to_library()) # True
print(sister_outsider.lent_out()) # False
print(len(Book.on_shelf)) # 2
print(len(Book.on_loan)) # 0