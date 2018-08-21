#!/usr/bin/env python3

import argparse

from configparser import ConfigParser

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config", help="Specify config file location",
                    default="wttrbot.conf", dest='conf_file')
args, remaining_argv = parser.parse_known_args()
conf_file = args.conf_file
conf = ConfigParser()
conf.read([conf_file])
token = conf.get('oauth', 'bot_token')
