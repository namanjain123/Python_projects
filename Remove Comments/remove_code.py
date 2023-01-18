# Import the file to delete the code
import json
import re
address=input("please enter the address of the code")
if(address.__contains__(".json")):
    with open('{address}', 'r') as handle:
        handle = str(handle)
        fixed_json = ''.join(line for line in handle if not line.startswith('//'))
        employee_data = json.loads(fixed_json)
        print(employee_data)
if address.__contains__(".py"):
    with open('{address}', 'r') as handle:
        code = str(handle)
        print(re.sub(r'(?m)^ *#.*\n?', '', code))
if address.__contains__(".cs"):
    with open('{address}', 'r') as handle:
        handle = str(handle)
        pattern = r'//.*'
        # remove single-line comments
        handle = re.sub(pattern, '', handle)
        # regular expression pattern to match multi-line comments
        pattern = r'/\*.*?\*/'
        # remove multi-line comments
        handle = re.sub(pattern, '', handle, flags=re.DOTALL)
        print(handle)
if address.__contains__(".cpp"):
    with open('{address}', 'r') as handle:
        handle = str(handle)
        handle=re.sub(r"(?://.*)|(/\*(.|\n)*?\*/)", "", handle)
        print(handle)

    

