import streamlit as st
import networkx as nx
from graphviz import Digraph
import graphviz

st.title('Graph Theory in Biology')
st.markdown('----------------')

st.subheader('De_bruijn Graph')

# input the reads 
reads = st.text_area('Enter the Reads here separated by space. for example: ', 'TTACGTT CCGTTA GTTAC GTTCGA CGTTC')

# input the k for k-mers 
k_mer = st.number_input('Enter Value of K-mer', 0, step=1)

# create the graph 
def de_bruijn(reads, k):
    list_of_reads = reads.split(' ')
    mers_list = []
    for read in list_of_reads:
        for i in range(len(read) - k + 1): 
            mer = read[i:i+k]
            mers_list.append(mer)

    graph = nx.DiGraph()
    for mer in mers_list:
        prefix = mer[:-1]
        suffix = mer[1:]
        graph.add_edge(prefix, suffix)

    return graph

de_bruijn_button = st.button('Show Graph')

if de_bruijn_button:
    graph = de_bruijn(reads, k_mer)

    dot = Digraph()
    for node in graph.nodes():
        dot.node(node)

    for edge in graph.edges():
        dot.edge(edge[0], edge[1])

    dot.attr() 
    st.graphviz_chart(dot.source)


