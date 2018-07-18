def to_rna(dna_strand):
    dnalist = list(dna_strand)
    rnalist = []
    i = 0 
    while i < len(dnalist):
        if dnalist[i] == 'G':
            rnalist.append('C')
        elif dnalist[i] == 'C':
            rnalist.append('G')
        elif dnalist[i] == 'T':
            rnalist.append('A')
        elif dnalist[i] == 'A':
            rnalist.append('U')
        else:
            raise Exception('Incorrect DNA nucleotide')
        i += 1
    
    return "".join(rnalist)