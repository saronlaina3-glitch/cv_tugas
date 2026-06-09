import streamlit as st

st.set_page_config(
    page_title="My Digital CV",
    page_icon="📄",
    layout="centered"
)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to:",
    ["About Me", "Skills & Education", "Experience", "Contact"]
)

# About Me
if page == "About Me":
    st.title("Welcome to My Digital CV! 📄")
    st.subheader("Hi, I am Sharon 👋")

    st.write(
        "I am an aspiring developer and technology enthusiast "
        "who enjoys building innovative solutions and learning new technologies."
    )
with col_img:
        # Menampilkan foto profil kamu (pastikan nama filenya cocok)
        st.image("CV_WEBSITE/foto_profil.jpg", width=180)

    st.markdown("---")

    st.subheader("Summary")
    st.write(
        "A motivated Electronics Engineering student with a growing foundation "
        "in engineering and technology. Eager to learn new tools, develop "
        "innovative projects, and contribute to efficient systems."
    )

# Skills & Education
elif page == "Skills & Education":
    st.title("Skills & Education")

    st.subheader("🎓 Education")
    st.write(
        "**Electronics Engineering Student**  \n"
        "Politeknik Caltex Riau (2024 - Present)"
    )

    st.write(
        "**High School Diploma**  \n"
        "SMA Negeri 1 Raya (2021 - 2023)"
    )

    st.markdown("---")

    st.subheader("🛠️ Skills")

    col1, col2 = st.columns(2)

    with col1:
        st.write("### Programming & Hardware")
        st.write("""
        - Python
        - C / C++
        - Arduino
        - AVR Microcontroller
        - HTML / CSS
        """)

    with col2:
        st.write("### Tools & Software")
        st.write("""
        - Streamlit
        - Proteus
        - VS Code
        - Git & GitHub
        - LabVIEW
        """)

# Experience
elif page == "Experience":
    st.title("Projects & Experience")

    st.subheader("💼 Project 1: Microcontroller & Embedded Systems")
    st.write(
        "- Designed and developed automated control systems using microcontrollers.\n"
        "- Integrated sensors and implemented hardware control logic."
    )

    st.subheader("💼 Project 2: Personal Portfolio Website")
    st.write(
        "- Developed a digital CV using Python and Streamlit.\n"
        "- Created a multi-page interface with navigation and responsive content."
    )

# Contact
elif page == "Contact":
    st.title("Contact Me")

    st.write(
        "Feel free to reach out through the platforms below:"
    )

    st.write("📧 Email: sharon24trse@mahasiswa.pcr.ac.id")
    st.write("🔗 LinkedIn: https://linkedin.com")
    st.write("💻 GitHub: https://github.com")