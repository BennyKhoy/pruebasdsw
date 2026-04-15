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
    if is_custom_delimiter and "," in numbers:
        pos = numbers.find(",")
        errors.append(f"'{raw_delimiter}' expected but ',' found at position {pos}.")

    if not is_custom_delimiter:
        wrong_sep = re.search(r"(\d)(,\n|\n,)(\d)", numbers)
        if wrong_sep:
            errors.append(
                "',' expected but '\\n' found at position " + str(wrong_sep.start() + 1)
            )

    if errors:
        raise ValueError("\n".join(errors))

    return sum(values)
