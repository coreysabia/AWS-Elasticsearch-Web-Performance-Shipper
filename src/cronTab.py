from crontab import CronTab
import os
from termcolor import colored

class Crontab(object):


    def __init__(self):

        self.cron = CronTab()
        self.cmd = 'cd ' + os.path.realpath('') + ' && ' + 'python main/' + os.path.basename(__file__) + ' --verbose=no'

        if self.does_not_exist() is not True:
            self.add_job()

    def add_job(self):

        self.job = self.cron.new(
            command=self.cmd, 
            comment='This cron job pushes webpage performance data to the AWS ES Endpoint every 5 minutes'
            )
        self.job.setall('*/2', '*', '*', '*', '*')          # every 2 minutes

        self.cron.write_to_user(user=True)
        print(colored('***Added the cron job to your crontab***', 'red'))

    def does_not_exist(self):

        for job in self.cron.commands:
            if job == self.cmd:
                return True