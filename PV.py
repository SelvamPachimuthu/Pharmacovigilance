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
/* Page background with reduced vibrant gradient */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, 
        #FF7F00,   /* orange */
        #FFFF00,   /* yellow */
        #00FF00,   /* green */
        #00FFFF    /* cyan */
    );
    background-size: 400% 400%;
    animation: gradientShift 25s ease infinite;
    position: relative;
}

/* Sidebar background with reduced vibrant colors */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, 
        #FF7F00, #FFFF00, #00FF00, #00FFFF
    );
}

/* Optional: animate the gradient if needed */
@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
            
/* Smooth gradient animation */
@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Animation keyframes for smooth gradient shift */
@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Floating pill style */
.pill {
    position: fixed;
    font-size: 50px;
    animation: float 12s linear infinite;
    opacity: 0.25;
    text-shadow: 0 0 10px #fff, 0 0 20px #ff69b4, 0 0 30px #87CEEB;
}

/* Different positions and animation durations */
.pill1 { left: 5%; animation-duration: 14s; }
.pill2 { left: 20%; animation-duration: 18s; }
.pill3 { left: 40%; animation-duration: 16s; }
.pill4 { left: 60%; animation-duration: 20s; }
.pill5 { left: 80%; animation-duration: 15s; }

/* Floating animation */
@keyframes float {
    0% { top: 110%; transform: rotate(0deg); }
    100% { top: -10%; transform: rotate(360deg); }
}

/* Gradient shift for a "lit" effect */
@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
</style>

<div class="pill pill1">🟠</div>
<div class="pill pill2">💊</div>
<div class="pill pill3">🔵</div>
<div class="pill pill4">🟢</div>
<div class="pill pill5">📄</div>
""", unsafe_allow_html=True)

# Title
st.title("💊📄 Pharmacovigilance - Drug Safety Data Management")

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
        "Regulatory Reporting / Submissions",
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
    st.write("• Regulatory Submissions")"
    st.write("• PV Technology and Automation")
    st.subheader("Global Guidelines")
    st.write("Good Pharmacovigilance Practices (GVP)")
    st.write("ICH Guidelines (E2A, E2B, E2C, E2D, E2E)")
    st.write("CIOMS Recommendations")

# ---------------- ICSR PROCESSING ----------------
elif page == "ICSR Processing":
    url = "https://www.ema.europa.eu/en/documents/regulatory-procedural-guideline/guideline-good-pharmacovigilance-practices-gvp-module-vi-collection-management-submission-reports-suspected-adverse-reactions-medicinal-products-rev-2_en.pdf"
    st.markdown(f"[📄 Guideline GVP Module VI (PDF)]({url})")

    # Display introductory text
    st.text(
        "📊 ICSR management is a fundamental activity of pharmacovigilance\n\n"
        "✨ ICSR = identifiable reporter, an identifiable patient, a suspect product, and an adverse event. "
        "Without all four, it’s a non-valid case."
    )

    # Define case workflow
    case_workflow = {
        "Case Intake": "Initial receipt of the case from healthcare provider, patient, literature, or other sources; "
                       "collection of all relevant information including demographics, medical history, suspect and concomitant drugs, and event details.",
        "Triage": "Assessment of the case to determine priority and next steps. Includes evaluating seriousness, expectedness, and completeness, and routing to the appropriate team for processing.",
        "Duplicate Check": "Comparison of the case with existing cases in the database to identify potential duplicates and prevent redundant reporting. Cases are marked as duplicate or unique.",
        "Data Entry": "Accurate entry of case information into the safety database, including patient details, drug information, adverse events, lab results, and other relevant data.",
        "Quality Review": "Medical review to evaluate clinical plausibility, completeness, and appropriate coding (e.g., MedDRA for events, WHO Drug for drugs). Ensures case is medically sound and complete.",
        "Quality Control": "Verification of data accuracy, consistency, and compliance with internal SOPs and regulatory requirements. May overlap with quality review but focuses on correctness and completeness.",
        "Regulatory Submission": "Preparation and submission of the case to regulatory authorities according to local and global regulations (e.g., CIOMS, E2B(R3) format). Includes tracking submissions and acknowledgments for serious or reportable cases."
    }

    # Display workflow as a table
    st.table(pd.DataFrame(case_workflow.items(), columns=["Step", "Description"]))

    st.text(
    """
