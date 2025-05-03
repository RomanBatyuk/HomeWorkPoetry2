import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
    filename="logs/masks.log",
    filemode="w",
    encoding="utf-8",
)

masks_logger = logging.getLogger("masks")


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая принимает на вход номер карты ввиде числа и возвраащает маску "XXXX XX** **** XXXX" """
    masks_logger.info(f"Получение номера карты: {card_number}")
    # Проверяем что номер состоит из 16 цифр
    masks_logger.info("Проверка из 16 цифр состоит номер карты или нет")
    if len(card_number) != 16:
        masks_logger.error("Номер карты должен содержать 16 цифр")
        raise ValueError("Номер должен содержать 16 цифр")
    masks_logger.info("Результат работы функции get_mask_card_number получен")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(mask_account: str) -> str:
    """Функция, которая принимает на вход номер счета ввиде числа и возвраащает маску "**XXXX" """
    masks_logger.info(f"Получение номера счета: {mask_account}")
    # Проверяем что номер состоит из 20 цифр
    masks_logger.info("Проверка из 20 цифр состоит номер счета или нет")
    if len(mask_account) < 20:
        masks_logger.error("Номер счета должен содержать 20 цифр")
        raise ValueError("Номер должен содержать 20 цифр")
    masks_logger.info("Результат работы функции get_mask_account получен")
    return f"**{mask_account[-4:]}"
