import requests
import re
import os
import csv
import unittest
from bs4 import BeautifulSoup


def get_titles_from_search_results(filename):
    """
    Write a function that creates a BeautifulSoup object on "search_results.htm". Parse
    through the object and return a list of tuples containing book titles (as printed on the Goodreads website) 
    and authors in the format given below. Make sure to strip() any newlines from the book titles and author names.

    [('Book title 1', 'Author 1'), ('Book title 2', 'Author 2')...]
    """

    with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), filename), 'r') as f:
        file = f.read()
        title_list =[]
        author_list = []
        titles_and_authors = []

        soup = BeautifulSoup(file, 'lxml')

        titles = soup.find_all('a', class_ = 'bookTitle')
        authors = soup.find_all('div', class_ = 'authorName__container')

        for t in titles:
            info = t.text.strip()
            title_list.append(info)


        for a in author:
            info = a.text.strip()
            author_list.append(info)

        for i in book_info:
            tup = (book_info[i], author_info[i])
            titles_and_authors.append(tup)
        
        return titles_and_authors

        




def get_search_links():
    
    url = 'https://www.goodreads.com/search?q=fantasy&qid=NwUsLiA2Nc'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    tags = soup.find_all('href', class_ = 'bookTitle')
    book_urls = []
    for i in tags:
        if 'https://www.goodreads.com/book/show/' in i:
            book_urls.append(i)

    return book_urls

    


def get_book_summary(book_url):
    """
    Write a function that creates a BeautifulSoup object that extracts book
    information from a book's webpage, given the URL of the book. Parse through
    the BeautifulSoup object, and capture the book title, book author, and number 
    of pages. This function should return a tuple in the following format:

    ('Some book title', 'the book's author', number of pages)

    HINT: Using BeautifulSoup's find() method may help you here.
    You can easily capture CSS selectors with your browser's inspector window.
    Make sure to strip() any newlines from the book title and number of pages.
    """

    pass


def summarize_best_books(filepath):
    """
    Write a function to get a list of categories, book title and URLs from the "BEST BOOKS OF 2020"
    page in "best_books_2020.htm". This function should create a BeautifulSoup object from a 
    filepath and return a list of (category, book title, URL) tuples.
    
    For example, if the best book in category "Fiction" is "The Testaments (The Handmaid's Tale, #2)", with URL
    https://www.goodreads.com/choiceawards/best-fiction-books-2020, then you should append 
    ("Fiction", "The Testaments (The Handmaid's Tale, #2)", "https://www.goodreads.com/choiceawards/best-fiction-books-2020") 
    to your list of tuples.
    """
    pass


def write_csv(data, filename):
    """
    Write a function that takes in a list of tuples (called data, i.e. the
    one that is returned by get_titles_from_search_results()), writes the data to a 
    csv file, and saves it to the passed filename.

    The first row of the csv should contain "Book Title" and "Author Name", and
    respectively as column headers. For each tuple in data, write a new
    row to the csv, placing each element of the tuple in the correct column.

    When you are done your CSV file should look like this:

    Book title,Author Name
    Book1,Author1
    Book2,Author2
    Book3,Author3
    ......

    This function should not return anything.
    """
    pass


def extra_credit(filepath):
    """
    EXTRA CREDIT

    Please see the instructions document for more information on how to complete this function.
    You do not have to write test cases for this function.
    """
    pass

