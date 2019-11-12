from src.performanceData import SeleniumDataGathering, CronTab

from argparse import ArgumentParser

def main()

    print(colored("""\
         _  _ _    ___    ___      _          _              ___         _           _     _   
        | \| | |  |   \  / __| ___| |___ _ _ (_)_  _ _ __   | __|_ _  __| |_ __  ___(_)_ _| |_ 
        | .` | |__| |) | \__ \/ -_) / -_) ' \| | || | '  \  | _|| ' \/ _` | '_ \/ _ \ | ' \  _|
        |_|\_|____|___/  |___/\___|_\___|_||_|_|\_,_|_|_|_| |___|_||_\__,_| .__/\___/_|_||_\__|
                                                                        |_|               
        """, 'blue'))
    parser = ArgumentParser(description='Run Selenium to push data to AWS ES', usage='python ' + argv[0] + ' --verbose=yes --add_cron_job=yes')
    parser.add_argument('--add_cron_job', default='no', help='Use cronjob for streaming data, use \'yes\' or \'no\' (default: no)')
    parser.add_argument('--verbose', default='no', help='View the script opening chrome, use \'yes\' or \'no\' (default: no)')

    if len(argv) < 2:
        print(parser.print_help())
    else :
        args = parser.parse_args()
        while True:
            SeleniumDataGathering(args.verbose)
        if args.add_cron_job == 'yes':
            Crontab()

if __name__ == "__main__":
    main()