import tkinter as tk
from tkinter import messagebox
import os

# --- DATABASE ---
USER_DATA = {
    "username": "admin",
    "password": "123",
    "security_code": "2424"
}

# --- SYSTEM LOGIN ---
def login_karein():
    if entry_user.get() == USER_DATA["username"] and entry_pass.get() == USER_DATA["password"]:
        messagebox.showinfo("Kamyabi", "Login Kamyab!")
        login_window.destroy()  
        main_dashboard_window()   
    else:
        messagebox.showerror("Error", "Username ya Password galat hai!")

# --- PASSWORD RESET ---
def reset_password_window():
    reset_win = tk.Toplevel(login_window)
    reset_win.title("Reset Password")
    reset_win.geometry("320x280")
    reset_win.configure(bg="#f8f9fa")
    
    tk.Label(reset_win, text="🔐 PASSWORD RESET", font=("Arial", 11, "bold"), bg="#f8f9fa", fg="#c0392b").pack(pady=10)
    
    tk.Label(reset_win, text="School Secret Code Likhein:", font=("Arial", 10), bg="#f8f9fa").pack()
    entry_code = tk.Entry(reset_win, font=("Arial", 10), width=25, bd=2, relief="groove")
    entry_code.pack(pady=5)
    
    tk.Label(reset_win, text="Naya Password Likhein:", font=("Arial", 10), bg="#f8f9fa").pack()
    entry_new_pwd = tk.Entry(reset_win, font=("Arial", 10), width=25, show="*", bd=2, relief="groove")
    entry_new_pwd.pack(pady=5)
    
    def save_new_password():
        if entry_code.get().strip() == USER_DATA["security_code"]:
            if entry_new_pwd.get().strip() != "":
                USER_DATA["password"] = entry_new_pwd.get().strip()
                messagebox.showinfo("Kamyabi", "Password tabdeel ho gaya hai!\nAb naye password se login karein.")
                reset_win.destroy()
            else:
                messagebox.showerror("Error", "Naya password khali nahi ho sakta!")
        else:
            messagebox.showerror("Error", "Secret Code galat hai!")
            
    tk.Button(reset_win, text="Update Password", font=("Arial", 10, "bold"), bg="#c0392b", fg="white", width=18, command=save_new_password).pack(pady=20)

# --- FRAME MANAGEMENT ---
def clear_content_frame():
    for widget in content_frame.winfo_children():
        widget.destroy()

def show_dashboard_home():
    clear_content_frame()
    tk.Label(content_frame, text="🏫 GOVT. HIGH SCHOOL 24 J.B. FAISALABAD", font=("Arial", 14, "bold"), bg="white", fg="#2c3e50").pack(pady=20)
    tk.Label(content_frame, text="✨ MUKAMMAL SCHOOL SYSTEM ACTIVE ✨", font=("Arial", 11, "bold"), fg="green", bg="white").pack(pady=5)
    tk.Label(content_frame, text="Sidebar menu se kisi bhi document ko select karke print nikaalein.", font=("Arial", 10), bg="white").pack(pady=10)

# --- 1. ADMISSION FORM ---
def show_admission_page():
    clear_content_frame()
    tk.Label(content_frame, text="📝 NEW ADMISSION FORM", font=("Arial", 14, "bold"), fg="#2980b9", bg="white").pack(pady=10)
    
    fields = ["Form No", "Admission No", "Student Name", "Father Name", "Contact No", "Present Address"]
    entries = {}
    
    for f in fields:
        tk.Label(content_frame, text=f + ":", font=("Arial", 10), bg="white").pack()
        e = tk.Entry(content_frame, font=("Arial", 10), width=35, bd=2, relief="groove")
        e.pack(pady=2)
        entries[f] = e

    def save_and_print_admission():
        name = entries["Student Name"].get().strip()
        if not name:
            messagebox.showerror("Error", "Student Name lazmi likhein!")
            return
        filename = f"Admission_{name.replace(' ', '_')}.txt"
        with open(filename, "w") as f:
            f.write("==================================================\n")
            f.write("    GOVT. HIGH SCHOOL 24 J.B. DISTT. FAISALABAD   \n")
            f.write("                  ADMISSION FORM                  \n")
            f.write("==================================================\n")
            for k, v in entries.items():
                f.write(f"{k}: {v.get().strip()}\n")
            f.write("==================================================\n")
        
        os.startfile(filename)
        messagebox.showinfo("Kamyabi", "Admission Data save ho gaya!")

    tk.Button(content_frame, text="💾 Save aur Print Karein", font=("Arial", 10, "bold"), bg="#2980b9", fg="white", command=save_and_print_admission).pack(pady=10)

