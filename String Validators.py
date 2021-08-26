s="P12A"
newList = [[c.isalnum(), c.isalpha(), c.isdigit(), c.islower(), c.isupper()] for c in s]
rolated=(list(zip(*newList)))
for i in rolated:
    print(any(i))