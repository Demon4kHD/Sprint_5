import random as rndm
import data

def create_valid_email_and_password(length_of_password):
    user_data = []
    user_data.append(str(rndm.choice(data.users_name)))

    new_random_number = ''
    for _ in range(3):
        random_number = str(rndm.randint(0, 9))
        new_random_number += random_number
    if user_data[0] == 'Kseniya':
        user_email = user_data[0].lower() + 'Luscheva99' + new_random_number + data.users_domain
    else:
        user_email = user_data[0].lower() + data.users_login + new_random_number + data.users_domain

    user_data.append(user_email)

    user_password = ''
    if length_of_password == "None":
        user_data.append("None")
    elif length_of_password == 1:
        user_data.append(str(rndm.choice(data.symbols_for_password)))
    else:
        for _ in range(length_of_password):
            random_symbol = str(rndm.choice(data.symbols_for_password))
            user_password += random_symbol
        user_data.append(user_password)

    return user_data