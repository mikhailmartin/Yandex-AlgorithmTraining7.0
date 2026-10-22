import sys


def main(lines: list[str] | None = None) -> str:

    lines = lines or sys.stdin.read().splitlines()

    command = lines[0]
    if command == "pack":
        string = lines[1]
    else:
        n = lines[1]
        string = lines[2]

    if command == "pack":
        return pack(string)
    else:
        return unpack(string)


def pack(string: str) -> str:

    encoded = encode_lzw(string)
    bits = encoded_to_bits(encoded)
    bytes = bits_to_bytes(bits)
    nums = bytes_to_nums(bytes)

    n = len(nums)
    return f"{n}\n{' '.join(map(str, nums))}"


def encode_lzw(string: str) -> list[int | str]:

    res = []
    vocab = {"": 0}
    count = 1
    left = 0
    for right, char in enumerate(string):
        curr_word = string[left:right + 1]
        if curr_word not in vocab:
            prev_word = string[left:right]
            res.append(vocab[prev_word])
            res.append(char)
            vocab[curr_word] = count
            count += 1
            left = right + 1

    if left != right + 1:
        word = string[left:]
        res.append(vocab[word])

    return res


def encoded_to_bits(encoded: list[int | str]) -> str:

    bits_on_char = 5
    bits_on_num = 1
    count = 1

    res = []
    for elem in encoded:
        if isinstance(elem, int):
            num = elem
            bits = bin(num)[2:].zfill(bits_on_num)
            res.append(bits)
        else:
            char = elem
            bits = bin(ord(char) - ord("a"))[2:].zfill(bits_on_char)
            res.append(bits)

            count += 1
            while count > (1 << bits_on_num):
                bits_on_num += 1

    return "".join(res)


def bits_to_bytes(bits: str) -> list[str]:
    bits += "1"
    padding = (8 - len(bits) % 8) % 8
    bits += "0" * padding
    return [bits[i:i+8] for i in range(0, len(bits), 8)]


def bytes_to_nums(bytes: list[str]) -> list[int]:
    return [int(byte, 2) for byte in bytes]


def unpack(string: str) -> str:

    nums = list(map(int, string.split()))
    bytes = nums_to_bytes(nums)
    bits = bytes_to_bits(bytes)
    encoded = bits_to_encoded(bits)
    result = encoded_to_result(encoded)

    return result


def nums_to_bytes(nums: list[int]) -> list[str]:
    return [bin(num)[2:].zfill(8) for num in nums]


def bytes_to_bits(bytes: list[str]) -> str:
    bits = "".join(bytes)
    last_one = bits.rfind("1")
    return bits[:last_one]


def bits_to_encoded(bits: str) -> list[int | str]:

    n = len(bits)

    bits_on_char = 5
    bits_on_num = 1
    count = 1

    res = []
    i = 0
    while i < n:
        num = int(bits[i:i + bits_on_num], 2)
        res.append(num)
        i += bits_on_num

        if i >= n:  # хвостовой индекс без символа
            break

        char = chr(int(bits[i:i + bits_on_char], 2) + ord("a"))
        res.append(char)
        i += bits_on_char

        count += 1
        while count > (1 << bits_on_num):
            bits_on_num += 1

    return res


def encoded_to_result(encoded: list[int | str]) -> str:

    res = []
    vocab = {0: ""}
    count = 1
    prev = encoded[0]
    for elem in encoded:
        if isinstance(elem, int):
            num = elem
            word = vocab[num]
            res.append(word)
            prev = word
        else:
            char = elem
            res.append(char)

            vocab[count] = f"{prev}{char}"
            count += 1

    return "".join(res)


if __name__ == "__main__":
    result = main()
    print(result)