# --- 2. CHARACTER CERTIFICATE ---
def show_character_page():
    clear_content_frame()
    tk.Label(content_frame, text="🏅 CHARACTER CERTIFICATE GENERATOR", font=("Arial", 14, "bold"), fg="#16a085", bg="white").pack(pady=10)
    
    fields = ["Roll No", "Regd No", "Candidate Name", "Father's Name", "Marks Obtained"]
    entries = {}
    
    for f in fields:
        tk.Label(content_frame, text=f + ":", font=("Arial", 10), bg="white").pack()
        e = tk.Entry(content_frame, font=("Arial", 10), width=35, bd=2, relief="groove")
        e.pack(pady=2)
        entries[f] = e

    def save_and_print_character():
        name = entries["Candidate Name"].get().strip()
        if not name:
            messagebox.showerror("Error", "Candidate Name lazmi likhein!")
            return
        filename = f"Character_{name.replace(' ', '_')}.txt"
        with open(filename, "w") as f:
            f.write("==================================================\n")
            f.write("        GOVT. HIGH SCHOOL 24 J.B. FAISALABAD      \n")
            f.write("               CHARACTER CERTIFICATE              \n")
            f.write("==================================================\n")
            for k, v in entries.items():
                f.write(f"{k}: {v.get().strip()}\n")
            f.write("==================================================\n")
            f.write("\n                                    HEAD MASTER\n")
        
        os.startfile(filename)
        messagebox.showinfo("Kamyabi", "Certificate Data save ho gaya!")

    tk.Button(content_frame, text="💾 Save aur Print Karein", font=("Arial", 10, "bold"), bg="#16a085", fg="white", command=save_and_print_character).pack(pady=10)

# --- 3. SCHOOL LEAVING CERTIFICATE (SLC) ---
def show_slc_page():
    clear_content_frame()
    tk.Label(content_frame, text="📜 SCHOOL LEAVING CERTIFICATE (SLC)", font=("Arial", 14, "bold"), fg="#d35400", bg="white").pack(pady=10)
    
    fields = ["Sr No", "File No", "Student Name", "Father's Name", "Class Reading In"]
    entries = {}
    
    for f in fields:
        tk.Label(content_frame, text=f + ":", font=("Arial", 10), bg="white").pack()
        e = tk.Entry(content_frame, font=("Arial", 10), width=35, bd=2, relief="groove")
        e.pack(pady=2)
        entries[f] = e

    def save_and_print_slc():
        name = entries["Student Name"].get().strip()
        if not name:
            messagebox.showerror("Error", "Student Name lazmi likhein!")
            return
        filename = f"SLC_{name.replace(' ', '_')}.txt"
        with open(filename, "w") as f:
            f.write("==================================================\n")
            f.write("        GOVT. HIGH SCHOOL 24 J.B. FAISALABAD      \n")
            f.write("             SCHOOL LEAVING CERTIFICATE           \n")
            f.write("==================================================\n")
            for k, v in entries.items():
                f.write(f"{k}: {v.get().strip()}\n")
            f.write("==================================================\n")
            f.write("\nPrepared By: _________            Headmaster: _________\n")
        
        os.startfile(filename)
        messagebox.showinfo("Kamyabi", "SLC Data save ho gaya!")

    tk.Button(content_frame, text="💾 Save aur Print Karein", font=("Arial", 10, "bold"), bg="#d35400", fg="white", command=save_and_print_slc).pack(pady=10)

# --- DASHBOARD WINDOW ---
def main_dashboard_window():
    global content_frame
    main_win = tk.Tk()
    main_win.title("GHS 24 J.B. - Main System")
    main_win.geometry("850x620")
    
    sidebar = tk.Frame(main_win, bg="#2c3e50", width=220)
    sidebar.pack(side="left", fill="y")
    sidebar.pack_propagate(False)
    
    tk.Label(sidebar, text="GHS 24 J.B.", font=("Arial", 12, "bold"), fg="white", bg="#2c3e50").pack(pady=15)
    
    tk.Button(sidebar, text="🏠 Home Dashboard", font=("Arial", 10), bg="#34495e", fg="white", bd=0, anchor="w", padx=10, command=show_dashboard_home).pack(fill="x", pady=4, padx=5)
    tk.Button(sidebar, text="📝 Admission Form", font=("Arial", 10), bg="#2980b9", fg="white", bd=0, anchor="w", padx=10, command=show_admission_page).pack(fill="x", pady=4, padx=5)
    tk.Button(sidebar, text="🏅 Character Certificate", font=("Arial", 10), bg="#16a085", fg="white", bd=0, anchor="w", padx=10, command=show_character_page).pack(fill="x", pady=4, padx=5)
    tk.Button(sidebar, text="📜 Leaving Certificate (SLC)", font=("Arial", 10), bg="#d35400", fg="white", bd=0, anchor="w", padx=10, command=show_slc_page).pack(fill="x", pady=4, padx=5)
    tk.Button(sidebar, text="🚪 Logout", font=("Arial", 10), bg="#c0392b", fg="white", bd=0, command=main_win.destroy).pack(fill="x", side="bottom", pady=20, padx=5)
    
    content_frame = tk.Frame(main_win, bg="white")
    content_frame.pack(side="right", fill="both", expand=True)
    
    show_dashboard_home()
    main_win.mainloop()

# --- LOGIN WINDOW (STARTUP) ---
login_window = tk.Tk()
login_window.title("School Login")
login_window.geometry("300x320") # Window thodi badi ki taake buttons sahi dikhein

tk.Label(login_window, text="SCHOOL LOGIN", font=("Arial", 12, "bold")).pack(pady=15)
tk.Label(login_window, text="Username:").pack()
entry_user = tk.Entry(login_window, font=("Arial", 10))
entry_user.pack(pady=5)
tk.Label(login_window, text="Password:").pack()
entry_pass = tk.Entry(login_window, font=("Arial", 10), show="*")
entry_pass.pack(pady=5)

# --- LOGIN BUTTONS ATTACHED HERE ---
btn_login = tk.Button(login_window, text="Login", font=("Arial", 10, "bold"), bg="blue", fg="white", width=15, command=login_karein)
btn_login.pack(pady=12)

