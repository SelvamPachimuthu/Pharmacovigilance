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

# Title
st.title("💊 Pharmacovigilance - Drug Safety Data Management")

st.markdown("""
Welcome to the **Pharmacovigilance Review Portal**.

This app can help with understanding of safety data management in the pharmaceutical industry, aligned with global regulatory guidelines.
""")

# Sidebar
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

# HOME
if page == "Home":
    st.header("Welcome to Pharmacovigilance Hub")
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

# ICSR PROCESSING
elif page == "ICSR Processing": 
    st.title("ICSR Processing Dashboard")

    # ------------------ Tabs ------------------
    tabs = st.tabs([
        "General", 
        "Reporter",
        "Patient", 
        "Parent Case", 
        "Adverse Event", 
        "Suspected Drug", 
        "Causality",
        "Analysis",
        "Reporting"
    ])

    # ------------------ General Tab ------------------
    with tabs[0]:
        st.header("General Case Information")
        case_received_date = st.date_input("Case Received Date", Date.today())
        report_type = st.selectbox(
            "Report Type",
            ["Spontaneous", "Clinical Trial", "Literature", "Other"]
        )
        country = st.text_input("Country")
        seriousness = st.selectbox("Seriousness", ["Non Serious", "Serious"])
        if seriousness == "Serious":
            seriousness_detail = st.selectbox(
                "Seriousness Criteria",
                [
                    "Death",
                    "Life Threatening",
                    "Inpatient Hospitalization",
                    "Disability",
                    "Congenital Anomaly",
                    "Medically Significant"
                ]
            )
        else:
            seriousness_detail = "Non Serious"

    # ------------------ Reporter Tab ------------------
    with tabs[1]:
        st.header("Reporter Information")
        reporter_name = st.text_input("Reporter Name")
        reporter_email = st.text_input("Reporter Email")
        reporter_contact = st.text_input("Reporter Contact Number")
        reporter_qualification = st.text_input("Reporter Qualification")

    # ------------------ Patient Tab ------------------
    with tabs[2]:
        st.header("Patient Information")
        patient_age = st.number_input("Patient Age", 0, 120)
        gender = st.selectbox("Gender", ["Male", "Female", "Other", "Unknown"])
        weight = st.number_input("Weight (kg)", 0.0, 300.0, 0.0)
        height = st.number_input("Height (cm)", 0.0, 250.0, 0.0)
        medical_history = st.text_area("Relevant Medical History")

    # ------------------ Parent Case Tab ------------------
    with tabs[3]:
        st.header("Parent Case Information")
        parent_case_id = st.text_input("Parent Case ID")
        parent_case_status = st.selectbox("Parent Case Status", ["Open", "Closed", "Ongoing"])
        related_cases = st.text_area("Related Cases")

    # ------------------ Adverse Event Tab ------------------
    with tabs[4]:
        st.header("Adverse Event Information")
        ae_verbatim = st.text_area("Adverse Event - Verbatim")
        ae_meddra = st.text_area("Adverse Event - MedDRA Code")
        ae_outcome = st.selectbox("Outcome", ["Recovered", "Recovering", "Not Recovered", "Fatal", "Unknown"])

    # ------------------ Suspected Drug Tab ------------------
    with tabs[5]:
        st.header("Suspected Drug Information")
        suspected_drug = st.text_input("Drug Name")
        dose = st.text_input("Dose")
        route = st.selectbox("Route of Administration", ["Oral", "IV", "IM", "Subcutaneous", "Other"])
        start_date = st.date_input("Start Date")
        end_date = st.date_input("End Date")
        indication = st.text_area("Indication / Reason for Use")

    # ------------------ Causality Tab ------------------
    with tabs[6]:
        st.header("Causality Assessment")
        causality_method = st.selectbox(
            "Causality Assessment Method",
            ["WHO-UMC", "Naranjo", "Other"]
        )
        causality_result = st.selectbox(
            "Assessment Result",
            ["Certain", "Probable", "Possible", "Unlikely", "Conditional", "Unassessable"]
        )
        reporter_comments = st.text_area("Reporter Comments")

    # ------------------ Analysis Tab ------------------
    with tabs[7]:
        st.header("Narrative and Analysis")
        case_summary = st.text_area("Case Summary")

    # ------------------ Reporting Tab ------------------
    with tabs[8]:
        st.header("Submit Case")
        if st.button("Generate CDSCO PDF"):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", 'B', 16)
            pdf.cell(0, 10, "ICSR Case Report - CDSCO", ln=True, align='C')
            pdf.ln(5)

            # General
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, "1. General Case Information", ln=True)
            pdf.set_font("Arial", '', 12)
            pdf.multi_cell(0, 8, f"Case Received Date: {case_received_date}\nReport Type: {report_type}\nCountry: {country}\nSeriousness: {seriousness}\nSeriousness Detail: {seriousness_detail}")
            pdf.ln(3)

            # Reporter
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, "2. Reporter Information", ln=True)
            pdf.set_font("Arial", '', 12)
            pdf.multi_cell(0, 8, f"Name: {reporter_name}\nEmail: {reporter_email}\nContact: {reporter_contact}\nQualification: {reporter_qualification}")
            pdf.ln(3)

            # Patient
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, "3. Patient Information", ln=True)
            pdf.set_font("Arial", '', 12)
            pdf.multi_cell(0, 8, f"Age: {patient_age}\nGender: {gender}\nWeight: {weight} kg\nHeight: {height} cm\nMedical History: {medical_history}")
            pdf.ln(3)

            # Parent Case
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, "4. Parent Case Information", ln=True)
            pdf.set_font("Arial", '', 12)
            pdf.multi_cell(0, 8, f"Parent Case ID: {parent_case_id}\nStatus: {parent_case_status}\nRelated Cases: {related_cases}")
            pdf.ln(3)

            # Adverse Event
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, "5. Adverse Event Information", ln=True)
            pdf.set_font("Arial", '', 12)
            pdf.multi_cell(0, 8, f"Verbatim: {ae_verbatim}\nMedDRA Code: {ae_meddra}\nOutcome: {ae_outcome}")
            pdf.ln(3)

            # Suspected Drug
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, "6. Suspected Drug Information", ln=True)
            pdf.set_font("Arial", '', 12)
            pdf.multi_cell(0, 8, f"Drug Name: {suspected_drug}\nDose: {dose}\nRoute: {route}\nStart Date: {start_date}\nEnd Date: {end_date}\nIndication: {indication}")
            pdf.ln(3)

            # Causality
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, "7. Causality Assessment", ln=True)
            pdf.set_font("Arial", '', 12)
            pdf.multi_cell(0, 8, f"Method: {causality_method}\nResult: {causality_result}\nReporter Comments: {reporter_comments}")
            pdf.ln(3)

            # Analysis
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, "8. Narrative and Analysis", ln=True)
            pdf.set_font("Arial", '', 12)
            pdf.multi_cell(0, 8, f"{case_summary}")
            pdf.ln(5)

            # CDSCO info if India
            if country.strip().lower() == "india":
                pdf.set_font("Arial", 'B', 12)
                pdf.cell(0, 10, "This case should be reported to CDSCO (India).", ln=True)

            # Save PDF
            pdf_file = "ICSR_CDSCO_Report.pdf"
            pdf.output(pdf_file)

            # Provide download link
            with open(pdf_file, "rb") as f:
                st.download_button(
                    label="Download CDSCO PDF",
                    data=f,
                    file_name=pdf_file,
                    mime="application/pdf"
                )
            st.success("PDF generated successfully!")

