################################################################################
#
#   Date Written: 06/26/2023        By: Joseph P. Merten
#   This script is for the Public Transit Database assignment:
#       https://lms.grandcircus.co/mod/assign/view.php?id=25290
#       https://docs.google.com/document/d/1Vf1kW-RKy-MKlLvyG1cJMT74Oxcgoa9lMVfZQrxBLnI/preview
#
#   These are the two sources for data:
#       https://data.ny.gov/Transportation/MTA-Monthly-Ridership-Traffic-Data-Beginning-Janua/xfre-bxip
#       https://data.cityofchicago.org/Transportation/CTA-Ridership-Daily-Boarding-Totals/6iiy-9s97
#   The actual files URLs are:
#       https://data.ny.gov/resource/xfre-bxip.csv
#       https://data.cityofchicago.org/api/views/6iiy-9s97/rows.csv?accessType=DOWNLOAD
#
#   URLS RE: Exploring data
#       https://realpython.com/pandas-python-explore-dataset/
#       https://realpython.com/pandas-dataframe/
#       https://datagy.io/pandas-exploratory-data-analysis/
#       https://towardsdatascience.com/exploring-the-data-using-python-47c4bc7b8fa2
#
#   colab workbook:
#       https://colab.research.google.com/drive/1OgmVuwqxjZLUDiSlSd-zGkkQPlEuKDDp#scrollTo=Hop_ihjGhmBy
#
# Build Specifications
#   ✓ Successfully able to launch backend server from main.py file (1 Point)
#   ✓ Users can successfully make a GET request to the specified endpoint (1 Point)
#   ✓ Each API call returns a random fact from your list of facts (1 Point)
#   ✓ Name the endpoint something that is representative of its task (1 Point)
#   ✓ List of facts are stored in a text file in your server directory (1 Point)
#   ✓ Correctly reading data from text file into Python (1 Point)
#   ✓ Index query parameter that allows the user to denote the specific fact they want returned by the index location of the fact (2 Points)
#   ✓ Logical naming of variables and endpoints and code legibility (2 Points)
# Extra Challenges:
#   Extend your API with a new endpoint to allow users to add new facts (i.e. /add). The new fact should be appended to the text file storing each fact. (2 Points)
#
################################################################################
#   imports...
import random
import csv
import pandas as pd

################################################################################
#   Source URLs...
ny_url = r"http://data.ny.gov/resource/xfre-bxip.csv"
ch_url = r"http://data.cityofchicago.org/api/views/6iiy-9s97/rows.csv?accessType=DOWNLOAD"
print(ny_url)
print(ch_url)

################################################################################
#   Extract data - return a pandas ddataframe from the specified file...
def extract_data(file_location):
    """This function will return a dataframe from reading the specified file."""
    if file_location.find(".csv"):
        my_df = pd.read_csv(file_location)
    elif file_location.find(".xml"):
        my_df = pd.read_xml(file_location)
    elif file_location.find(".json"):
        my_df = pd.read_json(file_location)
    return my_df

################################################################################
#   Test the function.
df_ny = extract_data(ny_url)
df_ch = extract_data(ch_url)
print(df_ny.head(10))
print(df_ny.describe())
print(df_ch.head(10))
print(df_ch.describe())
print('-'*80)




