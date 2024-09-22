import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="../logs/file.log",
    filemode="w",
)

mc_logger = logging.getLogger("masks")
ma_logger = logging.getLogger("masks")

# logger = logging.getLogger('masks')
# file_handler = logging.FileHandler('../logs/file.log')
# file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
# file_handler.setFormatter(file_formatter)
# logger.addHandler(file_handler)
# logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str | None:
    """Accepts the card number at the entrance and return its mask"""
    try:
        mc_logger.info("Проверка входящего номера карты на соответствие длины и символам")
        if card_number.isdigit() and len(card_number) == 16:
            mc_logger.info("Получение замаскированного номера карты")
            return f"{card_number[:4]} {card_number[4:6]}{'*' * 2} {'*' * 4} {card_number[12:]}"
        else:
            mc_logger.warning("Ошибка ввода")
            return "Ошибка ввода"
    except Exception as ex:
        mc_logger.error(f"Произошла ошибка: {ex}")


# print(get_mask_card_number(''))


def get_mask_account(acc_number: str) -> str | None:
    """Accepts the account number at the entrance and return its mask"""
    try:
        ma_logger.info("Проверка входящего номера счета на соответствие длины и символам")
        if acc_number.isdigit() and len(acc_number) == 20:
            mc_logger.info("Получение замаскированного номера счета")
            return f"{'*' * 2}{acc_number[-4::]}"
        else:
            ma_logger.warning("Ошибка ввода")
            return "Ошибка ввода"
    except Exception as ex:
        ma_logger.error(f"Произошла ошибка: {ex}")


# print(get_mask_account('12345678901234567890'))
