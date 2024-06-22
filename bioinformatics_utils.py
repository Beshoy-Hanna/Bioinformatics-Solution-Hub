# Count the nucleoties 
def count_nucleotides(dna):
    return {
        'A': dna.count('A'),
        'C': dna.count('C'),
        'G': dna.count('G'),
        'T': dna.count('T')
    }


# transcribtion
def transcribe_dna_to_rna(dna):
    return dna.replace('T', 'U')

# complement 
def complement_dna(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in dna)

# GC_content 
def gc_content(dna):
    gc_count = dna.count('G') + dna.count('C')
    return (gc_count / len(dna)) * 100

# mutation 
def count_point_mutations(dna1, dna2):
    return sum(1 for a, b in zip(dna1, dna2) if a != b)
