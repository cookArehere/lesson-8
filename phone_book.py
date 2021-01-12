def search_name(name, order):
    """
    находит словарь в спистке словарей по ключу name
    :param name: значение ключа name
    :param order: список словарй
    :return: список словарей
    """
    roll = [i for i in order if i["name"].lower().strip() == name or name in i["name"].lower().strip()]
    return roll


def search_state(state, order):
    """
    находит словарь в спистке словарей по ключу state
    :param state: значение ключа state
    :param order: список словарй
    :return: список словарей
    """
    roll = [i for i in order if i["state"].lower().strip() == state or state in i["state"].lower().strip()]
    return roll


def search_phone(phone, order):
    """
    находит словарь в спистке словарей по ключу phone
    :param phone: значение ключа phone
    :param order: список словарй
    :return: список словарей
    """
    roll = [i for i in order if i["phone"].lower().strip() == phone or phone in i["phone"].lower().strip()]
    return roll


def change_name(new_name, contact_act):
    """

    :param new_name:
    :param contact_act:
    :return:
    """
    change_name = contact_act[0]["name"] = new_name
    return change_name


def change_state(new_state, contact_act):
    """

    :param new_state:
    :param contact_act:
    :return:
    """
    change_state = contact_act[0]["state"] = new_state
    return change_state


def change_phone(new_phone, contact_act):
    """

    :param new_phone:
    :param contact_act:
    :return:
    """
    change_phone = contact_act[0]["state"] = new_phone
    return change_phone


def remove_contact(contact, contact_order):
    """

    :param contact:
    :param phone_book:
    :return:
    """
    new_contact_order = contact_order
    for i in new_contact_order:
        if i.items() == contact.items():
            new_contact_order.remove(i)
    return new_contact_order


def formatting_user_input(user_input):
    formatting_user_input = user_input.title().strip()
    return formatting_user_input


def checking_same_contact_name(name, phone_book):
    """

    :param name:
    :param phone_book:
    :return:
    """

    while True:
        order_name = []
        for i in phone_book:
            if i["name"] == name:
                order_name.append(i["name"])
        if len(order_name) > 0:
            name = formatting_user_input(input("This name already exists\n Choice new name:"))
            continue
        break
    return name


if __name__ == '__main__':

    """
    Add new entries 
Search by first name  
Search by full name
Search by telephone number
Search by city or state
Delete a record for a given telephone number
Update a record for a given telephone number
    """

    contact_1 = {"name": "Pavel",
                 "state": "Odesska obl",
                 "phone": "+380669846559"}

    contact_2 = {"name": "Oleg",
                 "state": "Odesska obl",
                 "phone": "+38066981865"}

    phone_book = [contact_1, contact_2]
    contact_act = []

    start = input("What do you want?\n"
                  "Add new contact, press - ad.\n"
                  "Search by name, press - sn.\n"
                  "Search by state, press - ss.\n"
                  "Search by telephone number, press - sph.\n"
                  "Type your choice:")

    user = start.lower().strip()

    if user == "ad":
        phone_book.append({"name": checking_same_contact_name(formatting_user_input(input("Name:")), phone_book),
                           "state": formatting_user_input(input("State:")),
                           "phone": formatting_user_input(input("Phone:"))})
    elif user == "sn":
        name = input("Type contact name:").lower().strip()
        contact_act = search_name(name, phone_book)
    elif user == "ss":
        state = input("Type contact state:").lower().strip()
        contact_act = search_state(state, phone_book)
    elif user == "sph":
        phone = input("Type contact phone:").lower().strip()
        contact_act = search_phone(phone, phone_book)

    if len(contact_act) > 1:
        print(contact_act)
        the_name = input("Choice contact what you need.\n Contact name:").lower().strip()
        contact_act = search_name(the_name, contact_act)
        print(contact_act)


    if user == "sn" or user == "ss" or user == "sph":

        action_selection = input("What do you want do with contact?\n"
                                 "Change name, press - chn.\n"
                                 "Change state, press - chs.\n"
                                 "Change phone, press - chp.\n"
                                 "Remove contact, press - rmc.\n"
                                 "Type your choice:")

        action_on_contact = action_selection.lower().strip()

        if action_on_contact == "chn":
            new_name = formatting_user_input(input("Type new name contact:"))
            change_name(new_name, contact_act)
        elif action_on_contact == "chs":
            new_state = formatting_user_input(input("Type new state contact:"))
            change_state(new_state, contact_act)
        elif action_on_contact == "chp":
            new_phone = formatting_user_input(input("Type new phone contact:"))
            change_phone(new_phone, contact_act)
        elif action_on_contact == "rmc":
            remove_contact(contact_act[0], phone_book)

    print(phone_book)
