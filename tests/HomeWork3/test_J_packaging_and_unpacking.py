import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork3.J_packaging_and_unpacking import Solver


@pytest.mark.parametrize(
    ("string", "encoded"),
    [
        param(
            "abacabaca",
            [0, "a", 0, "b", 1, "c", 1, "b", 3, "a"]
        ),
        param(
            "abacabacaabaac",
            [0, "a", 0, "b", 1, "c", 1, "b", 3, "a", 4, "a", 3],
        ),
    ],
)
def test_encode_lzw(string, encoded):
    assert Solver.encode_lzw(string) == encoded


@pytest.mark.parametrize(
    ("encoded", "bits"),
    [
        param(
            [0, "a", 0, "b", 1, "c", 1, "b", 3, "a"],
            "".join(["0", "00000", "0", "00001", "01", "00010", "01", "00001", "011", "00000"]),
        ),
        param(
            [0, "a", 0, "b", 1, "c", 1, "b", 3, "a", 4, "a", 3],
            "".join(["0", "00000", "0", "00001", "01", "00010", "01", "00001", "011", "00000", "100", "00000", "011"]),
        ),
    ],
)
def test_encoded_to_bits(encoded, bits):
    assert Solver.encoded_to_bits(encoded) == bits


@pytest.mark.parametrize(
    ("bits", "bytes"),
    [
        param(
            "00000000000110001001000011100000",
            ["00000000", "00011000", "10010000", "11100000", "10000000"],
        ),
        param(
            "0000000000011000100100001110000010000000011",
            ["00000000", "00011000", "10010000", "11100000", "10000000", "01110000"],
        ),
    ],
)
def test_bits_to_bytes(bits, bytes):
    assert Solver.bits_to_bytes(bits) == bytes


@pytest.mark.parametrize(
    ("bytes", "nums"),
    [
        param(
            ["00000000", "00011000", "10010000", "11100000"],
            [0, 24, 144, 224],
        ),
        param(
            ["00000000", "00011000", "10010000", "11100000", "10000000", "011"],
            [0, 24, 144, 224, 128, 3],
        ),
    ],
)
def test_bytes_to_nums(bytes, nums):
    assert Solver.bytes_to_nums(bytes) == nums


@pytest.mark.parametrize(
    ("bytes",),
    [
        param(["00000000", "00011000", "10010000", "11100000", "10000000"]),
        param(["00000000", "00011000", "10010000", "11100000", "10000000", "01110000"]),
    ],
)
def test_nums_to_bytes(bytes):
    nums = Solver.bytes_to_nums(bytes)
    assert Solver.nums_to_bytes(nums) == bytes


@pytest.mark.parametrize(
    ("string",),
    [
        param("abacabaca", id="example1"),
        param("abacabacaabaac", id="custom1"),
    ],
)
def test_solve(string):
    solver1 = Solver.from_strings(["pack", string])
    result1 = solver1.solve()

    solver2 = Solver.from_strings(["unpack", *result1.split("\n")])
    result2 = solver2.solve()

    assert result2 == string
