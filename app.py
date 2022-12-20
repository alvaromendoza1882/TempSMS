import os
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

#Define colors
R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'   # white
Y = '\033[33m'  # yellow

#Create a function to clear the screen
def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')
    
#Clear the screen
clear()
print("\n──────────────────────────────────────────────")
print(f'{G}>> {C}Select your Country{W}')
print("──────────────────────────────────────────────")

#Make a request to the website
response = requests.get("https://smstome.com/")

#Parse the HTML of the website
soup = BeautifulSoup(response.text, "html.parser")

#Find all links with the word "country" in the href
links = soup.find_all("a", href=lambda x: "country" in x)

#Create empty lists to store the text and href values
texts = []
hrefs = []

#Iterate over the links
for link in links:
  #Extract the text and href values
  text = link.text
  href = link["href"]
  
  #Append the text and href values to the lists
  texts.append(text)
  hrefs.append("https://smstome.com" + href)

#Print the menu of options
for i, text in enumerate(texts):
  A1 = f"{i+1:02d}"  # Add a leading zero if the option number is below 10
  print(f"[{A1}] {text}")

#Ask the user to select an option
print("──────────────────────────────────────────────")
option = int(input("Enter a menu option: "))

#Print the selected option and its href value
text = texts[option - 1]
href = hrefs[option - 1]
print(f"You selected: {text} ({href})")

#Clear the screen
clear()
print("\n──────────────────────────────────────────────")
print(f'{G}>> {C}Select your Number{W}')
print("──────────────────────────────────────────────")

#Make a request to the selected href
response = requests.get(f"{href}")

#Parse the HTML of the website
soup = BeautifulSoup(response.text, "html.parser")

#Find all elements with the class "numbutton"
numbuttons = soup.find_all(class_="button button-outline button-small numbutton")

#Create a list to store the numbers and hrefs
numbers_and_hrefs = []

#Iterate over the numbuttons and extract the number and href
for button in numbuttons:
    number = button.text
    href = button['href']
    numbers_and_hrefs.append((number, href))

#Print the menu options
for i, (number, href) in enumerate(numbers_and_hrefs):
    option_number = f"{i+1:02d}"  # Add a leading zero if the option number is below 10
    print(f"[{option_number}] {number}")

print("──────────────────────────────────────────────")
#Ask the user to select a menu option
selected_option = input("Enter a menu option: ")

#Get the selected number and href based on the user's input
selected_number, selected_href = numbers_and_hrefs[int(selected_option)-1]

#Print the selected menu option and its href
print(f"You selected: [{selected_option}] {selected_number} ({selected_href})")

#Clear the screen
clear()
print(f'\n{R}>> Selected number: {C}{selected_number}{W}')
print("──────────────────────────────────────────────")
print("──────────────────────────────────────────────\n")

#Make a request to the website
response = requests.get(selected_href)

#Parse the HTML of the website
soup = BeautifulSoup(response.text, "html.parser")

#Find the table element
table = soup.find('table')

#Find all rows in the table
rows = table.find_all('tr')

#Extract the header row and data rows from the table
header_row = rows[0]
data_rows = rows[1:]

#Extract the header cells from the header row
header_cells = header_row.find_all('th')
headers = [cell.text for cell in header_cells]

#Extract the data cells from the data rows
data = []
for row in data_rows[:10]:  # Only get the first 10 rows
    cells = row.find_all('td')
    row_data = [cell.text for cell in cells]
    data.append(row_data)

#Print the table using tabulate
print(tabulate(data, headers, tablefmt="grid"))
