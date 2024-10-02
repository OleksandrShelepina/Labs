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
    "пара1": type(main_dict["пара1"]),
    "пара2": type(main_dict["пара2"]),
    "пара3": {key: type(value) for key, value in main_dict["пара3"].items()},
    "пара4": type(main_dict["пара4"])
}

print("Основний словник:", main_dict)
print("Словник типів даних:", types_dict)
