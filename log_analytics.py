from Trie import trie
messages = []

def generate_permutations(data, edit_distance_limit = 3):
    "useful to wild-card log messages. Uses a simple DP algorithm to do so"
    n = len(data)
    permutations = [(data, 0)]
    for i in range(0, n):
        new_permutations = []
        for permutation, edit_distance in permutations:
            if edit_distance < edit_distance_limit:
                new_permutations.append((permutation[0:i] + '*' + permutation[i+1:], edit_distance + 1))
        permutations += new_permutations
    return [permutation for permutation, edit_distance in permutations]


def find_trending(foreground_messages, background_messages):
    fg_trie = trie()
    fg_trie.add_data(foreground_messages)
    bg_trie = trie()
    bg_trie.add_data(background_messages)
    ratio_dict = {}
    for message in foreground_messages:
        if not message in ratio_dict:
            fg_count = fg_trie.get_message_count(message)
            bg_count = bg_trie.get_message_count(message)
            ratio = fg_count / bg_count
            ratio_dict[message] = ratio
    return ratio_dict



