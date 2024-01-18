def hide_a_card_number():
    card_number = input("Write card numbers: ")
    card_number_hidden = ""
    for i in card_number[:-4]:
        card_number_hidden += "*"
    print(card_number_hidden + card_number[-4:])

def ask_for_card_change():
    changecard = input("do you want to change the card number ? [yes] or [no]")
    if changecard == "yes":
        hide_a_card_number()
    else:
        return

hide_a_card_number()
ask_for_card_change()

print("thanks for using my code")
