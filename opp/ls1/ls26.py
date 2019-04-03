class Book:
    def __init__(self, title, publisher, pages):
        self.title = title
        self.publisher = publisher
        self.pages = pages
# class Ebook (book):
#     def__init__ (self, title, publisher, pages, format_):
#         self.title = title
#         self.publisher = publisher
#         self.pages = pages
#         self.format = format_

class Ebook(Book):
    def __init__ (self, title, publisher, pages, format_):
        Book.__init__(self, title, publisher, pages)
        self.format_ = format_
ebook = Ebook(
    "Learn Python Programming", "Packt Publishing", 500, "PDF")
print(ebook.title)
print(ebook.publisher)
print(ebook.pages)
print(ebook.format_)

