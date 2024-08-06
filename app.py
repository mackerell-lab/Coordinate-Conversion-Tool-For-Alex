import psi4
import py3Dmol
import streamlit as st
from stmol import showmol

input = st.text_area("Enter Your Z-Matrix Coordinate Data Here Alex:")

def render_mol(xyz):
    view = py3Dmol.view(width=400, height=400)
    view.addModel(xyz, "xyz")
    view.setStyle({'stick': {}})
    view.setBackgroundColor('black')
    view.zoomTo()
    return view

if input:
    dimer = psi4.geometry(input)
    dimer.update_geometry()
    dimer.save_xyz_file('test.xyz', False)

    with open('test.xyz') as in_file:
        xyz_data = in_file.read()

    st.text_area(label="Output Coordinate:", value=file, height=550)

    st.title("XYZ Molecule Viewer")
        
    # Render the molecule
    st.subheader("3D Molecule Viewer:")
    view = render_mol(xyz_data)
    showmol(view, height=400, width=400)
        
    st.download_button(
      label="Download XYZ file",
      data=xyz_data,
      file_name="molecule.xyz",
      mime="chemical/x-xyz"
    )




