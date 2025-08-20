
import pandas as pd
from fpdf import FPDF

# Step 1: Read data from CSV
df = pd.read_csv("data.csv")

# Step 2: Analyze the data
total_employees = len(df)
average_salary = df["Salary"].mean()
max_salary = df["Salary"].max()
min_salary = df["Salary"].min()
department_counts = df["Department"].value_counts()

# Step 3: Create PDF report
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Employee Salary Report", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", "", 12)

# Summary Section
pdf.cell(0, 10, f"Total Employees: {total_employees}", ln=True)
pdf.cell(0, 10, f"Average Salary: ₹{average_salary:.2f}", ln=True)
pdf.cell(0, 10, f"Highest Salary: ₹{max_salary}", ln=True)
pdf.cell(0, 10, f"Lowest Salary: ₹{min_salary}", ln=True)
pdf.ln(10)

# Department Breakdown
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "Department-wise Employee Count:", ln=True)
pdf.set_font("Arial", "", 12)
for dept, count in department_counts.items():
    pdf.cell(0, 10, f"{dept}: {count}", ln=True)

pdf.ln(10)

# Table of Employees
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "Employee Details:", ln=True)
pdf.set_font("Arial", "", 12)
for index, row in df.iterrows():
    pdf.cell(0, 10, f"{row['Name']} | {row['Department']} | ₹{row['Salary']}", ln=True)

# Save PDF
pdf.output("Employee_Report.pdf")
print("✅ Report generated successfully as 'Employee_Report.pdf'")

