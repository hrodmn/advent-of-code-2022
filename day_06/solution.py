with open("test_input") as f:
    TEST_INPUT = [line for line in f]

with open("input") as f:
    INPUT = [line for line in f]


def find_packet(buffer, packet_len=4):
    for i in range(len(buffer)):
        stop = i + packet_len
        marker = buffer[i:stop]
        # return the stop index for the first set of non-repeating characters
        if len(marker) == len(set(marker)):
            return stop


# part 1
test_stops = [find_packet(buffer, packet_len=4) for buffer in TEST_INPUT]

assert test_stops == [7, 5, 6, 10, 11]

packet_stops = [find_packet(buffer, packet_len=4) for buffer in INPUT]
print(packet_stops)


# part 2
test_stops2 = [find_packet(buffer, packet_len=14) for buffer in TEST_INPUT]
assert test_stops2 == [19, 23, 23, 29, 26]

packet_stops2 = [find_packet(buffer, packet_len=14) for buffer in INPUT]
print(packet_stops2)
