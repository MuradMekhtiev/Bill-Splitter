import random

people = int(input("Enter the number of friends joining (including you):\n"))

dict_1 = {}
friends_list = []

if people < 1:
    print("No one is joining for the party")

else:
    print("Enter the name of every friend (including you), each on a new line:")

    for person in range(people):
        name = input("")
        friends_list.append(name)
        dict_1[name] = 0

    print("Enter the total bill value:")

    total_bill = int(input(""))

    print('Do you want to use the "Who is lucky? feature?" Write Yes/No:')
    luck_game = input("").lower()

    if luck_game == "yes":
        lucky_guy = random.choice(friends_list)
        print(f"{lucky_guy} is the lucky one!")

        # bpp(bill per person)
        bpp = round(total_bill / (people - 1), 2)

        for key, value in dict_1.items():
            if key == lucky_guy:
                continue
            else:
                dict_1[key] += bpp

    else:
        print("No one is going to be lucky")

        bpp = round(total_bill / people, 2)

        for key, value in dict_1.items():
            dict_1[key] += bpp

    print(dict_1)