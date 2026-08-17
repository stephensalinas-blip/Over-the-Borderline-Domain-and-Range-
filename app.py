import os
import time
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Over the Borderline: Domain and Range",
    layout="wide"
)

# Custom Cyberpunk/Arcade Theme Styling
st.markdown("""
<style>
    /* Dark grid background */
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #1a103c, #24243e);
        color: #ffffff;
        font-family: 'Poppins', sans-serif;
    }
    
    /* Glowing Title Header Card */
    .title-banner {
        text-align: center;
        padding: 25px;
        background: rgba(255, 255, 255, 0.03);
        border-radius: 16px;
        border: 2px solid #00ffcc;
        box-shadow: 0 0 25px rgba(0, 255, 204, 0.25);
        margin-bottom: 30px;
    }
    
    .main-title {
        font-size: 3rem;
        font-weight: 900;
        letter-spacing: 2px;
        background: linear-gradient(90deg, #ff007f, #00ffcc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-transform: uppercase;
        margin-bottom: 5px;
    }
    
    .sub-title {
        font-size: 1.3rem;
        color: #d1d5db;
        letter-spacing: 3px;
        font-weight: 600;
        text-transform: uppercase;
    }

    /* Question Cards */
    div[data-testid="stVerticalBlock"] > div {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 18px;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Interactive Buttons */
    .stButton > button {
        background: linear-gradient(90deg, #ff007f, #7928ca);
        color: white;
        font-size: 1rem;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        padding: 10px 24px;
        box-shadow: 0 0 12px rgba(255, 0, 127, 0.4);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) scale(1.02);
        box-shadow: 0 0 22px rgba(0, 255, 204, 0.8);
    }
</style>
""", unsafe_allow_html=True)

# Session State Initialization
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
if "stage" not in st.session_state:
    st.session_state.stage = 1
if "stage1_passed" not in st.session_state:
    st.session_state.stage1_passed = False
if "stage2_passed" not in st.session_state:
    st.session_state.stage2_passed = False
if "stage3_passed" not in st.session_state:
    st.session_state.stage3_passed = False

# Sidebar Controls
st.sidebar.title("Mission Control")

# Background Audio Player
if os.path.exists("bgm.mp3"):
    st.sidebar.subheader("Audio Controls")
    st.sidebar.audio("bgm.mp3", loop=True)

# Live Timer Tracker
elapsed_sec = int(time.time() - st.session_state.start_time)
mins, secs = divmod(elapsed_sec, 60)
st.sidebar.metric(label="Elapsed Time", value=f"{mins:02d}:{secs:02d}")

if elapsed_sec <= 2400:
    st.sidebar.info("Bonus Incentive Active: Complete in under 40:00 for +1 Quiz Score.")
else:
    st.sidebar.warning("40-Minute Bonus Time Expired.")

st.sidebar.markdown("---")
st.sidebar.markdown(f"**Current Stage:** Room {st.session_state.stage} of 3")
st.sidebar.markdown("**Mastery Threshold:** 17 / 20 correct answers per stage.")

# Main Title Display
st.markdown("""
    <div class="title-banner">
        <div class="main-title">Over the Borderline</div>
        <div class="sub-title">Domain and Range Escape Room</div>
    </div>
""", unsafe_allow_html=True)

