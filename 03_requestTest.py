# request the raw text of The Great Gatsby
# you will need to leverage the requests package
import requests
r = requests.get(r'https://gutenberg.org/cache/epub/75279/pg75279.txt')
great_gatsby = r.text

# first, remove unwanted new line and tab characters from the text
for char in ["\n", "\r", "\n", "\t"]:
    great_gatsby = great_gatsby.replace(char, " ")
    
# you can also subset for the book text
# (removing the project gutenburg introduction/footnotes)
great_gatsby = great_gatsby[1433:277912]
print(great_gatsby)