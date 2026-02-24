import streamlit as st
import pandas as pd
from datetime import date as Date
from fpdf import FPDF

# Page configuration
st.set_page_config(
    page_title="Pharmacovigilance Hub",
    page_icon="💊",
    layout="wide"
)
st.markdown("""
<style>

body {
    overflow-x: hidden;
}

/* floating pill style */
.pill {
    position: fixed;
    font-size: 40px;
    animation: float 12s linear infinite;
    opacity: 0.25;
}

/* different positions */
.pill1 { left: 5%; animation-duration: 14s; }
.pill2 { left: 20%; animation-duration: 18s; }
.pill3 { left: 40%; animation-duration: 16s; }
.pill4 { left: 60%; animation-duration: 20s; }
.pill5 { left: 80%; animation-duration: 15s; }

/* movement */
@keyframes float {
    0% { top: 110%; transform: rotate(0deg); }
    100% { top: -10%; transform: rotate(360deg); }
}

</style>

<div class="pill pill1">💊</div>
<div class="pill pill2">💊</div>
<div class="pill pill3">💊</div>
<div class="pill pill4">💊</div>
<div class="pill pill5">💊</div>

""", unsafe_allow_html=True)

# Title
st.title("💊 Pharmacovigilance - Drug Safety Data Management")

st.markdown("""
Welcome to the **Pharmacovigilance Review Portal**.

This app helps with understanding of safety data management in the pharmaceutical industry, aligned with global regulatory guidelines.
""")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    [
        "Home",
        "ICSR Processing",
        "Literature Review",
        "Aggregate Reports Preparation",
        "Signal Management",
        "Risk Management",
        "Quality Assurance (PV QA)",
        "Regulatory Reporting / Submissions",
        "Safety Database Management",
        "Real-World Evidence (RWE) Safety",
        "Automation / PV Technology",
    ],
)

# ---------------- HOME ----------------
if page == "Home":
    st.info("This application demonstrates core pharmacovigilance functional areas aligned with global regulatory guidelines.")

    st.subheader("Major PV Domains")
    st.write("• Individual Case Safety Report (ICSR) Management")
    st.write("• Literature Monitoring")
    st.write("• Signal Detection and Evaluation")
    st.write("• Periodic Safety Reports")
    st.write("• Risk Management Plans")
    st.write("• PV Quality Systems")
    st.write("• Regulatory Submissions")

    st.subheader("Global Guidelines")
    st.write("Good Pharmacovigilance Practices (GVP)")
    st.write("ICH Guidelines (E2A, E2B, E2C, E2D, E2E)")
    st.write("CIOMS Recommendations")

