card_number = input("Write card numbers: ")
card_number_hidden = ""
for i in card_number[:-4]:
    card_number_hidden += "*"
print(card_number_hidden + card_number[-4:])