# Question Data Bank (60 Questions Total)
questions_stage1 = [
    {"q": "1. Is the set of ordered pairs {(1,2), (2,3), (3,4), (4,5)} a function?", "opts": ["Yes", "No"], "a": "Yes"},
    {"q": "2. Is the relation {(1,2), (1,3), (2,4)} a function?", "opts": ["Yes", "No"], "a": "No"},
    {"q": "3. What is the domain of {(2,5), (3,7), (4,9)}?", "opts": ["{2, 3, 4}", "{5, 7, 9}", "{2, 5}"], "a": "{2, 3, 4}"},
    {"q": "4. What is the range of {(2,5), (3,7), (4,9)}?", "opts": ["{2, 3, 4}", "{5, 7, 9}", "{5, 9}"], "a": "{5, 7, 9}"},
    {"q": "5. A test used to determine if a graph represents a function is the...", "opts": ["Vertical Line Test", "Horizontal Line Test", "Diagonal Line Test"], "a": "Vertical Line Test"},
    {"q": "6. In the function f(x) = 3x + 2, the input variable x represents the...", "opts": ["Independent Variable", "Dependent Variable", "Constant"], "a": "Independent Variable"},
    {"q": "7. Domain of {(0,1), (0,2), (0,3)} is:", "opts": ["{0}", "{1, 2, 3}", "{0, 1, 2, 3}"], "a": "{0}"},
    {"q": "8. Range of {(-1,4), (0,4), (1,4)} is:", "opts": ["{-1, 0, 1}", "{4}", "{-1, 4}"], "a": "{4}"},
    {"q": "9. Does a vertical line graph represent a function?", "opts": ["Yes", "No"], "a": "No"},
    {"q": "10. Does a horizontal line graph represent a function?", "opts": ["Yes", "No"], "a": "Yes"},
    {"q": "11. If f(x) = 2x - 5, what is f(3)?", "opts": ["1", "3", "11"], "a": "1"},
    {"q": "12. What is the domain of any linear function f(x) = mx + b?", "opts": ["All Real Numbers", "x >= 0", "x > 0"], "a": "All Real Numbers"},
    {"q": "13. In a mapping diagram, if one input points to two outputs, the relation is...", "opts": ["Not a function", "A function", "Linear"], "a": "Not a function"},
    {"q": "14. Set of input values for a relation is called...", "opts": ["Domain", "Range", "Codomain"], "a": "Domain"},
    {"q": "15. Set of output values for a relation is called...", "opts": ["Range", "Domain", "Relation"], "a": "Range"},
    {"q": "16. Is y = x^2 a function?", "opts": ["Yes", "No"], "a": "Yes"},
    {"q": "17. Is x = y^2 a function?", "opts": ["Yes", "No"], "a": "No"},
    {"q": "18. Evaluate f(-2) for f(x) = x + 7.", "opts": ["5", "9", "-5"], "a": "5"},
    {"q": "19. Evaluate f(0) for f(x) = -4x + 10.", "opts": ["10", "0", "-4"], "a": "10"},
    {"q": "20. The graph of a circle represents a function.", "opts": ["False", "True"], "a": "False"}
]

questions_stage2 = [
    {"q": "1. What is the domain of f(x) = 1 / x?", "opts": ["x != 0", "All Real Numbers", "x > 0"], "a": "x != 0"},
    {"q": "2. What is the domain of f(x) = sqrt(x)?", "opts": ["x >= 0", "All Real Numbers", "x > 0"], "a": "x >= 0"},
    {"q": "3. What is the range of f(x) = x^2?", "opts": ["y >= 0", "All Real Numbers", "y > 0"], "a": "y >= 0"},
    {"q": "4. What is the domain of f(x) = 1 / (x - 3)?", "opts": ["x != 3", "x != -3", "x > 3"], "a": "x != 3"},
    {"q": "5. What is the domain of f(x) = sqrt(x - 5)?", "opts": ["x >= 5", "x >= 0", "x > 5"], "a": "x >= 5"},
    {"q": "6. Range of f(x) = |x| is:", "opts": ["y >= 0", "All Real Numbers", "y <= 0"], "a": "y >= 0"},
    {"q": "7. Domain of f(x) = (x + 2) / (x^2 - 4) excludes:", "opts": ["x = 2 and x = -2", "x = 2 only", "x = 0"], "a": "x = 2 and x = -2"},
    {"q": "8. Range of f(x) = x^2 + 4 is:", "opts": ["y >= 4", "y >= 0", "All Real Numbers"], "a": "y >= 4"},
    {"q": "9. Range of f(x) = -x^2 is:", "opts": ["y <= 0", "y >= 0", "All Real Numbers"], "a": "y <= 0"},
    {"q": "10. Domain of f(x) = 5 / (2x - 8) is:", "opts": ["x != 4", "x != 8", "x != 2"], "a": "x != 4"},
    {"q": "11. Domain of f(x) = sqrt(2x + 6) is:", "opts": ["x >= -3", "x >= 3", "x >= 0"], "a": "x >= -3"},
    {"q": "12. Domain of a polynomial function is always:", "opts": ["All Real Numbers", "x > 0", "x != 0"], "a": "All Real Numbers"},
    {"q": "13. What is the restriction for rational function domains?", "opts": ["Denominator != 0", "Radicand >= 0", "Numerator != 0"], "a": "Denominator != 0"},
    {"q": "14. Range of f(x) = 3x - 1 is:", "opts": ["All Real Numbers", "y >= 0", "y != 0"], "a": "All Real Numbers"},
    {"q": "15. Domain of f(x) = 1 / (x^2 + 1) is:", "opts": ["All Real Numbers", "x != -1", "x != 1"], "a": "All Real Numbers"},
    {"q": "16. Range of f(x) = -|x| + 2 is:", "opts": ["y <= 2", "y >= 2", "y <= 0"], "a": "y <= 2"},
    {"q": "17. Domain of f(x) = sqrt(4 - x) is:", "opts": ["x <= 4", "x >= 4", "x >= 0"], "a": "x <= 4"},
    {"q": "18. What is the horizontal asymptote of f(x) = 1 / x?", "opts": ["y = 0", "x = 0", "y = 1"], "a": "y = 0"},
    {"q": "19. What is the vertical asymptote of f(x) = 1 / (x + 1)?", "opts": ["x = -1", "x = 1", "y = -1"], "a": "x = -1"},
    {"q": "20. Range of f(x) = (x - 1)^2 - 3 is:", "opts": ["y >= -3", "y >= 1", "y >= 0"], "a": "y >= -3"}
]

