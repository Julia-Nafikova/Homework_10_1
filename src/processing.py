def filter_by_state(list_dict: list[dict], state = "EXECUTED") -> list[dict]:
    """ Функция которая отбирает словари из списка по указанному значению"""
    filtered_list = []
    for dictionary in list_dict:
        if dictionary['state'] == state:
            filtered_list.append(dictionary)
    return filtered_list

def sort_by_date(list_dict: list[dict], is_descending = True) -> list[dict]:
    """ Функция которая сортирует словари из списка по дате"""
    sorted_list = sorted(list_dict, key=lambda x: x['date'], reverse=is_descending)
    return sorted_list
