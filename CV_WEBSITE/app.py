import streamlit as st

# 1. Web Page Configuration
st.set_page_config(page_title="My Digital CV", page_icon="📄", layout="centered")

# 2. Sidebar Navigation Menu
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["About Me", "Skills & Education", "Experience", "Contact"])

# --- PAGE 1: ABOUT ME ---
if page == "About Me":
    st.title("Welcome to My Digital CV!")
    
    # Membuat kolom untuk teks perkenalan dan foto profil
    col_text, col_img = st.columns([2, 1])
    
    with col_text:
        st.subheader("Hi, I am Sharon 👋")
        st.write("I am an aspiring developer and technology enthusiast who enjoys building innovative solutions and learning new technologies.")
    
    with col_img:
        # Menampilkan foto profil (jalur relatif langsung ke file)
        st.image("ftprof.png", width=180)
    
    st.markdown("---")
    st.subheader("Summary")
    st.write("""
    A motivated Electronics Engineering student with a growing foundation in engineering and technology. 
    Eager to learn new tools, develop innovative projects, and contribute to efficient systems.
    """)

# --- PAGE 2: SKILLS & EDUCATION ---
elif page == "Skills & Education":
    st.title("Skills & Education")
    
    st.subheader("🎓 Education")
    st.write("**Technical & Engineering Student** - Electronics Engineering (2024 - Present)")
    st.write("**High School Diploma** - (2021 - 2024)")
    
    st.markdown("---")
    
    st.subheader("🛠️ Skills")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Programming Languages & Hardware:**")
        st.write("- Python\n- C / C++ (AVR & Arduino)\n- HTML / CSS")
    with col2:
        st.write("**Tools & Frameworks:**")
        st.write("- Streamlit\n- Proteus Simulation\n- VS Code & Git")

# --- PAGE 3: EXPERIENCE ---
elif page == "Experience":
    st.title("Projects & Experience")
    
    st.subheader("💼 Projects")
    st.write("**Project 1: Microcontroller & Embedded Systems**")
    st.write("- Designed and developed automated control systems utilizing microcontrollers.")
    st.write("- Programmed logic for sensor integration and sequential hardware operations.")
    
    st.write("") 
    
    st.write("**Project 2: Personal Portfolio Web**")
    st.write("- Built a multi-page digital CV using Python and Streamlit.")

# --- PAGE 4: CONTACT ---
elif page == "Contact":
    st.title("Contact Me")
    st.write("Feel free to reach out to me through any of the platforms below:")
    
    st.write("📧 **Email:** your.email@example.com")
    st.write("🔗 **LinkedIn:** [linkedin.com/in/username](https://linkedin.com)")
    st.write("💻 **GitHub:** [github.com/username](https://github.com)")