#!/usr/bin/env python3

from bitpacking import bitpack, bitunpack

ints = [
    1, 2, 0, 0,
    3, 0, 0, 0,
    0, 0, 0, 0,
    4, 0, 0, 0,
    0, 0, 0, 0,
    0, 5, 0, 6,
]

chunks = list(bitpack(fields=ints, field_width=3, chunk_width=64))
print(f"Bit-packed chunks: {chunks}")

fields = list(bitunpack(chunks=chunks, chunk_width=64, field_width=3))
print(f"Unpacked fields: {fields}")

assert fields == ints
