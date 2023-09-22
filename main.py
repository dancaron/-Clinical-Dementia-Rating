import streamlit as st

def compute_cdr(memory, orientation, judgment, community, home, personal):
    sum_of_boxes = memory + orientation + judgment + community + home + personal
    if sum_of_boxes == 0:
        return 0
    elif sum_of_boxes >= 0.5 and memory == 0.5:
        return 0.5
    elif sum_of_boxes >= 1 and memory >= 0.5:
        return 1
    elif sum_of_boxes >= 3 and memory >= 1:
        return 2
    elif sum_of_boxes >= 7 and memory >= 2:
        return 3
    else:
        return "Unclassified"

st.title("Clinical Dementia Rating (CDR) Calculator")

st.write("Please select the scores for each domain:")

memory = st.selectbox("Memory:", [0, 0.5, 1, 2, 3])
orientation = st.selectbox("Orientation:", [0, 0.5, 1, 2, 3])
judgment = st.selectbox("Judgment & Problem Solving:", [0, 0.5, 1, 2, 3])
community = st.selectbox("Community Affairs:", [0, 0.5, 1, 2, 3])
home = st.selectbox("Home & Hobbies:", [0, 0.5, 1, 2, 3])
personal = st.selectbox("Personal Care:", [0, 0.5, 1, 2, 3])

cdr = compute_cdr(memory, orientation, judgment, community, home, personal)

st.write(f"Computed CDR Score: **{cdr}**")

if st.button("Reset"):
    memory, orientation, judgment, community, home, personal = 0, 0, 0, 0, 0, 0
