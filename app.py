import streamlit as st

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Emoji_u1f985.svg/2048px-Emoji_u1f985.svg.png", width=100)  # Placeholder eagle logo

st.title("Sokol Group Business Valuation")

st.header("Input Financial Data")
profit = st.number_input("Net Profit ($)", min_value=0.0)
liabilities = st.number_input("Liabilities ($)", min_value=0.0)
owners_earnings = st.number_input("Owner's Earnings ($)", min_value=0.0)

st.header("Valuation Multiples")
sde_multiple = st.number_input("SDE Multiple", min_value=0.0, value=2.5)
ebitda_multiple = st.number_input("EBITDA Multiple", min_value=0.0, value=4.0)
discount_rate = st.number_input("Discount Rate (%)", min_value=0.1, value=10.0)

st.header("Valuation Results")

# SDE Valuation
sde_valuation = owners_earnings * sde_multiple
st.subheader("SDE Valuation")
st.write(f"${sde_valuation:,.2f}")

# EBITDA Valuation
ebitda_valuation = profit * ebitda_multiple
st.subheader("EBITDA Valuation")
st.write(f"${ebitda_valuation:,.2f}")

# DCF Valuation
dcf_valuation = profit / (discount_rate / 100)
st.subheader("DCF Valuation")
st.write(f"${dcf_valuation:,.2f}")
