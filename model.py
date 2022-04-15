# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
def get_list_states():
    """ Function reads from text file and returns list of every state
    ARGS: None

    Returns:
        return list of all the states in the US
    """
    lst_states = []
    with open("state.txt",'r') as f:
        lines_list = f.readlines()
        for state in lines_list:
            lst_states.append(state.strip())
    print(lst_states)
    return lst_states
            


