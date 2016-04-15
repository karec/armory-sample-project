import random
import time

import requests

from oct_turrets.base import BaseTransaction
from oct_turrets.tools import CustomTimer


class Transaction(BaseTransaction):
    def __init__(self, config):
        super(Transaction, self).__init__(config)
        self.base_url = config['base_url']

    def run(self):
        r = random.uniform(1, 2)
        with CustomTimer(self, 'a timer'):
            requests.get(self.base_url)
        time.sleep(r)


if __name__ == '__main__':
    trans = Transaction(None)
    trans.run()
    print(trans.custom_timers)
