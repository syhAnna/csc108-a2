def is_base_pair(base1, base2):
    ''' (str, str) -> bool
    
    Precondition: base1 and base2 are single characters among 'A', 'T', 'G', 'C'
    'A' and 'T' are a base pair, 'G' and 'C' are a base pair.
    
    Return True iff base1 and base2 are a base pair.
    
    >>> is_base_pair('A', 'T')
    True
    >>> is_base_pair('G', 'C')
    True
    >>> is_base_pair('A', 'G')
    False
    '''
    if base1 == 'A':
        return base2 == 'T'
    if base1 == 'T':
        return base2 == 'A'
    if base1 == 'G':
        return base2 == 'C'
    if base1 == 'C':
        return base2 == 'G'

def is_dna(strands1, strands2):
    ''' (str, str) -> bool
    
    Precondition: len(strand1) = len(strands2) and strands1 and strands2 only 
    contain 'A','T', 'G' and 'C'.
    
    Return True iff strand1 and strand2 can form a DNA sequence
    
    >>> is_dna('CTGACGCGCC', 'GACTGCGCGG')
    True
    >>> is_dna('CTGACGCGCC', 'GACAGCCAGG')
    False
    '''
    count = 0
    for i in range(len(strands1)):
        if is_base_pair(strands1[i], strands2[i]):
            count += 1
    return count == len(strands1)

def is_dna_palindrome(strands1, strands2):
    ''' (str, str) -> bool
    
    Return True iff strands1 and strands2 are DNA palindrome.
    
    >>> is_dna_palindrome('GGATCC', 'CCTAGG')
    True
    >>> is_dna_palindrome('GGCA', 'CCGT')
    False
    '''
    if is_dna(strands1, strands2):
        strands = strands1 + strands2
    
    count = 0 
    for i in range(len(strands) // 2):
        if strands[i] == strands[-(i + 1)]:
            count += 1
    return count == len(strands) // 2

def restriction_sites(strand, recog_sequence):
    ''' (str, str) -> list of int
    
    Precondition: only look from left to right.
    
    Return a list of all the indices where the recog_sequence appears in the 
    strand
    
    >>> restriction_sites('ATTGGGGATCCGACCTGGATCCTTAAGGATCCGGTTAA', 'GGATCC')
    [5, 16, 26]
    >>> restriction_sites('GGCCATCCTAGGCCGGAATCGGGCCATGGCCTTGGCCT', 'GGCC')
    [0, 10, 21, 27, 33]
    >>> restriction_sites('ATGACTTA', 'GGCC')
    []
    >>> restriction_sites('ATT', 'GGCC')
    []
    '''
    sequence = []
    index = strand.find(recog_sequence)
    while index != -1:
        sequence.append(index)
        index = strand.find(recog_sequence, index + len(recog_sequence))
    return sequence        
   

def match_enzymes(strand, names, sequence): 
    '''(str, list of str, list of str) -> list of two-item [str, int] lists
    
    Precondition: len(names) = len(sequence)
    
    Return a list of two-item lists where the first item is the name in the 
    names list and the second item is the list of indices in strand that the 
    enzyme cuts. 
    
    >>> match_enzymes('ATGGATCCTTCGAATTCATCGGATCCTA', ['EcoRI', 'BamHI'], 
    ['GAATTC', 'GGATCC'])
    [['EcoRI', [11]], ['BamHI', [2, 20]]]
    >>> match_enzymes('ATGCGGCCGCGGCCATAAGCTTTA', ['HindIII', 'HaeIII', 'NotI']
    , ['AAGCTT', 'GGCC', 'GCGGCCGC'])
    [['HindIII', [18]], ['HaeIII', [4, 12]], ['NotI', [2]]]
    '''
    full_list = []
    
    for i in range(len(names)):
        sub_list = []
        sub_list.append(names[i])
        sub_list.append(restriction_sites(strand, sequence[i]))
        full_list.append(sub_list)
    return full_list

def one_cutters(strand, names, sequence):
    ''' (str, list of str, list of str) -> list of two-item [str, int] lists
    
    Preconditon: strand contains the restriction sequence of the enzymes in 
    the list names. 
    
    Return a list of two-item lists representing the 1-cutters for the strand.
    
    >>> one_cutters('AGAATTCATTGGATCCC', ['EcoRI', 'BamHI'], 
    ['GAATTC', 'GGATCC'])
    [['EcoRI', 1], ['BamHI', 10]]
    >>> one_cutters('AAGGCCATTGACGCT', ['HaeIII', 'HgaI'], 
    ['GGCC', 'GACGC'])
    [['HaeIII', 2], ['HgaI', 9]] 
    >>>
    '''
    full_list = []
    
    for i in range(len(names)):
        sub_list = []
        sub_list.append(names[i])
        sub_list.append(strand.find(sequence[i]))
        full_list.append(sub_list)
        
    return full_list

def correct_mutations(strands, clean, names, sequences):
    ''' (list of str, str, list of str, list of str) -> NoneType
    
    Precondition: clean contains exactly one 1-cutter from the names and 
    sequences provides. 
    
    Return NoneType.
    
    >>> strands = ['ACGTGGCCTAGCT', 'CAGCTGATCG']
    >>> clean = 'ACGGCCTT'
    >>> names = ['HaeIII', 'HgaI', 'AluI']
    >>> sequences = ['GGCC', 'GACGC', 'AGCT']
    >>> correct_mutations(strands, clean, names, sequences)
    >>> strands
    ['ACGTGGCCTT', 'CAGCTGATCG']
    
    >>> strands = ['TAAAGCTT', 'TGGATCCTGAATTCT']
    >>> clean = 'AGGATCCTC'
    >>> names = ['EcoRI', 'BamHI', 'HindIII']
    >>> sequences = ['GAATTC', 'GGATCC', 'AAGCTT']
    >>> correct_mutations(strands, clean, names, sequences)
    >>> strands
    ['TAAAGCTT', 'TGGATCCTC']
    
    >>> strands = ['AATCGAGA', 'TACCTCGACAG']
    >>> clean = 'ATCGACT'
    >>> names = ['TaqI', 'Sau3A']
    >>> sequences = ['TCGA', 'GATC']
    >>> correct_mutations(strands, clean, names, sequences)
    >>> strands
    ['AATCGACT', 'TACCTCGACT']
    '''
    for i in range(len(sequences)):
        if sequences[i] in clean:
            site = sequences[i]
            index1 = clean.find(site)
            
    for i in range(len(strands)):
        if site in strands[i]:
            index2 = strands[i].find(site)
            strands[i] = strands[i][:index2] + clean[index1:]