Validated safety systems help capture, manage, and evaluate safety cases in alignment with Good Pharmacovigilance Practices (GVP) from the European Medicines Agency.

Common pharmacovigilance platforms include:

• Oracle Argus Safety
• ARISg
• Veeva Vault Safety
• LifeSphere MultiVigilance
• Clinevo Safety etc...

These systems support structured workflows such as case intake, triage, data entry, medical review, quality control, and regulatory reporting.

📈 Where Safety Information Comes From

1️⃣ ***Clinical Development ***

During clinical trials, safety is monitored closely according to guidelines from the International Council for Harmonisation.

• SAE (Serious Adverse Event)
Events that result in death, hospitalization, disability, life-threatening situations, or other medically important conditions.

• SUSAR (Suspected Unexpected Serious Adverse Reaction)
Serious reactions that are unexpected based on the Investigator’s Brochure or product information.

These findings contribute to annual submissions such as the Development Safety Update Report (DSUR).

2️⃣ ***Post-Marketing Surveillance***
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
• Social media monitoring
"""
    )

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

# ---------------- LITERATURE REVIEW ----------------
elif page == "Literature Review":
    st.header("Literature Monitoring")
    url = "https://www.ema.europa.eu/en/documents/regulatory-procedural-guideline/guideline-good-pharmacovigilance-practices-gvp-module-vi-collection-management-submission-reports-suspected-adverse-reactions-medicinal-products-rev-2_en.pdf"
    st.markdown(f"[📄 Guideline GVP Module VI (PDF)-Literature Screening]({url})")
    st.info(
        "The medical literature is a significant source of information for the monitoring of the safety profile and of the risk-benefit balance of medicinal products, particularly in relation to the detection of new safety signals or emerging safety issues. Marketing authorisation holders are therefore expected to maintain awareness of possible publications through a systematic literature review of widely used reference databases (e.g. Medline, Excerpta Medica or Embase) no less frequently than once a week."
        " Reports of suspected adverse reactions from the medical literature, including relevant published abstracts from meetings and draft manuscripts, should be reviewed and assessed by marketing authorisation holders to identify and record ICSRs."
        " If multiple medicinal products are mentioned in the publication, only those which are identified by the publication's author(s) as having at least a possible causal relationship with the suspected adverse reaction should be considered for literature review by the concerned marketing authorisation holder(s)."
    )

    # Example list of listed adverse events
    listed_adverse_events = ["Nausea", "Headache", "Rash", "Dizziness"]

    # Choose data type
    data_type = st.selectbox(
        "Choose single patient or aggregate data for literature screening", 
        ["Single Patient", "Aggregate Data"]
    )

    # Only show the instructions if nothing is selected yet
    if not data_type:
        st.write("Choose single patient or aggregate data for literature screening")

    # Inputs common to both
    drug = st.text_input("Drug")
    reaction = st.text_input("Adverse Reaction")

    # Inputs specific to Single Patient
    if data_type == "Single Patient":
        reporter_name = st.text_input("Primary Reporter Name")
        patient_identifier = st.text_input("Patient Identifier")
        MAH_marketing = st.selectbox(
            "Did MAH market the drug in the reporter's country?", 
            ["Yes", "No"]
        )

    if st.button("Screen Article"):
        # For Single Patient Data
        if data_type == "Single Patient":
            if MAH_marketing == "Yes":
                if reporter_name and patient_identifier and drug and reaction:
                    st.success("This qualifies as an ICSR.")

                    # Check if reaction is listed
                    if reaction.strip() in listed_adverse_events:
                        st.info("No potential safety information; listed adverse event.")
                    else:
                        st.warning("Potential safety information identified. Further assessment required.")
                else:
                    st.warning("Not an ICSR: Missing one or more required fields.")
            else:
                st.info("Drug not marketed in reporter's country. ICSR screening not applicable.")

        # For Aggregate Data
        else:
            if reaction:
                if reaction.strip() in listed_adverse_events:
                    st.info("No potential safety information; listed adverse event.")
                else:
                    st.warning("Potential safety information identified. Further assessment required.")
            else:
                st.warning("Aggregate data missing adverse reaction information.")
# ---------------- AGGREGATE REPORTS ----------------
elif page == "Aggregate Reports Preparation":
    st.header("Aggregate Safety Reports")
    url_PSUR_GVP_Module_7="https://www.ema.europa.eu/en/documents/scientific-guideline/guideline-good-pharmacovigilance-practices-gvp-module-vii-periodic-safety-update-report_en.pdf"
    url_PBRER_ICH_E2C_R2= "https://database.ich.org/sites/default/files/E2C_R2_Guideline.pdf"
    url_DSUR_ICH_E2F = "https://database.ich.org/sites/default/files/E2F_Guideline.pdf"

    aggregate_reports = {
        "PSUR": {
            "Frequency": "Periodic (6 months–3 years depending on lifecycle stage)",
            "Regulatory_Region_Example": ["EU", "India", "Other global regulators"],
            "Purpose": "Safety-focused: monitor cumulative safety data, detect new safety signals, evaluate risk-benefit",
            "Key_Notes": [
                "Primarily safety-oriented",
                "Structured as per ICH E2C(R2) guidelines",
                "Being gradually replaced in some regions by PBRER"
            ],
            "Link": [url_PSUR_GVP_Module_7]
        },
        "PBRER": {
            "Frequency": "Periodic (aligned with product lifecycle, similar to PSUR)",
            "Regulatory_Region_Example": ["EMA", "FDA", "Global harmonized standard"],
            "Purpose": "Integrated benefit-risk evaluation including safety and efficacy data",
            "Key_Notes": [
                "Modern standard replacing PSUR in many regions",
                "Includes missing information and cumulative benefit-risk analysis",
                "Based on ICH E2C(R2) guidelines"
            ],
            "Link": [url_PBRER_ICH_E2C_R2]
        },
        "DSUR": {
            "Frequency": "Annual",
            "Regulatory_Region_Example": ["USA", "EU", "Global"],
            "Purpose": "Safety monitoring during clinical development of investigational drugs",
            "Key_Notes": [
                "Pre-marketing report for clinical trials",
                "Summarizes adverse events (AEs/SAEs) and risk evaluation",
                "Based on ICH E2F guidelines"
            ],
            "Link": [url_DSUR_ICH_E2F]
        }
    }
    st.table(pd.DataFrame(aggregate_reports))

# ---------------- SIGNAL MANAGEMENT ----------------
elif page == "Signal Management":
    st.header("Signal Detection and Management")
    url = "https://www.ema.europa.eu/en/documents/scientific-guideline/guideline-good-pharmacovigilance-practices-gvp-module-ix-signal-management-rev-1_en.pdf"
    st.markdown(f"[📄 Guideline GVP Module IX (PDF)]({url})")
    st.subheader("Signal Detection Concepts")

    st.markdown("""
