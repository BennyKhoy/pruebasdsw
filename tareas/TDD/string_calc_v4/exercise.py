def add(numbers: str) -> int:
    if numbers == "":
        return 0
    numbers = numbers.replace("\n", ",")
    if numbers.endswith(","):
        raise ValueError("Number expected but EOF found")
    parts = numbers.split(",")
    return sum(int(p) for p in parts)
