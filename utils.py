import re
from datetime import datetime
import pandas as pd

def clean_names(name):
    if pd.isna(name):
        return None
    return name.strip().title()

def validate_email(email):
    if pd.isna(email):
        return False
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))

def validate_age(age):
    try:
        age = int(age)
        return 0 < age < 120
    except:
        return False
    
def parse_date(date_str):
    try:
        return pd.to_datetime(date_str, errors="coerce").date()
    except:
        return None