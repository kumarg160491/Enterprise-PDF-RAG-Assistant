from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os

base = "./data/documents"
os.makedirs(base, exist_ok=True)

styles = getSampleStyleSheet()

pdfs = {
    "employee_policy.pdf": """
    Employee Policy Document

    Leave Policy:
    Employees are eligible for 20 days of annual paid leave every calendar year.
    Leave requests must be submitted through the employee portal and approved by the reporting manager.

    Sick Leave:
    Employees can request sick leave when they are unwell.
    Medical documents may be required for extended sick leave.

    Work From Home:
    Employees may work remotely based on business requirements and manager approval.
    """,

    "loan_process_manual.pdf": """
    Loan Process Manual

    Loan Application:
    Customers must submit identity documents, income proof, and application details.

    Loan Approval:
    Applications are reviewed based on eligibility criteria, credit history, and risk assessment.

    Loan Closure:
    A loan can be closed after repayment of outstanding dues.
    The closure confirmation document is issued after successful verification.
    """
}

created = []

for filename, text in pdfs.items():
    path = os.path.join(base, filename)
    doc = SimpleDocTemplate(path)
    content = []
    for line in text.strip().split("\n\n"):
        content.append(Paragraph(line.replace("\n", "<br/>"), styles["BodyText"]))
        content.append(Spacer(1, 12))
    doc.build(content)
    created.append(path)

created
