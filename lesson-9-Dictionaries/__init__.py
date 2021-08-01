phonebok = {}
phonebok['a'] = '1234'
phonebok['b'] = 'aas'
phonebok['b'] = '213'

# del phonebok['a']
# phonebok.popitem()

phonebok.pop('a')
print(phonebok)

for name, a in phonebok.items():
    print(name + a)


phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781,
}

phonebook['Jake'] = 938273443

phonebook.pop('Jill')

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")

if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")