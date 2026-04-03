"""
271. Encode and Decode Strings

Description:
    Design an algorithm to encode a list of strings to a single string,
    then decode it back to the original list. Strings can contain any
    possible characters.

Approach:
    Encode each string as "length#string". The length tells decode
    exactly how many characters to read, so it works even if the
    string itself contains '#' or digits.
    - Encode: for each string, prepend its length and '#'.
    - Decode: read digits until '#', parse the length, take that
      many characters, move pointer to the next segment.

Tech Stack:
    - String manipulation with length-prefixed encoding
    - Pointer-based parsing

Complexity:
    - Time: O(m) for both encode and decode, m = total length of all strings
    - Space: O(m) for the encoded string / decoded list
"""


class Codec:

    def encode(self, strs):
        # prepend each string with its length and '#'
        encode_str = ""
        for s in strs:
            encode_str += str(len(s)) + "#" + s
        return encode_str

    def decode(self, s):
        message = []
        i = 0

        while i < len(s):
            # find '#' to know where the length number ends
            j = s.find("#", i)
            length = int(s[i:j])

            # take the next 'length' characters as the original string
            message.append(s[j + 1 : j + 1 + length])

            # move pointer to the start of the next segment
            i = j + 1 + length

        return message