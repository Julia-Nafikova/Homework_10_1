from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data_for_processing: str) -> str:
    """Data processing and number mask return"""
    number = ""
    name_card = ""
    if len(data_for_processing) > 0:
        for i in data_for_processing:
            if i.isdigit():
                number += i
            else:
                name_card += i

        if "Счет" in data_for_processing:
            return f"{name_card}{get_mask_account(number)}"
        else:
            return f"{name_card}{get_mask_card_number(number)}"
    return "Ошибка ввода"


def get_date(date: str) -> str:
    """Date format change"""
    if len(date) > 0:
        date_slice = date[0:10]
        date_list = date_slice.split("-")
        date_list_reverse = []
        date_list_reverse.extend([date_list[2], date_list[1], date_list[0]])
        date_change = ".".join(date_list_reverse)
        return date_change
    return "Ошибка ввода"
