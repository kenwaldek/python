

exdict = {'jack':15, 'bob':22, 'alice':12}

print(exdict)

print(exdict['jack'])
'''jack is de sleutel en 15 is de waarde'''

exdict['tim'] = 17
'''sleutel tim toevoegen met de waarde 17'''
print(exdict)

'''de waarde veranderen van tim'''
exdict['tim'] = 16
print(exdict)

'''
om een waarde uit dictonary te verwijderen
doen we onderstaande del funktie
'''
del exdict['tim']
print(exdict)