questions_stage3 = [
    {"q": "1. A store sells items for 5 dollars each. Domain for number of items sold x is:", "opts": ["Non-negative Integers", "All Real Numbers", "x <= 0"], "a": "Non-negative Integers"},
    {"q": "2. Height of a ball dropped from 100 ft: h(t) = -16t^2 + 100. Domain contextually represents:", "opts": ["Time until ball hits ground", "All Real Numbers", "Negative Time"], "a": "Time until ball hits ground"},
    {"q": "3. Piecewise function: f(x) = x for x < 0, and f(x) = 2x for x >= 0. Domain is:", "opts": ["All Real Numbers", "x >= 0", "x < 0"], "a": "All Real Numbers"},
    {"q": "4. Range of f(x) = 2^x is:", "opts": ["y > 0", "y >= 0", "All Real Numbers"], "a": "y > 0"},
    {"q": "5. Domain of f(x) = log(x) is:", "opts": ["x > 0", "x >= 0", "All Real Numbers"], "a": "x > 0"},
    {"q": "6. A car travels at 60 mph for 3 hours. Distance d(t) = 60t. Domain for t is:", "opts": ["[0, 3]", "All Real Numbers", "t >= 60"], "a": "[0, 3]"},
    {"q": "7. Range for distance d(t) = 60t where t is in [0, 3]:", "opts": ["[0, 180]", "[0, 60]", "All Real Numbers"], "a": "[0, 180]"},
    {"q": "8. What is the domain of f(x) = 1 / sqrt(x)?", "opts": ["x > 0", "x >= 0", "x != 0"], "a": "x > 0"},
    {"q": "9. If range of f(x) is y >= 2, range of f(x) + 3 is:", "opts": ["y >= 5", "y >= 2", "y >= 3"], "a": "y >= 5"},
    {"q": "10. Domain of f(x) = sqrt(x^2 - 9) is:", "opts": ["x <= -3 or x >= 3", "-3 <= x <= 3", "x >= 3"], "a": "x <= -3 or x >= 3"},
    {"q": "11. Range of constant function f(x) = 7 is:", "opts": ["{7}", "All Real Numbers", "y >= 7"], "a": "{7}"},
    {"q": "12. Maximum point of parabola with range y <= 5 is at y = ...", "opts": ["5", "0", "-5"], "a": "5"},
    {"q": "13. In a real-world scenario, can area of a square have a negative domain?", "opts": ["No", "Yes"], "a": "No"},
    {"q": "14. Domain of f(x) = (x - 1)/(x^2 - 1) is:", "opts": ["x != 1 and x != -1", "x != 1 only", "All Real Numbers"], "a": "x != 1 and x != -1"},
    {"q": "15. What is the range of f(x) = sin(x)?", "opts": ["[-1, 1]", "[0, 1]", "All Real Numbers"], "a": "[-1, 1]"},
    {"q": "16. What is the range of f(x) = cos(x) + 2?", "opts": ["[1, 3]", "[0, 2]", "[-1, 1]"], "a": "[1, 3]"},
    {"q": "17. Domain of composite relation where inner function is undefined at x=2:", "opts": ["Excludes x = 2", "Includes x = 2", "All Real Numbers"], "a": "Excludes x = 2"},
    {"q": "18. Step function f(x) = floor(x) has a range of:", "opts": ["All Integers", "All Real Numbers", "Positive Numbers"], "a": "All Integers"},
    {"q": "19. If domain of f(x) is [0, 10], domain of f(x - 2) is:", "opts": ["[2, 12]", "[-2, 8]", "[0, 10]"], "a": "[2, 12]"},
    {"q": "20. Final Escape Lock: If domain is [0, infinity) and range is (-infinity, 0], graph sits in Quadrant:", "opts": ["IV", "I", "II"], "a": "IV"}
]

