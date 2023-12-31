import streamlit as st
import pandas as pd

if 'count' not in st.session_state:
    st.session_state.count = 0
if 'appliance' not in st.session_state:
    st.session_state.appliance = []

st.set_page_config(
    page_icon=":books:",
    page_title="App",
    layout="wide",
)

st.header("Resource Budgeter")
st.markdown("The Resource Budgeter falls under the **Habitual** and **Awareness** categories of Green IoT Techniques", help="[Green IoT: An Investigation on Energy Saving Practices for 2020 and Beyond](https://www.researchgate.net/publication/318797858_Green_IoT_An_Investigation_on_Energy_Saving_Practices_for_2020_and_Beyond)")
st.markdown("This component creates a resource budget according to your household needs. It combines concepts like Habit Tracking and Smart Metering to help you identify the most significant areas of energy consumption, and suggests suitable conservation measures. The below metrics are taken from a study on [US households](https://www.eia.gov/energyexplained/use-of-energy/electricity-use-in-homes.php) and [Generatorist](https://generatorist.com/list-of-electric-appliances-their-wattage-usage).")

st.markdown("""
    <style>
                .marquee {
                background-color: #e6ffe6;
                width: 100%;
                line-height: 2rem;
                margin: 0 auto;
                overflow: hidden;
                box-sizing: border-box;
                border: 1px solid #ccc;
                border-radius: 5px;
                }

                .marquee span {
                display: inline-block;
                width: max-content;

                padding-left: 100%;
                /* show the marquee just outside the paragraph */
                will-change: transform;
                animation: marquee 20s linear infinite;
                }

                .marquee span:hover {
                animation-play-state: paused
                }


                @keyframes marquee {
                0% { transform: translate(0, 0); }
                100% { transform: translate(-100%, 0); }
                }

                @media (prefers-reduced-motion: reduce) {
                    .marquee span {
                        animation-iteration-count: 1;
                        animation-duration: 0.01; 
                        /* instead of animation: none, so an animationend event is 
                        * still available, if previously attached.
                        */
                        width: auto;
                        padding-left: 0;
                    }
                }
                </style>
    <p class = "marquee">
        <span>Quick Tip: Feel like the criteria is a bit vague? Check out the little question symbols on the side of the checkboxes - they provide further informaton</span>
    </p>
    <br>
""", unsafe_allow_html=True)

monthly_budget = st.slider("Monthly Budget", min_value=200, max_value=2500, step=50, format=None, key=None, help="in kilowatthours (kWH)", on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
daily_limit = monthly_budget//31

sheet_name = "Appliance_Electricity_Budget"
sheet_id = "1i0cOEFvfK6hQwfPDcoQ8BN1inneoRdKdY1VK3BuxwGE"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df = pd.read_csv(url, dtype=str)
# st.write(df)

count = []
sum = 0

c1, c2, c3 = st.columns([2, 1, 1], gap="small")

with c1:
    appliance = st.selectbox("Appliance", df["Appliance"])
with c2: 
    hours = st.number_input("Hours", min_value=0, max_value=24, step=1, format=None, key=None, on_change=None, args=None, kwargs=None, disabled=False)
with c3:
    minutes = st.number_input("Minutes", min_value=0, max_value=60, step=15, format=None, key=None, on_change=None, args=None, kwargs=None, disabled=False)

m1 = df["Appliance"].str.fullmatch(appliance, case=False)
df_search = df[m1]

count = []
sum = 0

if appliance:
    st.write(df_search)
    count.append(df_search["Wattage"].to_numpy(dtype=int))

spent = count[0][0] / 1000 * (hours + (minutes/60))
spent = round(spent, 2)
st.write("Expenditure: ", spent, "`kwh`")

b1, b2, b3 = st.columns([1, 1, 2], gap="small")
with b1:
    add = st.button("Add to Budget", use_container_width=True)
with b2:
    clear = st.button("Clear Budget", use_container_width=True)

if add and (hours != 0 or minutes != 0):
    st.session_state.count += spent
    appliances = []
    appliances.append(df_search["Appliance"].to_numpy(dtype=str)[0])
    appliances.append(spent)
    st.session_state.appliance.append(appliances)
if clear:
    st.session_state.count = 0
    st.session_state.appliance = []

r1, r2, r3, r4 = st.columns([1, 1, 1, 1], gap="small")
with r1: 
    st.metric("Daily Limit", daily_limit, help="in kWh", label_visibility="visible")
with r2: 
    st.metric("Total Spent", round(st.session_state.count, 2), help="in kWh", label_visibility="visible")
with r3:
    remaining = daily_limit - st.session_state.count
    if remaining >= 0:
        st.metric(":green[Remaining]", round(remaining, 2), help="in kWh", label_visibility="visible")
    else:
        st.metric("**:red[Remaining]**", round(remaining, 2), help="in kWh", label_visibility="visible")

if daily_limit < st.session_state.count:
    st.error("You're over your daily limit! Refer to our [Habit Tracker](./Habit_Tracker) to identify appliances that consume the most energy.")
if st.session_state.count > 500//31:
    st.success("Check out [Solar Suitability](./Solar_Suitability) to see if solar panels are a good fit for your home.")