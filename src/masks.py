def get_mask_card_number(card_number: str) -> str | None:
    """Accepts the card number at the entrance and return its mask"""
    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}{'*' * 2} {'*' * 4} {card_number[12:]}"
    else:
        return "Ошибка ввода"


def get_mask_account(acc_number: str) -> str | None:
    """Accepts the account number at the entrance and return its mask"""
    if acc_number.isdigit() and len(acc_number) == 20:
        return f"{'*' * 2}{acc_number[-4::]}"
    else:
        return "Ошибка ввода"
