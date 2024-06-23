
# Bioinformatics Solutions Hub

Welcome to Bioinformatics Solutions Hub, simple platform for solving some of bioinformatics problems. Designed with the powerful and user-friendly Streamlit framework, our website offers an intuitive interface and robust tools to facilitate various DNA, RNA, and protein operations for researchers, students, and bioinformatics enthusiasts. 

You can find all problems at [Rosalin Website](https://rosalind.info/problems/locations/)




## Installation

## Installation

To run this project, you'll need to install the following Python libraries:

- `streamlit`
- `streamlit_lottie`
- `networkx`
- `graphviz`
- `stmol`
- `py3Dmol`
- `requests`
- `biotite`

You can install all the required libraries using `pip`. We recommend using a virtual environment to avoid conflicts with other projects. Here are the steps to set up your environment and install the dependencies:

1. **Create and activate a virtual environment (optional but recommended)**

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Install the libraries**

    ```sh
    pip install streamlit streamlit_lottie networkx graphviz stmol py3Dmol requests biotite
    ```

### Additional Notes

- For `graphviz`, you may need to install Graphviz software on your system. You can download it from [Graphviz's official website](https://graphviz.org/download/).
- If you encounter any issues with the installation, make sure you have the necessary build tools and compilers installed on your system.

After installing the libraries, you can run the Streamlit app using the following command:

```sh
streamlit run Home.py
