# AI + Blockchain Financial Statement Verification

## Description
This project detects anomalies in financial statements using AI/ML and stores verified results on a blockchain for audit-proof tracking.

## Features
- AI-powered anomaly detection (IsolationForest)
- Verification of financial ratios (Profit Margin, Revenue, etc.)
- Blockchain logging of document hashes and verification status
- Streamlit UI for uploading statements and visualizing results

## Folder Structure
- `data/` → Sample financial statements
- `ai_verification/` → AI/ML logic
- `blockchain/` → Blockchain implementation
- `app.py` → Main integration and UI
- `requirements.txt` → Dependencies

## Run Project
1. Install dependencies: `pip install -r requirements.txt`
2. Run Streamlit: `streamlit run app.py`
3. Upload a CSV file to see AI verification & blockchain ledger
