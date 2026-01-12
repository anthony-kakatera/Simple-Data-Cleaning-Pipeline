import pandas as pd
from utils import clean_names, validate_email, validate_age, parse_date

def run_pipeline(input_path, output_path):
    df = pd.read_csv(input_path)

    print(f"Loaded {len(df)} rows")

    # Remove duplicates
    df = df.drop_duplicates()

    # Clean name column
    df["name"] = df["name"].apply(clean_names)

    # Validate email
    df["email_valid"] = df["email"].apply(validate_email)

    # Validate age
    df["age_valid"] = df["age"].apply(validate_age)

    # Parse signup date
    df["signup_date"] = df["signup_date"].apply(parse_date)

    # Drop invalid rows
    cleaned_df = df[
        (df["email_valid"]) &
        (df["age_valid"]) &
        (df["name"].notna())
    ]

    print(f"Cleaned data has {len(cleaned_df)} rows")

    cleaned_df.to_csv(output_path, index=False)

if __name__ == "__main__":
    run_pipeline("data/raw_data.csv", "data/cleaned_data.csv")