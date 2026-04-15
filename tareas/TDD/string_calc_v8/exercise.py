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

    numbers_normalized = numbers.replace("\n", ",")
    if numbers_normalized.endswith(","):
        raise ValueError("Number expected but EOF found")

    parts = re.split(delimiter + "|,", numbers_normalized)
    values = [int(p) for p in parts]

    errors = []

    negatives = [v for v in values if v < 0]
    if negatives:
        errors.append(
            "Negative number(s) not allowed: " + ", ".join(str(n) for n in negatives)
        )

    if raw_delimiter and "," in numbers:
        errors.append(
            f"'{raw_delimiter}' expected but ',' found at position {numbers.find(',')}."
        )
    elif not raw_delimiter:
        wrong_sep = re.search(r"(\d)(,\n|\n,)(\d)", numbers)
        if wrong_sep:
            errors.append(
                "',' expected but '\\n' found at position " + str(wrong_sep.start() + 1)
            )

    if errors:
        raise ValueError("\n".join(errors))

    return sum(v for v in values if v <= 1000)
