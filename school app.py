import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="GHS 24 J.B. System", page_icon="🏫")

# --- DATABASE IN SESSION ---
if "password" not in st.session_state:
    st.session_state["password"] = "123"
if "security_code" not in st.session_state:
    st.session_state["security_code"] = "2424"
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "reset_mode" not in st.session_state:
    st.session_state["reset_mode"] = False

# --- LOGIN BACKEND ---
if not st.session_state["logged_in"]:
    if not st.session_state["reset_mode"]:
        st.subheader("🔐 SYSTEM LOGIN")
        st.caption("Govt. High School 24 J.B. Faisalabad")
        user_input = st.text_input("Username", value="admin")
        pass_input = st.text_input("Password", type="password")
        
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Login Karein", type="primary", use_container_width=True):
                if user_input == "admin" and pass_input == st.session_state["password"]:
                    st.session_state["logged_in"] = True
                    st.rerun()
                else:
                    st.error("Username ya Password galat hai!")
        with c2:
            if st.button("Reset Password?", use_container_width=True):
                st.session_state["reset_mode"] = True
                st.rerun()
    else:
        st.subheader("🔐 RESET PASSWORD")
        code_input = st.text_input("School Secret Code")
        new_pwd_input = st.text_input("Naya Password", type="password")
        
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Update Password", type="primary", use_container_width=True):
                if code_input.strip() == st.session_state["security_code"]:
                    if new_pwd_input.strip() != "":
                        st.session_state["password"] = new_pwd_input.strip()
                        st.success("Password tabdeel ho gaya hai! Ab login karein.")
                        st.session_state["reset_mode"] = False
                        st.rerun()
                else:
                    st.error("Secret Code galat hai!")
        with c2:
            if st.button("Back to Login", use_container_width=True):
                st.session_state["reset_mode"] = False
                st.rerun()

# --- MAIN SYSTEM ---
else:
    st.sidebar.title("🏫 GHS 24 J.B.")
    st.sidebar.caption("Main System Menu")
    st.sidebar.divider()
    
    page = st.sidebar.radio(
        "Select Section:",
        ["🏠 Home Dashboard", "📝 Admission Form", "🏅 Character Certificate", "📜 School Leaving Certificate"]
    )
    
    st.sidebar.divider()
    if st.sidebar.button("Log Out", type="secondary", use_container_width=True):
        st.session_state["logged_in"] = False
        st.rerun()

    # --- HOME PAGE ---
    if page == "🏠 Home Dashboard":
        st.title("GOVT. HIGH SCHOOL 24 J.B. FAISALABAD")
        st.success("MUKAMMAL SCHOOL SYSTEM ACTIVE")
        st.info("Sidebar se form select karke details fill karein aur documents taiyar karein.")

    # --- 1. ADMISSION FORM ---
    elif page == "📝 Admission Form":
        st.title("📝 NEW ADMISSION FORM")
        
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
                doc_text = f"Form No: {form_no}\nAdmission No: {adm_no}\nStudent Name: {s_name}\nFather Name: {f_name}\nContact No: {contact}\nAddress: {address}"
                st.success("Data Save ho gaya!")
                st.download_button("📥 Download Admission File (.txt)", data=doc_text, file_name=f"Admission_{s_name}.txt")

    # --- 2. CHARACTER CERTIFICATE SECTION ---
    elif page == "🏅 Character Certificate":
        st.title("🏅 CHARACTER CERTIFICATE GENERATOR")
        
        # Inputs matching your premium certificate fields
        col1, col2 = st.columns(2)
        with col1:
            roll_no = st.text_input("Roll No.", value="510622")
            c_name = st.text_input("1. Name of Candidate", value="Awais Ali")
            residence = st.text_input("3. Residence", value="Chak No. 24 J.B. FAISALABAD")
            marks = st.text_input("5. Marks Obtained", value="692 / 1200")
            subjects = st.text_input("7. Subjects Offered", value="SCIENCE GROUP")
            remarks = st.text_input("9. Any Other Remarks", value="He is a regular student.")
        with col2:
            regd_no = st.text_input("Regd. No.", value="170663-PR-2022")
            f_name = st.text_input("2. Father's Name", value="Muhammad Ansir")
            exam_passed = st.text_input("4. Examination Passed", value="SSC 2024 (ANNUAL)")
            grade = st.text_input("Grade", value="C")
            moral = st.text_input("6. Moral Character", value="GOOD")
            games = st.text_input("8. Games Played at School", value="YES")
            
        cert_date = st.text_input("Dated", value="29-07-2024")
        prep_by = st.text_input("Prepared By", value="Staff Member")

        st.markdown("---")
        st.subheader("📄 Certificate Data Preview")
        
        # Safe display format without string parsing crashes
        st.code(f"""
        ==================================================================
                  GOVT. HIGH SCHOOL 24 J.B. FAISALABAD
                         CHARACTER CERTIFICATE
        ==================================================================
        Roll No: {roll_no}                               Regd No: {regd_no}
        ------------------------------------------------------------------
        1. Name of Candidate   :  {c_name}
        2. Father's Name       :  {f_name}
        3. Residence           :  {residence}
        4. Examination Passed  :  {exam_passed}
        5. Marks Obtained      :  {marks}               GRADE: {grade}
        6. Moral Character     :  {moral}
        7. Subjects Offered    :  {subjects}
        8. Games Played        :  {games}
        9. Any Other Remarks   :  {remarks}
        ------------------------------------------------------------------
        During his/her study in this school, his/her conduct has been good.
        
        Dated: {cert_date}        Prepared By: {prep_by}        HEAD MASTER
        ==================================================================
        """, language="text")

    # --- 3. SCHOOL LEAVING CERTIFICATE ---
    elif page == "📜 School Leaving Certificate":
        st.title("📜 SCHOOL LEAVING CERTIFICATE (SLC)")
        sr_no = st.text_input("Sr No")
        file_no = st.text_input("File No")
        stu_name = st.text_input("Student Name")
        fath_name = st.text_input("Father's Name")
        class_in = st.text_input("Class Reading In")
        
        if st.button("💾 Document Generate Karein", type="primary"):
            if not stu_name.strip():
                st.error("Student Name lazmi likhein!")
            else:
                slc_text = f"Sr No: {sr_no}\nFile No: {file_no}\nStudent Name: {stu_name}\nFather's Name: {fath_name}\nClass: {class_in}"
                st.success("SLC Document tayar hai!")
                st.download_button("📥 Download SLC File (.txt)", data=slc_text, file_name=f"SLC_{stu_name}.txt")
