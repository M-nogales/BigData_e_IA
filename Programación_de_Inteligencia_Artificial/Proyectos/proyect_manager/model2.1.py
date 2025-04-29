import pandas as pd
import io
import ast # To parse the string representation of dictionary


task_df = pd.read_csv("task_categories_copy.csv")
rrhh_df = pd.read_csv("datasets/RRHH.csv")

# --- Initial Exploration ---

print("--- Task Categories Info ---")
task_df.info()
print("\n--- Task Categories Head ---")
print(task_df.head())
# Add display for unique values or duplicates if needed
print("\nUnique Skills Required:")
print(task_df['Skill'].unique())
print("\nTask Description Duplicates:")
# Check for duplicate task descriptions which might need clarification
print(task_df[task_df.duplicated('Task Description', keep=False)])


print("\n\n--- RRHH Info ---")
rrhh_df.info()
print("\n--- RRHH Head ---")
# Display more rows to see variations
print(rrhh_df.head())


# --- Preprocessing: Parse 'technical_abilities' ---

# Function to safely parse the string representation of a dictionary
def parse_tech_abilities(abilities_str):
    """Safely parses a string literal representing a dictionary."""
    if pd.isna(abilities_str): # Handle potential NaN values
        return {}
    try:
        # Using ast.literal_eval is safer than eval() for untrusted input
        evaluated = ast.literal_eval(abilities_str)
        if isinstance(evaluated, dict):
            # Standardize keys to lowercase for consistent matching
            return {str(k).lower(): v for k, v in evaluated.items()}
        else:
            # Handle cases where the string might not evaluate to a dict
            print(f"Warning: Parsed data is not a dictionary for input: {abilities_str[:100]}...") # Log problematic data
            return {}
    except (ValueError, SyntaxError, TypeError) as e:
        # Return an empty dict if parsing fails
        print(f"Warning: Could not parse technical_abilities string: {abilities_str[:100]}... Error: {e}") # Log problematic data
        return {}

# Apply the function to the 'technical_abilities' column
# Make a copy to avoid SettingWithCopyWarning if modifying later
rrhh_df['technical_abilities_dict'] = rrhh_df['technical_abilities'].apply(parse_tech_abilities)

# Check the results of parsing for the first few employees
print("\n\n--- Parsed Technical Abilities (First 5 Employees) ---")
for i in range(min(5, len(rrhh_df))):
    print(f"\nEmployee {rrhh_df.loc[i, 'Employee_ID']}:")
    # Print only first few items if the dict is large
    abilities = rrhh_df.loc[i, 'technical_abilities_dict']
    print(dict(list(abilities.items())[:10]), "...") # Show first 10 skills

# Display basic descriptive statistics for numerical columns in RRHH
print("\n\n--- RRHH Numerical Describe ---")
# Use .round(2) for cleaner output
print(rrhh_df.describe().round(2))

# Display value counts for some categorical columns in RRHH
print("\n\n--- RRHH Categorical Value Counts ---")
print("\nDepartments:\n", rrhh_df['Department'].value_counts())
print("\nJob Titles:\n", rrhh_df['Job_Title'].value_counts())
print("\nEducation Levels:\n", rrhh_df['Education_Level'].value_counts())

# Convert 'Hire_Date' to datetime objects if not already done by read_csv
# It's good practice to explicitly convert date columns
rrhh_df['Hire_Date'] = pd.to_datetime(rrhh_df['Hire_Date'])
print("\n\n--- RRHH Info After Date Conversion ---")
rrhh_df.info() # Verify Hire_Date is datetime