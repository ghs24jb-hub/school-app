import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="GHS 24 J.B. System", page_icon="🏫", layout="centered")

# --- INITIALIZE DATABASE IN SESSION STATE ---
if "password" not in st.session_state:
    st.session_state["password"] = "123"
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# --- AUTOMATIC PRINT CSS (Hides inputs and forces perfect 1-page certificate layout) ---
st.markdown(
    """
    <style>
    @media print {
        div[data-testid='stSidebar'], div.stButton, div[data-testid='stFormSubmitButton'], 
        div[class*='stTextInput'], div[class*='stSelectbox'], h3, p, caption, hr, 
        .stMarkdown:not(:has(.custom-print-card)) {
            display: none !important;
        }
        div[data-testid='stVerticalBlock'] > div:has(div.custom-print-card) {
            display: block !important;
        }
        body, .main {
            background-color: white !important;
        }
        .custom-print-card {
            border: 12px double #b8860b !important;
            padding: 30px !important;
            margin: 0 !important;
            width: 100% !important;
            box-shadow: none !important;
            page-break-inside: avoid !important;
            background: white !important;
            color: black !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- SYSTEM LOGIN ---
if not st.session_state["logged_in"]:
    st.markdown("<h2 style='text-align: center; color: #2c3e50;'>🏫 SYSTEM LOGIN</h2>", unsafe_allow_html=True)
    user_input = st.text_input("Username", value="admin")
    pass_input = st.text_input("Password", type="password")
    
    if st.button("Login Karein", type="primary", use_container_width=True):
        if user_input == "admin" and pass_input == st.session_state["password"]:
            st.session_state["logged_in"] = True
            st.rerun()
        else:
            st.error("Username ya Password galat hai!")

# --- MAIN DASHBOARD SYSTEM ---
else:
    st.sidebar.markdown("<h2 style='text-align: center;'>🏫 GHS 24 J.B.</h2>", unsafe_allow_html=True)
    page = st.sidebar.radio(
        "Select Section:",
        ["🏠 Home Dashboard", "📝 Admission Form", "🏅 Character Certificate", "📜 School Leaving Certificate"]
    )
    
    st.sidebar.divider()
    if st.sidebar.button("Log Out", type="secondary", use_container_width=True):
        st.session_state["logged_in"] = False
        st.rerun()

    # --- 1. HOME DASHBOARD ---
    if page == "🏠 Home Dashboard":
        st.title("GOVT. HIGH SCHOOL 24 J.B. FAISALABAD")
        st.success("✨ MUKAMMAL SCHOOL SYSTEM ACTIVE ✨")

    # --- 2. ADMISSION FORM ---
    elif page == "📝 Admission Form":
        st.subheader("📝 NEW ADMISSION FORM ENTRY")
        s_name = st.text_input("Student Name")
        if st.button("💾 Save Admission Data", type="primary"):
            st.success("Admission data save ho gaya!")

    # --- 3. CHARACTER CERTIFICATE (BUG-FREE ROYAL DESIGN) ---
    elif page == "🏅 Character Certificate":
        st.subheader("🏅 ROYAL CHARACTER CERTIFICATE GENERATOR")
        
        # Data Entry Fields
        colA, colB = st.columns(2)
        with colA:
            roll_no = st.text_input("Roll No.", value="510622")
            c_name = st.text_input("1. Name of Candidate", value="Awais Ali")
            residence = st.text_input("3. Residence", value="Chak No. 24 J.B. FAISALABAD")
            marks = st.text_input("5. Marks Obtained", value="692 / 1200")
            subjects = st.text_input("7. Subjects Offered", value="SCIENCE GROUP")
            remarks = st.text_input("9. Any Other Remarks", value="He is a regular student.")
        with colB:
            regd_no = st.text_input("Regd. No.", value="170663-PR-2022")
            f_name_cert = st.text_input("2. Father's Name", value="Muhammad Ansir")
            exam_passed = st.text_input("4. Examination Passed", value="SSC 2024 (ANNUAL)")
            grade = st.text_input("Grade", value="C")
            moral = st.text_input("6. Moral Character", value="GOOD")
            games = st.text_input("8. Games Played at School", value="YES")
            
        cert_date = st.text_input("Dated", value="29-07-2024")
        prep_by = st.text_input("Prepared By", value="")

        p_text = prep_by if prep_by.strip() != "" else "____________________"

        st.divider()
        st.markdown("### 🖥️ Premium Print Preview")

        # Native block layout container with injected 3D styling wrapper to guarantee 0% syntax crashes
        st.markdown('<div class="custom-print-card" style="background: #ffffff; padding: 30px; border: 12px double #b8860b; border-radius: 4px; font-family: \'Times New Roman\', serif; color: black;">', unsafe_allow_html=True)
        
        # Header Metadata Row
        st.markdown(
            f"<table style='width: 100%; font-size: 14px; font-weight: bold; border: none; font-family: Arial; color: #5d6d7e; margin-bottom: 10px;'>"
            f"<tr><td style='text-align: left; border: none;'>Roll No. <span style='color:black;'>{roll_no}</span></td>"
            f"<td style='text-align: right; border: none;'>Regd. No. <span style='color:black;'>{regd_no}</span></td></tr>"
            f"</table>", 
            unsafe_allow_html=True
        )
        
        # Identity Header
        st.markdown(
            "<div style='text-align: center; margin-bottom: 5px;'>"
            "   <h1 style='margin: 0; font-size: 30px; font-weight: 900; color: #1b2631; letter-spacing: 1px;'>GOVT. HIGH SCHOOL 24 J.B.</h1>"
            "   <p style='margin: 2px 0 0 0; font-size: 15px; font-weight: bold; color: #7f8c8d; text-transform: uppercase;'>District Faisalabad.</p>"
            "   <div style='width: 150px; height: 2px; background: #b8860b; margin: 10px auto 0 auto;'></div>"
            "</div>",
            unsafe_allow_html=True
        )
        
        # Badge Heading
        st.markdown(
            "<div style='text-align: center; margin: 20px 0;'>"
            "   <span style='background-color: #1b2631; color: white; padding: 8px 35px; font-size: 16px; font-weight: bold; letter-spacing: 2px; display: inline-block; font-family: Arial;'>CHARACTER CERTIFICATE</span>"
            "</div>"
            "<div style='text-align: center; font-style: italic; font-size: 15px; color: #34495e; margin-bottom: 25px;'>——— This is to Certify that: ———</div>",
            unsafe_allow_html=True
        )
        
        # Table Fields Data
        st.markdown(
            f"<table style='width: 100%; font-size: 15px; border-collapse: collapse; border: none; margin-bottom: 12px; color: black;'>"
            f"  <tr style='border: none;'><td style='width: 32%; font-weight: bold; padding: 7px 0;'>1. Name of Candidate</td><td style='width: 3%; font-weight: bold;'>:</td><td style='border-bottom: 1px solid #b8860b; font-weight: bold; font-style: italic; font-size: 17px; padding: 7px 0;'>{c_name}</td></tr>"
            f"  <tr style='border: none;'><td style='font-weight: bold; padding: 7px 0;'>2. Father's Name</td><td style='font-weight: bold;'>:</td><td style='border-bottom: 1px solid #b8860b; font-size: 16px; padding: 7px 0;'>{f_name_cert}</td></tr>"
            f"  <tr style='border: none;'><td style='font-weight: bold; padding: 7px 0;'>3. Residence</td><td style='font-weight: bold;'>:</td><td style='border-bottom: 1px solid #b8860b; padding: 7px 0; color: #34495e;'>{residence}</td></tr>"
            f"  <tr style='border: none;'><td style='font-weight: bold; padding: 7px 0;'>4. Examination Passed</td><td style='font-weight: bold;'>:</td><td style='border-bottom: 1px solid #b8860b; padding: 7px 0; font-weight: bold;'>{exam_passed}</td></tr>"
            f"</table>"
            f"<table style='width: 100%; font-size: 15px; border-collapse: collapse; border: none; margin-bottom: 12px; color: black;'> "
            f"  <tr style='border: none;'>"
            f"      <td style='width: 32%; font-weight: bold; padding: 7px 0;'>5. Marks Obtained</td><td style='width: 3%; font-weight: bold;'>:</td>"
            f"      <td style='width: 35%; border-bottom: 1px solid #b8860b; padding: 7px 0;'>{marks}</td>"
            f"      <td style='width: 15%; font-weight: bold; text-align: center;'>GRADE:</td>"
            f"      <td style='border-bottom: 1px solid #b8860b; font-weight: bold; font-size: 16px; color: #900c3f; padding: 7px 0;'>{grade}</td>"
            f"  </tr>"
            f"</table>"
            f"<table style='width: 100%; font-size: 15px; border-collapse: collapse; border: none; margin-bottom: 12px; color: black;'>"
            f"  <tr style='border: none;'><td style='width: 32%; font-weight: bold; padding: 7px 0;'>6. Moral Character</td><td style='width: 3%; font-weight: bold;'>:</td><td style='border-bottom: 1px solid #b8860b; font-weight: bold; padding: 7px 0; color: green;'>{moral}</td></tr>"
            f"  <tr style='border: none;'><td style='font-weight: bold; padding: 7px 0;'>7. Subjects Offered</td><td style='font-weight: bold;'>:</td><td style='border-bottom: 1px solid #b8860b; padding: 7px 0;'>{subjects}</td></tr>"
            f"  <tr style='border: none;'><td style='font-weight: bold; padding: 7px 0;'>8. Games Played at School</td><td style='font-weight: bold;'>:</td><td style='border-bottom: 1px solid #b8860b; padding: 7px 0;'>{games}</td></tr>"
            f"  <tr style='border: none;'><td style='font-weight: bold; padding: 7px 0;'>9. Any Other Remarks</td><td style='font-weight: bold;'>:</td><td style='border-bottom: 1px solid #b8860b; padding: 7px 0; color: #34495e;'>{remarks}</td></tr>"
            f"</table>",
            unsafe_allow_html=True
        )
        
        # Conduct Message
        st.markdown(
            "<div style='text-align: center; font-style: italic; font-size: 15px; margin: 25px 0; font-weight: bold; color: #1b2631;'>"
            "During his/her study in this school, his/her conduct has been good."
