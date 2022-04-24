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

def is_valid_description(description):
    """ Funcition whill check if descroption is valid
    Args: str

    Returns
        Returns true if description is valid False if not valid
    """
    check_str = description
    return check_str.strip() != ""

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

def is_empty(characters):
    '''
    Function checks if the input field is empty or not.
    ARGS: Characters that user will enter in the input field.

    Returns: Boolean --> True if empty, otherwise False.
    '''
    if not characters:
        return True
    return False
            
def check_password_length(password):
    '''
    Checks if the password is at least 6 characters long.
    ARGS: password

    Returns: Boolean --> True if lenght is less than 6, otherwise False.
    '''
    if type(password) != str:
        raise TypeError("Password must be a string")

    if len(password) < 6:
        return True 
    return False
            
def check_password_validation(password):
    '''
    Checks if the password has alphanumeric characters and a symbol.
    ARGS: password

    Returns: Boolean --> True if password has alphanumeric characters, one uppercase
    , one lowercase, and at least a symbol, otherwise False.
    '''
    if type(password) != str:
        raise TypeError("Password must be a string")
    if len(password) < 6:
        raise ValueError("Password's length must be at least 6 characters.")

    frequncy = {"uppercase":0, "lowercase":0, "number":0, "symbol":0}

    for character in password:
        # checking if number
        if character.isdigit():
            frequncy["number"] += 1
        # checking if uppercase character
        elif character.isupper():
            frequncy["uppercase"] += 1
        # checking if lowercase character
        elif character.islower():
            frequncy["lowercase"] += 1
        # checking if symbol
        elif character in {'!', '@', '#', '%', '^', '&', '*'}:
            frequncy["symbol"] += 1
    
    for val in frequncy.values():
        # if any one of the condition is not satisfied, password is not validated
        if val == 0:
            return True
    # password is validated 
    return False


