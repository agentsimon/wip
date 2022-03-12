import time
import data_collect
import display_conf


if __name__ == '__main__':
    # service.py executed as script
    # do something

    data = data_collect.get_data()
    display_conf.data2_display(data, hour_req=0)