**1. Types of Signal Detection:**

- **Quantitative Signal Detection:**  
  - Uses statistical methods to identify disproportionality in adverse event reporting.  
  - Metrics include **Reporting Odds Ratio (ROR)**, **Proportional Reporting Ratio (PRR)**, **Bayesian Confidence Propagation Neural Network (BCPNN)**, and **Empirical Bayes Geometric Mean (EBGM)**.  
  - Objective: Detect unusual patterns or higher-than-expected reporting of specific adverse events associated with drugs.  

- **Qualitative Signal Detection:**  
  - Based on expert review of case reports, literature, clinical trial data, and regulatory intelligence.  
  - Focuses on **clinical relevance, seriousness, biological plausibility**, and temporal association.  
  - Often used to support or prioritize quantitative findings.

**2. Signal Evaluation Process:**

1. **Detection:**  
   - Identify potential signals using quantitative metrics or qualitative assessment.  

2. **Validation:**  
   - Check data quality, case completeness, duplicate reports, and confounding factors.  
   - Ensure that signal is not due to reporting bias or chance.

3. **Assessment / Analysis:**  
   - Detailed clinical review by safety experts.  
   - Consider patient demographics, dose-response relationship, concomitant medications, seriousness of the adverse event.  

4. **Confirmation:**  
   - Confirm whether the signal is likely to represent a true causal relationship.  
   - May involve literature review, epidemiological studies, or additional data collection.

