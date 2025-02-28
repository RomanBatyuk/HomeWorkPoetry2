def get_mask_card_number(card_number: str) -> str:
    """Функция, которая принимает на вход номер карты ввиде числа и возвраащает маску "XXXX XX** **** XXXX" """

    # Проверяем что номер состоит из 16 цифр
    if len(card_number) < 16:
        raise ValueError("Номер должен содержать 16 цифр")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(mask_account: str) -> str:
    """Функция, которая принимает на вход номер счета ввиде числа и возвраащает маску "**XXXX" """

    # Проверяем что номер состоит из 20 цифр
    if len(mask_account) < 20:
        raise ValueError("Номер должен содержать 20 цифр")
    return f"**{mask_account[-4:]}"
