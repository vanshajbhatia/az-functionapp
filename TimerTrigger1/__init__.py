import datetime
import logging
import time

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')
        
    print("Printed immediately.")
    time.sleep(300)
    print("Printed after 2.4 seconds.")

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
