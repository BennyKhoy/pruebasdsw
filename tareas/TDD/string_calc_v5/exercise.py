import re


def add(numbers: str) -> int:
    if numbers == "":
        return 0

    delimiter = ","
    raw_delimiter = ","
    is_custom_delimiter = False

    if numbers.startswith("//"):
        header, numbers = numbers.split("\n", 1)
        delimiter_match = re.match(r"^//(.+)$", header)

        raw_delimiter = delimiter_match.group(1)
        delimiter = re.escape(raw_delimiter)
        is_custom_delimiter = True

    if is_custom_delimiter and "," in numbers:
        pos = numbers.find(",")
        raise ValueError(f"'{raw_delimiter}' expected but ',' found at position {pos}.")

    numbers = numbers.replace("\n", ",")
    if numbers.endswith(","):
        raise ValueError("Number expected but EOF found")

    parts = re.split(delimiter + "|,", numbers)
    return sum(int(p) for p in parts)