class TestCases(unittest.TestCase):

    # call get_search_links() and save it to a static variable: search_urls
    search_urls = get_search_links()

    def test_get_titles_from_search_results(self):
        # call get_titles_from_search_results() on search_results.htm and save to a local variable
        title_test = get_titles_from_search_results('search_results.htm')

        # check that the number of titles extracted is correct (20 titles)
        self.assertEqual(len(title_test), 20)
        # check that the variable you saved after calling the function is a list
        self.assertEqual(type(title_test), list)
        # check that each item in the list is a tuple
        for i in title_test:
            self.assertEqual(type(i), tuple)
        # check that the first book and author tuple is correct (open search_results.htm and find it)
        self.assertEqual(title_test[0], ("Harry Potter and the Deathly Hallows (Harry Potter, #7)", "J.K. Rowling"))
        # check that the last title is correct (open search_results.htm and find it)
        self.assertEqual(title_test[19][0], 'Harry Potter: The Prequel (Harry Potter, #0.5')

    def test_get_search_links(self):
        # check that TestCases.search_urls is a list
        self.assertEqual(type(TestCases.search_urls), list)
        # check that the length of TestCases.search_urls is correct (10 URLs)
        self.assertEqual(len(TestCases.search_urls), 10)

        # check that each URL in the TestCases.search_urls is a string
        for i in TestCases.search_urls:
            self.assertEqual(type(i), str)
            self.assertEqual(i[0:32], 'https://goodreads.com/book/show/')
        # check that each URL contains the correct url for Goodreads.com followed by /book/show/


    def test_get_book_summary(self):
        # for each URL in TestCases.search_urls (should be a list of tuples)
        summaries = []
        for i in TestCases.search_urls:
            summaries.append(i)

        # check that the number of book summaries is correct (10)
        self.assertEqual(len(summaries), 10)
            # check that each item in the list is a tuple
        for tups in summaries:
            self.assertEqual(len(tups), 3)
            # check that each tuple has 3 elements
            for items in tup[0:2]:
                self.assertEqual(type(items), str)
            # check that the first two elements in the tuple are string
            self.assertEqual(type(tups[2]), int)
            # check that the third element in the tuple, i.e. pages is an int
        self.assertEqual(len(summaries[0][-1]), 337)
            # check that the first book in the search has 337 pages


    def test_summarize_best_books(self):
        # call summarize_best_books and save it to a variable
        test = summarize_best_books()
        # check that we have the right number of best books (20)
        self.assertEqual(len(test), 20)
            # assert each item in the list of best books is a tuple
        for i in test:
            self.assertEqual(type(i), tuple)
            # check that each tuple has a length of 3
            self.assertEqual(len(i), 3)
        self.assertEqual(test[0], ('Fiction', "The Midnight Library", 'https://www.goodreads.com/choiceawards/best-fiction-books-2020'))
        # check that the first tuple is made up of the following 3 strings: 'Fiction', "The Midnight Library", 'https://www.goodreads.com/choiceawards/best-fiction-books-2020'
        self.assertEqual(test[-1], ('Picture Books', 'Antiracist Baby', 'https://www.goodreads.com/choiceawards/best-picture-books-2020'))
        # check that the last tuple is made up of the following 3 strings: 'Picture Books', 'Antiracist Baby', 'https://www.goodreads.com/choiceawards/best-picture-books-2020'


    def test_write_csv(self):
        # call get_titles_from_search_results on search_results.htm and save the result to a variable
        titleResults = get_titles_from_search_results('search_results.htm')
        write_csv(titleResults, 'test.csv')
        csv_lines = csv.reader('test.csv')
        
        self.assertEqual(len(csv_lines), 21)
        self.assertEqual(csv_lines[0], 'Book title,Author Name')
        self.assertEqual(csv_lines[1], 'Harry Potter and the Deathly Hallows (Harry Potter, #7), J.K. Rowling')
        self.assertEqual(csv_lines[-1], 'Harry Potter: The Prequel (Harry Potter, #0.5), J.K. Rowling')
        # call write csv on the variable you saved and 'test.csv'

        # read in the csv that you wrote (create a variable csv_lines - a list containing all the lines in the csv you just wrote to above)


        # check that there are 21 lines in the csv

        # check that the header row is correct

        # check that the next row is 'Harry Potter and the Deathly Hallows (Harry Potter, #7)', 'J.K. Rowling'

        # check that the last row is 'Harry Potter: The Prequel (Harry Potter, #0.5)', 'J.K. Rowling'



if __name__ == '__main__':
    print(extra_credit("extra_credit.htm"))
    unittest.main(verbosity=2)



