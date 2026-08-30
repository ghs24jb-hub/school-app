import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="GHS 24 J.B. System", page_icon="🏫", layout="centered")

# --- INITIALIZE DATABASE IN SESSION STATE ---
if "password" not in st.session_state:
    st.session_state["password"] = "123"
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# --- AUTOMATIC INJECTION FOR CLEAN PRINTING & NO SCROLLBARS ---
st.markdown(
    """
    <style>
    html, body, [data-testid="stAppViewContainer"], [data-testid="stMarkdownContainer"] {
        overflow-x: hidden !important;
        overflow-y: auto !important;
    }
    @media print {
        [data-testid="stSidebar"], .stHeader, footer, .stDeployButton, 
        div.stButton:not(.print-btn-wrap), div[class*="stTextInput"], div[class*="stSelectbox"], 
        h2, h3, .stMarkdown:not(:has(.printable-certificate)), .print-action-trigger {
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
        
        # Bada Interactive Print Button (Screen par dikhega, print me hide ho jayega)
        st.markdown(
            '<div class="print-action-trigger" style="margin-bottom: 25px;">'
            '   <button onclick="window.print()" style="'
            '       background: linear-gradient(135deg, #1b2631 0%, #2c3e50 100%); '
            '       color: white; padding: 14px 30px; font-size: 18px; border: none; '
            '       border-radius: 6px; cursor: pointer; width: 100%; font-weight: bold; '
            '       box-shadow: 0 4px 15px rgba(0,0,0,0.15); text-transform: uppercase; letter-spacing: 1px;'
            '   ">🖨️ Click Here to Print Certificate</button>'
            '</div>',
            unsafe_allow_html=True
        )

        # Secure layout structure with table-row styling for lines extending to the end
        preview_template = """
        <div class='printable-certificate' style='border: 5px double #b8860b; padding: 25px; background: white; font-family: Arial; color: black; overflow: hidden;'>
            <div style='font-size: 14px; font-weight: bold; margin-bottom: 15px; overflow: hidden; color: black;'>
                <span style='float: left;'>Roll No. {0}</span>
                <span style='float: right;'>Regd. No. {1}</span>
            </div>
            <div style='text-align: center; margin-bottom: 20px;'>
                <h1 style='margin: 0; font-size: 26px; font-weight: bold; color: black;'>GOVT. HIGH SCHOOL 24 J.B.</h1>
                <p style='margin: 2px 0 0 0; font-size: 13px; color: gray;'>District Faisalabad.</p>
                <div style='width: 120px; height: 2px; background: #b8860b; margin: 8px auto 0 auto;'></div>
            </div>
            <div style='text-align: center; margin: 15px 0;'>
                <span style='border: 2px solid black; padding: 6px 30px; font-size: 15px; font-weight: bold; color: black; display: inline-block;'>CHARACTER CERTIFICATE</span>
            </div>
            <div style='text-align: center; font-style: italic; font-size: 14px; margin-bottom: 25px; color: black;'>——— This is to Certify that: ———</div>
            
            <table style='width: 100%; font-size: 15px; border-collapse: collapse; border: none; margin-bottom: 5px; color: black;'>
                <tr style='border: none;'><td style='width: 32%; font-weight: bold; padding: 8px 0;'>1. Name of Candidate</td><td style='width: 3%; font-weight: bold;'>:</td><td style='border-bottom: 1px solid black; font-weight: bold; font-style: italic; font-size: 16px; padding: 8px 0;'>{2}</td></tr>
                <tr style='border: none;'><td style='font-weight: bold; padding: 8px 0;'>2. Father's Name</td><td style='font-weight: bold;'>:</td><td style='border-bottom: 1px solid black; font-weight: bold; padding: 8px 0;'>{3}</td></tr>
                <tr style='border: none;'><td style='font-weight: bold; padding: 8px 0;'>3. Residence</td><td style='font-weight: bold;'>:</td><td style='border-bottom: 1px solid black; padding: 8px 0;'>{4}</td></tr>
                <tr style='border: none;'><td style='font-weight: bold; padding: 8px 0;'>4. Examination Passed</td><td style='font-weight: bold;'>:</td><td style='border-bottom: 1px solid black; font-weight: bold; padding: 8px 0;'>{5}</td></tr>
            </table>
            
            <table style='width: 100%; font-size: 15px; border-collapse: collapse; border: none; margin-bottom: 5px; color: black;'>
                <tr style='border: none;'>
                    <td style='width: 32%; font-weight: bold; padding: 8px 0;'>5. Marks Obtained</td><td style='width: 3%; font-weight: bold;'>:</td>
                    <td style='width: 32%; border-bottom: 1px solid black; padding: 8px 0;'>{6}</td>
                    <td style='width: 13%; font-weight: bold; text-align: center;'>GRADE:</td>
                    <td style='border-bottom: 1px solid black; font-weight: bold; padding: 8px 0;'>{7}</td>
                </tr>
            </table>
            
            <table style='width: 100%; font-size: 15px; border-collapse: collapse; border: none; margin-bottom: 25px; color: black;'>
                <tr style='border: none;'><td style='width: 32%; font-weight: bold; padding: 8px 0;'>6. Moral Character</td><td style='width: 3%; font-weight: bold;'>:</td><td style='border-bottom: 1px solid black; font-weight: bold; padding: 8px 0; color: green;'>{8}</td></tr>
                <tr style='border: none;'><td style='font-weight: bold; padding: 8px 0;'>7. Subjects Offered</td><td style='font-weight: bold;'>:</td><td style='border-bottom: 1px solid black; padding: 8px 0;'>{9}</td></tr>
                <tr style='border: none;'><td style='font-weight: bold; padding: 8px 0;'>8. Games Played at School</td><td style='font-weight: bold;'>:</td><td style='border-bottom: 1px solid black; padding: 8px 0;'>{10}</td></tr>
                <tr style='border: none;'><td style='font-weight: bold; padding: 8px 0;'>9. Any Other Remarks</td><td style='font-weight: bold;'>:</td><td style='border-bottom: 1px solid black; padding: 8px 0;'>{11}</td></tr>
            </table>
            