# LITERATURE REVIEW
elif page == "Literature Review":
    st.header("Literature Monitoring")
    st.write(
        """
Marketing authorization holders must monitor scientific and medical literature 
to identify potential adverse drug reactions as per regulatory expectations.
"""
    )

    article = st.text_input("Article Title")
    journal = st.text_input("Journal")
    drug = st.text_input("Drug")
    reaction = st.text_input("Adverse Reaction")

    if st.button("Screen Article"):
        st.warning("Potential safety information identified. Further assessment required.")




# AGGREGATE REPORTS
elif page == "Aggregate Reports Preparation":

    st.header("Aggregate Safety Reports")

    st.write(
        """
Aggregate reporting evaluates cumulative safety data of a medicinal product.

Common reports include:
• PSUR / PBRER
• DSUR
• Development Safety Updates
"""
    )

    data = {
        "Report Type": ["PSUR", "PBRER", "DSUR"],
        "Frequency": ["Periodic", "Periodic", "Annual"],
    }

    df = pd.DataFrame(data)

    st.table(df)


# SIGNAL MANAGEMENT
elif page == "Signal Management":
    
    st.header("Signal Detection and Management")
    st.write(
        """
      Signal management is defined in GVP Module IX and involves:

• Signal detection  
• Signal validation  
• Signal prioritization  
• Signal assessment  
• Recommendation for action
"""
    )

    data = {
        "Drug": ["Drug A", "Drug B", "Drug C"],
        "Signal Score": [3.2, 5.6, 2.1],
    }

    df = pd.DataFrame(data)

    st.bar_chart(df.set_index("Drug"))


