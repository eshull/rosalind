# Transcribing DNA into RNA
def transcribe_dna_into_rna(dna_string)
  dna_string.gsub("T", "U")
end

string = "TTCACGTCGCTAGCACCTGCCCTTCGGTCGAGTGGTATAAGCTAAGGTGGAAGAAAATAATGGTCATGAATCTGACGTCTTATTTGACATGGCACAGCCCTGACTGGCCAGCCATCTAAAGCTATAACAGCAGAGGAACATAACACGTCAAGTATACCCACAGGATCGTGGAGGCTGTTGATCAAATTGTACGAGCAATCGACGTAGCCGAGAGGGCTACATAAGCACGGCTCCTACCAAGTGGTATAAATAGCTCCTCCCCGTCAATGACAAGGCATCCATACCATGAGCGCTGGCTTCTTCTAGGTCTCCGAAACAACCTGAACTTCTGGAATCTACCCGTCGTGATTATTGTGACCATGTATGTGCGAGCGGAATCTCAGCGTTGCGAGAATCAGCCGGAAATCAAGGCTGGTGATATTCAACCTGTAATCAGCTACCCTCTACGCGCTAGGTTCTGCATCAAGCCCCTATATTAGGCCCAGCCTGGCCAGGTTCACGATCTCTTATTTTCATGCAAGTTCTGGCCGTATGATTCTGACTCATCTACTGCACTCGGCGTGGATCCATATCAACAAGTGTCCCTACGGACTTGTGCTTAAGTTGCCACAAACGACTTTTTCTAGAGTAGTCCAGGTCAATCTTATTGTTTTCCAGAAACTCTTCGGCTTTGGACACAATATGATTCGGGCAATATAATCCGTCGCGAACCATTTATAATTAATCGATCGGCTCTGCGTATGATCGAAGCCCAGAGTTGCGCCGCTTGTAAGGGGCGCGACCCAGTGGACACCATTCAGGAGGACATAATCTGTCTCCGGTCACTTGTCAGAATAACGTACTGTTATTGTTCGAGGCCAGACTCGCGAACGGATATATCTCCACGTGTGCCAGTGCTGCAAGTTATCCATGTCTGGG"
transcribe_dna_into_rna(string)
# Answer:
# UUCACGUCGCUAGCACCUGCCCUUCGGUCGAGUGGUAUAAGCUAAGGUGGAAGAAAAUAAUGGUCAUGAAUCUGACGUCUUAUUUGACAUGGCACAGCCCUGACUGGCCAGCCAUCUAAAGCUAUAACAGCAGAGGAACAUAACACGUCAAGUAUACCCACAGGAUCGUGGAGGCUGUUGAUCAAAUUGUACGAGCAAUCGACGUAGCCGAGAGGGCUACAUAAGCACGGCUCCUACCAAGUGGUAUAAAUAGCUCCUCCCCGUCAAUGACAAGGCAUCCAUACCAUGAGCGCUGGCUUCUUCUAGGUCUCCGAAACAACCUGAACUUCUGGAAUCUACCCGUCGUGAUUAUUGUGACCAUGUAUGUGCGAGCGGAAUCUCAGCGUUGCGAGAAUCAGCCGGAAAUCAAGGCUGGUGAUAUUCAACCUGUAAUCAGCUACCCUCUACGCGCUAGGUUCUGCAUCAAGCCCCUAUAUUAGGCCCAGCCUGGCCAGGUUCACGAUCUCUUAUUUUCAUGCAAGUUCUGGCCGUAUGAUUCUGACUCAUCUACUGCACUCGGCGUGGAUCCAUAUCAACAAGUGUCCCUACGGACUUGUGCUUAAGUUGCCACAAACGACUUUUUCUAGAGUAGUCCAGGUCAAUCUUAUUGUUUUCCAGAAACUCUUCGGCUUUGGACACAAUAUGAUUCGGGCAAUAUAAUCCGUCGCGAACCAUUUAUAAUUAAUCGAUCGGCUCUGCGUAUGAUCGAAGCCCAGAGUUGCGCCGCUUGUAAGGGGCGCGACCCAGUGGACACCAUUCAGGAGGACAUAAUCUGUCUCCGGUCACUUGUCAGAAUAACGUACUGUUAUUGUUCGAGGCCAGACUCGCGAACGGAUAUAUCUCCACGUGUGCCAGUGCUGCAAGUUAUCCAUGUCUGGG
