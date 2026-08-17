import streamlit as st
import time
import os
import base64

st.set_page_config(page_title="General Math Escape Room", page_icon="🔒", layout="centered")

# --- AUDIO EMBEDDER ---
def load_bgm():
    audio_file = "bgm.mp3"
    if not os.path.exists(audio_file) and os.path.exists("bgm.mp3.mp3"):
        audio_file = "bgm.mp3.mp3"

    if os.path.exists(audio_file):
        with open(audio_file, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            st.markdown(
                f"""
                <audio autoplay loop style="display:none;">
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                """,
                unsafe_allow_html=True
            )

# --- QUESTION BANK ---
ROOM_1_QUESTIONS = [
    {"level": "Easy (1/20)", "question": "What is a set of ordered pairs (x, y) called?", "options": ["A) Relation", "B) Function", "C) Asymptote", "D) Domain"], "answer": "A", "explanation": "A relation is simply any set of ordered pairs (x, y)."},
    {"level": "Easy (2/20)", "question": "In a relation, what is the set of all second components (y-values)?", "options": ["A) Domain", "B) Range", "C) Input", "D) Slope"], "answer": "B", "explanation": "Range refers strictly to the set of output y-values."},
    {"level": "Easy (3/20)", "question": "Which core rule defines a function?", "options": ["A) Every y-value has two x-values", "B) Every x-value is paired with EXACTLY ONE y-value", "C) All x-values must equal zero", "D) The graph must be a straight line"], "answer": "B", "explanation": "A relation is a function if and only if each input x has a unique output y."},
    {"level": "Easy (4/20)", "question": "Which graphical test determines if a drawn curve is a function?", "options": ["A) Horizontal Line Test", "B) Vertical Line Test", "C) Diagonal Test", "D) Circle Test"], "answer": "B", "explanation": "If a vertical line crosses a graph in more than one point, it fails the function test."},
    {"level": "Easy (5/20)", "question": "Which type of correspondence is ALWAYS a valid function?", "options": ["A) One-to-Many", "B) Many-to-One", "C) One-to-All", "D) Many-to-Many"], "answer": "B", "explanation": "Many-to-one (e.g., y = x^2) is a valid function because each x still yields only one y."},
    {"level": "Medium (6/20)", "question": "Is S = {(1, 2), (2, 3), (3, 4), (4, 5)} a function?", "options": ["A) Yes, all x-values are unique", "B) No, numbers are increasing", "C) No, y-values repeat", "D) It is an equation, not a relation"], "answer": "A", "explanation": "No x-value repeats, so every input has exactly one output."},
    {"level": "Medium (7/20)", "question": "Is R = {(2, 5), (2, 6), (3, 7)} a function?", "options": ["A) Yes", "B) No, the input 2 maps to both 5 and 6", "C) Yes, because 3 maps to 7", "D) No, range values are wrong"], "answer": "B", "explanation": "The input x = 2 has two different outputs (5 and 6), breaking the function rule."},
    {"level": "Medium (8/20)", "question": "Which mapping correspondence is NEVER a function?", "options": ["A) One-to-One", "B) Many-to-One", "C) One-to-Many", "D) Constant mapping"], "answer": "C", "explanation": "One-to-many assigns a single input to multiple outputs."},
    {"level": "Medium (9/20)", "question": "Does the set T = {(1, 4), (2, 4), (3, 4)} represent a function?", "options": ["A) Yes, it is a constant function (Many-to-One)", "B) No, y = 4 repeats", "C) No, x-values must be identical", "D) It is an undefined relation"], "answer": "A", "explanation": "Multiple x-values can output the same y-value without breaking function rules."},
    {"level": "Medium (10/20)", "question": "Does the line y = 3x + 2 represent y as a function of x?", "options": ["A) Yes, every x gives one unique y", "B) No, it has a slope", "C) No, x can yield two outputs", "D) Only if x > 0"], "answer": "A", "explanation": "All non-vertical linear equations are valid functions."},
    {"level": "Hard (11/20)", "question": "Does y = x^2 + 3 represent y as a function of x?", "options": ["A) Yes", "B) No, x is squared", "C) No, it yields +/- values", "D) Only for negative x"], "answer": "A", "explanation": "Squaring x gives one unique result for any single value of x."},
    {"level": "Hard (12/20)", "question": "Does x = y^2 represent y as a function of x?", "options": ["A) Yes", "B) No, solving for y gives y = +/- sqrt(x) (two outputs for one input)", "C) Yes, if x is negative", "D) Only if y = 0"], "answer": "B", "explanation": "An even exponent on y means one x-value yields two y-values (e.g., x = 4 gives y = 2 and y = -2)."},
    {"level": "Hard (13/20)", "question": "Which of the following equations fails to represent a function?", "options": ["A) y = |x|", "B) x^2 + y^2 = 25", "C) y = 1/x", "D) y = x^3"], "answer": "B", "explanation": "x^2 + y^2 = 25 represents a circle, which fails the Vertical Line Test."},
    {"level": "Hard (14/20)", "question": "Which rule correctly relates functions and relations?", "options": ["A) All relations are functions", "B) All functions are relations, but not all relations are functions", "C) Functions have no domain", "D) Relations are always linear"], "answer": "B", "explanation": "Functions are a specific restricted subset of all relations."},
    {"level": "Hard (15/20)", "question": "Is y = |x - 2| a function of x?", "options": ["A) Yes, absolute value yields a single clear output for every input", "B) No, absolute value makes two outputs", "C) Only when x > 2", "D) No, it forms a vertical line"], "answer": "A", "explanation": "Every input x produces exactly one non-negative output y."},
    {"level": "Master (16/20)", "question": "If f(x) = 3x - 5, what is the value of f(4)?", "options": ["A) 7", "B) 12", "C) 17", "D) -1"], "answer": "A", "explanation": "f(4) = 3(4) - 5 = 12 - 5 = 7."},
    {"level": "Master (17/20)", "question": "If f(x) = x^2 - 2x, evaluate f(-3):", "options": ["A) 3", "B) 15", "C) -3", "D) 21"], "answer": "B", "explanation": "f(-3) = (-3)^2 - 2(-3) = 9 + 6 = 15."},
    {"level": "Master (18/20)", "question": "A vending machine button dispensing a random drink each time is an analogy for a:", "options": ["A) Valid Function", "B) One-to-Many Relation (Not a Function)", "C) Linear Model", "D) Constant Function"], "answer": "B", "explanation": "One input giving multiple unpredictable outputs violates the function rule."},
    {"level": "Master (19/20)", "question": "Given f(x) = 2x + 1 and g(x) = x^2, find the composite value f(g(3)):", "options": ["A) 19", "B) 49", "C) 13", "D) 37"], "answer": "A", "explanation": "g(3) = 3^2 = 9. Then f(9) = 2(9) + 1 = 19."},
    {"level": "Master (20/20)", "question": "Why is the vertical line x = 4 NOT a function?", "options": ["A) It has zero slope", "B) The single input x = 4 maps to infinitely many y-values", "C) It has no y-intercept", "D) Its domain is all real numbers"], "answer": "B", "explanation": "An infinite set of points share x = 4, failing the function definition completely."}
]

ROOM_2_QUESTIONS = [
    {"level": "Easy (1/20)", "question": "A function forming a straight line with constant slope y = mx + b is a:", "options": ["A) Linear Function", "B) Quadratic Function", "C) Exponential Function", "D) Rational Function"], "answer": "A", "explanation": "Linear functions have a constant rate of change and straight-line graphs."},
    {"level": "Easy (2/20)", "question": "A U-shaped curve graph defined by y = ax^2 + bx + c is a:", "options": ["A) Linear Function", "B) Quadratic Function (Parabola)", "C) Logarithmic Function", "D) Step Function"], "answer": "B", "explanation": "Quadratic equations graph as parabolic U-shapes."},
    {"level": "Easy (3/20)", "question": "A function where the variable x is in the exponent (y = a * b^x) is an:", "options": ["A) Exponential Function", "B) Polynomial Function", "C) Absolute Value Function", "D) Radical Function"], "answer": "A", "explanation": "Variables placed in exponents define exponential functions."},
    {"level": "Easy (4/20)", "question": "A function defined by different formulas for different sub-domains is a:", "options": ["A) Piecewise Function", "B) Constant Function", "C) Linear Function", "D) Identity Function"], "answer": "A", "explanation": "Piecewise functions apply different operational rules across different intervals."},
    {"level": "Easy (5/20)", "question": "A fraction composed of two polynomials f(x) = P(x) / Q(x) is a:", "options": ["A) Rational Function", "B) Irrational Function", "C) Exponential Function", "D) Quadratic Function"], "answer": "A", "explanation": "Ratios of polynomials form rational functions."},
    {"level": "Medium (6/20)", "question": "Fake news doubling every hour during a crisis represents which model?", "options": ["A) Linear Growth", "B) Exponential Growth", "C) Quadratic Growth", "D) Logarithmic Growth"], "answer": "B", "explanation": "Doubling at fixed intervals represents exponential growth."},
    {"level": "Medium (7/20)", "question": "The trajectory of a thrown ball rising and falling under gravity models a:", "options": ["A) Linear Function", "B) Quadratic Function", "C) Rational Function", "D) Exponential Function"], "answer": "B", "explanation": "Gravity causes parabolic projectile paths modeled by quadratics."},
    {"level": "Medium (8/20)", "question": "A taxi charging Php 40 base pay plus Php 15 for every kilometer traveled is modeled by a:", "options": ["A) Linear Function", "B) Exponential Function", "C) Reciprocal Function", "D) Absolute Value Function"], "answer": "A", "explanation": "Constant increase per kilometer forms a linear equation: y = 15x + 40."},
    {"level": "Medium (9/20)", "question": "What is the term for a line that a graph continuously approaches but never touches?", "options": ["A) Slope", "B) Asymptote", "C) Vertex", "D) Intercept"], "answer": "B", "explanation": "Asymptotes act as boundary lines for functions (e.g. rational functions)."},
    {"level": "Medium (10/20)", "question": "Income tax tiers (0% for low income, 15% for middle, 25% for high) are modeled by a:", "options": ["A) Piecewise Function", "B) Linear Function", "C) Logarithmic Function", "D) Quadratic Function"], "answer": "A", "explanation": "Tax brackets switch rules at explicit income thresholds (piecewise)."},
    {"level": "Hard (11/20)", "question": "Splitting Php 1,000,000 aid equally among x disaster victims (y = 1,000,000/x) is a:", "options": ["A) Rational / Reciprocal Function", "B) Quadratic Function", "C) Linear Function", "D) Exponential Function"], "answer": "A", "explanation": "y = k/x is a reciprocal rational function where payout decreases as x increases."},
    {"level": "Hard (12/20)", "question": "Sound intensity in decibels or earthquake Richter scales exhibiting diminishing returns are modeled by:", "options": ["A) Exponential Functions", "B) Logarithmic Functions", "C) Linear Functions", "D) Quadratic Functions"], "answer": "B", "explanation": "Logarithmic functions grow rapidly at first and then flatten out."},
    {"level": "Hard (13/20)", "question": "Parking garage fees charging full rate per integer hour step is a:", "options": ["A) Greatest Integer (Floor) Function", "B) Linear Function", "C) Exponential Function", "D) Quadratic Function"], "answer": "A", "explanation": "Step functions jump at integer value boundaries."},
    {"level": "Hard (14/20)", "question": "What is the horizontal asymptote of f(x) = (1/x) + 4?", "options": ["A) y = 0", "B) y = 4", "C) x = 0", "D) x = 4"], "answer": "B", "explanation": "As x approaches infinity, 1/x approaches 0, leaving y = 4."},
    {"level": "Hard (15/20)", "question": "What is the vertical asymptote of f(x) = 3 / (x - 2)?", "options": ["A) x = 2", "B) x = -2", "C) y = 3", "D) y = 0"], "answer": "A", "explanation": "Setting denominator x - 2 = 0 yields vertical asymptote x = 2."},
    {"level": "Master (16/20)", "question": "Total Cost C(x) = 50x + 2000. What function type represents Average Cost A(x) = C(x)/x?", "options": ["A) Linear Function", "B) Rational Function", "C) Exponential Function", "D) Quadratic Function"], "answer": "B", "explanation": "A(x) = 50 + (2000/x) is a rational function."},
    {"level": "Master (17/20)", "question": "Half-life decay of radioactive waste N(t) = N_0(0.5)^t is an example of:", "options": ["A) Exponential Decay", "B) Linear Depreciation", "C) Logarithmic Decay", "D) Quadratic Falloff"], "answer": "A", "explanation": "Base between 0 and 1 (0.5) represents exponential decay."},
    {"level": "Master (18/20)", "question": "For projectile height h(t) = -16t^2 + 64t + 80, the maximum height occurs at the parabola's:", "options": ["A) Y-intercept", "B) Vertex (t = -b / 2a)", "C) Asymptote", "D) X-intercept"], "answer": "B", "explanation": "The vertex t = -64 / (2 * -16) = 2 seconds gives the maximum peak height."},
    {"level": "Master (19/20)", "question": "Why does f(x) = (x^2 - 4) / (x - 2) have a removable hole at x = 2 rather than a vertical asymptote?", "options": ["A) The factor (x - 2) cancels out in numerator and denominator", "B) It is a linear function", "C) The numerator is zero", "D) It has no domain restriction"], "answer": "A", "explanation": "(x^2-4)/(x-2) = (x-2)(x+2)/(x-2) = x+2 for x != 2, creating a hole at (2, 4)."},
    {"level": "Master (20/20)", "question": "Given piecewise f(x) = { 2x + 1 for x < 3 ; x^2 - 2 for x >= 3 }, evaluate f(3):", "options": ["A) 7", "B) 9", "C) 5", "D) 11"], "answer": "A", "explanation": "At x = 3, use second rule (x >= 3): f(3) = 3^2 - 2 = 7."}
]

ROOM_3_QUESTIONS = [
    {"level": "Easy (1/20)", "question": "What does the DOMAIN of a function represent?", "options": ["A) All valid input x-values", "B) All output y-values", "C) The y-intercept", "D) The graph slope"], "answer": "A", "explanation": "Domain is the complete set of input x-values."},
    {"level": "Easy (2/20)", "question": "What does the RANGE of a function represent?", "options": ["A) All valid input x-values", "B) All resulting output y-values", "C) The x-intercept", "D) The vertical asymptote"], "answer": "B", "explanation": "Range is the set of output y-values."},
    {"level": "Easy (3/20)", "question": "In interval notation, which symbol indicates an EXCLUDED endpoint?", "options": ["A) Square bracket [ ]", "B) Parenthesis ( )", "C) Curly brace { }", "D) Angle bracket < >"], "answer": "B", "explanation": "Parentheses ( ) mean the boundary value is excluded."},
    {"level": "Easy (4/20)", "question": "What is the DOMAIN of A = {(1, 5), (2, 6), (3, 7)}?", "options": ["A) {5, 6, 7}", "B) {1, 2, 3}", "C) {1, 2, 3, 5, 6, 7}", "D) (1, 3)"], "answer": "B", "explanation": "Domain consists of x-coordinates: {1, 2, 3}."},
    {"level": "Easy (5/20)", "question": "What is the RANGE of B = {(4, 10), (5, 10), (6, 12)}?", "options": ["A) {4, 5, 6}", "B) {10, 12}", "C) {4, 5, 6, 10, 12}", "D) [10, 12]"], "answer": "B", "explanation": "Range consists of unique y-coordinates: {10, 12}."},
    {"level": "Medium (6/20)", "question": "What is the domain of any standard linear polynomial function f(x) = 4x - 9?", "options": ["A) [0, inf)", "B) All real numbers (-inf, inf)", "C) x != 0", "D) (0, inf)"], "answer": "B", "explanation": "Polynomials have no division or radicals, so domain is (-inf, inf)."},
    {"level": "Medium (7/20)", "question": "What is the range of constant function f(x) = 5?", "options": ["A) (-inf, inf)", "B) {5}", "C) [5, inf)", "D) x != 5"], "answer": "B", "explanation": "Output is always 5, so range is single value set {5}."},
    {"level": "Medium (8/20)", "question": "Express 'x is greater than or equal to 3' in interval notation:", "options": ["A) (3, inf)", "B) [3, inf)", "C) (-inf, 3]", "D) [3, 100]"], "answer": "B", "explanation": "'Greater than or equal to' includes 3, using bracket [3, inf)."},
    {"level": "Medium (9/20)", "question": "Express 'x is strictly between -2 and 5 (not included)' in interval notation:", "options": ["A) [-2, 5]", "B) (-2, 5)", "C) [-2, 5)", "D) (-2, 5]"], "answer": "B", "explanation": "Strictly between without endpoints uses parentheses (-2, 5)."},
    {"level": "Medium (10/20)", "question": "What algebraic operation creates a domain restriction in f(x) = 1/x?", "options": ["A) Division by zero", "B) Squaring negative numbers", "C) Adding positive numbers", "D) Multiplying by fractions"], "answer": "A", "explanation": "Denominator cannot be zero, so x != 0."},
    {"level": "Hard (11/20)", "question": "In real numbers, what restriction applies to radical function f(x) = sqrt(x)?", "options": ["A) x must be negative", "B) Radicand must be non-negative (x >= 0)", "C) x != 1", "D) No restriction"], "answer": "B", "explanation": "Square root of negative numbers is not real, so x >= 0."},
    {"level": "Hard (12/20)", "question": "What is the domain of f(x) = 7 / (x - 4)?", "options": ["A) All real numbers", "B) (-inf, 4) U (4, inf) or x != 4", "C) [4, inf)", "D) (-inf, 4]"], "answer": "B", "explanation": "Setting x - 4 = 0 gives x = 4 as excluded restriction."},
    {"level": "Hard (13/20)", "question": "What is the domain of g(x) = sqrt(x - 3)?", "options": ["A) [3, inf)", "B) (3, inf)", "C) (-inf, 3]", "D) All real numbers"], "answer": "A", "explanation": "Solve x - 3 >= 0 -> x >= 3 -> [3, inf)."},
    {"level": "Hard (14/20)", "question": "What is the range of quadratic function f(x) = x^2?", "options": ["A) (-inf, inf)", "B) [0, inf)", "C) (0, inf)", "D) [-1, inf)"], "answer": "B", "explanation": "Squaring any real number yields non-negative values [0, inf)."},
    {"level": "Hard (15/20)", "question": "What is the range of f(x) = x^2 + 5?", "options": ["A) [0, inf)", "B) [5, inf)", "C) (5, inf)", "D) (-inf, 5]"], "answer": "B", "explanation": "Minimum value of x^2 is 0, so x^2 + 5 has minimum value 5: [5, inf)."},
    {"level": "Master (16/20)", "question": "What is the domain of h(x) = 1 / sqrt(x - 2)?", "options": ["A) [2, inf)", "B) (2, inf)", "C) (-inf, 2)", "D) x != 2"], "answer": "B", "explanation": "x - 2 must be > 0 (strictly positive to avoid division by zero): (2, inf)."},
    {"level": "Master (17/20)", "question": "What is the range of f(x) = |x - 4| - 3?", "options": ["A) [0, inf)", "B) [-3, inf)", "C) [-4, inf)", "D) (-inf, -3]"], "answer": "B", "explanation": "Minimum value of |x - 4| is 0, so minimum output is 0 - 3 = -3: [-3, inf)."},
    {"level": "Master (18/20)", "question": "What is the domain of f(x) = (x + 2) / (x^2 - 9)?", "options": ["A) x != 3 and x != -3", "B) x != -2", "C) [3, inf)", "D) All real numbers"], "answer": "A", "explanation": "Denominator x^2 - 9 = 0 at x = 3 and x = -3."},
    {"level": "Master (19/20)", "question": "What is the range of inverted parabola f(x) = -x^2 + 4?", "options": ["A) [4, inf)", "B) (-inf, 4]", "C) (-inf, inf)", "D) [0, 4]"], "answer": "B", "explanation": "Parabola opens downward with vertex peak at y = 4: (-inf, 4]."},
    {"level": "Master (20/20)", "question": "What is the domain of logarithmic function f(x) = ln(x + 1)?", "options": ["A) (-1, inf)", "B) [-1, inf)", "C) (0, inf)", "D) All real numbers"], "answer": "A", "explanation": "Argument of log must be positive: x + 1 > 0 -> x > -1 -> (-1, inf)."}
]

STAGES = [
    {"name": "Room 1: The Lock of Relations and Functions", "questions": ROOM_1_QUESTIONS},
    {"name": "Room 2: The Vault of Function Types", "questions": ROOM_2_QUESTIONS},
    {"name": "Room 3: The Sanctuary of Domain and Range", "questions": ROOM_3_QUESTIONS}
]

# --- SESSION STATE INITIALIZATION ---
if "game_started" not in st.session_state:
    st.session_state.game_started = False
if "current_room" not in st.session_state:
    st.session_state.current_room = 0
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "start_time" not in st.session_state:
    st.session_state.start_time = 0
if "answered" not in st.session_state:
    st.session_state.answered = False
if "user_choice" not in st.session_state:
    st.session_state.user_choice = None

# --- UI HEADER ---
st.title("ESCAPE ROOM: GENERAL MATH QUEST")
st.caption("Master of Functions Challenge")
st.divider()

# --- START SCREEN ---
if not st.session_state.game_started:
    st.subheader("Mission Briefing")
    st.write("You are trapped in the Function Complex. To escape, you must solve door lock codes across 3 rooms.")
    st.markdown("""
    - **Requirement:** Score at least **17 out of 20** to unlock each door.
    - **Difficulty:** Code lock mechanisms scale from Level 1 to Level 20.
    - **Bonus Voucher:** Complete all 3 rooms in under 40 minutes to claim your +1 Quiz Bonus code!
    """)
    if st.button("Start Timer & Begin Escape Room", type="primary"):
        st.session_state.game_started = True
        st.session_state.start_time = time.time()
        st.rerun()

else:
    load_bgm()
    room_idx = st.session_state.current_room

    if room_idx < len(STAGES):
        current_stage = STAGES[room_idx]
        questions = current_stage["questions"]
        q_idx = st.session_state.q_index
        q_data = questions[q_idx]

        st.subheader(f"{current_stage['name']}")
        st.progress((q_idx + 1) / 20, text=f"Door Lock Mechanism {q_idx + 1} of 20")

        col1, col2 = st.columns(2)
        col1.markdown(f"**Difficulty:** {q_data['level']}")
        col2.markdown(f"**Current Room Score:** {st.session_state.score}/{q_idx}")
        st.divider()

        st.write(f"**Question {q_idx + 1}:** {q_data['question']}")

        choice = st.radio("Select your door code entry:", q_data["options"], key=f"q_{room_idx}_{q_idx}")

        if not st.session_state.answered:
            if st.button("Submit Answer", type="primary"):
                st.session_state.user_choice = choice[0]
                st.session_state.answered = True
                if choice[0] == q_data["answer"]:
                    st.session_state.score += 1
                st.rerun()
        else:
            if st.session_state.user_choice == q_data["answer"]:
                st.success(f"[CORRECT] Lock tumbler engaged! Correct answer: {q_data['answer']}")
            else:
                st.error(f"[INCORRECT] Lock failed! Correct answer was: {q_data['answer']}")
                st.info(f"Hint: {q_data['explanation']}")

            if st.button("Next Question"):
                st.session_state.answered = False
                if q_idx + 1 < len(questions):
                    st.session_state.q_index += 1
                else:
                    # END OF ROOM EVALUATION
                    final_score = st.session_state.score
                    if final_score >= 17:
                        st.session_state.current_room += 1
                        st.session_state.q_index = 0
                        st.session_state.score = 0
                    else:
                        st.session_state.q_index = 0
                        st.session_state.score = 0
                st.rerun()

    else:
        # ALL ROOMS COMPLETED
        total_minutes = (time.time() - st.session_state.start_time) / 60
        st.balloons()
        st.success("[ESCAPE SUCCESSFUL] YOU HAVE FREED YOURSELF FROM ALL ROOMS!")
        st.write(f"**Total Escape Time:** {total_minutes:.2f} minutes")
        st.divider()

        if total_minutes <= 40.0:
            st.subheader("=== BONUS VOUCHER UNLOCKED ===")
            st.write("You escaped all 3 rooms in under 40 minutes!")
            st.code("+1-QUIZ-BONUS-MASTER", language="text")
            st.write("Present this voucher code to your GenMath teacher to claim +1 on your next quiz!")
        else:
            st.info("Time exceeded 40 minutes. No bonus voucher granted, but successfully escaped!")

        if st.button("Play Again"):
            st.session_state.game_started = False
            st.session_state.current_room = 0
            st.session_state.q_index = 0
            st.session_state.score = 0
            st.rerun()