**3. Signal Status:**

- **Signal Under Evaluation:**  
  - Signal has been detected but is still being analyzed and confirmed.  

- **Confirmed Signal:**  
  - Evidence supports that there is a likely causal relationship between the drug and the adverse event.  

- **Closed / Rejected Signal:**  
  - Signal investigation shows no causal relationship or insufficient evidence.  
  - No further regulatory action is typically required, but monitoring continues.

**4. Regulatory Implications:**

- Confirmed signals may lead to:  
  - Label changes / safety warnings  
  - Risk minimization measures  
  - Further clinical studies  
  - Updates in PSUR/PBRER reports  

- Signals under evaluation are tracked and monitored in safety databases.  
- Closed signals are documented with rationale and archived.
""")

    df = pd.DataFrame({
    "Drug": ["Drug A", "Drug B", "Drug C"],
    "Signal Score": [3.2, 5.6, 2.1],
    "Signal Status": ["Under Evaluation", "Confirmed", "Closed"]
})

# --- Display the DataFrame ---
    st.dataframe(df)

# --- Bar chart for Signal Scores ---
    st.bar_chart(df.set_index("Drug")["Signal Score"])

# ---------------- RISK MANAGEMENT ----------------
elif page == "Risk Management":
    st.header("Risk Management Plan")
    url = "https://www.ema.europa.eu/en/documents/scientific-guideline/guideline-good-pharmacovigilance-practices-module-v-risk-management-systems-rev-2_en.pdf"
    st.markdown(f"[📄 Guideline GVP Module V (PDF)]({url})")

    st.markdown("""
1. Signal Detection

A signal is any information suggesting a potential causal association between a medicinal product and an adverse event. Signals can originate from:

- Spontaneous adverse event reports
- Clinical trials
- Literature reports
- Epidemiological studies

Purpose: Identify new safety concerns or new aspects of known adverse events.

Example: Reports of liver injury in patients taking Drug A.

2. Signal Validation

Once a signal is detected, it must be validated to confirm whether it represents a real safety concern:

- Qualitative evaluation: Reviewing individual case narratives for medical plausibility.
- Quantitative evaluation: Using statistical methods like disproportionality analysis (e.g., Reporting Odds Ratio) to detect unusual patterns.

Outcome: Determination of whether the signal is clinically relevant and warrants further action.

3. Risk Identification

Validated signals are translated into risks for inclusion in the Risk Management Plan (RMP).

- Identified Risk: A safety concern confirmed to be causally related to the drug.
- Potential Risk: A plausible risk that is suspected but not confirmed.
- Missing Information: Gaps in knowledge about certain populations, dosing, or long-term effects.

Example: Signal of liver injury → Identified risk: hepatotoxicity associated with Drug A.

4. Risk Characterization

Each risk is described in terms of:

- Nature: Type of adverse event (e.g., liver toxicity).
- Frequency: How often it occurs (common, rare, very rare).
- Severity: Mild, moderate, severe, or life-threatening.
- Outcome: Reversible, irreversible, fatal.

This ensures the risk is clearly understood and can guide appropriate management.

5. Risk Minimization

GVP emphasizes proactive measures to reduce the probability or impact of identified risks:

- Routine measures:
  - Product labeling
  - Package inserts for patients
  - Guidance for healthcare professionals
