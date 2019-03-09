#spytac o nazwe pliku
filename = input ("Jaka jest nazwa? ")
text = input ("wprowadz text ")

with open (filename, 'w') as f:
    f.write(text + '\n')


#zmiana na masterze



