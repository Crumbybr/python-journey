import PyPDF2
import re
import os

# Function to extract the professor's contact information
def extract_professor_info(text):
    professor_info = {}
    email_pattern = r'Email:\s+([\w\.-]+@[\w\.-]+)'
    name_pattern = r'Dr\.\s+([A-Za-z\s]+)'

    email_match = re.search(email_pattern, text)
    name_match = re.search(name_pattern, text)

    if name_match:
        professor_info['Name'] = name_match.group(1).strip()
    if email_match:
        professor_info['Email'] = email_match.group(1).strip()

    return professor_info

# Function to extract grade breakdown
def extract_grade_breakdown(text):
    grade_breakdown = {}
    grade_pattern = r'(Exam\s+\w+|Online Participation|Online Discussions|Chapter Quizzes/Surveys|PC College-Wide Africana Studies Department Assessment)\s+(\d+%)'
    grade_matches = re.findall(grade_pattern, text)

    for match in grade_matches:
        grade_breakdown[match[0]] = match[1]

    return grade_breakdown

# Function to format output in Markdown
def format_to_markdown(professor_info, grade_breakdown):
    markdown_output = ""

    # Professor Contact Information
    markdown_output += "### Professor Contact Information:\n"
    if 'Name' in professor_info:
        markdown_output += f"- **Name**: {professor_info['Name']}\n"
    if 'Email' in professor_info:
        markdown_output += f"- **Email**: {professor_info['Email']}\n"

    # Grade Breakdown
    markdown_output += "\n### Grade Breakdown:\n"
    for category, percentage in grade_breakdown.items():
        markdown_output += f"- **{category}**: {percentage}\n"

    return markdown_output

# Main script
fname = input("Enter File Directory: ")
if len(fname) < 1 : fname = 'test.pdf'

pdf_file = open(fname, 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Initialize a string to store the extracted text
extracted_text = ""

# Extract text from each page
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]    
    extracted_text += page.extract_text()

pdf_file.close()

# Extract information
professor_info = extract_professor_info(extracted_text)
grade_breakdown = extract_grade_breakdown(extracted_text)

# Generate Markdown output
markdown_output = format_to_markdown(professor_info, grade_breakdown)

# Define the output directory
output_directory = "/Users/brandon/downloads"

# Ensure the output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Save the Markdown output to a file in the specified directory
output_file_path = os.path.join(output_directory, "syllabus_summary.md")
with open(output_file_path, "w") as md_file:
    md_file.write(markdown_output)

print(f"Markdown summary saved to: {output_file_path}")
