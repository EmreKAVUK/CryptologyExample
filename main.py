file = open("sifreli.txt","r")
text = file.read()

chars = dict()

for char in text:
    try:
        chars[char]
    except KeyError:
        chars[char] = 1
    else:
        chars[char] += 1

for char, n in chars.items():
    print(f"{repr(char)} karakteri metinde {n} kere tekrar eder.")