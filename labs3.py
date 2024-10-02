main_dict = {
    "пара1": 42,
    "пара2": "привіт",
    "пара3": {
        "ключ1": 1,
        "ключ2": "два",
        "ключ3": True,
        "ключ4": 3.14,
        "ключ5": None
    },
    "пара4": [1, 2, 3]
}

types_dict = {
    key: type(value) if not isinstance(value, dict) else {k: type(v) for k, v in value.items()}
    for key, value in main_dict.items()
}

print("Основний словник:", main_dict)
print("Словник типів даних:", types_dict)
