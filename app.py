import streamlit as st
import pandas as pd
from src.scraper import get_county_data, get_msme_impact_data
from src.calculator import calculate_tps, get_category
from src.ui_components import plot_funnel, plot_impact_bar

# --- THEME & CONFIG ---
K_GREEN = "#006633"
K_GOLD = "#FFD700"
st.set_page_config(page_title="Kenya AHP Monitor", layout="wide")

# --- LOAD DATA ---
df = get_county_data()
msme_stats, supply_df = get_msme_impact_data()

# --- SIDEBAR: SEARCH ---
st.sidebar.title("🇰🇪 AHP Project Finder")
search_query = st.sidebar.text_input("Search by County or Project Name", placeholder="Try 'Kiambu' or 'Starehe'")
st.sidebar.divider()
st.sidebar.caption("National Housing Registry v2.2")

# --- MAIN TABS ---
tab1, tab2, tab3 = st.tabs(["📊 National Project Monitor", "🛠️ Jua Kali & MSMEs", "🏠 My Boma Calculator"])

with tab1:
    st.title("AHP National Project Directory")
    
    # Filter Logic
    if search_query:
        display_df = df[df['County'].str.contains(search_query, case=False) | 
                        df['Project'].str.contains(search_query, case=False)]
    else:
        display_df = df

    # KPI Summary
    m1, m2, m3 = st.columns(3)
    m1.metric("National Applicants", "1.1M+")
    m2.metric("Filtered Projects", f"{len(display_df)}")
    m3.metric("Total Planned Units", f"{display_df['Units'].sum():,}")

    st.divider()
    
    col_l, col_r = st.columns([2, 1])
    with col_l:
        st.subheader("Interactive Project List")
        # Display the table with all projects across 47 counties
        st.dataframe(display_df.sort_values(by=["County", "Units"], ascending=[True, False]), 
                     use_container_width=True, hide_index=True)
    
    with col_r:
        st.subheader("Program Progress")
        st.plotly_chart(plot_funnel(K_GREEN), use_container_width=True)

with tab2:
    st.header("MSME Transformation")
    st.write(f"Contracts totaling **{msme_stats['budget']}** have been awarded to local Jua Kali clusters.")
    st.plotly_chart(plot_impact_bar(supply_df, K_GOLD), use_container_width=True)
    st.table(supply_df)

with tab3:
    st.header("🏠 Boma Yangu: My Ownership Calculator")
    st.markdown("Calculate your monthly 'Rent-to-Own' cost based on the official 7% TPS rate.")
    
    col_input, col_result = st.columns(2)
    
    with col_input:
        # User inputs for income and house price
        user_income = st.number_input("Monthly Household Income (KES)", value=45000, step=5000)
        house_price = st.selectbox("Select Target Unit Price", 
                                   [1000000, 1500000, 2000000, 3000000, 4000000, 5000000],
                                   format_func=lambda x: f"KES {x:,}")
        user_savings = st.number_input("Current Boma Yangu Savings (Deposit)", value=int(house_price * 0.1), step=10000)

    with col_result:
        # Calculate the logic using our src/calculator.py engine
        category = get_category(user_income)
        monthly_payment = calculate_tps(house_price, user_savings)
        
        st.write(f"### Eligibility: **{category}**")
        st.metric("Estimated Monthly Payment", f"KES {monthly_payment:,.2f}")
        
        # Friendly breakdown for someone who understands nothing
        st.info(f"""
        **How it works:**
        - **Deposit:** You are paying KES {user_savings:,} upfront.
        - **Duration:** 25 Years (300 months).
        - **Interest:** Fixed at 7% (Government-backed).
        """)
        
        if monthly_payment > (user_income * 0.4):
            st.warning("⚠️ Warning: This payment exceeds 40% of your income. Consider a lower-priced unit.")
        else:
            st.success("✅ This unit fits your budget based on standard affordability rules.")
