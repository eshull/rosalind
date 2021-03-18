def counting_point_mutations(dna_string_one, dna_string_two):
    mutations = 0
    chars_one = split_characters(dna_string_one)
    chars_two = split_characters(dna_string_two)
    for i, char in enumerate(chars_one, start=0):
        char_two = dna_string_two[i]
        if char != char_two:
            mutations += 1
    print(mutations)

def split_characters(word):
    return [char for char in word] 

counting_point_mutations('GACGGGAGCATCCGATTGACATTTCGTGGGTCATGTACGTACCCGACGATGGGAAATAACTACCCGGCATGTGAATCATACGATGGTAGGTGGGGACGGCTGGATCTGTGCTTACAGTATCCGAAGTTCGCACGAGCTTGGTAATTATGGGGAATTTGCCGCGGCATCATGGGGCTGGGTTTGGTCAGATGTACTTTAGAGAGGGGCACCGGCGAGTGTTAACCTTATCTCAACCCACTGGCTAACTTTGGTGACTCGTTAAAGCCGGAGGATTCGGAAGAGAGGACGCATTGTGGTTCATTGCTTACCTATACGTCTTCTGGCATAGCGCTGCTCTGTGTCAGGTAATATAAGCCATGCGAACCGTGTGGAAGTCGAATTCCCCAAGGCTACGAGGTTATTTCCCGTACATGAGACCTGTGACTCAACAAGAAGATAAGGCGAGACCGTCGCGCGTCGCTTCACGATACTATAAGCTTGAAGGTAACAGGGGGTCTCACCCAAGGTGAATGTTGTGATTCGGGCCAAGATAGTAATTCATTATACTCCCAAAGCTAGCCGTAGCGGAGATACTTGATCGAGACCATGTTACCATAAGTCTTCCTGGAAATTAGGAATTTACCGCGAAGGTAGGGCCAATGCTGGCACCGACTGGAACCATCGCAGTAAAGGGGATGGCTAGACTGATTAAGGTCACTAAGTCGGTATCGCAATAACGCGTAATCGGGGGACTCTTGGTCAGAAGTAAAGACCGCGCATGAAGGGTGTTTCAAAGCCCTACTAAGCGTTACTGAGGTGTCACTCGGTTCCAGCAATTAAGTGTCTACGTGAGGGCGAATCCCGACAATTTATAGTGGCCAACCGGCCGACGGGCCGCCAGGTGGGGATGGCGATGCCATAGGAGCGGCATGAGTCTCGCAA', 'GGCGGCGGTTGTCAATTCGGATGAACTCGGTCGTATACTAACGCCCGGTGGTAAGCTGACTGCTCAACGTGTGCCTCATCTGAGCTAAGCTTGAACGGAATGGATCCCCTTTCCGAAGAATAAATGCGAGCACGATCTATGCGATGATGGTTAAGTTGCTATGTACACTGAGGTCGATGTTAGAGGAGGTCACTTATATTCTGTGACAGTCGCATCGGTCAACCACCTCACAAGCAGCTTGCTAATAGAGGTTGCTCGTTACATAATGTGCATGCTGAGCAGGTCGCGCACCGAGGGTTGTTACATAGTTGGACGTAGTCAGGAAACGATTTGCTGCGATGTATTTTAGGTATCCAGTGAGGCCTATGCCCAAACCCAATCTAAAAGTGCTAGGAACATATTTCGCGTTTTTGCGCCCAATACACCTGGAAATAACTTCGGGTAAACCGCCTCGACCCGTTCGACCAAACTCAACCCAGAAAACTATCGACGCGTCGCTGTCAAGTCGAGTACTGAAATTCGGTCGCAGAGCGTACCACAGTATACGCCGAATAATAATCGCCTCTGCGGAACGTAATCTGGCGCATGGAACCATGAGGTGATGAGCAAAGGTCTAACATGCCTTTATCATGCGCAGAGAGCAGGTCCGAATTGGAGAAGTAACACTATAAGGCTTTGCGATCATGCTGACCGTCACGCGCCATGTAGCACGTACCCTCGTATTCTTGCTCTTCTTGCTTGGTAGGTGACTCCCCTTCTCCTGTGTTTTTAGAAAATCTAAATTGGTTTCCAACAGTTACGCCTGCTTCAAGTGAATAAGAAACAACCTGTGCGCGAATCCCCCCAATAGTTATATCTGGACGTGCCGAATCAGCGTCAGGGGAAAACCGAACTTCCCCATTCGTCTTCTGAGAGTCCGAA')