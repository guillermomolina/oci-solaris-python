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
import argparse

class Kill:
    @staticmethod
    def init_parser(parent_parser, command_parser):
        parser = command_parser.add_parser('kill',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            description='''The kill command sends the specified signal (default:
                SIGTERM) to the container's init process''',
            help='sends the specified signal to the container\'s init process')
        parser.add_argument('-a', '--all',
            help='send the specified signal to all processes inside the container', 
            action='store_true')
        parser.add_argument('container_id',
            help='name for the instance of the container')
        parser.add_argument('signal',
            help='the signal to be sent to the init process',
            nargs='?',
            default='SIGTERM')

    def __init__(self, options):
        signals = {
            'SIGHUP': '1',
            'SIGINT': '2',
            'SIGQUIT': '3',
            'SIGILL': '4',
            'SIGTRAP': '5',
            'SIGIOT': '6',
            'SIGABRT': '6',
            'SIGEMT': '7',
            'SIGFPE': '8',
            'SIGKILL': '9',
            'SIGBUS': '10',
            'SIGSEGV': '11',
            'SIGSYS': '12',
            'SIGPIPE': '13',
            'SIGALRM': '14',
            'SIGTERM': '15',
            'SIGUSR1': '16',
            'SIGUSR2': '17',
            'SIGCLD': '18',
            'SIGCHLD': '18',
            'SIGPWR': '19',
            'SIGWINCH': '20',
            'SIGURG': '21',
            'SIGPOLL': '22',
            'SIGIO': '22',
            'SIGSTOP': '23',
            'SIGTSTP': '24',
            'SIGCONT': '25',
            'SIGTTIN': '26',
            'SIGTTOU': '27',
            'SIGVTALRM': '28',
            'SIGPROF': '29',
            'SIGXCPU': '30',
            'SIGXFSZ': '31',
            'SIGWAITING': '32',
            'SIGAIOCANCEL': '33',
            'SIGLWP': '33',
            'SIGFREEZE': '34',
            'SIGTHAW': '35',
            'SIGCANCEL': '36',
            'SIGLOST': '37',
            'SIGXRES': '38',
            'SIGJVM1': '39',
            'SIGJVM2': '40'
        }

        signal = options.signal
        if signal in signals:
            signal = signals[signal]
        cmd = [options.runz, 'kill', options.container_id, signal]
        if options.debug:
            print('running: ' + ' '.join(cmd))
        p = subprocess.run(cmd)
        exit(p.returncode)