# RISK MANAGEMENT
elif page == "Risk Management":

    st.header("Risk Management Plan")

    st.write(
        """
Risk Management Plans describe safety concerns and risk minimization measures.

Components include:
• Safety specification
• Pharmacovigilance plan
• Risk minimization measures
"""
    )

    risk = st.text_input("Important Identified Risk")

    mitigation = st.text_area("Risk Minimization Measure")

    if st.button("Save Risk"):
        st.success("Risk entry recorded.")


# PV QA
elif page == "Quality Assurance (PV QA)":

      st.header("Pharmacovigilance Quality System")

      st.write(
        """
PV Quality ensures compliance with regulatory requirements.

Key elements:
• SOP compliance
• Audits and inspections
• CAPA management
• Training documentation
"""
    )

      audit = st.text_input("Audit Name")

      finding = st.text_area("Observation")

      if st.button("Log Finding"):
        st.info("Quality record logged.")


# REGULATORY
elif page == "Regulatory Reporting / Submissions":

      st.header("Regulatory Safety Reporting")

      st.write(
        """
Expedited reporting requirements:

• 7 Day Fatal or Life-Threatening cases
• 15 Day Serious cases
• Non-serious periodic submissions
"""
    )

      authority = st.selectbox(
        "Regulatory Authority",
        ["FDA", "EMA", "MHRA", "PMDA", "Health Canada"],
    )

      if st.button("Prepare Submission"):
        st.success("Submission package simulated.")


# SAFETY DATABASE
elif page == "Safety Database Management":

      st.header("Safety Database Systems")

      st.write(
        """
Common PV safety databases used by industry:

• Argus Safety
• ARISg
• Veeva Safety
• Oracle Empirica
"""
    )

      systems = ["Argus", "ARISg", "Veeva", "Empirica"]

      st.write(systems)


# RWE
elif page == "Real-World Evidence (RWE) Safety":

      st.header("Real World Evidence in Drug Safety")

      st.write(
        """
Real world data sources:

• Electronic Health Records
• Insurance Claims
• Patient Registries
• Post-Marketing Studies
"""
    )

      data = {
        "Source": ["EHR", "Claims", "Registry"],
        "Cases": [120, 85, 45],
    }

      df = pd.DataFrame(data)

      st.bar_chart(df.set_index("Source"))


# AUTOMATION
elif page == "Automation / PV Technology":

      st.header("Automation in Pharmacovigilance")

      st.write(
        """
Emerging technologies transforming PV:

• Artificial Intelligence for case intake
• NLP for literature screening
• Signal detection algorithms
• Robotic Process Automation
"""
    )

      tool = st.selectbox(
        "Technology",
        ["AI Case Processing", "NLP Literature Screening", "Automation Bots"],
    )

      st.write("Selected:", tool)
