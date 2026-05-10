import streamlit as st

# Page Configuration
st.set_page_config(page_title="Mechanical Unit Converter", layout="centered")

# Header Section with Student Info
st.title("Mechanical Unit Converter & Material Density Checker")
st.markdown("---")
st.sidebar.header("Student Information")
st.sidebar.write(f"**Name:** MUHAMMAD SAIM MAZHAR")
st.sidebar.write(f"**Roll Number:** 25-ME-136")

st.info("Developed by: **MUHAMMAD SAIM MAZHAR** (Roll No: 25-ME-136)")

# Selection Menu
option = st.selectbox("Choose a tool:", ["Unit Converter", "Material Density Checker"])

# --- TOOL 1: UNIT CONVERTER ---
if option == "Unit Converter":
    st.subheader("⚙️ Unit Converter")
    category = st.radio("Select Category:", ["Pressure", "Power", "Force"])

    col1, col2 = st.columns(2)

    if category == "Pressure":
        val = col1.number_input("Value in Pascal (Pa):", value=1.0)
        # 1 Pa = 1e-5 bar, 1 Pa = 9.8692e-6 atm
        col2.write(f"**Bar:** {val * 1e-5:.6f}")
        col2.write(f"**Atmosphere (atm):** {val * 9.8692e-6:.7f}")
        col2.write(f"**PSI:** {val * 0.000145038:.6f}")

    elif category == "Power":
        val = col1.number_input("Value in Watts (W):", value=1.0)
        # 1 W = 0.00134102 HP
        col2.write(f"**Horsepower (HP):** {val * 0.00134102:.6f}")
        col2.write(f"**BTU/hr:** {val * 3.41214:.4f}")

    elif category == "Force":
        val = col1.number_input("Value in Newtons (N):", value=1.0)
        # 1 N = 0.224809 lbf
        col2.write(f"**Pound-force (lbf):** {val * 0.224809:.4f}")
        col2.write(f"**Kilonewtons (kN):** {val / 1000:.3f}")

# --- TOOL 2: DENSITY CHECKER ---
else:
    st.subheader("🔬 Material Density Checker")
    
    # Common engineering materials (kg/m^3)
    materials = {
        "Steel": 7850,
        "Aluminum": 2700,
        "Copper": 8960,
        "Cast Iron": 7200,
        "Titanium": 4506,
        "Concrete": 2400,
        "Water": 1000
    }
    
    selected_material = st.selectbox("Select Material:", list(materials.keys()))
    density = materials[selected_material]
    
    st.metric(label=f"Density of {selected_material}", value=f"{density} kg/m³")
    
    st.write("### Mass Calculator")
    volume = st.number_input("Enter Volume (m³):", min_value=0.0, value=1.0)
    mass = density * volume
    st.success(f"The calculated mass for {volume} m³ of {selected_material} is **{mass:,.2f} kg**.")

st.markdown("---")
st.caption("2026 Mechanical Engineering Assignment - Taxila")
