"""Functions to determine the RNA complement of a given DNA sequence."""

def to_rna(dna_strand):
    return dna_strand.translate(str.maketrans('ACGT', 'UGCA'))