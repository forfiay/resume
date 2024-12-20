import streamlit as st
from pathlib import Path

from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
profile_pic = current_dir / "assets" / "pp.png"

PAGE_TITLE = "Digital Resume | Nesha"
PAGE_ICON = ":wave:"
NAME = "Nesha Nestiana Putri"
DESCRIPTION = """
> 5 years of experience in Financial Industry, have a good experience in Data Analytics and Risk Management
"""
LOCATION = "Jakarta"
PHONE = "+62 8579 3110 323"
EMAIL = "neshaanes@email.com"
WEBSITE = "https://id.linkedin.com/in/neshanestiana"


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.markdown("""
<style>
body {
    background-color: #CFB095;
}
</style>
""", unsafe_allow_html=True)

profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write("📍", LOCATION)
    st.write("📞", PHONE)
    st.write("📧", EMAIL)
    st.write("🔗", WEBSITE)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work Experience")

# --- JOB 1
st.write("🏛", "**Integrated Risk Management | Bank Muamalat Indonesia**")
st.write("Jun 2022 - Jan 2024")
st.write(
    """
- Job position named **Risk Methodology & Analytics - Manager**, in charge of **managing Credit and Operational Risks including regulatory reports**
- Responsible for internal and external/regulatory reporting related to operational and credit risks
- Managing bankwide data related to operational risk for Risk Profile in Risk-Based Bank Rating
- Developing operational risk framework, methodologies, and tools. Managed to update the new Key Risk Indicator for Operational Risk in 2023
- Monitoring operational risk losses and risk events in Loss Event Databases
- Designing operational risk awareness (risk culture) in the company
- Secretary of Risk Management Committee (RMC), organizing RMC event and ensuring the RMC’s recommendation to be followed up by the risk taking unit
- Monitoring credit risk exposure. Data analytics using both MS Excel & Python
"""
)

# --- JOB 2
st.write('\n')
st.write("🏛", "**Distribution Network & Management | Bank Muamalat Indonesia**")
st.write("Jun 2020 - May 2022")
st.write(
    """
- Job position named **Sales Culture Optimization Specialist** with main role namely, **managing sales-people performance and designing business strategy**
- Providing sales team performance data, monitoring sales activity & productivity, initiating internal program and designing marketing strategy to boost sales, in collaboration with Human Resource Division to design learning & development program, designing reward & recognition program, and forming sales culture for sales people in branches
- Retail banking segment succesfully achieved Funding & Financing target in half year 2022
"""
)

# --- JOB 3
st.write('\n')
st.write("🏛", "**Consumer Liabilities Product Division | Bank Muamalat Indonesia**")
st.write("Dec 2019 - Jun 2020")
st.write(
    """
- Completing project 'Time Deposit (TD) product's system and process enhancement' in Consumer Liabilities Product Division for 7 months as a part of Management Trainee program
- Sucessfully **accomplished process improvement** for TD product, in result less people and time to be involved in the process
- Sucessfully **managing system enhancement** related to TD product for regulatory purpose
"""
)

# --- JOB 4
st.write('\n')
st.write("🏛", "**Compliance Division | Bank Muamalat Indonesia**")
st.write("Jun 2019 - Dec 2019")
st.write(
    """
- Completing project 'Compliance Assurance' in Compliance Division for 7 months as a part of Management Trainee program
- Succesfully **accomplished process improvement** for Anti Money Laundry and Prevention Terrorism Financing (AML-PTF) regulatory reporting process
- Succesfully **creating tools** for bank's prudential ratio assurance (regulatory purpose)
"""
)

# --- JOB 5
st.write('\n')
st.write("🏛", "**Management Trainee (MODP Future Leader Batch 3) | Bank Muamalat Indonesia**")
st.write("Apr 2018 - Jun 2019")
st.write(
    """
- In-class training of basic sharia banking for 4 months
- On the job training in business, risk, and operation functions (both corporate and retail segment) for 10 months

"""
)

# --- AREAS OF EXPERTISE ---
st.write('\n')
st.subheader("Areas of Expertise")
st.write("📊 Good understanding on data analytics using MS Excel, Python, and SQL (for manipulating data only)")
st.write("📚 Good experience in Enterprise Risk Management (Credit, Liquidity, Market) and Operational Risk Management, especially Credit and Operational Risks Reporting & Data Analysis")
st.write("👩‍💻 Good experience in managing project related to Process Improvement")

# --- CERTIFICATION & TRAINING ---
st.write('\n')
st.subheader("Certification & Training")
st.write("✔️ Fullstack Data Science / Sanbercode, 2024 (on going)")
st.write("✔️ Intermediate to Advance - Excel Data Analysis and Interactive Dashboard / Muamalat Institute, 2022")
st.write("✔️ Risk Management Level 2 / LSP Keuangan Syariah, 2022")
st.write("✔️ Risk Management Level 1 / LSP Keuangan Syariah, 2020")
st.write("✔️ General Banking / Badan Nasional Sertifikasi Profesi, 2018")

# --- EDUCATION ---
st.write('\n')
st.subheader("Education")
st.write("🏫", "**Bachelor of Civil Engineering | Institut Teknologi Bandung**")
st.write("2013 - 2017")
st.write("Graduated Cumlaude with concentration on Construction Management (GPA 3.50 out of 4.00)")