def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """Функция которая отбирает словари из списка по указанному значению"""
    filtered_list = []
    for dictionary in list_dict:
        if dictionary["state"] == state:
            filtered_list.append(dictionary)
    return filtered_list


def sort_by_date(list_dict: list, is_descending: bool = True) -> list:
    """Функция которая сортирует словари из списка по дате"""
    sorted_list = sorted(list_dict, key=lambda x: x["date"], reverse=is_descending)
    return sorted_list
