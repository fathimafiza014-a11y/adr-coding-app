import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Pharmacovigilance - ADR Signal Detection App")

# File uploader
uploaded_file = st.file_uploader("Upload ADR Report CSV", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded CSV
    df = pd.read_csv(uploaded_file)
    st.write("### Uploaded Data")
    st.write(df.head())

    # Example: expecting ADR and SOC columns
    if "ADR" in df.columns and "SOC" in df.columns:
        st.write("### Frequency Analysis of System Organ Classes (SOC)")
        soc_counts = df["SOC"].value_counts()

        # Display table
        st.write(soc_counts)

        # Plot
        fig, ax = plt.subplots()
        soc_counts.plot(kind="bar", ax=ax)
        ax.set_ylabel("Number of ADRs")
        ax.set_xlabel("System Organ Class (SOC)")
        ax.set_title("ADR Frequency by SOC")
        st.pyplot(fig)
    else:
        st.warning("CSV must contain columns: 'ADR' and 'SOC'.")
