"""Function to determine the RNA complement of a given DNA sequence."""

def to_rna(dna_strand):
    dna = 'ACGT'
    rna = 'UGCA'
    translator = str.maketrans(dna, rna)
    return dna_strand.translate(translator)