# Room Rendering Logic
def render_stage(stage_num, question_set, state_flag):
    st.header(f"STAGE {stage_num}: ESCAPE ROOM GATEWAY")
    st.write("Answer the 20 questions below. Score at least 17/20 to unlock the gate.")
    
    user_answers = []
    with st.form(f"stage_{stage_num}_form"):
        for idx, q in enumerate(question_set):
            ans = st.radio(q["q"], q["opts"], key=f"s{stage_num}_q{idx}")
            user_answers.append((ans, q["a"]))
        
        submitted = st.form_submit_button(f"Submit Stage {stage_num} Answers")
        
        if submitted:
            score = sum(1 for user_a, correct_a in user_answers if user_a == correct_a)
            st.write(f"**Your Score:** {score} / 20")
            st.progress(score / 20)
            
            if score >= 17:
                st.session_state[state_flag] = True
                st.success(f"STAGE {stage_num} CLEARED! Gate unlocked.")
                if stage_num < 3:
                    st.session_state.stage = stage_num + 1
                    st.rerun()
            else:
                st.error(f"Mastery Threshold Not Met (17/20 required). Review your answers and try again.")

# Stage Controller
if st.session_state.stage == 1:
    render_stage(1, questions_stage1, "stage1_passed")

elif st.session_state.stage == 2:
    if not st.session_state.stage1_passed:
        st.warning("You must complete Stage 1 first!")
        st.session_state.stage = 1
        st.rerun()
    else:
        render_stage(2, questions_stage2, "stage2_passed")

elif st.session_state.stage == 3:
    if not st.session_state.stage2_passed:
        st.warning("You must complete Stage 2 first!")
        st.session_state.stage = 2
        st.rerun()
    else:
        render_stage(3, questions_stage3, "stage3_passed")

# Final Victory Screen
if st.session_state.stage3_passed:
    st.balloons()
    total_time = int(time.time() - st.session_state.start_time)
    final_mins, final_secs = divmod(total_time, 60)
    
    st.markdown("""
        <div style="text-align: center; border: 3px solid #00ffcc; padding: 30px; border-radius: 20px; background: rgba(0,255,204,0.1);">
            <h1 style="color: #00ffcc;">ESCAPE SUCCESSFUL!</h1>
            <h3>You have mastered Domain, Range, and Functions!</h3>
        </div>
    """, unsafe_allow_html=True)
    
    st.write(f"**Total Completion Time:** {final_mins} minutes and {final_secs} seconds.")
    
    if total_time <= 2400:
        st.success("BONUS EARNED: Sub-40 Minute Completion! Show this screen to your teacher for +1 Quiz Score Bonus.")
    else:
        st.info("Completed successfully! (Over 40 minutes - Bonus incentive target missed).")
