# 📊 Excel Automation Project

This project automates the process of combining, cleaning, and summarizing Excel data using **Python and Pandas**.  
It reads multiple Excel files from a folder, merges them into one dataset, performs grouping and aggregation, and generates a summary Excel report automatically.

---

## 🚀 Features

- Automatically reads all Excel files from the `/data` folder  
- Combines data into a single DataFrame  
- Groups and summarizes the data (e.g., by Product or Category)  
- Exports the final summary into a clean Excel report  
- Simple and lightweight — great for learning Python automation  

---

## 🛠️ Technologies Used

- **Python 3**
- **Pandas** for data manipulation
- **OpenPyXL / XlsxWriter** for Excel handling

---

## excel_automation/
│
├── data/ # Folder containing input Excel files
├── output/ # Folder where final reports are saved
├── src/
│ └── automate_reports.py # Main Python script
├── venv/ # Virtual environment (optional)
└── README.md


---

## ⚙️ How to Run the Project

1. **Clone this repository:**
   ```bash
   git clone https://github.com/LybahMaryam/excel-automation.git
   cd excel-automation


Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate     # on Windows


Install dependencies:

pip install pandas openpyxl


Add your Excel files inside the data folder.

Run the automation script:

python src/automate_reports.py


The summary Excel file will appear in the output folder ✅

  Example Use Case

Imagine a company receives daily sales reports from different branches.
Instead of combining them manually, this script automatically merges and summarizes all Excel files in seconds — saving hours of manual work.

  Learning Outcome

This project demonstrates:

Data automation using Python

Working with Pandas for Excel processing

File handling and output management

Basic understanding of data grouping and summarization

 Future Improvements

Add a simple GUI using Tkinter or Streamlit

Integrate email alerts when new reports are generated

Support for CSV and Google Sheets

Author

Lybah Maryam
git push origin main📂 Project Structure

# excel-automation
