import streamlit as st

st.set_page_config(
    page_icon=":bulb:",
    page_title="WattsUp",
    layout="wide",
)

st.title(":bulb: :green[O]ffset")

st.success("👈 Want to reduce your carbon footprint, but don't know where to start? Check out Watts-Up's collection of tools to help you get started.")

a1, a2 = st.columns([1, 1], gap="large")
    
with a1:
    st.success("👇 Want to know more about these tools? Click one of these buttons!")
    rb = st.button("Resource Budgeter", type="primary", use_container_width=True)
    ht = st.button("Habit Tracker", type="primary", use_container_width=True)
    ss = st.button("Solar Suitability", type="primary", use_container_width=True)
    bx = st.button("Best of X", type="primary", use_container_width=True)
    lp = st.button("🤫 Extra: Landing Page", use_container_width=True)

with a2:
    if not rb and not ht and not ss and not bx or (lp):
        st.image("https://github.com/Akshu-on-github/MLH-H4H/blob/main/assets/carbon_footprint.png?raw=true", caption="Carbon Footprint - Photo by Evie S.")
    if rb:
        st.image("https://github.com/Akshu-on-github/MLH-H4H/blob/main/assets/esource_budgeter.png?raw=true", caption="Resource Budgeter - Photo by Daniel Norris")
    if ht:
        st.image("https://github.com/Akshu-on-github/MLH-H4H/blob/main/assets/habit_tracker.png?raw=true", caption="Habit Tracker - Photo by Kelly Sikkema")
    if ss:
        st.image("https://github.com/Akshu-on-github/MLH-H4H/blob/main/assets/solar_suitability.png?raw=true", caption="Solar Suitability - Photo by Manny Becerra")
    if bx:
        st.image("https://github.com/Akshu-on-github/MLH-H4H/blob/main/assets/of_x.png?raw=true", caption="Best of X - Photo by Peter Broomfield")

if rb:
    ht = ss = bx = lp = False
    st.subheader("Resource Budgeter")

    image, text = st.columns([1, 2], gap="large")
    with image:
        st.image("https://github.com/Akshu-on-github/MLH-H4H/blob/main/assets/w/design.png?raw=true", caption="Figma Wireframe")
    with text:
        st.markdown("""
            ### Design
            - This was the first component that I worked on, that's why it doesn't have the sidebar
            - My main objective was to make it intuitive and easy to use
            - I wanted to keep the number of questions to a minimum, so I spent a bit of time on that
            - It was fun to experiment with different ways to get user input
        """)

    text, image = st.columns([2, 1], gap="large")
    with image:
        st.image("https://github.com/Akshu-on-github/MLH-H4H/blob/main/assets/w/code.png?raw=true", caption="Screenshot of VSCode")
    with text:
        st.markdown("""
            ### Code
            - While I was working on this, I was also exploring streamlit for the first time
            - Handling data from an external source was a bit tricky, but I managed to figure it out
            - I also had to figure out how to use session state, which took a bit of time
        """)
    st.markdown("👈 Check out the final result in the sidebar!")

if ht:
    rb = ss = bx = lp = False
    st.subheader("Habit Tracker")
    st.markdown("This is Habit Tracker")

    image, text = st.columns([1, 2], gap="large")
    with image:
        st.image("https://github.com/Akshu-on-github/MLH-H4H/blob/main/assets/c/design.png?raw=true", caption="Figma Wireframe")
    with text:
        st.markdown("""
            ### Design
            - At this stage, we realized that this was definitely going to be a multipage app
            - My main objective was to give the users a way to visualize their energy usage
            - I had just realized that I could not use `plt.show()` in streamlit, so I deliberately depicted the graphs as empty rectangles
            - Looking back, the wireframe was pretty simple, but I think it was a good starting point
        """)

    text, image = st.columns([2, 1], gap="large")
    with image:
        st.image("https://github.com/Akshu-on-github/MLH-H4H/blob/main/assets/c/code.png?raw=true", caption="Screenshot of VSCode")
    with text:
        st.markdown("""
            ### Code
            - The statefulness that I introduced in the previous component was very useful here - I had to extend the session state to hold multiple values, which was a bit tricky!
            - Since I wasn't sure if there would be enough data points to fully showcase the functionality, I decided to have mock data as backup
        """)
    st.markdown("👈 Check out the final result in the sidebar!")

