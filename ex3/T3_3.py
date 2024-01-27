import re

def format_text(input_text):
    input_text = input_text.rstrip()
    char_enum = list(enumerate(input_text))
    
    at_positions = [index for index, char in char_enum if char == '@']
    hash_positions = [index for index, char in char_enum if char == '#']

    for at_pos in at_positions:
        for hash_pos in range(at_pos):
            if hash_pos in hash_positions:
                hash_positions.remove(hash_pos)

        if hash_positions:
            min_hash_pos = min(hash_positions)
            hash_positions.remove(min_hash_pos)
            char_enum.remove((min_hash_pos, '#'))

    formatted_text = ''.join(char for _, char in char_enum)
    formatted_text = re.sub(r'\s{2,}', ' ', formatted_text)
    formatted_text = formatted_text.replace(r'\n', '\n')

    return formatted_text

if __name__ == "__main__":
    input_text = input()
    formatted_text = format_text(input_text)
    print('Formatted Text:', formatted_text)
