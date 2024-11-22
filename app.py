import streamlit as st

# Define the function Gen_Eff
def Gen_Eff(V, CL, IL, K, Rse, Ra):
    # Calculate Core Loss (CUL)
    CUL = (K * IL) ** 2 * (Rse + Ra)

    # Calculate Efficiency (Eff)
    Eff = (K * V * IL - CL - CUL) / (K * V * IL) * 100
    
    return Eff, CUL

# Web Application Interface
def main():
    st.title("2205A21011-PS11")  # Change title to your roll number and problem statement number
    st.write("calculate the efficiency of DC series motor in various loads")
    # Input fields for the user to enter the values
    V = st.number_input("Voltage (V)", value=230.0)  # Default voltage 220V
    CL = st.number_input("Core Loss (CL) in Watts", value=100.0)  # Default core loss
    IL = st.number_input("Full Load Current (IL) in Amps", value=15.0)  # Default current
    K = st.number_input("Loading on Motor (K)", value=1)  # Default loading
    Rse = st.number_input("Series Field Resistance (Rse) in Ohms", value=0.20)  # Default resistance
    Ra = st.number_input("Armature Resistance (Ra) in Ohms", value=0.10)  # Default resistance

    if st.button("Calculate Efficiency"):
        # Calculate efficiency and core loss using the Gen_Eff function
        Eff, CUL = Gen_Eff(V, CL, IL, K, Rse, Ra)

        # Display results
        st.write(f"**Efficiency of a DC series motor(%)**: {Eff:.2f}%")
        st.write(f"**Core Loss (CUL) in Watts**: {CUL:.2f} W")

if __name__ == "__main__":
    main()
