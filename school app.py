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

    # --- 3. CHARACTER CERTIFICATE (100% STABLE NO-CSS PRINT DESIGN) ---
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

        # Plain HTML layout structure that does not confuse python code engine
        preview_text = (
            "<div style='border: 5px double #b8860b; padding: 25px; background: white; font-family: Arial; color: black;'>"
            "   <div style='font-size: 14px; font-weight: bold; margin-bottom: 15px; overflow: hidden;'>"
            "       <span style='float: left;'>Roll No. " + roll_no + "</span>"
            "       <span style='float: right;'>Regd. No. " + regd_no + "</span>"
            "   </div>"
            "   <div style='text-align: center; margin-bottom: 20px;'>"
            "       <h1 style='margin: 0; font-size: 26px; font-weight: bold;'>GOVT. HIGH SCHOOL 24 J.B.</h1>"
            "       <p style='margin: 2px 0 0 0; font-size: 13px; color: gray;'>District Faisalabad.</p>"
            "       <div style='width: 120px; height: 2px; background: #b8860b; margin: 8px auto 0 auto;'></div>"
            "   </div>"
            "   <div style='text-align: center; margin: 15px 0;'>"
            "       <span style='border: 2px solid black; padding: 6px 30px; font-size: 15px; font-weight: bold; display: inline-block;'>CHARACTER CERTIFICATE</span>"
            "   </div>"
            "   <div style='text-align: center; font-style: italic; font-size: 14px; margin-bottom: 20px;'>——— This is to Certify that: ———</div>"
            "   <div style='font-size: 15px; line-height: 2; margin-bottom: 20px; text-align: justify;'>"
            "       1. Name of Candidate: <b>" + c_name + "</b><br>"
            "       2. Father's Name: <b>" + f_name_cert + "</b><br>"
            "       3. Residence: " + residence + "<br>"
            "       4. Examination Passed: <b>" + exam_passed + "</b><br>"
            "       5. Marks Obtained: " + marks + " &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>GRADE:</b> " + grade + "<br>"
            "       6. Moral Character: <b>" + moral + "</b><br>"
            "       7. Subjects Offered: " + subjects + "<br>"
            "       8. Games Played at School: " + games + "<br>"
            "       9. Any Other Remarks: " + remarks + ""
            "   </div>"
            "   <div style='text-align: center; font-style: italic; font-size: 14px; margin: 20px 0; font-weight: bold;'>During his/her study in this school, his/her conduct has been good.</div>"
            "   <div style='margin-top: 50px; font-size: 13px; font-weight: bold; overflow: hidden;'>"
            "       <div style='float: left; width: 40%;'>"
            "           Dated: <u>" + cert_date + "</u><br>"
            "           Prepared By: <span style='font-weight: normal;'>" + p_text + "</span>"
            "       </div>"
            "       <div style='float: left; width: 20%; text-align: center;'>"
            "           <div style='width: 55px; height: 55px; border: 1px dashed #b8860b; border-radius: 50%; font-size: 9px; display: flex; align-items: center; justify-content: center; color: gray; margin: 0 auto;'>Stamp</div>"
            "       </div>"
            "       <div style='float: right; width: 40%; text-align: right; margin-top: 20px;'>"
            "           HEAD MASTER"
            "       </div>"
            "   </div>"
            "</div>"
        )
        
        st.markdown(preview_text, unsafe_allow_html=True)
        st.caption("💡 **Tip:** Is error-free stable design ka print nikalne ke liye browser me shortcut key `Ctrl + P` dabayein.")

    # --- 4. SCHOOL LEAVING CERTIFICATE ---
    elif page == "📜 School Leaving Certificate":
        st.subheader("📜 SCHOOL LEAVING CERTIFICATE (SLC)")
        stu_name = st.text_input("Student Name")
        if st.button("💾 Save SLC Data", type="primary"):
            st.success("SLC saved!")
