'''
Assume to have a text document in one string…

Check if the word “Book” is mentioned in the document, case-sensitive?
Check if the word “book” is mentioned in the document, case-insensitive?
Check if the document ends with “The end”, case-sensitive?
Check if the document is empty, that is, only contains white space if any?
'''

TEXT = "This is a text on a book. The end"

if "Book" in TEXT:
    print("The word 'Book' appears in the text")
else:
    print("The word 'Book' does not appear in the text")

if "book" in TEXT.lower():
    print("The word 'Book' appears in the text, case sensitive") #insensitive?
else:
    print("The word 'Book' does not appear in the text, case insensitive")

if TEXT.endswith("The end"):
    print("Text ends nicely")

if TEXT.isspace():
    print("The document is basically empty")
else:
    print("The document has text in it ...")




