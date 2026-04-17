'''                              Library management system

The library class is responsible for storing and managing details about the books in the library.
This class is responsible for show books in library, searching for books, and handling the borrowing and returning of books.
'''

class library:
    library_no = set()

    def __init__(self,libno): 
        self.libno = libno
        self.library_booklist={"novel":5 , "story":10 , "poem":5}
        if self.libno not in library.library_no:
             library.library_no.add(self.libno)


    # Display a list of all available books and quantity in the library.
    def Display(self):
        for self.bookname,self.library_booklist[self.bookname] in self.library_booklist.items():
            print(f"{self.bookname}:{self.library_booklist[self.bookname]}")
    

    # Check book availability based on their title.
    def Check_Bookavailability(self,bookname):
        self.bookname=bookname
        if bookname in self.library_booklist and self.library_booklist[bookname] >0:
            print(f"{self.bookname} is available")
        else:
            print("Book not available")

    # Users can borrow a book if it's available.
    def Barrow_book(self,bookname):
        self.bookname=bookname

        if bookname in self.library_booklist and self.library_booklist[bookname] >0:
            self.library_booklist[bookname]-=1
            print(f"{self.bookname} is barrow succesfully")
            print(f"Now the available Collection of {self.bookname} :",self.library_booklist[bookname] )

        else:
            print(f"{self.bookname} not available in library")

    # Users can be returned barrow book to the library.
    def Return_book (self,bookname):
        if  bookname in self.library_booklist:
            self.library_booklist[bookname]+=1
            print("Thank you for returning")

            
if __name__== "__main__":
     # Create a library object with ID 123
    s=library(123)
    
    # Display current library status
    s.Display()
    
    # Check if the book "poem" is available
    s.Check_Bookavailability("poem")

    # Borrow the book "poem"
    s.Barrow_book("poem")

    # Display updated library status
    s.Display()

    # Return the book "poem"
    s.Return_book("poem")
    
    