- Additional measures (if needed):
  - Restricted distribution
  - Controlled use programs
  - Special patient monitoring or registries

Purpose: Protect patient safety and ensure the safe use of the drug in clinical practice.

6. Risk Management Plan (RMP)

An RMP is a structured document submitted to regulatory authorities, describing:

- Identified risks
- Potential risks
- Missing information
- Planned pharmacovigilance activities
- Risk minimization strategies

It is continuously updated throughout the product’s lifecycle to reflect new safety information.

7. Signal-to-Risk Workflow (Summary)

- Signal detection: New safety concern identified.
- Signal validation: Confirm clinical relevance using qualitative and quantitative methods.
- Risk identification: Transform validated signals into risks (identified, potential, or missing info).
- Risk characterization: Describe nature, frequency, severity, and outcome.
- Risk minimization planning: Implement routine and additional measures.
- Documentation in RMP: Communicate and track safety measures over the product lifecycle.
""")

    # --- Inputs ---
    source_signal = st.selectbox(
        "Source Signal (from Signal Detection)", 
        ["Drug A - Liver Injury", "Drug B - Rash", "Drug C - Headache"]
    )

    risk = st.text_input("Risk what we found (e.g., hepatotoxicity, dermatological reaction, etc.)")
    risk_category = st.selectbox(
        "Risk Category",
        ["Identified Risk", "Potential Risk", "Missing Information"]
    )

    frequency = st.selectbox(
        "Frequency of Risk", ["Very Common", "Common", "Uncommon", "Rare", "Very Rare"]
    )
    severity = st.selectbox(
        "Severity", ["Mild", "Moderate", "Severe", "Life-threatening"]
    )
    outcome = st.text_input("Outcome (e.g., reversible, irreversible, fatal)")
    mitigation = st.text_area("Risk Minimization Measure (Routine or Additional)")

    # --- Save Button ---
    if st.button("Save Risk"):
        st.success("✅ Risk entry recorded in mini-RMP format.")
        st.markdown(f"""
### Risk Management Entry
**Signal Source:** {source_signal}  
**Identified Risk:** {risk}  
**Risk Category:** {risk_category}  
**Frequency:** {frequency}  
**Severity:** {severity}  
**Outcome:** {outcome}  
**Risk Minimization Measures:** {mitigation}
""")

    st.markdown("""
#### How Signals Transfer to Risks (GVP Module V)
1. **Signal Detection:** Identified from safety databases, literature, or clinical trials.  
2. **Validation:** Evaluated qualitatively and quantitatively to confirm clinical relevance.  
3. **Risk Identification:** Transformed into an identified, potential, or missing risk in the RMP.  
4. **Risk Characterization:** Nature, frequency, severity, and outcome of the risk are described.  
5. **Risk Minimization:** Routine (labeling, guidance) and additional measures (restricted use, monitoring) are planned.  
6. **Documentation:** Captured in the Risk Management Plan and updated throughout the product lifecycle.
""")

# ---------------- REGULATORY REPORTING ----------------
elif page == "Regulatory Reporting / Submissions":
    st.header("📄 Regulatory Safety Reporting")
    st.subheader("Overview")
    st.markdown("""
Regulatory safety reporting is a **core pharmacovigilance activity**. It ensures that adverse events and safety data are reported to health authorities in compliance with regulations to **protect patient safety**.  

Key points:
- Compliance with global regulations.
- Enables signal detection and risk management.
- Protects public health and ensures ongoing monitoring of drugs.
""")

    authority = st.selectbox(
        "Select Regulatory Authority",
        ["FDA (USA)", "EMA (Europe)", "MHRA (UK)", "PMDA (Japan)", "Health Canada (Canada)","CDSCO (India)", "TGA (Australia)"]
    )

    if authority:
        st.markdown("### Authority Details:")

        if authority == "FDA (USA)":
            st.markdown("""
