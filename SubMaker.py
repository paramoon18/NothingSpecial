#!/usr/bin/env python3
# SubMaker.py - Encode proxy list (vless, vmess, trojan, ss, etc.) to Base64 subscription file

import base64
import os

INPUT_FILE = "WanaBSpecial.txt"
OUTPUT_FILE = "SpecialOne.txt"

def main():
    # Check if input file exists
    if not os.path.isfile(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found in current directory.")
        return 1

    # Read the whole file as binary (preserves newlines)
    with open(INPUT_FILE, "rb") as f:
        raw_data = f.read()

    # Base64 encode without any extra wrapping
    encoded_data = base64.b64encode(raw_data).decode("ascii")

    # Write the encoded string to the output file
    with open(OUTPUT_FILE, "w") as f:
        f.write(encoded_data)

    print(f"Success: {INPUT_FILE} encoded and saved to {OUTPUT_FILE}")
    return 0

if __name__ == "__main__":
    exit(main())