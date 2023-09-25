# 12th project - Reverse key and value in dictionary
# Purpose: To practice dictionary with vocabs in 's'en aller' lyrics

def reverse_dict(dict):
    new_dict = {}
    for key, value in dict.items():
            new_dict[value] = key
    return new_dict

vocab = {
    'le pire': 'the worst',
    'le fil': 'Brin long et fin des matières textiles',
    'combler': 'fill in',
    'vide': 'empty',
    'épine': 'thorn',
    'bête': 'beast'
}

print("FR-ENG\n{}\n".format(vocab))

reversed_vocab = reverse_dict(vocab)
print("ENG-FR\n{}".format(reversed_vocab))