# ---------------- ICSR PROCESSING ----------------
elif page == "ICSR Processing":
    url = "https://www.ema.europa.eu/en/documents/regulatory-procedural-guideline/guideline-good-pharmacovigilance-practices-gvp-module-vi-collection-management-submission-reports-suspected-adverse-reactions-medicinal-products-rev-2_en.pdf"
    st.markdown(f"[📄 Guideline GVP Module VI (PDF)]({url})")

    st.info("📊 ICSR management is a fundamental activity of pharmacovigilance

✨ICSR ( identifiable reporter, an identifiable patient, a suspect product, and an adverse event. Without all four, it’s a "non-valid" case.)
📋Steps:
Case intake
Triage
Duplicate check
Data entry
Quality review 
Medical review
Quality control
Regulatory submission

Validated safety systems help capture, manage, and evaluate safety cases in alignment with Good Pharmacovigilance Practices (GVP) from the European Medicines Agency.

Common pharmacovigilance platforms include:

• Oracle Argus Safety
• ARISg
• Veeva Vault Safety
• LifeSphere MultiVigilance
• Clinevo Safety etc...

These systems support structured workflows such as case intake, triage, data entry, medical review, quality control, and regulatory reporting.

📈 Where Safety Information Comes From

1️⃣ Clinical Development

During clinical trials, safety is monitored closely according to guidelines from the International Council for Harmonisation.

• SAE (Serious Adverse Event)
Events that result in death, hospitalization, disability, life-threatening situations, or other medically important conditions.

• SUSAR (Suspected Unexpected Serious Adverse Reaction)
Serious reactions that are unexpected based on the Investigator’s Brochure or product information.

These findings contribute to annual submissions such as the Development Safety Update Report (DSUR).

2️⃣ Post-Marketing Surveillance
Once medicines reach the market, safety monitoring expands to real-world sources.

✨Solicited sources (organized programs)

• Patient Support Programs
• Disease registries
• Post-Authorization Safety Studies (PASS)
• Non-interventional studies
• Compassionate use programs
• Named patient programs

✨Unsolicited sources (spontaneous reporting)

• Healthcare professional reports
• Consumer or patient reports
• Medical information contacts
• Health authority communications
• Scientific and medical literature
• Social media monitoring")

    st.title("ICSR Processing Model Dashboard")

    tabs = st.tabs([
        "General", "Reporter", "Patient", "Parent Case", "Adverse Event",
        "Suspected Drug", "Causality", "Analysis", "Reporting"
    ])

    # General Tab
    with tabs[0]:
        st.header("General Case Information")
        case_received_date = st.date_input("Case Received Date", Date.today())
        report_type = st.selectbox("Report Type", ["Spontaneous", "Clinical Trial", "Literature", "Other"])
        country = st.text_input("Country")
        seriousness = st.selectbox("Seriousness", ["Non Serious", "Serious"])
        seriousness_detail = st.selectbox(
            "Seriousness Criteria",
            ["Death", "Life Threatening", "Inpatient Hospitalization", "Disability", "Congenital Anomaly", "Medically Significant"]
        ) if seriousness == "Serious" else "Non Serious"

    # Reporter Tab
    with tabs[1]:
        st.header("Reporter Information")
        reporter_name = st.text_input("Reporter Name")
        reporter_email = st.text_input("Reporter Email")
        reporter_contact = st.text_input("Reporter Contact Number")
        reporter_qualification = st.text_input("Reporter Qualification")

    # Patient Tab
    with tabs[2]:
        st.header("Patient Information")
        patient_age = st.number_input("Patient Age", 0, 120)
        gender = st.selectbox("Gender", ["Male", "Female", "Other", "Unknown"])
        weight = st.number_input("Weight (kg)", 0.0, 300.0, 0.0)
        height = st.number_input("Height (cm)", 0.0, 250.0, 0.0)
        medical_history = st.text_area("Relevant Medical History")

    # Parent Case Tab
    with tabs[3]:
        st.header("Parent Case Information")
        parent_case_id = st.text_input("Parent Case ID")
        parent_case_status = st.selectbox("Parent Case Status", ["Open", "Closed", "Ongoing"])
        related_cases = st.text_area("Related Cases")

    # Adverse Event Tab
    with tabs[4]:
        st.header("Adverse Event Information")
        ae_verbatim = st.text_area("Adverse Event - Verbatim")
        ae_meddra = st.text_area("Adverse Event - MedDRA Code")
        ae_outcome = st.selectbox("Outcome", ["Recovered", "Recovering", "Not Recovered", "Fatal", "Unknown"])

    # Suspected Drug Tab
    with tabs[5]:
        st.header("Suspected Drug Information")
        suspected_drug = st.text_input("Drug Name")
        dose = st.text_input("Dose")
        route = st.selectbox("Route of Administration", ["Oral", "IV", "IM", "Subcutaneous", "Other"])
        start_date = st.date_input("Start Date")
        end_date = st.date_input("End Date")
        indication = st.text_area("Indication / Reason for Use")

    # Causality Tab
    with tabs[6]:
        st.header("Causality Assessment")
        causality_method = st.selectbox("Causality Assessment Method", ["WHO-UMC", "Naranjo", "Other"])
        causality_result = st.selectbox("Assessment Result", ["Certain", "Probable", "Possible", "Unlikely", "Conditional", "Unassessable"])
        reporter_comments = st.text_area("Reporter Comments")

    # Analysis Tab
    with tabs[7]:
        st.header("Narrative and Analysis")
        case_summary = st.text_area("Case Summary")

    # Reporting Tab
    with tabs[8]:
        st.header("Submit Case")
        if st.button("Generate PDF"):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", 'B', 16)
            pdf.cell(0, 10, "ICSR Case Report", ln=True, align='C')
            pdf.ln(5)

            # Add sections here... (your existing multi_cell PDF generation code)

            pdf_file = "ICSR_CDSCO_Report.pdf"
            pdf.output(pdf_file)

            with open(pdf_file, "rb") as f:
                st.download_button("Download PDF", f, file_name=pdf_file, mime="application/pdf")
            st.success("PDF generated successfully!")

# ---------------- Other Pages ----------------
elif page == "Literature Review":
    st.header("Literature Monitoring")
    st.info("The medical literature is a significant source of information for the monitoring of the safety profile and of the risk-benefit balance of medicinal products, particularly in relation to the detection of new safety signals or emerging safety issues. Marketing authorisation holders are therefore expected to maintain awareness of possible publications through a systematic literature review of widely used reference databases (e.g. Medline, Excerpta Medica or Embase) no less frequently than once a week."
            "Reports of suspected adverse reactions from the medical literature, including relevant published abstracts from meetings and draft manuscripts, should be reviewed and assessed by marketing authorisation holders to identify and record ICSRs."
            "If multiple medicinal products are mentioned in the publication, only those which are identified by the publication's author(s) as having at least a possible causal relationship with the suspected adverse reaction should be considered for literature review by the concerned marketing authorisation holder(s).")

    article = st.text_input("Article Title")
    journal = st.text_input("Journal")
    drug = st.text_input("Drug")
    reaction = st.text_input("Adverse Reaction")
    if st.button("Screen Article"):
        st.warning("Potential safety information identified. Further assessment required.")

elif page == "Aggregate Reports Preparation":
    st.header("Aggregate Safety Reports")
    data = {"Report Type": ["PSUR", "PBRER", "DSUR"], "Frequency": ["Periodic", "Periodic", "Annual"]}
    st.table(pd.DataFrame(data))

elif page == "Signal Management":
    st.header("Signal Detection and Management")
    data = {"Drug": ["Drug A", "Drug B", "Drug C"], "Signal Score": [3.2, 5.6, 2.1]}
    st.bar_chart(pd.DataFrame(data).set_index("Drug"))

elif page == "Risk Management":
    st.header("Risk Management Plan")
    risk = st.text_input("Important Identified Risk")
    mitigation = st.text_area("Risk Minimization Measure")
    if st.button("Save Risk"):
        st.success("Risk entry recorded.")

elif page == "Quality Assurance (PV QA)":
    st.header("Pharmacovigilance Quality System")
    audit = st.text_input("Audit Name")
    finding = st.text_area("Observation")
    if st.button("Log Finding"):
        st.info("Quality record logged.")

elif page == "Regulatory Reporting / Submissions":
    st.header("Regulatory Safety Reporting")
    authority = st.selectbox("Regulatory Authority", ["FDA", "EMA", "MHRA", "PMDA", "Health Canada"])
    if st.button("Prepare Submission"):
        st.success("Submission package simulated.")

elif page == "Safety Database Management":
    st.header("Safety Database Systems")
    systems = ["Argus", "ARISg", "Veeva", "Empirica"]
    st.write(systems)

elif page == "Real-World Evidence (RWE) Safety":
    st.header("Real World Evidence in Drug Safety")
    data = {"Source": ["EHR", "Claims", "Registry"], "Cases": [120, 85, 45]}
    st.bar_chart(pd.DataFrame(data).set_index("Source"))

elif page == "Automation / PV Technology":
    st.header("Automation in Pharmacovigilance")
    tool = st.selectbox("Technology", ["AI Case Processing", "NLP Literature Screening", "Automation Bots"])
    st.write("Selected:", tool)