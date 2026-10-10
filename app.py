import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Neon Star Calculator", page_icon="⭐", layout="centered"
)

# Custom CSS for Neon Blue & Star Theme
st.markdown(
    """
    <style>
    /* Neon Blue Background with Yellow & Hot Pink Neon Stars */
    .stApp {
        background-color: #050b14;
        background-image: 
            radial-gradient(#ff007f 1.5px, transparent 1.5px), 
            radial-gradient(#ffe600 1.5px, #050b14 1.5px);
        background-size: 50px 50px;
        background-position: 0 0, 25px 25px;
    }
    
    /* Main container frame - Neon Blue Glassmorphism */
    .block-container {
        background-color: rgba(10, 25, 47, 0.85);
        padding: 30px;
        border-radius: 25px;
        box-shadow: 0px 0px 30px rgba(0, 243, 255, 0.3);
        border: 2px solid #00f3ff;
        max-width: 380px;
        margin: auto;
    }

    /* Display box */
    .element-container div[data-testid="stMarkdownContainer"] p {
        background-color: #020c1b;
        color: #ffe600;
        font-size: 32px;
        font-weight: bold;
        text-align: right;
        padding: 10px 15px;
        border-radius: 12px;
        border: 2px solid #ff007f;
        box-shadow: inset 0 0 10px rgba(255, 0, 127, 0.3);
        margin-bottom: 15px;
    }

    /* General buttons styling */
    .stButton > button {
        width: 100%;
        height: 55px;
        border-radius: 15px;
        font-size: 20px;
        font-weight: bold;
        border: 1px solid #00f3ff;
        background-color: #172a45;
        color: #00f3ff;
        transition: 0.2s;
        box-shadow: 0 0 10px rgba(0, 243, 255, 0.1);
    }
    .stButton > button:hover {
        background-color: #ff007f;
        color: #ffffff;
        border-color: #ffe600;
        box-shadow: 0 0 15px #ff007f;
    }

    /* Footer label */
    .footer-text {
        text-align: center;
        color: #ffe600;
        font-size: 14px;
        font-style: italic;
        margin-top: 20px;
        text-shadow: 0 0 5px rgba(255, 230, 0, 0.5);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Initialize Session State
if "display" not in st.session_state:
    st.session_state.display = "0"
if "reset" not in st.session_state:
    st.session_state.reset = False

# Display Screen
st.markdown(f"<p>{st.session_state.display}</p>", unsafe_allow_html=True)


# Button Handlers
def click_num(num):
    if (
        st.session_state.display in ["0", "Error", "Cannot divide by 0"]
        or st.session_state.reset
    ):
        st.session_state.display = str(num)
        st.session_state.reset = False
    else:
        st.session_state.display += str(num)


def click_op(op):
    if st.session_state.display not in ["Error", "Cannot divide by 0"]:
        st.session_state.display += f" {op} "
        st.session_state.reset = False


def click_clear():
    st.session_state.display = "0"
    st.session_state.reset = False


def click_backspace():
    if (
        len(st.session_state.display) > 1
        and st.session_state.display not in ["Error", "Cannot divide by 0"]
    ):
        st.session_state.display = st.session_state.display[:-1].strip()
    else:
        st.session_state.display = "0"


def click_equal():
    try:
        expr = (
            st.session_state.display.replace("×", "*")
            .replace("÷", "/")
            .replace("%", "/100")
        )
        res = eval(expr)
        if isinstance(res, float) and res.is_integer():
            res = int(res)
        st.session_state.display = str(res)
        st.session_state.reset = True
    except ZeroDivisionError:
        st.session_state.display = "Cannot divide by 0"
        st.session_state.reset = True
    except Exception:
        st.session_state.display = "Error"
        st.session_state.reset = True


# Keypad Grid Layout
row1 = st.columns(4)
row1[0].button("AC", on_click=click_clear)
row1[1].button("⌫", on_click=click_backspace)
row1[2].button("%", on_click=lambda: click_op("%"))
row1[3].button("÷", on_click=lambda: click_op("÷"))

row2 = st.columns(4)
row2[0].button("7", on_click=lambda: click_num("7"))
row2[1].button("8", on_click=lambda: click_num("8"))
row2[2].button("9", on_click=lambda: click_num("9"))
row2[3].button("×", on_click=lambda: click_op("×"))

row3 = st.columns(4)
row3[0].button("4", on_click=lambda: click_num("4"))
row3[1].button("5", on_click=lambda: click_num("5"))
row3[2].button("6", on_click=lambda: click_num("6"))
row3[3].button("-", on_click=lambda: click_op("-"))

row4 = st.columns(4)
row4[0].button("1", on_click=lambda: click_num("1"))
row4[1].button("2", on_click=lambda: click_num("2"))
row4[2].button("3", on_click=lambda: click_num("3"))
row4[3].button("+", on_click=lambda: click_op("+"))

row5 = st.columns(4)
row5[0].button("0", on_click=lambda: click_num("0"))
row5[1].button(".", on_click=lambda: click_num("."))
row5[2].button("=", on_click=click_equal)
row5[3].button("±", on_click=lambda: click_num("-"))

# Bottom Credit
st.markdown(
    "<div class='footer-text'>Built by Amna Sahar</div>", unsafe_allow_html=True
)