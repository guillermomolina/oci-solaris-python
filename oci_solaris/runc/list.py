# Copyright 2020, Guillermo Adrián Molina
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import subprocess
import json
import glob
import argparse

from oci_api.util.print import print_table

class List:
    @staticmethod
    def init_parser(parent_parser):
        parser = parent_parser.add_parser('list',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            description='Lists containers started by runc with the given root.',
            help='lists containers started by runc with the given root')
        parser.add_argument('--format', 
            help='set the output format',
            choices=['table', 'json'],
            default='table')
        parser.add_argument('--quiet', '-q',
            help='display only container IDs', 
            action='store_true')

    def __init__(self, options):
        state_list = []
        for state_file in glob.iglob(options.root + '/state/*.state'):
            with open(state_file,encoding='utf-8') as json_file:
                state_json = json.load(json_file)
                state_list.append(state_json)

        if options.format == 'json':
            print(json.dumps(state_list))
        else:
            print_table(state_list)
