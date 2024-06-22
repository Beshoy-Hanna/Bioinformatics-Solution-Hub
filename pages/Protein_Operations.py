import streamlit as st

# Title and layout setup
st.title('Protein Operations')
st.markdown('---')

# Codon table as a dictionary
CODON_TABLE = {
    'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
    'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
    'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
    'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
    'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
    'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
    'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
    'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
    'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
    'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
    'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
    'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
    'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}


# amino acids weights 
amino_acid_masses = {
    'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259, 'F': 147.06841, 'G': 57.02146,
    'H': 137.05891, 'I': 113.08406, 'K': 128.09496, 'L': 113.08406, 'M': 131.04049, 'N': 114.04293, 
    'P': 97.05276, 'Q': 128.05858, 'R': 156.10111, 'S': 87.03203, 'T': 101.04768, 'V': 99.06841,
    'W': 186.07931, 'Y': 163.06333
}


# Function for RNA validation
def is_valid_rna(rna):
    return all(nuc in 'AGCUagcu' for nuc in rna)

# Function to translate RNA into Protein
def translate_rna_to_protein(rna):
    if not is_valid_rna(rna):
        st.error('Invalid RNA sequence.')
        return None

    rna = rna.upper()
    protein = []

    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        amino_acid = CODON_TABLE.get(codon)

        if amino_acid == 'Stop':
            break
        if amino_acid:
            protein.append(amino_acid)
        else:
            st.error('Invalid RNA sequence.')
            return None

    return ''.join(protein)

# Function to check if the protein is Valid
def is_valid_protein(protein):
    valid_amino_acids = set(CODON_TABLE.values())
    for amino in protein:
        if amino not in valid_amino_acids:
            st.warning('Invalid Protein')
            return False
    return True

# Function to calculate the Protein Mass
def calculate_protein_mass(rna):
    
    if is_valid_rna(rna):
        protein = translate_rna_to_protein(rna)

        total_mass = 0

        for amino in protein: 
            if amino in amino_acid_masses:
                total_mass += amino_acid_masses[amino]

    return total_mass
    

# User input for RNA sequence
rna_sequence = st.text_area('Enter your RNA', 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA')


col1, col2 = st.columns(2)

with col1:
    # Button to trigger translation to protein
    if st.button('Translate into Protein'):
        protein = translate_rna_to_protein(rna_sequence)
        if protein:
            st.write('Protein:', protein)

with col2:
    if st.button("Calculate Protein Mass"):
        st.write("Protein Mass: ", calculate_protein_mass(rna_sequence))