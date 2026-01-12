import re
from datetime import datetime
import pandas as pd

def clean_names(name):
    if pd.isna(name):
        return None
    return name.strip().title()