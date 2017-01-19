from prettytable import PrettyTable

# Initialize the object passing the table headers
t = PrettyTable(['A', 'B', 'C'])

t.align='l'
t.border=False

t.add_row([111,222,333])
t.add_row([444,555,666])
t.add_row(['longer text',777,'even longer text here'])

print (str(t))