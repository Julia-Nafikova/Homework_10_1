def filter_by_state(list_dict: list[dict], state = "EXECUTED") -> list[dict]:
    """ Функция которая отбирает словари из списка по указанному значению"""
    new_list_dict_state = []
    for dictionary in list_dict:
        if dictionary['state'] == state:
            new_list_dict_state.append(dictionary)
    return new_list_dict_state

def sort_by_date(list_dict: list[dict], date = True) -> list[dict]:
    """ Функция которая сортирует словари из списка по дате"""
    new_list_dict_date = sorted(list_dict, key=lambda x: x['date'], reverse=date)
    return new_list_dict_date
