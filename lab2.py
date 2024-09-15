a = 10
b = "Hello"
c = 3.14
d = [1, 2, 3]
e = {'key': 'value'}
values = [a, b, c, d, e]
types = [type(value) for value in values]
from collections import Counter
type_counts = Counter(types)
most_common_type = type_counts.most_common(1)[0][0]
print(f"Найчастіший тип даних: {most_common_type}")
