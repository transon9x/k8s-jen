import time
from datetime import date

today = date.today()
print("Today's date:", today)
print('-'*10)
print("Start sleep: 20s")
time.sleep(20)
print("Done sleep: 20s")