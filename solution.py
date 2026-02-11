import pandas as pd

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:

    """
    Function that create a new DataFrame that includes the original data along 
    with an additional column calculated based on specified operations.
    """
    
    df_result = df.copy()

    #Validation to check column labels consist only of letters and underscore
    all_columns = list(df.columns) + [new_column]

    for col in all_columns:
        for char in col:
            if not (char.isalpha() or char == '_'):
                return pd.DataFrame()

    #Validation to check that function supports provided operations

    available_roles = ["+","-","*"]

    if not any(op in role for op in available_roles):
        return pd.DataFrame()

    #Calculations 

    try:
        df_result[new_column] = df_result.eval(role)
        return df_result
    except Exception:
        return pd.DataFrame()