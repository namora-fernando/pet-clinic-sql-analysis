# Pet Clinic SQL Analysis 🐾

This project explores a simulated pet clinic database using SQLite and Python.

We created mock datasets for pet owners and their pets, then queried them using SQL inside a Jupyter Notebook. Finally, we visualized some of the insights with seaborn.

## 📁 Project Structure

- `create_dummy_pet_database.ipynb` — Generates CSVs for pet owners and pets
- `analyze_pet_database_sql_version.ipynb` — Main analysis notebook (with SQL queries + charts)
- `data/owners.csv`, `data/pets.csv` — Simulated source data
- `data/pet_clinic.db` — SQLite database generated from the CSVs
- `analyze_pet_database_sql_version.html` — Exported HTML for easy viewing

> 🗂️ Tip: Keep all raw data and DB files inside the `data/` folder for a cleaner repo structure.

## 🔍 Key Highlights

- Run SQL queries on pet & owner data
- Analyze license activity and pet distributions
- Discover quirky stories like Willand’s cats 🐱
- Use pandas + matplotlib/seaborn for visualization

## 🛠️ Tools Used

- Python (pandas, sqlite3)
- SQLite
- Jupyter Notebook
- seaborn & matplotlib

## 💡 Future Ideas

- Time series plot of license activity using `license_date_created`
- Correlation between pet type and license status
- Add dashboard with Streamlit or Tableau for interactive exploration

## 📌 Notes

- This project assumes the notebook is run locally. Make sure `data/` folder exists with required files.
- Output cells are preserved for clarity — do not clear outputs before exporting to HTML or PDF.

This notebook is a static portfolio piece and is not intended to be re-run. All outputs are preserved for clarity.
