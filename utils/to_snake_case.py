def to_snake_case(string: str) -> str:
    """
    Преобразует строку из CamelCase в snake_case.

    :param string: Входная строка в формате CamelCase.
    :return: Строка преобразованная в формате snake_case.
    """

    return ''.join(
        [
            '_' + char.lower() if char.isupper()
            else char
            for char in string
        ]
    ).strip('_')
