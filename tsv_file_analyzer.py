
import csv
import os
import sys
import click
import pathlib
import logging
import calendar
import time
import pathlib
from colorama import Fore, Style
from datetime import datetime
from datetime import date

DEFAULT_COLUMNS_ONLY = False

DEFAULT_OUTDIR = "/tmp/" + os.path.basename(__file__) + '/' + str(datetime.today().strftime('%Y-%m-%d-%H%M%S'))

LOGGING_FORMAT = "%(levelname)s : %(asctime)s : %(pathname)s : %(lineno)d : %(message)s"

LOG_LEVEL = logging.INFO


position_to_header_lookup = {}


def display_columns(parts):

    print(Fore.YELLOW + "\nHere are the columns\n")
    print(Style.RESET_ALL + '', end='')

    for i, field in enumerate(parts, 1):
        field = field.replace('"', '')      
        print("{}. ".format(i), end='')  
        print(Fore.BLUE + "{}".format(field))
        print(Style.RESET_ALL + '', end='')


def display_record(parts, rec_ctr, line_ctr):

    print(Fore.YELLOW + "\nHere record number '{}' (at line '{}')".format(rec_ctr, line_ctr))
    print(Style.RESET_ALL + '', end='')

    for i, field in enumerate(parts):
        field = field.replace('"', '')
        header = position_to_header_lookup[i]
        print(Fore.BLUE + "{}:".format(header), end='')
        print(Style.RESET_ALL + '', end='')
        print(" {}".format(field))
        # print("{}: {}".format(header, field))



@click.command()
@click.option('--outdir', help='The default is the current working directory')
@click.option('--infile', help="The tab-delimited file to be analyzed")
@click.option('--logfile', help="The log file")
@click.option('--columns_only', is_flag=True, help="If specified, will only display the column names")
def main(outdir, infile, logfile, columns_only):
    """Analyze a tab-delimited file
    """

    error_ctr = 0

    if infile is None:
        print(Fore.RED + "--infile was not specified")
        print(Style.RESET_ALL + '', end='')
        error_ctr += 1

    if error_ctr > 0:
        sys.exit(1)
    
    assert isinstance(infile, str)

    if outdir is None:
        outdir = DEFAULT_OUTDIR
        print(Fore.YELLOW + "--outdir was not specified and therefore was set to '{}'".format(outdir))
        print(Style.RESET_ALL + '', end='')

    assert isinstance(outdir, str)

    if not os.path.exists(outdir):
        pathlib.Path(outdir).mkdir(parents=True, exist_ok=True)
        print(Fore.YELLOW + "Created output directory '{}'".format(outdir))
        print(Style.RESET_ALL + '', end='')

    if logfile is None:
        logfile = outdir + '/' + os.path.basename(__file__) + '.log'
        print(Fore.YELLOW + "--logfile was not specified and therefore was set to '{}'".format(logfile))
        print(Style.RESET_ALL + '', end='')

    assert isinstance(logfile, str)

    if columns_only is None:
        columns_only = DEFAULT_COLUMNS_ONLY
        print(Fore.YELLOW + "--columns_only was not specified and therefore was set to '{}'".format(columns_only))
        print(Style.RESET_ALL + '', end='')

    logging.basicConfig(filename=logfile, format=LOGGING_FORMAT, level=LOG_LEVEL)

    global position_to_header_lookup

    with open(infile, 'r') as f:
        line_ctr = 0
        rec_ctr = 0
        position_to_header_lookup = {}
        for line in f:
            line_ctr += 1
            parts = line.split("\t")
            if line_ctr == 1:
                for i, header in enumerate(parts):
                    header = header.replace('"', '')
                    position_to_header_lookup[i] = header.strip()
                if columns_only:
                    display_columns(parts)
                    break
                continue
            else:
                rec_ctr += 1
                
                if rec_ctr > 1:
                    yes_or_no = input("Would you like to see the next record? [Y/n] ")
                    if yes_or_no is None or yes_or_no == '' or yes_or_no.lower()  == 'y':
                        pass
                    else:
                        break
                display_record(parts, rec_ctr, line_ctr)


if __name__ == "__main__":
    main()