import streamlit as st

# ================= PAGE SETTINGS =================
st.set_page_config(
    page_title="Mechanical Unit Converter",
    page_icon="⚙️",
    layout="centered"
)

# ================= TITLE =================
st.markdown(
    """
    <h1 style='text-align:center; color:#0E76A8;'>
    ⚙️ Mechanical Unit Converter & Density Checker
    </h1>
    """,
    unsafe_allow_html=True
)

# ================= STUDENT INFO =================
st.markdown(
    """
    <div style='padding:15px;
                border-radius:10px;
                background-color:#f0f2f6;
                border:1px solid #d3d3d3;'>

    <h3>Student Information</h3>

    <b>Name:</b> M Ahmed<br>
    <b>Reg No:</b> 25ME15

    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ================= SIDEBAR =================
menu = st.sidebar.selectbox(
    "Choose Option",
    ["Unit Converter", "Material Density Checker"]
)

# =================================================
# UNIT CONVERTER
# =================================================
if menu == "Unit Converter":

    st.header("🔄 Unit Converter")

    category = st.selectbox(
        "Select Conversion Type",
        ["Length", "Mass", "Temperature"]
    )

    # ---------------- LENGTH ----------------
    if category == "Length":

        value = st.number_input("Enter Value", value=0.0)

        from_unit = st.selectbox(
            "From",
            ["Meter", "Centimeter", "Millimeter"]
        )

        to_unit = st.selectbox(
            "To",
            ["Meter", "Centimeter", "Millimeter"]
        )

        # Convert to meter
        if from_unit == "Meter":
            meter = value
        elif from_unit == "Centimeter":
            meter = value / 100
        else:
            meter = value / 1000

        # Convert from meter
        if to_unit == "Meter":
            result = meter
        elif to_unit == "Centimeter":
            result = meter * 100
        else:
            result = meter * 1000

        st.success(f"Converted Value = {result:.4f} {to_unit}")

    # ---------------- MASS ----------------
    elif category == "Mass":

        value = st.number_input("Enter Value", value=0.0)

        from_unit = st.selectbox(
            "From",
            ["Kilogram", "Gram"]
        )

        to_unit = st.selectbox(
            "To",
            ["Kilogram", "Gram"]
        )

        # Convert to kg
        if from_unit == "Kilogram":
            kg = value
        else:
            kg = value / 1000

        # Convert from kg
        if to_unit == "Kilogram":
            result = kg
        else:
            result = kg * 1000

        st.success(f"Converted Value = {result:.4f} {to_unit}")

    # ---------------- TEMPERATURE ----------------
    elif category == "Temperature":

        value = st.number_input("Enter Temperature", value=0.0)

        conversion = st.selectbox(
            "Select Conversion",
            [
                "Celsius to Fahrenheit",
                "Fahrenheit to Celsius"
            ]
        )

        if conversion == "Celsius to Fahrenheit":
            result = (value * 9/5) + 32
            st.success(f"{value} °C = {result:.2f} °F")

        else:
            result = (value - 32) * 5/9
            st.success(f"{value} °F = {result:.2f} °C")

# =================================================
# DENSITY CHECKER
# =================================================
elif menu == "Material Density Checker":

    st.header("🧱 Material Density Checker")

    materials = {
        "Steel": 7850,
        "Aluminum": 2700,
        "Copper": 8960,
        "Brass": 8500,
        "Iron": 7874
    }

    material = st.selectbox(
        "Select Material",
        list(materials.keys())
    )

    density = materials[material]

    st.info(f"Density of {material} = {density} kg/m³")

    st.subheader("Mass Calculator")

    volume = st.number_input(
        "Enter Volume (m³)",
        min_value=0.0,
        value=1.0
    )

    mass = density * volume

    st.success(f"Calculated Mass = {mass:.2f} kg")

# ================= FOOTER =================
st.markdown("---")

st.markdown(
    """
    <div style='text-align:center;'>
    Developed by <b>M Ahmed</b> | Reg No: <b>25ME15</b>
    </div>
    """,
    unsafe_allow_html=True
)
