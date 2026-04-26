import streamlit as st
from streamlit_option_menu import option_menu
import os

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Saurabh Rai | AI Engineer",
    page_icon="🤖",
    layout="wide"
)

# ------------------ LOAD CSS ------------------
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("styles.css")


# ------------------ SIDEBAR ------------------
with st.sidebar:
    selected = option_menu(
        "Saurabh Rai",
        ["Home", "Projects", "Skills", "Experience", "Contact"],
        icons=["house", "cpu", "gear", "briefcase", "envelope"],
        default_index=0
    )


# ------------------ PROJECT COMPONENT ------------------
def project_section(title, desc, link, tags, image=None, architecture=None, caption=None):
    
    with st.container():

        tag_html = "".join([f'<span class="tag">{t}</span>' for t in tags])

        st.markdown(f"""
        <div class="card">
            <h3 style="color:#ffffff;">{title}</h3>
            <p>{desc}</p>
            {tag_html}
        </div>
        """, unsafe_allow_html=True)

        # ✅ FIXED IMAGE (no warning)
        if image and os.path.exists(image):
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.image(image, width="stretch")

        st.info("⚠️ App may take **20–30 seconds to wake up** if inactive (Streamlit free tier).")

        st.markdown("""
👉 Click below to open the app.  
If it’s sleeping, click **“Yes, get this app back up!”** and wait a few seconds.
""")

        st.link_button("🚀 Open App", link)

        # ✅ FIXED ARCHITECTURE IMAGE
        if architecture and os.path.exists(architecture):
            with st.expander("⚙️ View Architecture"):
                col1, col2, col3 = st.columns([1, 5, 1])
                with col2:
                    st.image(architecture, width="stretch")
                if caption:
                    st.caption(caption)

        st.markdown("---")


# ------------------ HOME ------------------
if selected == "Home":

    col1, col2, col3 = st.columns([1, 4, 1])

    with col2:
        st.title("🤖 AI Engineer | GenAI + ML Systems")

        st.markdown("""
I build intelligent systems combining **Machine Learning (prediction)** and  
**Generative AI (reasoning)**.

---

### 🔥 What I specialize in:
- RAG-based AI applications  
- Agentic AI systems  
- ML models for prediction & segmentation  
- End-to-end AI solutions on cloud  

---

### 🧠 How I build AI systems:
- **ML →** embeddings, prediction, ranking  
- **GenAI →** reasoning, generation, decision making  

This hybrid approach enables scalable, production-ready AI systems.
""")


# ------------------ PROJECTS ------------------
elif selected == "Projects":

    col1, col2, col3 = st.columns([1, 4, 1])

    with col2:
        st.header("🚀 Projects")

        st.subheader("🤖 GenAI Systems")

        project_section(
            "Medical Assistance App",
            "RAG-based chatbot providing context-aware medical responses using LLM + vector database.",
            "https://medical-assistance-app-srgenaiprojects.streamlit.app",
            ["RAG", "LLM", "LangChain", "Vector DB"],
            image="assets/medical_assistance_app.png",
            architecture="assets/rag_architecture.png",
            caption="User query → embedding → similarity search → top-k chunks → LLM generates grounded response"
        )

        project_section(
            "Stratamind Deep Research",
            "Agentic AI system for multi-step research automation and intelligent reasoning workflows.",
            "https://stratamind-deep-research-srgenaiprojects.streamlit.app",
            ["Agents", "LLM", "Automation"],
            image="assets/stratamind_app.png"
        )

        st.subheader("📊 Machine Learning Systems")

        project_section(
            "BookVerse",
            "Recommendation system for personalized book suggestions using ML techniques.",
            "https://bookverseapp-srmlprojects.streamlit.app",
            ["Recommendation", "ML"],
            image="assets/bookverse_app.png"
        )

        project_section(
            "AutoValue Insight",
            "Regression-based ML model for predicting car prices with data-driven insights.",
            "https://autovalue-insight-srmlprojects.streamlit.app",
            ["Regression", "ML"],
            image="assets/autovalue_insight_app.png"
        )

        project_section(
            "HealthCalc Pro",
            "Health analytics tool leveraging predictive ML models for risk estimation.",
            "https://healthcalc-pro-srmlprojects.streamlit.app/",
            ["Prediction", "Healthcare ML"],
            image="assets/healthcalc_pro_app.png"
        )

        project_section(
            "Client Categorizer",
            "Customer segmentation using clustering techniques for business insights.",
            "https://clientcatergorizergit-saurabhraimlprojects.streamlit.app/",
            ["Clustering", "K-Means"],
            image="assets/client_categorizer_app.png"
        )


# ------------------ SKILLS ------------------
elif selected == "Skills":

    col1, col2, col3 = st.columns([1, 4, 1])

    with col2:
        st.header("⚙️ Skills")

        st.markdown("""
### 🤖 Generative AI
- Vertex AI  
- LangChain  
- RAG (Retrieval Augmented Generation)  
- Agentic AI  

### 📊 Machine Learning
- Regression  
- Clustering (K-Means)  
- Recommendation Systems  

### 🛠 Backend & Tools
- Python  
- FastAPI  
- Streamlit  

### ☁️ Cloud
- GCP  
- Azure  
""")


# ------------------ EXPERIENCE ------------------
elif selected == "Experience":

    col1, col2, col3 = st.columns([1, 4, 1])

    with col2:
        st.header("💼 Experience")

        st.markdown("""
### AI Cloud Presales Engineer

- Designed and demonstrated GenAI and ML solutions  
- Built real-world AI applications using Vertex AI, LangChain  
- Worked on enterprise use cases and solution architecture  
- Delivered end-to-end AI workflows for clients  
""")


# ------------------ CONTACT ------------------
elif selected == "Contact":

    col1, col2, col3 = st.columns([1, 4, 1])

    with col2:
        st.header("📬 Contact")

        st.markdown("""
- 📧 Email: saurabhrai473@gmail.com  
- 💼 LinkedIn: https://linkedin.com  
- 💻 GitHub: https://github.com/SaurabhRai19  
""")