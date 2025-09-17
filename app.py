import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("💊 Pharmacovigilance - ADR Signal Detection App")

st.markdown("""
### 📌 Instructions:
- Upload a CSV file with **two columns**:  
  1. `ADR` → Adverse Drug Reaction (e.g., Nausea, Rash, Headache)  
  2. `SOC` → System Organ Class (e.g., Gastrointestinal disorders, Skin disorders, Nervous system disorders)  

👉 Example:
| ADR       | SOC                          |
|-----------|------------------------------|
| Nausea    | Gastrointestinal disorders   |
| Headache  | Nervous system disorders     |
""")

# File uploader
uploaded_file = st.file_uploader("📂 Upload ADR Report CSV", type=["csv"])

if uploaded_file is not None:
    # Read uploaded CSV
    df = pd.read_csv(uploaded_file)
    st.write("### ✅ Uploaded Data")
    st.write(df.head())

    if "ADR" in df.columns and "SOC" in df.columns:
        # Frequency analysis
        soc_counts = df["SOC"].value_counts()
        soc_percent = df["SOC"].value_counts(normalize=True) * 100
        results = pd.DataFrame({"Count": soc_counts, "Percentage": soc_percent.round(2)})

        st.write("### 📊 ADR Frequency Analysis by SOC")
        st.write(results)

        # Plot
        fig, ax = plt.subplots()
        soc_counts.plot(kind="bar", ax=ax, color="skyblue", edgecolor="black")
        ax.set_ylabel("Number of ADRs")
        ax.set_xlabel("System Organ Class (SOC)")
        ax.set_title("ADR Frequency by SOC")
        st.pyplot(fig)

        # Download option
        csv = results.to_csv().encode("utf-8")
        st.download_button(
            label="⬇️ Download Results as CSV",
            data=csv,
            file_name="adr_analysis_results.csv",
            mime="text/csv",
        )
    else:
        st.error("⚠️ CSV must contain both 'ADR' and 'SOC' columns.")
