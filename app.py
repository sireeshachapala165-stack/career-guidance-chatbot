import streamlit as st

st.set_page_config(
    page_title="AI Career Guidance Chatbot",
    page_icon="🎓",
    layout="wide"
)

# Sidebar
st.sidebar.title("🎓 Career Guidance Bot")

menu = st.sidebar.radio(
    "Choose Option",
    ["Home", "Career Guidance", "Resume Tips", "Interview Prep", "Coding Questions"]
)

st.title("🎓 AI Career Guidance Chatbot")

# ---------------- HOME ----------------
if menu == "Home":
    st.subheader("Welcome to Your AI Career Guidance Assistant 🚀")

    st.write("""
    This chatbot helps students and beginners explore career paths, build skills, and prepare for interviews.

    You can discover career options like Java, Python, AI/ML, and more.

    It also helps you improve your resume and practice coding questions step by step.

    Use the sidebar to start your learning journey.
    """)

# ---------------- CAREER GUIDANCE ----------------
elif menu == "Career Guidance":

    name = st.text_input("Enter Your Name")

    career = st.selectbox(
        "Choose Career",
        [
            "Select Career",
            "Java Developer",
            "Python Developer",
            "Data Analyst",
            "AI/ML Engineer",
            "Web Developer"
        ]
    )

    if st.button("Get Guidance"):

        if career == "Java Developer":
            st.success(f"Hello {name} 👋")

            st.subheader("📚 Skills")
            st.write("Core Java, OOP, Collections, JDBC, SQL, Spring Boot")

            st.subheader("🛣️ Roadmap")
            st.write("""
            Beginner → Java Basics  
            Intermediate → OOP + Collections + SQL  
            Advanced → Spring Boot + Projects + Deployment  
            """)

            st.subheader("💼 Projects")
            st.write("""
            Student Management System  
            Banking System  
            Employee Management System  
            """)

            st.subheader("🎯 Interview Questions")
            st.write("""
            What is JVM?  
            What is OOP?  
            Difference between ArrayList and LinkedList?  
            """)

        elif career == "AI/ML Engineer":
            st.success(f"Hello {name} 👋")

            st.subheader("📚 Skills")
            st.write("Python, Machine Learning, Deep Learning, NLP, Data Science")

            st.subheader("💼 Projects")
            st.write("""
            Chatbot  
            Fake News Detection  
            Recommendation System  
            """)

            st.subheader("🛣️ Roadmap")
            st.write("""
            Python → Statistics → ML Algorithms → Deep Learning → Projects → Deployment  
            """)

# ---------------- RESUME TIPS ----------------
elif menu == "Resume Tips":

    st.subheader("📄 Resume Tips")

    st.write("""
    - Keep resume clean and simple (1 page for freshers)
    - Highlight technical skills clearly
    - Add real projects with GitHub links
    - Mention internships or certifications
    - Use strong action words (Built, Designed, Developed)
    - Add LinkedIn profile
    - Avoid grammar mistakes
    """)

    st.success("A strong project section can improve interview chances 🚀")

# ---------------- INTERVIEW PREP ----------------
elif menu == "Interview Prep":

    st.subheader("🎯 Interview Preparation")

    st.write("""
    Technical:
    - Data Structures
    - OOP Concepts
    - SQL Queries
    - Programming basics

    HR:
    - Tell me about yourself
    - Strengths and weaknesses
    - Why this company?
    - Career goals

    Tips:
    - Practice mock interviews
    - Improve communication
    - Stay confident
    """)

    st.info("Consistency is the key to success 🔥")

# ---------------- CODING QUESTIONS ----------------
elif menu == "Coding Questions":

    st.subheader("💻 Basic Coding Questions")

    st.code("""
1. Reverse a string
2. Check palindrome number
3. Find largest element in array
4. Fibonacci series
5. Factorial of a number
6. Check prime number
7. Swap two numbers
8. Count vowels in string
    """)

    st.success("Practice daily to improve logic 💡")