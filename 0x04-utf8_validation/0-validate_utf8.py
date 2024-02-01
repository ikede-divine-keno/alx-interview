#!/usr/bin/python3
""" Write a method that determines if a
given data set represents a valid UTF-8 encoding."""


def validUTF8(data):
    """_summary_
    Args:data (list[int]): a list of integers
    """
    expected_continuation_bytes = 0

    # Define bit patterns for UTF-8 encoding rule
    mask_to_determine_the_order = 0b10000000  # 10000000
    mask_to_check_if_highbitorder_is_zero_or_not = 0b01000000  # 01000000

    # Loop over each byte in the input data
    for byte in data:
        # Initialize a mask to check for leading
        # 1's in the current byte if its 2nd 3rd or forth order sequence
        mask_to_determine_the_order_seq = mask_to_determine_the_order

        # If we are not currently expecting any
        # continuation bytes
        if expected_continuation_bytes == 0:
            # Count the number of leading 1's in the
            # current byte to determine the number of
            # continuation bytes
            while mask_to_determine_the_order_seq & byte:
                expected_continuation_bytes += 1
                mask_to_determine_the_order_seq =\
                    mask_to_determine_the_order_seq >> 1

            # If the byte is not a multi-byte sequence,
            # number is less than 128
            # move to the next byte correct
            if expected_continuation_bytes == 0:
                continue

            # If the number of continuation bytes is not
            # between 2 and 4, the sequence is invalid
            if expected_continuation_bytes == 1 or\
                    expected_continuation_bytes > 4:
                return False

        # If we are expecting continuation bytes
        else:
            # Check that the byte starts with a "10"
            # prefix and not a "11" prefix
            if not (byte & mask_to_determine_the_order and not
                    (byte & mask_to_check_if_highbitorder_is_zero_or_not)):
                return False
        # Decrement the expected number of continuation bytes
        expected_continuation_bytes = expected_continuation_bytes - 1

    # If we have processed all bytes and are not expecting
    # any more continuation bytes, the sequence is valid
    if expected_continuation_bytes == 0:
        return True
    else:
        return False
