import pandas as pd

# Reading all the files
january = pd.read_csv("./2022_01.csv")
february = pd.read_csv("./2022_02.csv")
march = pd.read_csv("./2022_03.csv")
april = pd.read_csv("./2022_04.csv")
may = pd.read_csv("./2022_05.csv")
june = pd.read_csv("./2022_06.csv")
july = pd.read_csv("./2022_07.csv")
august = pd.read_csv("./2022_08.csv")
september = pd.read_csv("./2022_09.csv")
october = pd.read_csv("./2022_10.csv")
november = pd.read_csv("./2022_11.csv")
december = pd.read_csv("./2022_12.csv")

# Joining all the files together
df = pd.concat([january, february, march, april, may, june, july, august, september, october, november, december])

# Deleting unnecessary columns and deleting all rows that contain invalid values
df.drop(columns=["start_station_id", "start_station_name", "end_station_id", "end_station_name", "start_lat", "start_lng", "end_lat", "end_lng"], inplace=True)
df.dropna(axis=1)

# Converting time data to a suitable format and creating new columns that are gonna be useful in the future
df["started_at"] = pd.to_datetime(df["started_at"])
df["ended_at"] = pd.to_datetime(df["ended_at"])

df.insert(loc = 4, column = "duration", value = df["ended_at"] - df["started_at"])
df = df.loc[(df["duration"] > "0 days 00:01:00") & (df["duration"] < "1 days 00:00:00")]

df.insert(loc = 5, column = "day", value = df["started_at"].dt.weekday)
df["day"] = df["day"].map({0: "monday", 1: "tuesday", 2: "wednesday", 3: "thursday", 4: "friday", 5: "saturday", 6: "sunday"})

df.insert(loc = 6, column = "month", value = df["started_at"].dt.month)
df["month"] = df["month"].map({1: "january", 2: "february", 3: "march", 4: "april", 5: "may", 6: "june", 7: "july", 8: "august", 9: "september", 10: "october", 11: "november", 12: "december"})

df = df.sort_values(by = "started_at")

# Making the index match the amount of rows we have left after all the cleaning
df.reset_index()
