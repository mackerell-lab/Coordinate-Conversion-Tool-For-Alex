import psi4
import streamlit as st

input = st.text_area("Enter Your Z-Matrix Coordinate Data Here Alex:")

if input:
    dimer = psi4.geometry(input)
    dimer.update_geometry()
    dimer.save_xyz_file('test.xyz', False)

    with open('test.xyz') as in_file:
        file = in_file.read()

    st.text_area(label="Output Coordinate:", value=file, height=550)
