import random as rndm
import data

def create_valid_email_and_password(length_of_password):
    user_data = []
    user_data.append(str(rndm.choice(data.users_name)))

    new_random_number = ''

    for _ in range(3):

        random_number = str(rndm.randint(0, 9))
        new_random_number += random_number
    user_email = user_data[0].lower() + data.user_soname[data.users_name.index(
        user_data[0])].lower() + data.users_kagorta + new_random_number + data.users_domain

    user_data.append(user_email)

    user_password = ''
    upper_or_lowercase = [True, False]
    register = rndm.choice(upper_or_lowercase)
    for _ in range(length_of_password):
        register = rndm.choice(upper_or_lowercase)
        random_symbol = str(rndm.choice(data.symbols_for_password))
        if register == True:
            user_password += random_symbol.upper()
        else:
            user_password += random_symbol.lower()
    user_data.append(user_password)

    return user_data
