# Library Management System
A Library Management System used for storing and managing details about the books in the library.It helps librarians searching, borrowing and returning of books available in the library. 

## Features
*  Display list of all available books in library
* Search book using name
* Issuing and returning books

## Project Structure
main.py: Contains the core library class logic.

## How to run?

1. **clone this repo:**
``` git clone https://github.com/Rohinibawake/Library_management```

2. **Navigate to the project folder:**
``` cd library_management/ ```

3. **Build docker image :**
``` docker build -t librarymanagement .```

4. **Run docker container**
``` docker run -it --name library librarymanagement ```


