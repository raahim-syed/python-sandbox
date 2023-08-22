monthConversions = {
    "Jan" : "January",
    "Feb" : "Feburary",
    "Sept" : "September"
}

print(monthConversions.get("123", "Not a valid key"))
print(monthConversions["Sept"])
print(monthConversions.keys())
print(monthConversions.items())


for month in monthConversions:
    print(month)