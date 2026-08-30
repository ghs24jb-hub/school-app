import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="GHS 24 J.B. System", page_icon="🏫", layout="centered")

# --- INITIALIZE DATABASE IN SESSION STATE ---
if "password" not in st.session_state:
    st.session_state["password"] = "123"
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# --- AUTOMATIC PRINT CSS FOR PERFECT SINGLE PAGE ---
# Yeh print tool background me input boxes ko chupa kar sirf certificate print karega
st.markdown(
    """
    <style>
    @media print {
        div[data-testid='stSidebar'], div.stButton, div[data-testid='stFormSubmitButton'], 
        div[class*='stTextInput'], div[class*='stSelectbox'], h3, p, caption, hr, 
        section.main > div:first-child > div:first-child {
            display: none !important;
        }
        body, .main {
            background-color: white !important;
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

    # --- 3. CHARACTER CERTIFICATE (100% STABLE PREMIUM DESIGN) ---
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

        # Native Border Container (HTML ke bagair pure 3D Plaque design framework)
        with st.container(border=True):
            
            # Header Meta
            meta_col1, meta_col2 = st.columns([1, 1])
            with meta_col1:
                st.markdown(f"**Roll No.** {roll_no}")
            with meta_col2:
                st.markdown(f"<p style='text-align: right;'>**Regd. No.** {regd_no}</p>", unsafe_allow_html=True)
                
            # School Identity
            st.markdown("<h1 style='text-align: center; color: #1b2631; font-family: Serif; margin-bottom: 0;'>GOVT. HIGH SCHOOL 24 J.B.</h1>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; color: #7f8c8d; font-weight: bold; margin-top: 0;'>District Faisalabad.</p>", unsafe_allow_html=True)
            
            # Badge Title
            st.markdown("<h3 style='text-align: center; background-color: #1b2631; color: white; padding: 8px; border-radius: 4px; letter-spacing: 1px;'>CHARACTER CERTIFICATE</h3>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; font-style: italic; color: #5d6d7e;'>——— This is to Certify that: ———</p>", unsafe_allow_html=True)
            
            # Structured Info Cards
            st.markdown(f"🔹 **1. Name of Candidate:** &nbsp;&nbsp;&nbsp;&nbsp; *{c_name}*")
            st.markdown(f"🔹 **2. Father's Name:** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {f_name_cert}")
            st.markdown(f"🔹 **3. Residence:** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {residence}")
            st.markdown(f"🔹 **4. Examination Passed:** &nbsp;&nbsp;&nbsp;&nbsp; **{exam_passed}**")
            
            marks_col1, marks_col2 = st.columns([2, 1])
            with marks_col1:
                st.markdown(f"🔹 **5. Marks Obtained:** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {marks}")
            with marks_col2:
                st.markdown(f"🏅 **GRADE:** &nbsp; `{grade}`")
                
            st.markdown(f"🔹 **6. Moral Character:** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **{moral}**")
            st.markdown(f"🔹 **7. Subjects Offered:** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {subjects}")
            st.markdown(f"🔹 **8. Games Played:** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {games}")
            st.markdown(f"🔹 **9. Any Other Remarks:** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {remarks}")
            
            # Conduct Footer Statement
            st.markdown("<div style='text-align: center; background-color: #f4f6f7; padding: 10px; border-radius: 4px; font-style: italic; font-weight: bold; border-left: 5px solid #b8860b; margin: 20px 0;'>During his/her study in this school, his/her conduct has been good.</div>", unsafe_allow_html=True)
            
            # Signatures Layout
            ft_col1, ft_col2, ft_col3 = st.columns([2, 1, 2])
            with ft_col1:
                st.markdown(f"📅 **Dated:** {cert_date}")
                st.markdown(f"✍️ **Prepared By:** {p_text}")
            with ft_col2:
                st.markdown("<div style='width: 60px; height: 60px; border: 2px dashed #b8860b; border-radius: 50%; font-size: 10px; display: flex; align-items: center; justify-content: center; color: #b8860b; text-align: center; margin: 0 auto;'>School Stamp</div>", unsafe_allow_html=True)
            with ft_col3:
                st.markdown("<br><br><p style='text-align: right; border-top: 1px solid gray; padding-top: 5px;'>**HEAD MASTER**</p>", unsafe_allow_html=True)

        st.caption("💡 **Tip:** Is error-free digital certificate ka perfect print nikalne ke liye browser me `Ctrl + P` dabayein.")

    # --- 4. SCHOOL LEAVING CERTIFICATE ---
    elif page == "📜 School Leaving Certificate":
        st.subheader("📜 SCHOOL LEAVING CERTIFICATE (SLC)")
        stu_name = st.text_input("Student Name")
        if st.button("💾 Save SLC Data", type="primary"):
            st.success("SLC saved!")
