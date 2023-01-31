
import datetime

def log_data(data , log_file = 'logs/log.txt'):
    date = datetime.datetime.now().strftime('%H:%M:%S  -  %D')
    day = datetime.datetime.now().strftime('%a')
    traped = f'\n[ {date} - {day} ] {data}\n'
    with open(log_file , "a+") as logger:
        logger.write(traped)
