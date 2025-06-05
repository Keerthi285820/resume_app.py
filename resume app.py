import streamlit as st

st.set_page_config(page_title="Simple Resume Builder", layout="centered")
st.title("📝 Simple Resume Builder")

# Form
with st.form("resume_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    education = st.text_area("Education Details")
    experience = st.text_area("Work Experience")
    skills = st.text_area("Skills")

    submitted = st.form_submit_button("Generate Resume")

# Output
if submitted:
    st.success("🎉 Resume Generated Below!")

    resume = f"""
    =============================
              RESUME
    =============================
    Name: {name}
    Email: {email}
    Phone: {phone}

    EDUCATION:
    {education}

    EXPERIENCE:
    {experience}

    SKILLS:
    {skills}
    =============================
    """

    st.text_area("📄 Your Resume", resume, height=300)
    st.download_button("📥 Download as Text File", data=resume, file_name="resume.txt")

    html_resume = f"""
    <html>
    <body>
        <h1>{name}</h1>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>Phone:</strong> {phone}</p>
        <h2>Education</h2><p>{education}</p>
        <h2>Experience</h2><p>{experience}</p>
        <h2>Skills</h2><p>{skills}</p>
    </body>
    </html>
    """
    st.download_button("📥 Download as HTML", data=html_resume, file_name="resume.html", mime="text/html")
