alphabet = [
    "a", "b", "c", "d", "e", "f", "g",
    "h", "i", "j", "k", "l", "m", "n",
    "o", "p", "q", "r", "s", "t", "u",
    "v", "w", "x", "y", "z"
]
code = True
while code == True:
    print("Welcome do my ceaser cipher mechanism!!!")
    answer1 = str(input("Do tou want to encode ou decode?\n"))
    if answer1 == "encode":
        def encode(word):
            result = ""
            valor = int(input("What is the quantity of number you want to jump?(1...26)\n"))
            for letter in word:
                    if letter in alphabet:
                        position = alphabet.index(letter)
                        new_index = (position + valor) % 26
                        new_letter = alphabet[new_index]
                        result += new_letter
                    if letter == " ":
                            result+= " "
            print(f"Your encripted word is: {result}")


        encode(input(f"Write a word to encode:\n").lower())



    elif answer1 == "decode":
        def decode(word):
                result = ""
                valor = int(input("What is the value of the main key do decode your word?\n"))
                for letter in word:
                        if letter in alphabet:
                            position = alphabet.index(letter)
                            new_index = (position - valor) % 26
                            new_letter = alphabet[new_index]
                            result += new_letter
                        elif letter == " ":
                            result += " "
                print(f"Your decripted word is: {result}")

        decode(input("Write a word to decode\n"))
    else:
        print("Wrong answer, plese answer again\n")
        answer1 = str(input("Do tou want to encode ou decode?\n").lower())

    repeat = str(input("Do you want to use our ceaser cipher mechanism again?(yer/no)\n").lower())
    if repeat == "yes":
        code = True
    elif repeat == "no":
        print("End of the mechanism")
        code = False