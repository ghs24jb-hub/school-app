import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="GHS 24 J.B. System", page_icon="🏫", layout="centered")

# --- INITIALIZE DATABASE IN SESSION STATE ---
if "password" not in st.session_state:
    st.session_state["password"] = "123"
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# --- AUTOMATIC INJECTION FOR PERFECT A4 PRINTING ---
st.markdown(
    """
    <style>
    html, body, [data-testid="stAppViewContainer"], [data-testid="stMarkdownContainer"] {
        overflow-x: hidden !important;
        overflow-y: auto !important;
    }
    
    @media print {
        /* Force A4 Page Settings */
        @page {
            size: A4 portrait !important;
            margin: 15mm !important;
        }
        
        /* Hide everything except the certificate box */
        [data-testid="stSidebar"], .stHeader, footer, .stDeployButton, 
        div.stButton, div[class*="stTextInput"], div[class*="stSelectbox"], 
        h2, h3, hr, caption, .print-action-box, .stMarkdown:not(:has(.printable-a4-card)) {
            display: none !important;
            height: 0px !important;
            padding: 0 !important;
            margin: 0 !important;
        }
        
        /* Main area stretching */
        .main .block-container {
            max-width: 100% !important;
            padding: 0 !important;
            margin: 0 !important;
            width: 100% !important;
        }
        
        /* Absolute visibility enforcement for certificate layout */
        div[data-testid="stBlock"]:has(.printable-a4-card) {
            display: block !important;
            visibility: visible !important;
            width: 100% !important;
        }
        
        .printable-a4-card {
            display: block !important;
            visibility: visible !important;
            border: 8px double #b8860b !important;
            padding: 40px !important;
            background: white !important;
            color: black !important;
            width: 100% !important;
            box-sizing: border-box !important;
            page-break-inside: avoid !important;
        }
        
        .printable-a4-card * {
            color: black !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- SYSTEM LOGIN ---
if not st.session_state["logged_in"]:
    st.markdown("<h2 style='text-align: center;'>🏫 SYSTEM LOGIN</h2>", unsafe_allow_html=True)
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

    # --- 3. CHARACTER CERTIFICATE (A4 PERFECT FORMAT) ---
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

        p_text = prep_by if prep_by.strip() != "" else "___________"

        st.divider()
        
        # Bada Interactive Print Button
        st.markdown(
            '<div class="print-action-box" style="margin-bottom: 25px;">'
            '   <button onclick="window.print()" style="'
            '       background: linear-gradient(135deg, #1b2631 0%, #2c3e50 100%); '
            '       color: white; padding: 14px 30px; font-size: 18px; border: none; '
            '       border-radius: 6px; cursor: pointer; width: 100%; font-weight: bold; '
            '       box-shadow: 0 4px 15px rgba(0,0,0,0.15); text-transform: uppercase; letter-spacing: 1px;'
            '   ">🖨️ Click Here to Print Certificate</button>'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown("### 🖥️ Premium Print Preview")

        # Stable and Robust Layout with Underlined table rows spanning perfectly to the end of A4 width
        preview_text = (
            "<div class='printable-a4-card' style='border: 5px double #b8860b; padding: 30px; background: white; font-family: Arial; color: black; overflow: hidden;'>"
            "   <div style='font-size: 14px; font-weight: bold; margin-bottom: 20px; overflow: hidden; color: black;'>"
            "       <span style='float: left;'>Roll No. " + roll_no + "</span>"
            "       <span style='float: right;'>Regd. No. " + regd_no + "</span>"
            "   </div>"
            "   <div style='text-align: center; margin-bottom: 25px;'>"
            "       <h1 style='margin: 0; font-size: 28px; font-weight: bold; color: black; font-family: \"Times New Roman\", Times, serif;'>GOVT. HIGH SCHOOL 24 J.B.</h1>"
            "       <p style='margin: 4px 0 0 0; font-size: 14px; color: gray;'>District Faisalabad.</p>"
            "       <div style='width: 140px; height: 2px; background: #b8860b; margin: 10px auto 0 auto;'></div>"
            "   </div>"
            "   <div style='text-align: center; margin: 20px 0;'>"
            "       <span style='border: 2px solid black; padding: 8px 35px; font-size: 16px; font-weight: bold; color: black; display: inline-block;'>CHARACTER CERTIFICATE</span>"
            "   </div>"
            "   <div style='text-align: center; font-style: italic; font-size: 15px; margin-bottom: 30px; color: black;'>——— This is to Certify that: ———</div>"
            
            "   <table style='width: 100%; font-size: 16px; border-collapse: collapse; border: none; margin-bottom: 8px; color: black;'>"
            "       <tr style='border: none;'><td style='width: 32%; font-weight: bold; padding: 10px 0;'>1. Name of Candidate</td><td style='width: 3%; font-weight: bold;'>:</td><td style='border-bottom: 1px solid black; font-weight: bold; font-style: italic; font-size: 17px; padding: 10px 0;'>" + c_name + "</td></tr>"
            "       <tr style='border: none;'><td style='font-weight: bold; padding: 10px 0;'>2. Father's Name</td><td style='font-weight: bold;'>:</td><td style='border-bottom: 1px solid black; font-weight: bold; padding: 10px 0;'>" + f_name_cert + "</td></tr>"
            "       <tr style='border: none;'><td style='font-weight: bold; padding: 10px 0;'>3. Residence</td><td style='font-weight: bold;'>:</td><td style='border-bottom: 1px solid black; padding: 10px 0;'>" + residence + "</td></tr>"
            "       <tr style='border: none;'><td style='font-weight: bold; padding: 10px 0;'>4. Examination Passed</td><td style='font-weight: bold;'>:</td><td style='border-bottom: 1px solid black; font-weight: bold; padding: 10px 0;'>" + exam_passed + "</td></tr>"
            "   </table>"
            
            "   <table style='width: 100%; font-size: 16px; border-collapse: collapse; border: none; margin-bottom: 8px; color: black;'>"
            "       <tr style='border: none;'>"
            "           <td style='width: 32%; font-weight: bold; padding: 10px 0;'>5. Marks Obtained</td><td style='width: 3%; font-weight: bold;'>:</td>"
            "           <td style='width: 32%; border-bottom: 1px solid black; padding: 10px 0;'>" + marks + "</td>"
            "           <td style='width: 13%; font-weight: bold; text-align: center;'>GRADE:</td>"
            "           <td style='border-bottom: 1px solid black; font-weight: bold; padding: 10px 0;'>" + grade + "</td>"
            "       </tr>"
            "   </table>"
            
            "   <table style='width: 100%; font-size: 16px; border-collapse: collapse; border: none; margin-bottom: 30px; color: black;'> "
