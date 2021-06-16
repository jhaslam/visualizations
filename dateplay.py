from datetime import datetime

datestr: str = "2021-06-15"
mydate: datetime = datetime.strptime(datestr, "%Y-%m-%d")
print(mydate)