import re


def add(numbers: str) -> int:
    if numbers == "":
        return 0

    delimiter = ","
    raw_delimiter = None

    if numbers.startswith("//"):
        header, numbers = numbers.split("\n", 1)
        delimiter_match = re.match(r"^//(.+)$", header)
        raw_delimiter = delimiter_match.group(1)
        delimiter = re.escape(raw_delimiter)

    if raw_delimiter and "," in numbers:
        raise ValueError(
            f"'{raw_delimiter}' expected but ',' found at position {numbers.find(',')}."
        )

    numbers_normalized = numbers.replace("\n", ",")
    if numbers_normalized.endswith(","):
        raise ValueError("Number expected but EOF found")

    parts = re.split(delimiter + "|,", numbers_normalized)
    values = [int(p) for p in parts]

    negatives = [v for v in values if v < 0]
    if negatives:
        raise ValueError(
            "Negative number(s) not allowed: " + ", ".join(str(n) for n in negatives)
        )

    return sum(values)
