"""
ApScheduler doens't run from Atom-python-run
Raises module not found.

works fine from command line.
"""


import sys
from time import sleep, gmtime, strftime

from apscheduler.schedulers.background import BackgroundScheduler
scheduler = BackgroundScheduler()
scheduler.start()
from price_scraper import get_price

def my_get_price():
    with open("price_history.txt", mode='a+')  as f:
        f.write(f"Price: \"{get_price()}\" >>> {strftime('%a, %d %b %Y %H:%M:%S', gmtime())}\n")

def main():
    scheduler.add_job(func=my_get_price, trigger='interval', minutes=2)
    print("Job Added")

    # Infinite loop is needed to keep the program alive.
    while True:
        sleep(5)
        sys.stdout.write('.')
        sys.stdout.flush()

if __name__ == '__main__':
    main()
