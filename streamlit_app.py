import streamlit as st

st.title("Simple Packing List Generator")
st.write("Please upload your CSV file to generate a professional packing list.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    # When user uploads file, parse and generate PDF
    if st.button("Generate Packing List"):
        # Call your parsing and PDF generation function
        pdf_path = generate_packing_list(uploaded_file)
        
        if pdf_path:
            # Display a success message and a download link
            st.success("Packing list generated successfully!")
            with open(pdf_path, "rb") as f:
                st.download_button("Download Packing List PDF", f, file_name="packing_list.pdf")
        else:
            st.error("An error occurred while generating the packing list.")
