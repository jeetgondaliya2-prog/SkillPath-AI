import streamlit as st
import requests
import os


# ----------------------------- 
# Configuration
# -----------------------------

BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://backend:8000"
)
API_URL = f"{BACKEND_URL}/api/analyze"

RESUME_API_URL = f"{BACKEND_URL}/api/resume/analyze"

LEARNING_API_URL = f"{BACKEND_URL}/api/learning/recommend"


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="SkillPath AI",
    page_icon="🎯",
    layout="wide"
)


# -----------------------------
# Custom CSS
# -----------------------------

st.markdown(
    """
    <style>

    .main-title {
        font-size: 45px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .score-box {
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        border: 1px solid #ddd;
    }

    .score {
        font-size: 45px;
        font-weight: bold;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Header
# -----------------------------

st.markdown(
    '<div class="main-title">🎯 SkillPath AI</div>',
    unsafe_allow_html=True
)

st.markdown(    '<div class="subtitle">AI-powered career roadmap and skill gap analyzer</div>',
    unsafe_allow_html=True
)


# -----------------------------
# Student Information
# -----------------------------

st.header("👤 Student Profile")

col1, col2 = st.columns(2)

with col1:

    name = st.text_input(
        "Your Name",
        placeholder="Enter your name"
    )

    education = st.text_input(
        "Education",
        placeholder="e.g. B.Tech ECE"
    )

with col2:

    experience = st.selectbox(
        "Experience",
        [
            "Fresher",
            "Intern",
            "0-1 Years",
            "1-2 Years",
            "2+ Years"
        ]
    )

    target_role = st.selectbox(
        "Target Career",
        [
            "Software Developer",
            "Data Analyst",
            "ML Engineer",
            "GenAI Engineer"
        ]
    )


# -----------------------------
# Skills
# -----------------------------

st.header("🧠 Your Current Skills")

skills_input = st.text_area(
    "Enter your skills separated by commas",
    placeholder="C++, Python, DSA, SQL, Git, FastAPI",
    height=100
)


# Convert input into list

skills = [
    skill.strip()
    for skill in skills_input.split(",")
    if skill.strip()
]


# -----------------------------
# Projects
# -----------------------------

st.header("🚀 Your Projects")

projects_input = st.text_area(
    "Enter your projects separated by commas",
    placeholder="ElectroMind AI, Insurance Premium Predictor",
    height=100
)

projects = [
    project.strip()
    for project in projects_input.split(",")
    if project.strip()
]


# -----------------------------
# Analyze Button
# -----------------------------

st.divider()

analyze_button = st.button(
    "🚀 Analyze My Career",
    use_container_width=True
)


# -----------------------------
# API Request
# -----------------------------

if analyze_button:

    if not name:
        st.warning("Please enter your name.")

    elif not education:
        st.warning("Please enter your education.")

    elif not skills:
        st.warning("Please enter at least one skill.")

    else:

        payload = {
            "name": name,
            "target_role": target_role,
            "skills": skills,
            "education": education,
            "projects": projects,
            "experience": experience
        }

        try:

            with st.spinner("🤖 SkillPath AI is analyzing your profile..."):

                response = requests.post(
                    API_URL,
                    json=payload,
                    timeout=120
                )

            if response.status_code == 200:

                data = response.json()

                analysis = data["analysis"]
                st.session_state["analysis"] = analysis

                roadmap = data.get(
                    "roadmap",
                    "Roadmap could not be generated."
                )

                st.success("Analysis completed successfully! 🎉")

                # -----------------------------
                # Readiness Score
                # -----------------------------

                st.header("📊 Your Career Readiness")

                score = analysis["readiness_score"]

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.metric(
                        "Target Role",
                        analysis["target_role"]
                    )

                with col2:

                    st.metric(
                        "Readiness Score",
                        f"{score}%"
                    )

                with col3:

                    st.metric(
                        "Missing Skills",
                        len(analysis["missing_skills"])
                    )

                # -----------------------------
                # Matched Skills
                # -----------------------------

                st.header("✅ Skills You Already Have")

                if analysis["matched_skills"]:

                    for skill in analysis["matched_skills"]:

                        st.success(
                            f"✓ {skill}"
                        )

                else:

                    st.info(
                        "No matching skills found yet."
                    )

                # -----------------------------
                # Missing Skills
                # -----------------------------

                st.header("❌ Skills You Need")

                if analysis["missing_skills"]:

                    for skill in analysis["missing_skills"]:

                        st.error(
                            f"• {skill}"
                        )

                else:

                    st.success(
                        "Amazing! You have all the required skills."
                    )

                # -----------------------------
                # AI Roadmap
                # -----------------------------

                st.header("🗺️ Your Personalized AI Roadmap")

                st.markdown(roadmap)

            else:

                st.error(
                    f"Backend error: {response.status_code}"
                )

                st.code(response.text)

        except requests.exceptions.ConnectionError:

            st.error(
                "❌ Cannot connect to FastAPI backend."
            )

            st.info(
                "Make sure your FastAPI server is running."
            )

        except requests.exceptions.Timeout:

            st.error(
                "⏳ Request timed out. Mistral may be taking too long."
            )

        except Exception as e:

            st.error(
                f"Something went wrong: {str(e)}"
            )
# =========================================================
# RESUME ANALYZER
# =========================================================

st.divider()

st.header("📄 Resume Analyzer")

st.write(
    "Upload your resume and SkillPath AI will automatically "
    "identify your skills and find your career gaps."
)

resume_file = st.file_uploader(
    "Upload your Resume",
    type=["pdf"],
    key="resume_upload"
)

resume_role = st.selectbox(
    "Select Target Career",
    [
        "Software Developer",
        "Data Analyst",
        "ML Engineer",
        "GenAI Engineer"
    ],
    key="resume_role"
)

if st.button(
    "📊 Analyze My Resume",
    use_container_width=True
):

    if resume_file is None:

        st.warning("Please upload your resume.")

    else:

        try:

            with st.spinner(
                "🤖 Analyzing your resume..."
            ):

                files = {
                    "file": (
                        resume_file.name,
                        resume_file,
                        "application/pdf"
                    )
                }

                payload = {
                    "target_role": resume_role
                }

                response = requests.post(
                    RESUME_API_URL,
                    files=files,
                    data=payload,
                    timeout=180
                )

            if response.status_code == 200:

                result = response.json()

                if "error" in result:

                    st.error(result["error"])

                else:

                    st.success(
                        "Resume analysis completed! 🎉"
                    )

                    # =====================================
                    # RESUME SKILLS
                    # =====================================

                    st.subheader(
                        "🧠 Skills Found in Your Resume"
                    )

                    skills = result.get(
                        "resume_skills",
                        []
                    )

                    if skills:

                        st.write(
                            " • ".join(skills)
                        )

                    else:

                        st.info(
                            "No technical skills were detected."
                        )

                    # =====================================
                    # CAREER READINESS
                    # =====================================

                    analysis = result["analysis"]

                    st.subheader(
                        "📊 Career Readiness"
                    )

                    col1, col2, col3 = st.columns(3)

                    with col1:

                        st.metric(
                            "Target Role",
                            analysis["target_role"]
                        )

                    with col2:

                        st.metric(
                            "Readiness",
                            f'{analysis["readiness_score"]}%'
                        )

                    with col3:

                        st.metric(
                            "Skill Gaps",
                            len(
                                analysis["missing_skills"]
                            )
                        )

                    # =====================================
                    # MATCHED SKILLS
                    # =====================================

                    st.subheader(
                        "✅ Skills You Already Have"
                    )

                    matched_skills = analysis.get(
                        "matched_skills",
                        []
                    )

                    if matched_skills:

                        for skill in matched_skills:

                            st.success(
                                f"✓ {skill}"
                            )

                    else:

                        st.info(
                            "No matching skills found."
                        )

                    # =====================================
                    # MISSING SKILLS
                    # =====================================

                    st.subheader(
                        "❌ Skills You Need"
                    )

                    missing_skills = analysis.get(
                        "missing_skills",
                        []
                    )

                    if missing_skills:

                        for skill in missing_skills:

                            st.error(
                                f"• {skill}"
                            )

                    else:

                        st.success(
                            "You have all required skills! 🎉"
                        )

                    # =====================================
                    # AI ROADMAP
                    # =====================================

                    st.subheader(
                        "🗺️ Personalized AI Roadmap"
                    )

                    st.markdown(
                        result.get(
                            "roadmap",
                            "Roadmap could not be generated."
                        )
                    )

            else:

                st.error(
                    f"Backend error: "
                    f"{response.status_code}"
                )

                st.code(
                    response.text
                )

        except requests.exceptions.ConnectionError:

            st.error(
                "❌ Cannot connect to FastAPI backend."
            )

            st.info(
                "Make sure FastAPI is running."
            )

        except requests.exceptions.Timeout:

            st.error(
                "⏳ Request timed out."
            )

        except Exception as e:

            st.error(
                f"Something went wrong: {str(e)}"
            )
# =========================================================
# CAREER RECOMMENDATION
# =========================================================

st.divider()

st.header("🎯 Career Recommendation")

st.write(
    "Find the career paths that best match your current skills."
)

career_skills_input = st.text_area(
    "Enter your skills",
    placeholder="Python, C++, DSA, SQL, FastAPI, GenAI",
    height=100,
    key="career_skills"
)

career_skills = [
    skill.strip()
    for skill in career_skills_input.split(",")
    if skill.strip()
]

if st.button(
    "🎯 Find My Best Career",
    use_container_width=True
):

    if not career_skills:

        st.warning(
            "Please enter at least one skill."
        )

    else:

        payload = {
            "skills": career_skills
        }

        try:

            with st.spinner(
                "🤖 Finding the best career paths for you..."
            ):

                response = requests.post(
                    "http://127.0.0.1:8000/api/career/recommend",
                    json=payload,
                    timeout=60
                )

            if response.status_code == 200:

                result = response.json()

                recommendations = result[
                    "recommendations"
                ]

                st.success(
                    "Career recommendations generated! 🎉"
                )

                st.subheader(
                    "🏆 Your Recommended Careers"
                )

                for index, career in enumerate(
                    recommendations
                ):

                    st.markdown(
                        f"### {index + 1}. {career['role']}"
                    )

                    st.metric(
                        "Career Match",
                        f"{career['match_percentage']}%"
                    )

                    col1, col2 = st.columns(2)

                    with col1:

                        st.write(
                            "### ✅ Skills You Have"
                        )

                        if career[
                            "matched_skills"
                        ]:

                            for skill in career[
                                "matched_skills"
                            ]:

                                st.success(
                                    f"✓ {skill}"
                                )

                        else:

                            st.info(
                                "No matching skills."
                            )

                    with col2:

                        st.write(
                            "### ❌ Skills To Learn"
                        )

                        if career[
                            "missing_skills"
                        ]:

                            for skill in career[
                                "missing_skills"
                            ]:

                                st.error(
                                    f"• {skill}"
                                )

                        else:

                            st.success(
                                "No major skill gaps!"
                            )

                    st.divider()

            else:

                st.error(
                    f"Backend error: "
                    f"{response.status_code}"
                )

                st.code(
                    response.text
                )

        except requests.exceptions.ConnectionError:

            st.error(
                "❌ Cannot connect to FastAPI."
            )

        except requests.exceptions.Timeout:

            st.error(
                "⏳ Request timed out."
            )

        except Exception as e:

            st.error(
                f"Something went wrong: {str(e)}"
            )
# =========================================================
# PERSONALIZED AI ROADMAP
# =========================================================

st.divider()

st.header("🗺️ Personalized AI Learning Roadmap")

st.write(
    "Generate a personalized learning plan based on your "
    "target career and current skill gaps."
)

roadmap_role = st.selectbox(
    "Select Target Career",
    [
        "Software Developer",
        "Data Analyst",
        "ML Engineer",
        "GenAI Engineer"
    ],
    key="roadmap_role"
)

roadmap_current_skills = st.text_area(
    "Your Current Skills",
    placeholder="Python, C++, DSA, SQL, FastAPI",
    height=100,
    key="roadmap_current_skills"
)

roadmap_missing_skills = st.text_area(
    "Skills You Need to Learn",
    placeholder="OOP, DBMS, Operating Systems, Git",
    height=100,
    key="roadmap_missing_skills"
)


current_skills = [
    skill.strip()
    for skill in roadmap_current_skills.split(",")
    if skill.strip()
]

missing_skills = [
    skill.strip()
    for skill in roadmap_missing_skills.split(",")
    if skill.strip()
]


if st.button(
    "🗺️ Generate My Roadmap",
    use_container_width=True
):

    if not current_skills:

        st.warning(
            "Please enter your current skills."
        )

    elif not missing_skills:

        st.warning(
            "Please enter your missing skills."
        )

    else:

        payload = {
            "target_role": roadmap_role,
            "user_skills": current_skills,
            "missing_skills": missing_skills
        }

        try:

            with st.spinner(
                "🤖 Mistral AI is creating your roadmap..."
            ):

                response = requests.post(
                    "http://127.0.0.1:8000/api/roadmap/generate",
                    json=payload,
                    timeout=180
                )

            if response.status_code == 200:

                result = response.json()

                st.success(
                    "Your personalized roadmap is ready! 🎉"
                )

                st.subheader(
                    f"🚀 Roadmap for {result['target_role']}"
                )

                st.markdown(
                    result["roadmap"]
                )

            else:

                st.error(
                    f"Backend error: "
                    f"{response.status_code}"
                )

                st.code(
                    response.text
                )

        except requests.exceptions.ConnectionError:

            st.error(
                "❌ Cannot connect to FastAPI backend."
            )

            st.info(
                "Make sure your FastAPI server is running."
            )

        except requests.exceptions.Timeout:

            st.error(
                "⏳ Request timed out."
            )

        except Exception as e:

            st.error(
                f"Something went wrong: {str(e)}"
            )
# =========================================================
# LEARNING RESOURCES
# =========================================================

st.divider()

st.header("📚 Learning Resources")

st.write(
    "Get personalized resources for the skills you need to learn."
)

# Get previous career analysis
analysis = st.session_state.get("analysis")

if analysis is None:

    st.info(
        "First click 'Analyze My Career' above."
    )

else:

    missing_skills = analysis.get(
        "missing_skills",
        []
    )

    if not missing_skills:

        st.success(
            "🎉 You don't have any missing skills!"
        )

    else:

        st.write("### Skills you should learn:")

        for skill in missing_skills:

            st.write(f"• {skill}")

        if st.button(
            "📚 Get Learning Resources",
            use_container_width=True
        ):

            learning_payload = {
                "missing_skills": missing_skills,
                "target_role": analysis.get(
                    "target_role",
                    "Software Developer"
                )
            }

            try:

                with st.spinner(
                    "🤖 Finding the best learning resources..."
                ):

                    response = requests.post(
                        LEARNING_API_URL,
                        json=learning_payload,
                        timeout=180
                    )

                if response.status_code == 200:

                    result = response.json()

                    st.success(
                        "Learning resources generated! 🎉"
                    )

                    resources = result.get(
                        "resources",
                        result
                    )

                    st.write(resources)

                else:

                    st.error(
                        f"Backend error: {response.status_code}"
                    )

                    st.code(
                        response.text
                    )

            except requests.exceptions.ConnectionError:

                st.error(
                    "❌ Cannot connect to FastAPI backend."
                )

            except requests.exceptions.Timeout:

                st.error(
                    "⏳ Request timed out."
                )

            except Exception as e:

                st.error(
                    f"Something went wrong: {str(e)}"
                )
