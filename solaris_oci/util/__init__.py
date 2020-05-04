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


import secrets

def generate_random_sha256():
    return secrets.token_hex(nbytes=32)

def generate_random_id():
    return secrets.token_hex(nbytes=8)

def digest_to_id(digest):
    return digest.split(':')[1]

def id_to_digest(id):
    return 'sha256:' + id 
