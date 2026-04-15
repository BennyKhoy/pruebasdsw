def add(numbers: str) -> int:
    if numbers == "":
        return 0
    numbers = numbers.replace("\n", ",")
    parts = numbers.split(",")
    return sum(int(p) for p in parts)
