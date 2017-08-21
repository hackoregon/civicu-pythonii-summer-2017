def to_rna(input):
    keys = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    new_list = []
    for letter in input:
        new_list.append(keys.get(letter, ''))
    answer = "".join(new_list)
    if len(answer) != len(input): answer = ''
    return answer

#def to_rna(input):
#    if set(new_input + "CGAT") != set("CGAT"): 
#        return ''
#    new_input = input.translate(str.maketrans("CGAT", "GCUA"))
#    return new_input
