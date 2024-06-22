import streamlit as st
from streamlit_lottie import st_lottie

# Title and layout setup
st.title("DNA Operations")
st.markdown('---')

# DNA validation function
def is_valid_dna(sequence):
    return all(nuc in 'AGCTagct' for nuc in sequence)

# len of DNA sequence
def dna_len(sequence):
    if is_valid_dna(sequence):
        return len(sequence)
    else:
        st.error('Invalid DNA Sequence')
        return None

# Function to count nucleotides in DNA
def count_nucleotides(sequence):
    nucleotides = {'G':0, 'C':0, 'A':0, 'T':0}

    if is_valid_dna(sequence):
        sequence = sequence.upper()
        for nuc in sequence:
            nucleotides[nuc] += 1

        return nucleotides
    else:
        st.error('Invalid DNA sequence.')
        return None

# Function to calculate GC content
def calculate_gc_content(sequence):
    if not is_valid_dna(sequence):
        st.error('Invalid DNA sequence.')
        return None
    sequence = sequence.upper()
    gc_count = sequence.count('G') + sequence.count('C')
    return f'{(gc_count / len(sequence)) * 100:.2f}%'

# Function to transcribe DNA to RNA
def transcribe_dna_to_rna(sequence):
    if is_valid_dna(sequence):
        return sequence.upper().replace('T', 'U')
    else:
        st.error('Invalid DNA sequence.')
        return None

# Function to complement a DNA strand
def complement_dna(sequence):
    if not is_valid_dna(sequence):
        st.error('Invalid DNA sequence.')
        return None
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[nuc] for nuc in sequence.upper())

# Function to count point mutations between two DNA sequences
def count_point_mutations(seq1, seq2):
    if len(seq1) != len(seq2):
        st.error('Sequences must be of equal length.')
        return None
    return sum(1 for a, b in zip(seq1, seq2) if a != b)

# Function to find reverse complement of DNA
def reverse_complement(sequence):
    return complement_dna(sequence)[::-1] if is_valid_dna(sequence) else None

# Function to find motif in DNA sequence
def find_motif(sequence, motif):
    if not is_valid_dna(sequence):
        st.error('Invalid DNA sequence.')
        return None
    positions = [i + 1 for i in range(len(sequence) - len(motif) + 1) if sequence[i:i+len(motif)] == motif]
    return positions

# User input for DNA sequence
sequence = st.text_area('Enter DNA sequence', 'AGTCCTGATCA')

# Layout for function buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button('Count Nucleotides'):
        result = count_nucleotides(sequence)
        if result is not None:
            st.write('Nucleotide Count:', result)

with col2:
    if st.button('GC Content'):
        result = calculate_gc_content(sequence)
        if result is not None:
            st.write('GC Content:', result)

with col3:
    if st.button('DNA Length'):
        result = dna_len(sequence)
        if result is not None:
            st.write('Length:', result)


col1, col2, col3 = st.columns(3)

with col1:
    if st.button('Transcribe'):
        result = transcribe_dna_to_rna(sequence)
        if result is not None:
            st.write('RNA Sequence:', result)

with col2:
    if st.button('Complement DNA'):
        result = complement_dna(sequence)
        if result is not None:
            st.write('Complementary DNA:', result)

with col3:
    if st.button('Reverse Complement'):
        result = reverse_complement(sequence)
        if result is not None:
            st.write('Reverse Complementary DNA:', result)

# Additional section for point mutation calculation
st.markdown('---')
st.subheader('Calculate Point Mutations')

col1, col2 = st.columns(2)
with col1:

    seq1 = st.text_area("Sequence 1", 'ACGT')
with col2:
    seq2 = st.text_area("Sequence 2", 'ACCT')


if st.button('Calculate Point Mutations'):
    result = count_point_mutations(seq1, seq2)
    if result is not None:
        st.write('Number of Point Mutations:', result)

# Motif Finding Section
st.markdown('---')
st.subheader('Motif Finding')

col1, col2 = st.columns(2)
with col1:
    seq1 = st.text_area("DNA Sequence", 'GATATATGCATATACTT')
with col2:
    motif = st.text_area("Motif", 'ATAT')

if st.button('Find Motif'):
    result = find_motif(seq1, motif)
    if result is not None:
        st.write('Found Motif at:', result)

# ------------------------------------------

st.write('---')
st.subheader('Consensus and Profile')

# Inject custom CSS to control the width and height of the text area
st.markdown("""
    <style>
    .custom-text-area {
        width: 500px; /* Set your desired width */
        height: 300px; /* Set your desired height */
    }
    </style>
    """, unsafe_allow_html=True)

# Create a text area with a custom class
dna_strings = st.text_area("Enter DNA Strings with the same length here:", ">A T C C A G C T\n>G G G C A A C T\n>A T G G A T C T\n>A A G C A A C C\n>T T G G A A C T\n>A T G C C A T T\n>A T G G C A C T", key="custom_text_area", height=300, max_chars=None, placeholder=None)

# Apply the custom class to the text area
st.markdown(f"""
    <script>
    var textarea = document.querySelectorAll('.stTextArea textarea')[0];
    textarea.classList.add('custom-text-area');
    </script>
    """, unsafe_allow_html=True)


def parse_fasta(fasta_strings):
    sequences = []
    sequence = ''
    
    for line in fasta_strings:
        if line.startswith('>'):
            if sequence:
                sequences.append(sequence)
                sequence = ''
        else:
            sequence += line.strip()
    if sequence:
        sequences.append(sequence)
    
    return sequences

def profile_matrix_and_consensus(sequences):
    from collections import defaultdict
    
    n = len(sequences[0])
    profile = {
        'A': [0] * n,
        'C': [0] * n,
        'G': [0] * n,
        'T': [0] * n
    }
    
    for sequence in sequences:
        for i, nucleotide in enumerate(sequence):
            profile[nucleotide][i] += 1
    
    consensus = ''
    for i in range(n):
        max_count = 0
        max_nucleotide = ''
        for nucleotide in 'ACGT':
            if profile[nucleotide][i] > max_count:
                max_count = profile[nucleotide][i]
                max_nucleotide = nucleotide
        consensus += max_nucleotide
    
    return profile, consensus

def print_results(profile, consensus):
    st.write("Consensus: ", consensus)
    for nucleotide in 'ACGT':
        st.write(f"{nucleotide}: {' '.join(map(str, profile[nucleotide]))}")

profile_consensus = st.button('Protile Matrix and Consensus')
if profile_consensus:
    sequences = parse_fasta(dna_strings)
    profile, consensus = profile_matrix_and_consensus(sequences)
    print_results(profile, consensus)

