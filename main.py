from Utils.download_data import get_data

asset_list = [
    "FXE",
    "EWJ",
    "GLD",
    "QQQ",
    "SPY",
    "SHV",
    "DBA",
    "USO",
    "XBI",
    "ILF",
    "EPP",
    "FEZ"
]
start_date = "2007-03-01"
end_date = "2022-10-31"

if __name__ == "__main__":
    get_data(asset_list, start_date, end_date)
