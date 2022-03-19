"""
This module will orchestrate the entire running of the App
The scheduler will operate based on the user input
"""

from datetime import datetime
from sched import scheduler
import time
import os
from apscheduler.schedulers.background import BackgroundScheduler
import data_collect
import display_conf

# Maintains record of the current display state
# 0 = Adverts display, 1 = Current weather display, 2 = forecast display
app_state = 0  # 0 = Adverts display
fetch_active = 0
current_weather_active = 0
forecast_active = 0
data = data_collect.get_data()

# Add global variable for the current screen state


def start_conducting():
    # fetch_data()
    # data = data_collect.get_data()
    display_data(0)
    # display_conf.data2_display(data, hour_req=0)


def fetch_data():
    print('Fetching data: %s' % datetime.now())
    fetch_active = 1
    data = data_collect.get_data()
    fetch_active = 0
    # This could be fetch fresh data


def display_data(hour_req):
    print('Displaying data: %s' % datetime.now())
    display_conf.data2_display(data, hour_req)
    # This could be change the screen depending on its current state


def adverts_display():
    print('Displaying adverts: %s' % datetime.now())
    # This could be change the screen depending on its current state


if __name__ == '__main__':
    scheduler_fetch = BackgroundScheduler()
    scheduler_fetch.add_job(fetch_data, 'interval', hours=1)

    scheduler_display = BackgroundScheduler()
    scheduler_display.add_job(display_data(0), 'interval', seconds=20)
    if app_state == 2:  # currently displaying forecast
        app_state = 1   # change the state to displaying Current weather
        # Here, we will display the current Weather
    elif app_state == 1:    # currently displaying current weather
        app_state = 0       # change the state to (IDLE) displaying Adverts
        # here, we will revert to displaying Adverts
    else:
        if scheduler_display.running:
            scheduler_display.shutdown()
            print("Here we are")

    scheduler_adverts = BackgroundScheduler()
    scheduler_adverts.add_job(adverts_display, 'interval', seconds=10)

    fetch_active = 1
    data = data_collect.get_data()
    scheduler_fetch.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
