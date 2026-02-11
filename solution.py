import pandas as pd

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:

    """
    Function that create a new DataFrame that includes the original data along 
    with an additional column calculated based on specified operations.
    """
    
    df = df.copy()

    #Validation to check column labels consist only of letters and underscore
    all_columns = list(df.columns) + [new_column]

    for col in all_columns:
        for char in col:
            if not (char.isalpha() or char == '_'):
                return pd.DataFrame()

    #Validation to check that function supports provided operations

    avaiables_roles = ["+","-","*"]


    if any(op in role for op in avaiables_roles):
        try:
            df[new_column] = df.eval(role)
            return df
        except Exception as e:
            print(f"Bad computing: {e}")
            return pd.DataFrame()
    else:
        print("Inncorect operator")
        return pd.DataFrame()
    

#TEST

df_input = pd.DataFrame({'A': [10,20], 'B': [30,40]})

result = add_virtual_column(df_input, "A + B", "C-minor")
print(result)