- **Full Form:** Food and Drug Administration  
- **Reporting Requirements:** IND Safety Reports (clinical trials), **PADER** (Periodic Adverse Drug Experience Report for marketed drugs)  
- **Regulations:** 21 CFR Part 312, 21 CFR Part 314  
- **Submission Methods:** Electronic via FAERS (FDA Adverse Event Reporting System)
""")
        elif authority == "EMA (Europe)":
            st.markdown("""
- **Full Form:** European Medicines Agency  
- **Reporting Requirements:** **PBRER (Periodic Benefit-Risk Evaluation Report)** for marketed drugs, SUSARs for clinical trials  
- **Regulations:** EU Clinical Trials Regulation, Good Pharmacovigilance Practices (GVP)  
- **Submission Methods:** EudraVigilance system
""")
        elif authority == "MHRA (UK)":
            st.markdown("""
- **Full Form:** Medicines and Healthcare products Regulatory Agency  
- **Reporting Requirements:** Yellow Card Scheme for adverse events, PSUR/PBRER as applicable  
- **Regulations:** UK Pharmacovigilance Legislation (post-Brexit)  
- **Submission Methods:** MHRA Gateway
""")
        elif authority == "PMDA (Japan)":
            st.markdown("""
- **Full Form:** Pharmaceuticals and Medical Devices Agency  
- **Reporting Requirements:** ADR reports, PBRER for marketed drugs  
- **Regulations:** Japanese GCP, Japanese Pharmacovigilance Guidelines  
- **Submission Methods:** PMDA portal electronic submission
""")
        elif authority == "Health Canada (Canada)":
            st.markdown("""
- **Full Form:** Health Canada  
- **Reporting Requirements:** ADR reports, PBRER/PSUR as applicable, Special Access Program notifications  
- **Regulations:** Food and Drugs Act, Canadian GVP guidelines  
- **Submission Methods:** Canada Vigilance Program portal
""")
        elif authority == "CDSCO (India)":
            st.markdown("""
- **Full Form:** Central Drugs Standard Control Organization  
- **Reporting Requirements:** ADR reports, PBRER/PSUR as applicable  
- **Regulations:** Indian Pharmacovigilance Guidelines  
- **Submission Methods:** CDSCO portal
""")
        elif authority == "TGA (Australia)":
            st.markdown("""
- **Full Form:** Therapeutic Goods Administration  
- **Reporting Requirements:** ADR reports, PBRER/PSUR as applicable  
- **Regulations:** Australian GVP guidelines  
- **Submission Methods:** TGA portal
""")

    if st.button("Prepare Submission"):
        st.success(f"✅ Submission package simulated for {authority} authority.")
        st.info("This is a simulation. No real data has been submitted.")

    st.markdown("""
### Typical Submission Steps:
1. Case collection and validation.
2. Aggregate report preparation (if applicable, e.g., PBRER or PADER).
3. Review by Quality/Medical team.
4. Prepare regulatory submission package.
5. Submit via the respective authority portal.
6. Track acknowledgement and follow-up.
""")

# ---------------- AUTOMATION / PV TECHNOLOGY ----------------
elif page == "Automation / PV Technology":
    st.header("Automation in Pharmacovigilance")
    tool = st.selectbox("Technology", ["AI Case Processing", "NLP Literature Screening", "Automation Bots"])

    if tool == "AI Case Processing":
        st.markdown("""
**AI Case Processing** automates ICSR handling:
- Extracts patient, drug, and event information automatically.
- Classifies cases by seriousness and completeness.
- Flags urgent or duplicate cases for review.
**Benefits:** Faster processing, fewer errors, more time for medical review.
""")
    elif tool == "NLP Literature Screening":
        st.markdown("""
**NLP Literature Screening** helps detect adverse events in publications:
- Screens journals, abstracts, and medical reports.
- Highlights relevant safety signals.
**Benefits:** Early detection of new safety issues, less manual reading.
""")
    elif tool == "Automation Bots":
        st.markdown("""
**Automation Bots** (RPA) handle repetitive tasks:
- Download reports from portals.
- Check drug listedness.
- Generate routine PV reports automatically.
**Benefits:** Saves time, improves accuracy, operates continuously.
""")