# 💻 Data Integrity & Deployment Audit Tool

### Project Overview
One thing that's become clear is AI deployments don't fail because of the AI itself, but rather there's an issue where companies have messy data which means they're going to have messy outputs.

I created a tool that would help serve as an 'Audit Layer' between raw warehouse data and a system's ability to properly ingest and use the data.

What I created will identify critical data blockers, standardize messy inputs, and generate a human-readable conflict report for stakeholder resolution so it's obvious what manual intervention needs to take place. 

After all, Garbage In, Garbage Out. 

---

🚀 Key Features
* **Automated Data Standardization:** Converts mixed-type strings (for ex: "TBD", "Out of Stock") into machine-readable numeric formats using `coercion` logic.
* **Duplicate ID Detection:** Identifies repeated `item_id` entries and isolates them into a "Conflict Report" to prevent data overwriting and confusion.
* * **Schema Consistency:** Normalizes date formatting to ensure that quantitative fields (ex: Price/Quantity) are calculation-ready.
* **Health Score Visualization:** Generates a visual summary of data quality issues to provide immediate feedback on "AI Readiness."

---

### 📊 The Workflow
The workflow consists of 3 main parts: 
1.  **Auditing:** The script scans a raw CSV that one might want to utilize for AI injestion. I created a test dataset with 5000+ rows. My script looks for missing IDs, duplicate ID's, non-numeric values across a variety of columns, and dates with varied formats.
2.  **Cleaning:** Non numeric values are generally set to NaN, date formats are standardized, and duplicate item_id's are identified. 
3.  **Artifact Generation:**
The script is able to handle issues with formatting and NaN values. However, we are unable to know how to handle duplicate item_id's with varied values across other columns. This requires manual intervention. I created two artifacts with this in mind:

    * `cleaned_inventory_v1.csv`: The sanitized data ready for upload. This essentially improves the current data by cleaning the original upload. 
    * `action_required_duplicates.csv`: These are still the item_id duplicates requiring human decision-making.

---

### 🛠️ Tech Stack
* **Language:** Python 3
* **Libraries:** `pandas` (Data Manipulation), `matplotlib` (Visualization)
* **Environment:** Developed for high-scale deployment scenarios (Stress-tested with 5,000+ rows).

---

### 📈 Sample Output
The tool provides an "AI Readiness Report" in the terminal:
- Missing IDs: __
- Duplicate IDs: __
- Non-Numeric Prices: __
- CSV download with the duplicates that need investigating for further review
- Result of the audit: Pass or Fail

### 📈 Executive Snapshot of Issues
I was able to create a quick bar chart which shows the issues. This helps management see where certain reports may be lacking along with how AI readiness trends over time. 
<img width="591" height="454" alt="Screenshot 2026-03-01 at 11 48 02 AM" src="https://github.com/user-attachments/assets/30fbaf19-2bd8-43c4-ad88-5ddab85f9675" />
