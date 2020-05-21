def proteins(strand):
    codon_dict = {'AUG': 'Methionine', 'UUU': 'Phenylalanine',
                  'UUC': 'Phenylalanine', 'UUA': 'Leucine', 'UUG': 'Leucine',
                  'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine',
                  'UAU': 'Tyrosine', 'UAC': 'Tyrosine', 'UGU': 'Cysteine',
                  'UGC': 'Cysteine', 'UGG': 'Tryptophan', 'UAA': 'STOP', 'UAG': 'STOP',
                  'UGA': 'STOP'}

    strand_length = len(strand)
    counter = 0
    amino_acids = []
    while counter < strand_length:
        codon = strand[counter] + strand[counter + 1] + strand[counter + 2]
        counter += 3
        if codon_dict.get(codon) == 'STOP':
            break
        else:
            amino_acid = codon_dict.get(codon)
            amino_acids.append(amino_acid)

    return amino_acids
