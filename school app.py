import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="GHS 24 J.B. System", page_icon="🏫", layout="centered")

# --- INITIALIZE DATABASE IN SESSION STATE ---
if "password" not in st.session_state:
    st.session_state["password"] = "123"
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# --- AUTOMATIC INJECTION FOR CLEAN PRINTING & BORDER FIXES ---
st.markdown(
    """
    <style>
    /* Live layout me se right side ki line aur extra border space khatam karne ke liye */
    iframe, [data-testid="stMarkdownContainer"] {
        overflow: hidden !important;
    }
    
    @media print {
        /* Print ke waqt sidebar aur input fields ko mukammal chupanay ke liye */
        [data-testid="stSidebar"], .stHeader, footer, .stDeployButton, 
        div.stButton:not(.print-btn-wrap), div[class*="stTextInput"], div[class*="stSelectbox"], 
        h2, h3, .stMarkdown:not(:has(.printable-certificate)) {
            display: none !important;
            height: 0px !important;
            padding: 0 !important;
            margin: 0 !important;
        }
        .main .block-container {
            max-width: 100% !important;
            padding: 0 !important;
            margin: 0 !important;
        }
        /* Certificate card rules - forces right line removal */
        .printable-certificate {
            display: block !important;
            visibility: visible !important;
            border: 10px double #b8860b !important;
            padding: 30px !important;
            background: white !important;
            color: black !important;
            width: 100% !important;
            box-sizing: border-box !important;
            page-break-inside: avoid !important;
            overflow: hidden !important;
        }
        .printable-certificate * {
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

    # --- 3. CHARACTER CERTIFICATE ---
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
        
        # JS Print Trigger
        st.markdown(
            '<div class="print-btn-wrap">'
            '   <button onclick="window.print()" style="'
            '       background-color: #1b2631; color: white; padding: 10px 24px; '
            '       font-size: 16px; border: none; border-radius: 4px; cursor: pointer; '
            '       width: 100%; font-weight: bold; margin-bottom: 20px;'
            '   ">🖨️ Print Certificate Now</button>'
            '</div>',
            unsafe_allow_html=True
        )

        # VIP Design Layout with clean text and Underlined Points
        preview_text = (
            "<div class='printable-certificate' style='border: 5px double #b8860b; padding: 25px; background: white; font-family: Arial; color: black; overflow: hidden;'>\n"
            "   <div style='font-size: 14px; font-weight: bold; margin-bottom: 15px; overflow: hidden; color: black;'>\n"
            "       <span style='float: left;'>Roll No. " + roll_no + "</span>\n"
            "       <span style='float: right;'>Regd. No. " + regd_no + "</span>\n"
            "   </div>\n"
            "   <div style='text-align: center; margin-bottom: 20px;'>\n"
            "       <h1 style='margin: 0; font-size: 26px; font-weight: bold; color: black;'>GOVT. HIGH SCHOOL 24 J.B.</h1>\n"
            "       <p style='margin: 2px 0 0 0; font-size: 13px; color: gray;'>District Faisalabad.</p>\n"
            "       <div style='width: 120px; height: 2px; background: #b8860b; margin: 8px auto 0 auto;'></div>\n"
            "   </div>\n"
            "   <div style='text-align: center; margin: 15px 0;'>\n"
            "       <span style='border: 2px solid black; padding: 6px 30px; font-size: 15px; font-weight: bold; color: black; display: inline-block;'>CHARACTER CERTIFICATE</span>\n"
            "   </div>\n"
            "   <div style='text-align: center; font-style: italic; font-size: 14px; margin-bottom: 20px; color: black;'>——— This is to Certify that: ———</div>\n"
            "   <div style='font-size: 15px; line-height: 2.2; margin-bottom: 20px; text-align: justify; color: black;'>\n"
            "       <u>1. Name of Candidate: <b>" + c_name + "</b></u><br>\n"
            "       <u>2. Father's Name: <b>" + f_name_cert + "</b></u><br>\n"
            "       <u>3. Residence: " + residence + "</u><br>\n"
            "       <u>4. Examination Passed: <b>" + exam_passed + "</b></u><br>\n"
            "       <u>5. Marks Obtained: " + marks + " &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>GRADE:</b> " + grade + "</u><br>\n"
            "       <u>6. Moral Character: <b>" + moral + "</b></u><br>\n"
            "       <u>7. Subjects Offered: " + subjects + "</u><br>\n"
            "       <u>8. Games Played at School: " + games + "</u><br>\n"
            "       <u>9. Any Other Remarks: " + remarks + "</u>\n"
            "   </div>\n"
            "   <div style='text-align: center; font-style: italic; font-size: 14px; margin: 20px 0; font-weight: bold; color: black;'>During his/her study in this school, his/her conduct has been good.</div>\n"
            "   <div style='margin-top: 50px; font-size: 13px; font-weight: bold; overflow: hidden; color: black;'>\n"
            "       <div style='float: left; width: 40%;'>\n"
            "           Dated: <u>" + cert_date + "</u><br>\n"
            "           Prepared By: <span style='font-weight: normal;'>" + p_text + "</span>\n"
            "       </div>\n"
            "       <div style='float: left; width: 20%; text-align: center;'>\n"
            "           <div style='width: 55px; height: 55px; border: 1px dashed #b8860b; border-radius: 50%; font-size: 9px; display: flex; align-items: center; justify-content: center; color: gray; margin: 0 auto;'>Stamp</div>\n"
            "       </div>\n"
            "       <div style='float: right; width: 40%; text-align: right; margin-top: 20px; color: black;'>\n"
            "           HEAD MASTER\n"
            "       </div>\n"
            "   </div>\n"
            "</div>"
        )
        
        st.markdown(preview_text, unsafe_allow_html=True)

    # --- 4. SCHOOL LEAVING CERTIFICATE ---
    elif page == "📜 School Leaving Certificate":
        st.subheader("📜 SCHOOL LEAVING CERTIFICATE (SLC)")
        stu_name = st.text_input("Student Name")
        if st.button("💾 Save SLC Data", type="primary"):
            st.success("SLC saved!")
