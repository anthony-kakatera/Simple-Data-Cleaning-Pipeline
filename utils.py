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