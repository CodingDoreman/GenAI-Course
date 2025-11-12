# expense_splitter.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Expense Splitter", layout="centered")

# 🌿 Custom CSS for pastel green background
page_bg = """
<style>
    [data-testid="stAppViewContainer"] {
        background-color: #d8f3dc; /* pastel green */
    }
    [data-testid="stHeader"] {
        background: rgba(0,0,0,0);
    }
    [data-testid="stToolbar"] {
        right: 2rem;
    }
    /* improve table/card contrast */
    .stDataFrame table {
        background: rgba(255,255,255,0.9);
    }
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

st.title("🍽️ Expense Splitter")
st.write("Enter total, number of people, then fill names & contributions in the table. Press Calculate to see who owes/gets back and an easy summary column.")

# Step 1: Get total amount and number of people
total = st.number_input("Enter total amount (₹):", min_value=0.0, value=0.0, step=100.0, format="%.2f")
n_people = st.number_input("Enter number of people:", min_value=1, value=2, step=1)

st.markdown("### 👥 Enter Names and Contributions")
# Create initial dataframe sized to number of people
df_input = pd.DataFrame({
    "Name": [f"Person {i+1}" for i in range(int(n_people))],
    "Contribution (₹)": [0.0 for _ in range(int(n_people))]
})

# editable grid
edited_df = st.data_editor(
    df_input,
    num_rows="fixed",
    use_container_width=True,
    key="editor"
)

# Calculate button
if st.button("💰 Calculate Split"):
    # extract inputs
    names = edited_df["Name"].astype(str).tolist()
    # ensure numeric contributions
    contributions = pd.to_numeric(edited_df["Contribution (₹)"], errors="coerce").fillna(0.0).astype(float).tolist()

    n = int(n_people)
    share_each = round(float(total) / n, 2) if n > 0 else 0.0
    balances = [round(c - share_each, 2) for c in contributions]
    total_contrib = round(sum(contributions), 2)

    # build summary strings
    summary_texts = []
    for bal in balances:
        if bal < 0:
            summary_texts.append(f"Owes ₹{abs(bal):,.2f}")
        elif bal > 0:
            summary_texts.append(f"Gets ₹{bal:,.2f}")
        else:
            summary_texts.append("Settled")

    # results dataframe (keep Net numeric for sorting/charting, but show formatted columns)
    result_df = pd.DataFrame({
        "Name": names,
        "Contribution (₹)": [f"{c:,.2f}" for c in contributions],
        "Share (₹)": [f"{share_each:,.2f}" for _ in contributions],
        "Net (₹)": balances,
        "Summary": summary_texts
    })

    # display metrics
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total bill", f"₹ {total:,.2f}")
        st.metric("Sum of contributions", f"₹ {total_contrib:,.2f}")
    with col2:
        st.metric("Per-person share", f"₹ {share_each:,.2f}")

    # show table sorted by Net (Net formatted with sign)
    display_df = result_df.copy()
    display_df = display_df.sort_values("Net (₹)")
    # format Net column for display
    display_df["Net (₹)"] = display_df["Net (₹)"].apply(lambda x: f"{x:+,.2f}")
    st.subheader("📊 Result — who owes / gets back")
    st.table(display_df[["Name", "Contribution (₹)", "Share (₹)", "Net (₹)", "Summary"]])

    # textual summary
    owes = [(names[i], balances[i]) for i in range(len(balances)) if balances[i] < 0]
    gets = [(names[i], balances[i]) for i in range(len(balances)) if balances[i] > 0]
    settled = [names[i] for i in range(len(balances)) if balances[i] == 0]
    
    if settled:
        st.write("⚪ **Settled (exact share):** " + ", ".join(settled))

    # check matching of contributions vs total
    diff = round(total_contrib - float(total), 2)
    if diff < 0:
        st.warning(f"₹ {abs(diff):,.2f} is still unpaid.")
    elif diff > 0:
        st.info(f"₹ {diff:,.2f} extra paid.")
    else:
        st.success("✅ Contributions match the total. All settled!")

    st.markdown("---")
   # st.caption("🌿 Added 'Summary' column and a slim-bar chart for clearer visualization.")
