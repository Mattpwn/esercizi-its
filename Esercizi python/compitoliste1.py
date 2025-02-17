
alphabet = ["a", "b", "c", "d", "e"]

first_letter = alphabet[0]

last_letter = alphabet[-1]

first_three = alphabet[:3]

last_three = alphabet[2:]

# alphabet.append("f")
# alphabet.append("g")
# alphabet.append("h")

alphabet.extend(["f", "g", "h"])   # vanno bene  entrambi i modi

last_three = alphabet[-3:]

alphabet.remove("h")

print(alphabet)
print(first_letter)
print(first_three)
print(last_letter)
print(last_three)