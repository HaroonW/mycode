#!/usr/bin/python3

def print_length(list_o_words):
    s_count = 0
    m_count = 0
    L_count = 0
    for words in list_o_words:
        if len(words) < 5:
            s_count += 1
        elif len(words) < 10:
            m_count += 1
        else: 
            L_count += 1
    print(f'there are {s_count} short words, {m_count} medium words, and {L_count} long words')

example_list = ['banana', 'blueberries', 'nuts' 'acrons']
print_length(example_list)

