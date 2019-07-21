from datetime import date, datetime #Used to calculate due dates.
import random #Used to choose a random book from the shelf.

class Book():
    #These are class variables.
    entire_library = []
    on_shelf = []
    on_loan = []

    #These are instance methods.
    def __init__(self, title, author, ISBN, genre):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.genre = genre
        self.on_hold = False

    def __str__(self):
        return(f'{self.title} - {self.author} - {self.ISBN} - {self.genre} - On hold: {self.on_hold}')

    def lent_out(self):
        for book in self.on_shelf: #Iterates through all books on_shelf
            if book.title == self.title: #If current book is the same as the one triggering the instance method.
                # print(f'\'{book.title}\' is available!') #This line is not necessary.
                return False #The book has not been taken out.
            else: #Else, it will keep looking.
                pass
        #The loop is over and the book was not found.
        # print(f'\'{self.title}\' is already lent out.') #This line is not necessary.
        return True #The book has been taken out.

    def borrow(self):
        if self.lent_out(): #The book is already lent out.
            self.on_hold = True
            print(f'The book \'{self.title}\' is already lent out. It is due on {self.due_date}.')
            print('It has been put on hold for you.')
            return False
        else: #Else the book is not lent out.
            print(f'\'{self.title}\' is available!')
            self.due_date = self.current_due_date()  #Sets the book's due_date to new due_date.
            self.on_hold = False
            self.on_loan.append(self) #Appends book to on_loan list.
            self.on_shelf.remove(self) #Removes book on_shelf list.
            print(f'You have borrowed \'{self.title}\'. It is due on {self.due_date}.')
            return True

    def return_to_library(self):
        if (self.lent_out()): #If lent_out is true.
            self.on_shelf.append(self) #Appends book to on_shelf list.
            self.on_loan.remove(self) #Removes book on_loan list.
            print('The book was returned.')
            return True
        else: #Else lent_out is false.
            print('The book wasn\'t on loan in the first place.')
            return False

    def renew(self): #Renews the book by setting the due_date for 2 weeks from now.
        if (self.lent_out()): #If lent_out is true.
            if (self.on_hold): #If book is on hold.
                print('The book is on hold and cannot be renewed.')
                return False
            else: #Else book is not on hold.
                self.due_date = datetime.now() #This line is unecessary. It's to simulate the book being due today.
                self.due_date = self.current_due_date() #Sets the book's due_date to new due_date.
                print(f'You have renewed \'{self.title}\'. It is now due on {self.due_date}.')
                return True
        else: #Else lent_out is false.
            print('The book wasn\'t on loan in the first place.')
            return False

    #These are class methods.
    @classmethod
    def create(cls, title, author, ISBN, genre):
        new_book = Book(title, author, ISBN, genre)
        cls.entire_library.append(new_book)
        cls.on_shelf.append(new_book)
        print(new_book)
        return new_book

    @classmethod
    def current_due_date(cls):
        today = datetime.combine(date.today(), datetime.min.time()) #Today's date at midnight, 2019-07-21 00:00:00.
        two_weeks = 60 * 60 * 24 * 15 - 1 # Fifteen days (minus 1 second), expressed in seconds.
        future_timestamp = today.timestamp() + two_weeks #Two weeks from today, at 11.59:59pm, expressed in seconds.
        return datetime.fromtimestamp(future_timestamp) #Converts the future_timestamp to 2019-08-04 23:59:59

    @classmethod
    def overdue_books(cls):
        overdue_list = []
        
        for book in cls.on_loan: #Iterates through each book in the on_loan list.
            if (book.due_date < datetime.now()): #If current book's due_date happened before this moment.
                print('THAT\'S OVERDUEE!')
                overdue_list.append(book)
        return overdue_list

    @classmethod
    def browse(cls): #Returns a random book from the on_shelf list.
        return random.choice(cls.on_shelf)

    @classmethod
    def search_books(cls, user_input, trait):
        print(f'Looking for {trait} - {user_input}:')

        if trait == 'Author':
            for book in cls.entire_library:
                if book.author.find(user_input) >= 0:
                    print(book)
        elif trait == 'ISBN':
            for book in cls.entire_library:
                if book.ISBN.find(user_input) >= 0:
                    print(book)
        elif trait == 'Genre':
            for book in cls.entire_library:
                if book.genre == user_input:
                    print(book)
        else:
            for book in cls.entire_library:
                if book.title.find(user_input) >= 0:
                    print(book)
        print()