import pandas as pd
from sklearn.ensemble import IsolationForest
import hashlib

def verify_financial_statement(file_path):
    df = pd.read_csv(file_path)
    
    # Compute ratios
    df['Profit_Margin'] = df['Profit'] / df['Revenue']
    
    # Anomaly detection
    model = IsolationForest(contamination=0.1, random_state=42)
    df['anomaly'] = model.fit_predict(df[['Revenue', 'Expenses', 'Profit', 'Profit_Margin']])
    
    # Assign verification status
    df['Verification_Status'] = df['anomaly'].apply(lambda x: 'Flagged' if x == -1 else 'Valid')
    
    # Generate document hash
    df['Document_Hash'] = df.apply(lambda row: hashlib.sha256(str(row.to_dict()).encode()).hexdigest(), axis=1)
    
    return df
