import streamlit as st
import pandas as pd
from utility import check_password

# Do not continue if check_password is not True.  
if not check_password():  
    st.stop()

# File path
file_path = 'data/ListingofCentres.csv'
file_path_2 = 'data/postalcode.csv'

# Read the CSV file into a DataFrame
childcare_centre = pd.read_csv(file_path)
postal_code =pd.read_csv(file_path_2)

#Transform childcare data
childcare_centre = childcare_centre[childcare_centre['postal_code'] != 0]
childcare_centre['postal_code_format'] = childcare_centre['postal_code'].astype(str).str.zfill(6)
childcare_centre['FirstTwoDigits'] = childcare_centre['postal_code_format'].astype(str).str[:2]

#Transform postal_code data
postal_code['Area'] = postal_code['Area'].str.replace('\xa0', ' ')
postal_code['FirstTwoDigits'] = postal_code['Postal Code'].astype(str).str.zfill(2)

resultdf=childcare_centre.merge(postal_code,on="FirstTwoDigits",how='left')

st.set_page_config(layout="wide")

st.header("Childcare Centre Finder")

st.divider()

st.write("We can provide you the list of childcare centres near your area and their availability slots:)")

input_postcode = st.text_input(
    label = "Please enter your postal code:",
    max_chars=6,
    placeholder = "Postal Code"
)

if len(input_postcode) > 0:
    if len(input_postcode) != 6:
        st.error("Invalid postcode")
    else:
        st.write(f"Your postalcode is {input_postcode}." )
        area = postal_code[postal_code['FirstTwoDigits'] == input_postcode[:2]]['Area'].values[0]
        st.write(f"Your area is {area}")
        st.write(f"Childcare Centre near your area:")
        # Apply filters to the DataFrame
        filtered_df = resultdf[resultdf['FirstTwoDigits'] ==  input_postcode[:2]]
        filtered_df = filtered_df[['centre_name', 'centre_address','government_subsidy','infant_vacancy_current_month','pg_vacancy_current_month','n1_vacancy_current_month','n2_vacancy_current_month','k1_vacancy_current_month','k2_vacancy_current_month']]
        # List of new column names
        new_column_names = ['Centre Name', 'Address', 'Government Subsidy','Infant','PG','N1','N2','K1',"K2" ]
        # Rename all columns
        filtered_df.columns = new_column_names
        st.dataframe(filtered_df,hide_index=True,use_container_width=True)