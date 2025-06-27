####################################################################################################
#
#  Date Written: 04/12/2023        By: Joseph P. Merten
#  Day 19: WTA Matches - Importing Data
#  https://docs.google.com/document/d/1mUSGXX6UdfvGw5faAru7LuYUHNCt9I0dZLtB5enM5P8/preview#heading=h.rfelkkkw1wcf
#  .gitignore tutorial...
#  https://www.freecodecamp.org/news/gitignore-file-how-to-ignore-files-and-folders-in-git/
#
# Question 1:
# Download the wta_matches_2022.csv file. Read the file into a DataFrame and display the first five rows.
#
# Question 2:
# Download the wta_matches_2022.tsv file. Read the file into a DataFrame and display the first five rows. (Note this is a tab separated file, meaning it uses the tab character as a delimiter.)
#
# Question 3:
# Read the wta_matches_2022.xlsx file into a DataFrame and display the last five rows.
#
# Question 4:
# Read the wta_matches_2022.parquet file into a DataFrame and use the .describe() function to describe the dataset.
#
# Question 5:
# Utilize the %time magic function in Jupyter to measure the imports of the 3 different data files and
# compare the results. Which data file read was fastest?
#
####################################################################################################
#   imports
import pandas as pd


####################################################################################################
#   Variables
csv_path = "./wta_matches_2022/wta_matches_2022.csv"
tsv_path = "./wta_matches_2022/wta_matches_2022.tsv"
xls_path = "./wta_matches_2022/wta_matches_2022.xlsx"
parquet_path = "./wta_matches_2022/wta_matches_2022.parquet"


####################################################################################################
#   Functions
def q1():
   """Download the wta_matches_2022.csv file. Read the file into a DataFrame and
   display the first five rows."""
   df_csv = pd.read_csv(csv_path)
   print(df_csv.head(5))
   return


def q2():
   """Download the wta_matches_2022.tsv file. Read the file into a DataFrame and display the
   first five rows. (Note this is a tab separated file, meaning it uses the tab character as
   a delimiter.)"""
   df_tsv = pd.read_csv(tsv_path, sep="\t")
   print(df_tsv.head(5))
   return

def q3():
   """Read the wta_matches_2022.xlsx file into a DataFrame and display the last five rows."""
   df_xls = pd.read_excel(xls_path)
   print(df_xls.head(5))
   return


def q4():
   """Read the wta_matches_2022.parquet file into a DataFrame and use the .describe()
   function to describe the dataset."""
   df_parquet = pd.read_parquet(parquet_path)
   print(df_parquet.describe())
   return


####################################################################################################
#   Classes


####################################################################################################
#   Lambdas


####################################################################################################
#   Main code
if __name__ == "__main__":
   q1()
   q2()
   q3()
   q4()
