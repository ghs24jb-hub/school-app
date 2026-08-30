import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="GHS 24 J.B. System", page_icon="🏫", layout="centered")

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
        user_input = st.text_input("Username", value="admin")
        pass_input = st.text_input("Password", type="password")
        
        col1, col2 = st.columns(2)
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
        code_input = st.text_input("School Secret Code")
        new_pwd_input = st.text_input("Naya Password", type="password")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Update Password", type="primary", use_container_width=True):
                if code_input.strip() == st.session_state["security_code"] and new_pwd_input.strip() != "":
                    st.session_state["password"] = new_pwd_input.strip()
                    st.success("Password tabdeel ho gaya hai! Login karein.")
                    st.session_state["reset_mode"] = False
                    st.rerun()
        with col2:
            if st.button("Back to Login", use_container_width=True):
                st.session_state["reset_mode"] = False
                st.rerun()

# --- MAIN SYSTEM DASHBOARD ---
else:
    st.sidebar.markdown("<h3 style='text-align: center; color: white;'>🏫 GHS 24 J.B.</h3>", unsafe_allow_html=True)
    page = st.sidebar.radio(
        "Select Document Type:",
        ["🏠 Home Dashboard", "📝 Admission Form", "🏅 Character Certificate", "📜 School Leaving Certificate"]
    )
    
    if st.sidebar.button("Log Out", type="secondary", use_container_width=True):
        st.session_state["logged_in"] = False
        st.rerun()

    # --- HOME PAGE ---
    if page == "🏠 Home Dashboard":
        st.markdown("<h2 style='text-align: center; color: #2c3e50;'>🏫 GOVT. HIGH SCHOOL 24 J.B. FAISALABAD</h2>", unsafe_allow_html=True)
        st.success("MUKAMMAL SCHOOL SYSTEM ACTIVE")

    # --- 1. ADMISSION FORM ---
    elif page == "📝 Admission Form":
        st.markdown("<h3>📝 NEW ADMISSION FORM</h3>", unsafe_allow_html=True)
        s_name = st.text_input("Student Name")
        if st.button("💾 Save", type="primary"):
            st.success("Data Save!")

    # --- 2. CHARACTER CERTIFICATE (PURE 3D PLAQUE EMBOSSED DESIGN) ---
    elif page == "🏅 Character Certificate":
        st.markdown("<h2 style='color: #16a085;'>🏅 3D CHARACTER CERTIFICATE</h2>", unsafe_allow_html=True)
        
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
        prepared_by_name = st.text_input("Prepared By", value="")

        prepared_text = prepared_by_name if prepared_by_name.strip() != "" else "____________________"

        # Safe String with .format() to eliminate string compiler crashes 
        certificate_html = """
        <div style="
            background: #ffffff; 
            padding: 35px; 
            margin: 10px auto;
            border-left: 8px solid #784212;
            border-top: 2px solid #eaeaea;
            border-right: 2px solid #eaeaea;
            border-bottom: 6px solid #b3b3b3;
            border-radius: 8px; 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            color: #2c3e50;
            line-height: 1.7; 
            box-shadow: 0 15px 35px rgba(0,0,0,0.12), 0 5px 15px rgba(0,0,0,0.06);
        ">
            <!-- Top Header Meta -->
            <table style="width: 100%; font-size: 13px; font-weight: bold; margin-bottom: 15px;">
                <tr>
                    <td style="text-align: left; border: none; color: #7f8c8d;">Roll No. <span style="color: #2c3e50;">{0}</span></td>
                    <td style="text-align: right; border: none; color: #7f8c8d;">Regd. No. <span style="color: #2c3e50;">{1}</span></td>
                </tr>
            </table>

            
            <div style="text-align: center; margin-bottom: 20px;">
                <h1 style="margin: 0; font-size: 28px; color: #1b2631; font-family: 'Georgia', serif; font-weight: 900; text-transform: uppercase; letter-spacing: 0.5px;">GOVT. HIGH SCHOOL 24 J.B.</h1>
                <p style="margin: 3px 0 0 0; font-size: 14px; font-weight: bold; color: #7f8c8d; text-transform: uppercase; letter-spacing: 1px;">District Faisalabad.</p>
                <div style="width: 50px; height: 3px; background-color: #784212; margin: 12px auto 0 auto; border-radius: 2px;"></div>
            </div>

            <!-- Header Badge 3D Button Style -->
            <div style="text-align: center; margin-bottom: 30px;">
                <span style="
                    background: linear-gradient(135deg, #2c3e50 0%, #1a252f 100%);
                    color: #ffffff; 
                    padding: 10px 35px; 
                    font-size: 15px; 
                    font-weight: bold; 
                    letter-spacing: 2px;
                    border-radius: 4px;
                    display: inline-block;
                    box-shadow: 0 4px 10px rgba(0,0,0,0.15), inset 0 1px 0 rgba(255,255,255,0.2);
                    text-shadow: 0 1px 2px rgba(0,0,0,0.3);
                ">CHARACTER CERTIFICATE</span>
            </div>

            <!-- Introductory tagline -->
            <div style="text-align: center; font-style: italic; font-size: 14px; margin-bottom: 25px; font-weight: 600; color: #7f8c8d;">
                ——— This is to Certify that ———
            </div>

            <!-- 3D Structured fields info cards layout -->
            <div style="background: #fdfefe; padding: 20px; border-radius: 6px; border: 1px solid #f2f4f4; box-shadow: inset 0 1px 3px rgba(0,0,0,0.02); margin-bottom: 20px;">
                <table style="width: 100%; font-size: 14px; border-collapse: collapse;">
                    <tr style="border: none;"><td style="width: 32%; font-weight: bold; color: #34495e; padding: 8px 0;">1. Name of Candidate</td><td style="width: 3%; font-weight: bold; color: #7f8c8d;">:</td><td style="font-weight: 700; font-size: 16px; color: #16a085; padding: 8px 0;">{2}</td></tr>
                    <tr style="border: none;"><td style="font-weight: bold; color: #34495e; padding: 8px 0;">2. Father's Name</td><td style="font-weight: bold; color: #7f8c8d;">:</td><td style="font-weight: 600; color: #2c3e50; padding: 8px 0;">{3}</td></tr>
                    <tr style="border: none;"><td style="font-weight: bold; color: #34495e; padding: 8px 0;">3. Residence</td><td style="font-weight: bold; color: #7f8c8d;">:</td><td style="color: #5d6d7e; padding: 8px 0;">{4}</td></tr>
                    <tr style="border: none;"><td style="font-weight: bold; color: #34495e; padding: 8px 0;">4. Examination Passed</td><td style="font-weight: bold; color: #7f8c8d;">:</td><td style="font-weight: 600; color: #2c3e50; padding: 8px 0;">{5}</td></tr>
                </table>
            </div>
            
            <div style="background: #fdfefe; padding: 20px; border-radius: 6px; border: 1px solid #f2f4f4; box-shadow: inset 0 1px 3px rgba(0,0,0,0.02); margin-bottom: 20px;">
                <table style="width: 100%; font-size: 14px; border-collapse: collapse;">
                    <tr style="border: none;">
                        <td style="width: 32%; font-weight: bold; color: #34495e; padding: 8px 0;">5. Marks Obtained</td>
                        <td style="width: 3%; font-weight: bold; color: #7f8c8d;">:</td>
                        <td style="width: 35%; color: #2c3e50; padding: 8px 0;">{6}</td>
                        <td style="width: 15%; font-weight: bold; text-align: right; color: #34495e; padding: 8px 0; padding-right: 10px;">GRADE:</td>
                        <td style="font-weight: 800; color: #d35400; font-size: 16px; padding: 8px 0;">{7}</td>
