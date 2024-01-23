# Step 1: Define the list of books
books = [
    {"title": "Harry Potter and the Deathly Hallows", "pages": 640},
    {"title": "Rich Dad Poor Dad", "pages": 336},
    {"title": "The Great Gatsby", "pages": 160},
    {"title": "The Hobbit", "pages": 400}
]

# Step 2: Create a custom function
def has_many_pages(book, min_pages=350):
    """Check if the book has more than min_pages."""
    return book["pages"] > min_pages

# Step 3: Use filter() with the custom function
filtered_books = filter(lambda book: has_many_pages(book), books)

# Convert the filter object to a list and print
filtered_books_list = list(filtered_books)
print(filtered_books_list)


#фунція в фунуції
def count_percent(num1, num2, num3):
	def inner(num):
		return num * 30 / 100
	return (inner(num1), inner(num2), inner(num3))

print(count_percent(700, 300, 1000))