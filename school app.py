import streamlit as st

# --- STREAMLIT PAGE CONFIG ---
st.set_page_config(page_title="GHS 24 J.B. - School System", page_icon="🏫", layout="centered")

# --- INITIALIZE DATABASE IN SESSION STATE ---
if "password" not in st.session_state:
    st.session_state["password"] = "123"
if "security_code" not in st.session_state:
    st.session_state["security_code"] = "2424"
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "reset_mode" not in st.session_state:
    st.session_state["reset_mode"] = False

# --- LOGIN SCREEN ---
if not st.session_state["logged_in"]:
    if not st.session_state["reset_mode"]:
        st.markdown("<h2 style='text-align: center; color: #2c3e50;'>🔐 SYSTEM LOGIN</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Govt. High School 24 J.B. Faisalabad</p>", unsafe_allow_html=True)
        
        user_input = st.text_input("Username", value="admin")
        pass_input = st.text_input("Password", type="password")
        
        col1, col2 = st.columns()
        with col1:
            if st.button("Login Karein", type="primary", use_container_width=True):
                if user_input == "admin" and pass_input == st.session_state["password"]:
                    st.session_state["logged_in"] = True
                    st.rerun()
                else:
                    st.error("Username ya Password galat hai!")
        with col2:
            if st.button("Reset Password?", use_container_width=True):
                st.session_state["reset_mode"] = True
                st.rerun()
                
    else:
        st.markdown("<h2 style='text-align: center; color: #c0392b;'>🔐 RESET PASSWORD</h2>", unsafe_allow_html=True)
        code_input = st.text_input("School Secret Code Likhein")
        new_pwd_input = st.text_input("Naya Password Likhein", type="password")
        
        col1, col2 = st.columns()
        with col1:
            if st.button("Update Password", type="primary", use_container_width=True):
                if code_input.strip() == st.session_state["security_code"]:
                    if new_pwd_input.strip() != "":
                        st.session_state["password"] = new_pwd_input.strip()
                        st.success("Password tabdeel ho gaya hai! Ab naye password se login admin karein.")
                        st.session_state["reset_mode"] = False
                        st.rerun()
                    else:
                        st.error("Naya password khali nahi ho sakta!")
                else:
                    st.error("Secret Code galat hai!")
        with col2:
            if st.button("Back to Login", use_container_width=True):
                st.session_state["reset_mode"] = False
                st.rerun()

