import sys


def main(lines: list[str] | None = None) -> str:

    lines = lines or sys.stdin.read().splitlines()

    num = lines[0].strip()
    x = lines[1].strip()

    if num == "1":
        return encode(x)
    else:
        return decode(x)


def encode(x: str) -> str:

    n = len(x)

    parity_bit_count = 0
    while (1 << parity_bit_count) < n + parity_bit_count + 1:
        parity_bit_count += 1

    m = n + parity_bit_count
    res = [0] * m

    # расставляем информационные биты
    x_idx = 0
    for pos in range(1, m + 1):
        if (pos & (pos - 1)) == 0:
            continue
        res[pos-1] = 1 if x[x_idx] == "1" else 0
        x_idx += 1

    # расставляем контрольные биты
    for k in range(parity_bit_count):
        p = 1 << k
        parity = 0
        step = p << 1
        for start in range(p, m + 1, step):
            end = min(start + p, m + 1)
            for pos in range(start, end):
                parity ^= res[pos-1]
        res[p-1] = parity

    return "".join("1" if bit else "0" for bit in res)


def decode(z: str) -> str:

    m = len(z)

    r = 0
    while (1 << r) < m + 1:
        r += 1

    bits = [1 if char == "1" else 0 for char in z]

    # Ищем позицию ошибки
    error_pos = 0
    for k in range(r):
        p = 1 << k
        parity = 0
        step = p << 1
        for start in range(p, m + 1, step):
            end = min(start + p, m + 1)
            for pos in range(start, end):
                parity ^= bits[pos-1]
        if parity != 0:
            error_pos += p

    if error_pos > 0:
        bits[error_pos - 1] ^= 1

    res = []
    for pos in range(1, m + 1):
        if (pos & (pos - 1)) != 0:
            res.append("1" if bits[pos - 1] else "0")

    return "".join(res)


if __name__ == "__main__":
    result = main()
    print(result)
