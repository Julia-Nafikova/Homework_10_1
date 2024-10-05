def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """Функция которая отбирает словари из списка по указанному значению"""
    new_list = []
    for key in list_dict:
        if key.get("state") == state:
            new_list.append(key)

    return new_list


def sort_by_date(list_dict: list, is_descending: bool = True) -> list:
    """Функция которая сортирует словари из списка по дате"""
    return sorted(list_dict, key=lambda x: x.get("date"), reverse=is_descending)
