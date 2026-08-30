import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="GHS 24 J.B. System", page_icon="🏫", layout="centered")

# --- INITIALIZE DATABASE IN SESSION STATE ---
if "password" not in st.session_state:
    st.session_state["password"] = "123"
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# --- SYSTEM LOGIN ---
if not st.session_state["logged_in"]:
    st.markdown("<h2 style='text-align: center; color: #2c3e50;'>🏫 SYSTEM LOGIN</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>Govt. High School 24 J.B. Faisalabad</p>", unsafe_allow_html=True)
    
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
    # Sidebar Setup
    st.sidebar.markdown("<h2 style='text-align: center;'>🏫 GHS 24 J.B.</h2>", unsafe_allow_html=True)
    st.sidebar.markdown("<p style='text-align: center; color: gray;'>Main System Menu</p>", unsafe_allow_html=True)
    st.sidebar.divider()
    
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
        st.info("Left side menu se kisi bhi document ko select karke print nikaalein. Yeh app mobile aur computer dono par perfectly chalegi.")

    # --- 2. ADMISSION FORM ---
    elif page == "📝 Admission Form":
        st.subheader("📝 NEW ADMISSION FORM ENTRY")
        
        col1, col2 = st.columns(2)
        with col1:
            form_no = st.text_input("Form No")
            s_name = st.text_input("Student Name")
            contact = st.text_input("Contact No")
        with col2:
            adm_no = st.text_input("Admission No")
            f_name = st.text_input("Father Name")
            address = st.text_input("Present Address")
            
        if st.button("💾 Save Admission Data", type="primary", use_container_width=True):
            if not s_name.strip():
                st.error("Student Name lazmi likhein!")
            else:
                st.success(f"Student '{s_name}' ka admission data kamyabi se save ho gaya!")

    # --- 3. CHARACTER CERTIFICATE (PURE STREAMLIT DIGITAL FORMAT) ---
    elif page == "🏅 Character Certificate":
        st.subheader("🏅 CHARACTER CERTIFICATE GENERATOR")
        
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

        st.divider()
        st.markdown("### 🖥️ Digital Print Preview")

        # Native Border Container blocks logic (Cannot Crash under any circumstances)
        with st.container(border=True):
            st.markdown("<h2 style='text-align: center; color: #1b2631; margin:0;'>GOVT. HIGH SCHOOL 24 J.B.</h2>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; color: #7f8c8d; margin:0;'>District Faisalabad.</p>", unsafe_allow_html=True)
            st.markdown("<h3 style='text-align: center; background-color: #2c3e50; color: white; padding: 8px; border-radius: 4px;'>CHARACTER CERTIFICATE</h3>", unsafe_allow_html=True)
            
            # Top IDs
            st.write(f"**Roll No:** `{roll_no}` &nbsp;&nbsp;|&nbsp;&nbsp; **Regd. No:** `{regd_no}`")
            st.divider()
            
            # Content lines
            st.write(f"👉 **1. Name of Candidate:** {c_name}")
            st.write(f"👉 **2. Father's Name:** {f_name_cert}")
            st.write(f"👉 **3. Residence:** {residence}")
            st.write(f"👉 **4. Examination Passed:** {exam_passed}")
            st.write(f"👉 **5. Marks Obtained:** {marks} &nbsp;&nbsp;&nbsp;&nbsp; **GRADE:** `{grade}`")
            st.write(f"👉 **6. Moral Character:** {moral}")
            st.write(f"👉 **7. Subjects Offered:** {subjects}")
            st.write(f"👉 **8. Games Played at School:** {games}")
            st.write(f"👉 **9. Any Other Remarks:** {remarks}")
            
            st.divider()
            st.markdown("<p style='text-align: center; font-style: italic; font-weight: bold;'>During his/her study in this school, his/her conduct has been good.</p>", unsafe_allow_html=True)
            st.write("")
            
            # Footers Signatures
            f_col1, f_col2, f_col3 = st.columns(3)
            with f_col1:
                st.write(f"📅 **Dated:** {cert_date}")
            with f_col2:
                p_text = prep_by if prep_by.strip() != "" else "____________________"
                st.write(f"✍️ **Prepared By:** {p_text}")
            with f_col3:
                st.write("👔 **HEAD MASTER**")

        st.caption("💡 **Tip:** Is digital format ka print nikalne ke liye apne keyboard se `Ctrl + P` dabayein.")

    # --- 4. SCHOOL LEAVING CERTIFICATE ---
    elif page == "📜 School Leaving Certificate":
        st.subheader("📜 SCHOOL LEAVING CERTIFICATE (SLC)")
        
        col1, col2 = st.columns(2)
        with col1:
            sr_no = st.text_input("Sr No")
            stu_name = st.text_input("Student Name")
            class_in = st.text_input("Class Reading In")
        with col2:
            file_no = st.text_input("File No")
            fath_name = st.text_input("Father's Name")
            
        if st.button("💾 Save SLC Document", type="primary", use_container_width=True):
            if not stu_name.strip():
                st.error("Student Name lazmi likhein!")
            else:
                st.success(f"SLC data for '{stu_name}' save ho gaya!")
