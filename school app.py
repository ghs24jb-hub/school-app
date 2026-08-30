import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="GHS 24 J.B. System", page_icon="🏫", layout="centered")

# --- INITIALIZE DATABASE IN SESSION STATE ---
if "password" not in st.session_state:
    st.session_state["password"] = "123"
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# --- ULTRA POWERFUL AUTOMATIC PRINT CSS FOR PERFECT SINGLE PAGE ---
# This CSS completely removes the sidebar background and forces all content block text visibility during print
st.markdown(
    """
    <style>
    @media print {
        /* Sidebar, inputs, buttons aur header ko mukammal ghayab karne ke liye */
        div[data-testid='stSidebar'], section[data-testid='stSidebar'], .stHeader, div.stButton, div[data-testid='stFormSubmitButton'], 
        div[class*='stTextInput'], div[class*='stSelectbox'], h3, p, caption, hr, 
        .stDeployButton, #main-menu-button {
            display: none !important;
            width: 0px !important;
        }
        /* Main area ko poori screen par phelane ke liye */
        .main, .block-container, div[data-testid='stVerticalBlock'] {
            padding: 0 !important;
            margin: 0 !important;
            width: 100% !important;
            max-width: 100% !important;
        }
        /* Certificate ke container aur uske andar mojud saari lines ko force-show karne ke liye */
        div[data-testid='stBlock'] {
            display: block !important;
            visibility: visible !important;
            opacity: 1 !important;
            width: 100% !important;
        }
        div[data-testid='stMarkdownContainer'], div[data-testid='stMarkdownContainer'] * {
            display: block !important;
            visibility: visible !important;
            color: black !important;
        }
        /* Border box setup */
        div:has(> div.custom-box-border) {
            border: 4px double #b8860b !important;
            padding: 25px !important;
            background: white !important;
            page-break-inside: avoid !important;
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
        st.markdown("### 🖥️ Premium Print Preview")

        # Container with a custom anchor class for advanced print rules
        with st.container(border=True):
            # Anchor tag for CSS engine to find this block
            st.markdown('<div class="custom-box-border"></div>', unsafe_allow_html=True)
            
            # Header IDs
            st.markdown(f"**Roll No.** {roll_no} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Regd. No.** {regd_no}")
            
            # School Identity
            st.markdown("<h1 style='text-align: center; color: #1b2631; font-family: Serif; margin-top: 10px; margin-bottom: 0;'>GOVT. HIGH SCHOOL 24 J.B.</h1>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; color: #7f8c8d; font-weight: bold; margin-top: 0; margin-bottom: 15px;'>District Faisalabad.</p>", unsafe_allow_html=True)
            
            # Badge Title
            st.markdown("<h3 style='text-align: center; background-color: #1b2631; color: white; padding: 8px; border-radius: 4px; letter-spacing: 1px; margin-bottom: 15px;'>CHARACTER CERTIFICATE</h3>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; font-style: italic; color: #5d6d7e; margin-bottom: 20px;'>——— This is to Certify that: ———</p>", unsafe_allow_html=True)
            
            # Certificate Core Text Fields 
            st.markdown(f"🔹 **1. Name of Candidate:** &nbsp;&nbsp;&nbsp;&nbsp; *{c_name}*")
            st.markdown(f"🔹 **2. Father's Name:** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {f_name_cert}")
            st.markdown(f"🔹 **3. Residence:** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {residence}")
            st.markdown(f"🔹 **4. Examination Passed:** &nbsp;&nbsp;&nbsp;&nbsp; **{exam_passed}**")
            st.markdown(f"🔹 **5. Marks Obtained:** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {marks} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **GRADE:** `{grade}`")
            st.markdown(f"🔹 **6. Moral Character:** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **{moral}**")
            st.markdown(f"🔹 **7. Subjects Offered:** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {subjects}")
            st.markdown(f"🔹 **8. Games Played:** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {games}")
            st.markdown(f"🔹 **9. Any Other Remarks:** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {remarks}")
            
            # Conduct Footer Statement
            st.markdown("<div style='text-align: center; background-color: #f4f6f7; padding: 12px; border-radius: 4px; font-style: italic; font-weight: bold; border-left: 5px solid #b8860b; margin: 25px 0; color: black;'>During his/her study in this school, his/her conduct has been good.</div>", unsafe_allow_html=True)
            
            st.write("<br>", unsafe_allow_html=True)
            
            # Safe Native row spacing for layout footers during printer processing
            foot_col1, foot_col2, foot_col3 = st.columns([2, 1, 2])
            with foot_col1:
                st.markdown(f"📅 **Dated:** {cert_date}")
                st.markdown(f"✍️ **Prepared By:** {p_text}")
            with foot_col2:
                st.markdown("<div style='width: 60px; height: 60px; border: 2px dashed #b8860b; border-radius: 50%; font-size: 10px; display: flex; align-items: center; justify-content: center; color: #b8860b; text-align: center; margin: 15px auto 0 auto;'>School Stamp</div>", unsafe_allow_html=True)
            with foot_col3:
                st.markdown(f"<p style='text-align: right; margin-top: 40px; border-top: 1px solid gray; padding-top: 5px;'>**HEAD MASTER**</p>", unsafe_allow_html=True)

    # --- 4. SCHOOL LEAVING CERTIFICATE ---
    elif page == "📜 School Leaving Certificate":
        st.subheader("📜 SCHOOL LEAVING CERTIFICATE (SLC)")
        stu_name = st.text_input("Student Name")
        if st.button("💾 Save SLC Data", type="primary"):
            st.success("SLC saved!")
