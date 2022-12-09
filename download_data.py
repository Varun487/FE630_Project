import yfinance as yf
import os
import requests

def get_data(asset_list, start_date, end_date):
    # Create DATA folder if it doesn't exist
    if 'DATA' not in os.listdir():
        os.mkdir('./DATA')
        print("Created 'DATA' directory.")

    # Source and store data in the 'DATA' directory if it doesn't exist
    for asset in asset_list:
        if f"{asset}.csv" not in os.listdir("./DATA"):
            print(f"Sourcing data for {asset}")
            asset_data = yf.download(asset, start=start_date, end=end_date)
            asset_data.to_csv(f"./DATA/{asset}.csv")

    # Get french fama data
    french_fama_data = requests.get(
        "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip"
    )
    # url = r'https://linktofile'
    output = r'./DATA/FFDATA.zip'

    r = requests.get(french_fama_data)
    with open(output, 'wb') as f:
        f.write(r.content)

    print("---------- COMPLETED SOURCING REQUIRED DATA ----------")
