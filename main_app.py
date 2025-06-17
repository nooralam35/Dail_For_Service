# main_app.py

import streamlit as st

# Page config
st.set_page_config(page_title="Dial For Service", layout="wide")

# --- App Navigation ---
menu = st.sidebar.selectbox("Navigation", [
    "Home",
    "Login",
    "Customer Dashboard",
    "Admin Dashboard",
    "Services",
    "Cart",
    "Donate"
])

# --- Home Page ---
if menu == "Home":
    st.title("Welcome to Dial For Service")
    st.markdown("A one-stop platform for all your service needs.")

# --- Login Page ---
elif menu == "Login":
    st.title("Mobile OTP Login")
    phone = st.text_input("Enter Mobile Number")
    if st.button("Send OTP"):
        st.success("OTP Sent (simulated)")

# --- Customer Dashboard ---
elif menu == "Customer Dashboard":
    st.title("Customer Dashboard")
    st.info("Track orders, update profile, and explore services.")

# --- Admin Dashboard ---
elif menu == "Admin Dashboard":
    st.title("Admin Dashboard")
    st.warning("Restricted area. Admin access only.")

# --- Services Page ---
elif menu == "Services":
    st.title("Available Services")
    services = [
        "Plumbing", "Electrical", "House Cleaning", "Appliance Repair", "Gardening",
        "Painting", "Pest Control", "AC Service", "Carpenter", "Mobile Repair"
    ]
    for s in services:
        st.write(f"🔧 {s}")

# --- Cart Page ---
elif menu == "Cart":
    st.title("Your Cart")
    st.info("No items in cart yet.")

# --- Donation Page ---
elif menu == "Donate":
    st.title("Donate to Bokaro Janseva Trust")
    amount = st.slider("Donation Amount (INR)", 1, 100000, 500)
    if st.button("Donate Now"):
        st.success(f"Thank you for donating ₹{amount}!")

# --- Footer ---
st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Dial For Service")
