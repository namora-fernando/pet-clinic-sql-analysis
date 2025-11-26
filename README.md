# Pet Clinic SQL Analysis 🐾

This project explores a simulated pet clinic database using SQLite and Python.

The mock datasets created for pet owners and their pets, then queried using SQL inside a Jupyter Notebook. After that, the data visualized with seaborn for some of insights.

## 📁 Project Structure

- `create_dummy_pet_database.ipynb` — Generates CSVs for mock datasets of pet owners and pets
- `analyze_pet_database_sql_version.ipynb` — Main analysis notebook (with SQL queries + charts)
- `data/owners.csv`, `data/pets.csv` — Simulated source data (created from before)
- `data/pet_clinic.db` — SQLite database generated from the CSVs

## Key Highlights

- Run SQL queries on pet & owner data
- Analyze license activity and pet distributions
- Discover quirky stories like Willand’s cats 🐱
- Use pandas + matplotlib/seaborn for visualization

## 🛠️ Tools Used

- Python (pandas, sqlite3, seaborn, matplotlib)
- SQLite
- Jupyter Notebook

## 💡 Future Ideas

- Bigger dataset for more related with real life scenario
- Time series plot of license activity using `license_date_created`
- Correlation between pet type and license status
- Add dashboard with Streamlit or Tableau for interactive exploration

## 📌 Notes

- This project assumes the notebook is run locally. Make sure `data/` folder exists with required files.
- Output cells are preserved for clarity

This notebook is a static portfolio piece and is not intended to be re-run. All outputs are preserved for clarity.
