import yfinance as yf
import os


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

    print("---------- COMPLETED SOURCING REQUIRED DATA ----------")