if ss:
    rb = ht = bx = lp = False
    st.subheader("Solar Suitability")
    st.markdown("This is Solar Suitability")

    image, text = st.columns([1, 2], gap="large")
    with image:
        st.image("https://github.com/Akshu-on-github/MLH-H4H/blob/main/assets/y/design.png?raw=true", caption="Figma Wireframe")
    with text:
        st.markdown("""
            ### Design
            - Initially, this was supposed to be a cost calculator for solar panels, but we felt that there was a more pressing need for a suitability calculator
            - Solar Panels are not a one size fits all solution, so we wanted to expand on that idea
            - I wanted to make it as simple as possible, so I used a checklist
            - I also wanted to make it as informative as possible while preserving brevity, so I added tooltips
        """)

    text, image = st.columns([2, 1], gap="large")
    with image:
        st.image("https://github.com/Akshu-on-github/MLH-H4H/blob/main/assets/y/code.png?raw=true", caption="Screenshot of VSCode")
    with text:
        st.markdown("""
            ### Code
            - While coding this, I figured out how to convey requirements without taking up too much space
            - I wanted to structure it in such a way that the user only needed to see the warnngs that were applicable to them
            - I also wanted to make it informative as possible without being too verbose, so I added extra information below the warning messages
        """)
    st.markdown("👈 Check out the final result in the sidebar!")
    

if bx:
    rb = ht = ss = lp = False

    st.subheader("Best of X")
    st.markdown("This is Best of X")

    image, text = st.columns([1, 2], gap="large")
    with image:
        st.image("https://github.com/Akshu-on-github/MLH-H4H/blob/main/assets/lp/design.png?raw=true", caption="Figma Wireframe")
    with text:
        st.markdown("""
            ### Design
            - Initially the Best of X was designed to allow the consumer to get all the details of different cars so they can compare other cars.
            - But due to time constraint I had to change it to allow the consumer to get them what can be there dream cars by getting their needs.
            - Consumers can get the details of the cars and get there cars according to their cars
            
        """)

    text, image = st.columns([2, 1], gap="large")
    with image:
        st.image("https://github.com/Akshu-on-github/MLH-H4H/blob/main/assets/lp/code.png?raw=true", caption="Screenshot of VSCode")
    with text:
        st.markdown("""
            ### Code
            - I have no prior knowledge of streamlit but it was easy to use and allowed to easy implement my code.
            - Because of this it was a great experirence.I wanted to make this so that consumer can get their dream car from a big database
            - I beleive that with this people can get great cars according to their budget. Every car has it's own benefit.
                            """)
    st.markdown("👈 Check out the final result in the sidebar!")

if lp:
    rb = ht = ss = bx = False

    st.subheader("Landing Page")
    st.markdown("This is Landing Page")

    image, text = st.columns([1, 2], gap="large")
    with image:
        st.image("https://github.com/Akshu-on-github/MLH-H4H/blob/main/assets/lp/design.png?raw=true", caption="Figma Wireframe")
    with text:
        st.markdown("""
            ### Design
            - The design ended up having a lot more elements than I had anticipated
            - Initially, I wanted write up a business use case for all of the components in series, but I realized that it would be too much
            - Consequently, I decided to make it a bit more interactive, and allow the user to explore the components on their own
        """)

    text, image = st.columns([2, 1], gap="large")
    with image:
        st.image("https://github.com/Akshu-on-github/MLH-H4H/blob/main/assets/lp/code.png?raw=true", caption="Screenshot of VSCode")
    with text:
        st.markdown("""
            ### Code
            - Figuring out how to toggle views using buttons was the trickiest part
            - However, writing up the desctiptions and turne out to be the most time consuming task
            - Since I was adding elements as I was designing, I had to figure out how to juggle design and code
            - Still, I'm pretty happy with how it turned out
            - I hope you enjoyed this little easter egg 🐣
        """)
