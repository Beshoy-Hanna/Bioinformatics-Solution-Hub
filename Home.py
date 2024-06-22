import streamlit as st
import json
from streamlit_lottie import st_lottie

st.title("Bioinformatics Solutions Hub")

def load_lottiefile(filepath: str):
    with open(filepath, 'r') as f:
        return json.load(f)
    
col1, col2 = st.columns(2)

with col1:
    st.markdown('''
    Welcome to Bioinformatics Solutions Hub, your one-stop online platform for solving a wide range of bioinformatics problems. Designed with the powerful and user-friendly Streamlit framework, our website offers an intuitive interface and robust tools to facilitate various DNA, RNA, and protein operations for researchers, students, and bioinformatics enthusiasts.

    ### Key Features:

    #### DNA Operations
    - **Count Nucleotides**            
    - **GC Content**
    - **Transcription** 
    - **DNA Length**
    - **Complement DNA**
    - **Reverse Complement**
    - **Transcription**
    - **Motif Finding**
    - **Consensus and Profile Matrix Calculation**

    #### Graph Algorithms:
    - **De-bruijn Graph**
    - **Visualize De-bruijn Graph**
                
    #### RNA to Protein Translation:
    - **RNA Translation**
    - **Calcuating Protein Mass**            

    #### Protein Structure Prediction:
    - **Predict Protein Structure using ESMFold**
    - **plDDT** is a per-residue estimate of the confidence in prediction on a scale from 0-100.
    - **Download PDB file**
    ''')

with col2:
    animation = load_lottiefile("E:/Bioinformatics Projects/Rosland Problems/AnimationDNA.json")
    st_lottie(animation, height=500, width=500, key="dna")