# --- MAIN SYSTEM DASHBOARD ---
else:
    st.sidebar.markdown("<h3 style='text-align: center; color: white;'>🏫 GHS 24 J.B.</h3>", unsafe_allow_html=True)
    st.sidebar.markdown("<p style='text-align: center; color: #bdc3c7;'>Main System Menu</p>", unsafe_allow_html=True)
    st.sidebar.divider()
    
    page = st.sidebar.radio(
        "Select Document Type:",
        ["🏠 Home Dashboard", "📝 Admission Form", "🏅 Character Certificate", "📜 School Leaving Certificate"]
    )
    
    st.sidebar.divider()
    if st.sidebar.button("Log Out", type="secondary", use_container_width=True):
        st.session_state["logged_in"] = False
        st.rerun()

    # --- HOME PAGE ---
    if page == "🏠 Home Dashboard":
        st.markdown("<h2 style='text-align: center; color: #2c3e50;'>🏫 GOVT. HIGH SCHOOL 24 J.B. FAISALABAD</h2>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: green;'>✨ MUKAMMAL SCHOOL SYSTEM ACTIVE ✨</h4>", unsafe_allow_html=True)
        st.info("Sidebar menu se kisi bhi document ko select karke print nikaalein. Yeh app mobile aur computer dono par chalegi.")

    # --- 1. ADMISSION FORM ---
    elif page == "📝 Admission Form":
        st.markdown("<h3 style='color: #2980b9;'>📝 NEW ADMISSION FORM</h3>", unsafe_allow_html=True)
        form_no = st.text_input("Form No")
        adm_no = st.text_input("Admission No")
        s_name = st.text_input("Student Name")
        f_name = st.text_input("Father Name")
        contact = st.text_input("Contact No")
        address = st.text_area("Present Address")
        
        if st.button("💾 Document Generate Karein", type="primary"):
            if not s_name.strip():
                st.error("Student Name lazmi likhein!")
            else:
                doc_content = f"Form No: {form_no}\nAdmission No: {adm_no}\nStudent Name: {s_name}\nFather Name: {f_name}\nContact No: {contact}\nPresent Address: {address}"
                st.success("Admission Document tayar hai!")
                st.download_button(label="📥 Download Admission File (.txt)", data=doc_content, file_name=f"Admission_{s_name.replace(' ', '_')}.txt", mime="text/plain")

    # --- 2. CHARACTER CERTIFICATE (ADDED PREPARED BY OPTION) ---
    elif page == "🏅 Character Certificate":
        st.markdown("<h3 style='color: #16a085;'>🏅 CHARACTER CERTIFICATE GENERATOR</h3>", unsafe_allow_html=True)
        
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
            f_name = st.text_input("2. Father's Name", value="Muhammad Ansir")
            exam_passed = st.text_input("4. Examination Passed", value="SSC 2024 (ANNUAL)")
            grade = st.text_input("Grade", value="C")
            moral = st.text_input("6. Moral Character", value="GOOD")
            games = st.text_input("8. Games Played at School", value="YES")
            
        cert_date = st.text_input("Dated", value="29-07-2024")
        prepared_by_name = st.text_input("Prepared By (Naam likhein ya khali chorr dein line ke liye)", value="")

        # Dynamic name fallback for Prepared By field
        prepared_text = prepared_by_name if prepared_by_name.strip() != "" else "____________________"

        certificate_html = f"""
        <div style="background: white; padding: 30px; border: 15px double #784212; border-radius: 4px; font-family: 'Arial', sans-serif; color: #1c2833; line-height: 1.6; box-shadow: 0px 0px 10px rgba(0,0,0,0.1);">
            <table style="width: 100%; font-size: 13px; border: none; font-weight: bold; margin-bottom: 10px;">
                <tr>
                    <td style="text-align: left; border: none;">Roll No. {roll_no}</td>
                    <td style="text-align: right; border: none;">Regd. No. {regd_no}</td>
                </tr>
            </table>

            <div style="text-align: center; margin-bottom: 5px;">
                <h1 style="margin: 0; font-size: 26px; color: #1b2631; font-family: 'Times New Roman', serif; font-weight: bold; letter-spacing: 1px;">GOVT. HIGH SCHOOL 24 J.B.</h1>
                <p style="margin: 2px 0 15px 0; font-size: 14px; font-weight: bold; color: #566573;">District Faisalabad.</p>
                <div style="width: 80%; height: 1px; background: linear-gradient(to right, transparent, #784212, transparent); margin: 0 auto 15px auto;"></div>
            </div>

            <div style="text-align: center; margin-bottom: 25px;">
                <span style="background-color: #1b2631; color: white; padding: 8px 30px; font-size: 16px; font-weight: bold; letter-spacing: 2px; border-radius: 2px; display: inline-block;">CHARACTER CERTIFICATE</span>
            </div>

            <div style="text-align: center; font-style: italic; font-size: 14px; margin-bottom: 20px; font-weight: bold; color: #2c3e50;">
                ——— This is to Certify that: ———
            </div>

            <table style="width: 100%; font-size: 14px; border-collapse: collapse; border: none;">
                <tr style="border: none;"><td style="width: 35%; font-weight: bold; padding: 6px 0; border: none;">1. Name of Candidate</td><td style="width: 3%; font-weight: bold; border: none;">:</td><td style="border-bottom: 1px solid #bdc3c7; font-style: italic; font-weight: bold; font-size: 15px; padding: 6px 0; color: #1f3a52;">{c_name}</td></tr>
                <tr style="border: none;"><td style="font-weight: bold; padding: 6px 0; border: none;">2. Father's Name</td><td style="font-weight: bold; border: none;">:</td><td style="border-bottom: 1px solid #bdc3c7; font-size: 14px; padding: 6px 0;">{f_name}</td></tr>
                <tr style="border: none;"><td style="font-weight: bold; padding: 6px 0; border: none;">3. Residence</td><td style="font-weight: bold; border: none;">:</td><td style="border-bottom: 1px solid #bdc3c7; font-size: 14px; padding: 6px 0;">{residence}</td></tr>
                <tr style="border: none;"><td style="font-weight: bold; padding: 6px 0; border: none;">4. Examination Passed</td><td style="font-weight: bold; border: none;">:</td><td style="border-bottom: 1px solid #bdc3c7; font-size: 14px; padding: 6px 0; font-weight: bold;">{exam_passed}</td></tr>
            </table>
            
            <table style="width: 100%; font-size: 14px; border-collapse: collapse; border: none;">
                <tr style="border: none;">
                    <td style="width: 35%; font-weight: bold; padding: 6px 0; border: none;">5. Marks Obtained</td>
                    <td style="width: 3%; font-weight: bold; border: none;">:</td>
