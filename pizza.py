import sys
import csv
from tabulate import tabulate

def line_arguments(arguments):
    if len(arguments) < 2:
        sys.exit("Too few command-line arguments")
    if len(arguments) > 2:
        sys.exit("Too many command-line arguments")
    
    if arguments[1].split(".")[1] != "csv":
        sys.exit("Not a csv file")

    try:
        open(arguments[1], "r")
    except:
        sys.exit("File does not exist")

    return arguments[1]  

try:
    with open(sys.argv[1], "r") as file:
        reader = csv.reader(file)
        header = next(reader)
except FileNotFoundError:
    sys.exit("File does not exist")

# Check if file  is correct  format
if header != ["Sicilian Pizza", "Small", "Large"]:
    sys.exit("isn't correct format")

# Read file and print formatted table
with open(sys.argv[1], "r") as file:
    reader = csv.reader(file)
    next(reader) # skip header
    rows = [[item.strip() for item in row] for row in reader]
    print(tabulate(rows, headers=["Sicilian Pizza", "Small", "Large"], tablefmt="grid"))