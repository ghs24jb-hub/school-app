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
        
        col1, col2 = st.columns([1, 1])
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
        
        col1, col2 = st.columns([1, 1])
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
    # Sidebar navigation
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
                doc_content = (
                    "==================================================\n"
                    "    GOVT. HIGH SCHOOL 24 J.B. DISTT. FAISALABAD   \n"
                    "                  ADMISSION FORM                  \n"
                    "==================================================\n"
                    f"Form No: {form_no}\n"
                    f"Admission No: {adm_no}\n"
                    f"Student Name: {s_name}\n"
                    f"Father Name: {f_name}\n"
                    f"Contact No: {contact}\n"
                    f"Present Address: {address}\n"
                    "==================================================\n"
                )
                st.success("Admission Document tayar hai! Neeche download button par click karen.")
                st.download_button(
                    label="📥 Download Admission File (.txt)",
                    data=doc_content,
                    file_name=f"Admission_{s_name.replace(' ', '_')}.txt",
                    mime="text/plain"
                )

    # --- 2. CHARACTER CERTIFICATE ---
    elif page == "🏅 Character Certificate":
        st.markdown("<h3 style='color: #16a085;'>🏅 CHARACTER CERTIFICATE GENERATOR</h3>", unsafe_allow_html=True)
        
        roll_no = st.text_input("Roll No")
        regd_no = st.text_input("Regd No")
        c_name = st.text_input("Candidate Name")
        fat_name = st.text_input("Father's Name")
        marks = st.text_input("Marks Obtained")
        
        if st.button("💾 Document Generate Karein", type="primary"):
            if not c_name.strip():
                st.error("Candidate Name lazmi likhein!")
            else:
                doc_content = (
                    "==================================================\n"
                    "        GOVT. HIGH SCHOOL 24 J.B. FAISALABAD      \n"
                    "               CHARACTER CERTIFICATE              \n"
                    "==================================================\n"
                    f"Roll No: {roll_no}\n"
                    f"Regd No: {regd_no}\n"
                    f"Candidate Name: {c_name}\n"
                    f"Father's Name: {fat_name}\n"
                    f"Marks Obtained: {marks}\n"
                    "==================================================\n"
                    "\n                                    HEAD MASTER\n"
                )
                st.success("Certificate Document tayar hai! Neeche download button par click karen.")
                st.download_button(
                    label="📥 Download Certificate File (.txt)",
                    data=doc_content,
                    file_name=f"Character_{c_name.replace(' ', '_')}.txt",
                    mime="text/plain"
                )

    # --- 3. SCHOOL LEAVING CERTIFICATE ---
    elif page == "📜 School Leaving Certificate":
        st.markdown("<h3 style='color: #d35400;'>📜 SCHOOL LEAVING CERTIFICATE (SLC)</h3>", unsafe_allow_html=True)
        
        sr_no = st.text_input("Sr No")
        file_no = st.text_input("File No")
        stu_name = st.text_input("Student Name")
        fath_name = st.text_input("Father's Name")
        class_in = st.text_input("Class Reading In")
        
        if st.button("💾 Document Generate Karein", type="primary"):
            if not stu_name.strip():
                st.error("Student Name lazmi likhein!")
            else:
                doc_content = (
                    "==================================================\n"
                    "        GOVT. HIGH SCHOOL 24 J.B. FAISALABAD      \n"
                    "             SCHOOL LEAVING CERTIFICATE           \n"
                    "==================================================\n"
                    f"Sr No: {sr_no}\n"
                    f"File No: {file_no}\n"
                    f"Student Name: {stu_name}\n"
                    f"Father's Name: {fath_name}\n"
                    f"Class Reading In: {class_in}\n"
                    "==================================================\n"
                    "\nPrepared By: _________            Headmaster: _________\n"
                )
                st.success("SLC Document tayar hai! Neeche download button par click karen.")
                st.download_button(
                    label="📥 Download SLC File (.txt)",
                    data=doc_content,
                    file_name=f"SLC_{stu_name.replace(' ', '_')}.txt",
                    mime="text/plain"
                )
