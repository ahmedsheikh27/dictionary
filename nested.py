person = {
    "Name": "John",
    "Age": 30,
    "Address": {
        "Street": "123 Elm St",
        "City": "Boston",
        "Phone":"123-456-7890"
    }
}
person.pop('Address')
for key in person:
    print(key)
print(person)