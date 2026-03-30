gadgets = ["mobile", "laptop", 100, "camara", 310.28, "speckers",
           27.00, "television", 1000, "laptop case", "camera lens"]
strings = [item for item in gadgets if isinstance(item, str)]
numbers = [item for item in gadgets if isinstance(item, (int, float))]
print("Strings list:", strings)
print("Numbers list:", numbers)
