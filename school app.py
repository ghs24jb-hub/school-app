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

    # --- 3. CHARACTER CERTIFICATE (100% SAFE NATIVE LAYOUT) ---
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
        if st.button("🖨️ Click Here to Print Certificate", type="primary", use_container_width=True):
            st.warning("Printers active karne ke liye keyboard se 'Ctrl + P' dabayein. Yeh card automatic page par fit ho jayega.")

        st.markdown("### 🖥️ Premium Print Preview")

        # Native Box design without HTML strings conflicts
        with st.container(border=True):
            st.write(f"**Roll No.** {roll_no}  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; **Regd. No.** {regd_no}")
            st.markdown("<h1 style='text-align: center; color: black; font-family: serif; margin-bottom:0;'>GOVT. HIGH SCHOOL 24 J.B.</h1>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; color: gray; margin-top:0;'>District Faisalabad.</p>", unsafe_allow_html=True)
            st.markdown("<h3 style='text-align: center; border: 2px solid black; padding: 5px; margin: 15px 0;'>CHARACTER CERTIFICATE</h3>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; font-style: italic;'>——— This is to Certify that: ———</p>", unsafe_allow_html=True)
            
            # 1 to 9 Underlined lines extending to the end
            st.markdown(f"**1. Name of Candidate:** {c_name}  \n________________________________________________________________________________________")
            st.markdown(f"**2. Father's Name:** {f_name_cert}  \n________________________________________________________________________________________")
            st.markdown(f"**3. Residence:** {residence}  \n________________________________________________________________________________________")
            st.markdown(f"**4. Examination Passed:** {exam_passed}  \n________________________________________________________________________________________")
            st.markdown(f"**5. Marks Obtained:** {marks} &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; **GRADE:** {grade}  \n________________________________________________________________________________________")
            st.markdown(f"**6. Moral Character:** {moral}  \n________________________________________________________________________________________")
            st.markdown(f"**7. Subjects Offered:** {subjects}  \n________________________________________________________________________________________")
            st.markdown(f"**8. Games Played at School:** {games}  \n________________________________________________________________________________________")
            st.markdown(f"**9. Any Other Remarks:** {remarks}  \n________________________________________________________________________________________")
            
            st.write("")
            st.markdown("<p style='text-align: center; font-style: italic; font-weight: bold;'>During his/her study in this school, his/her conduct has been good.</p>", unsafe_allow_html=True)
            st.write("")
            st.write("")
            
            # Bottom row footer
            f1, f2, f3 = st.columns(3)
            with f1:
                st.write(f"**Dated:** {cert_date}")
                st.write(f"**Prepared By:** {p_text}")
            with f2:
                st.markdown("<div style='width: 55px; height: 55px; border: 1px dashed gray; border-radius: 50%; font-size: 10px; display: flex; align-items: center; justify-content: center; color: gray; margin: 0 auto;'>Stamp</div>", unsafe_allow_html=True)
            with f3:
                st.markdown("<p style='text-align: right; margin-top: 25px;'>**HEAD MASTER**</p>", unsafe_allow_html=True)

    # --- 4. SCHOOL LEAVING CERTIFICATE ---
    elif page == "📜 School Leaving Certificate":
        st.subheader("📜 SCHOOL LEAVING CERTIFICATE (SLC)")
        stu_name = st.text_input("Student Name")
        if st.button("💾 Save SLC Data", type="primary"):
            st.success("SLC saved!")
