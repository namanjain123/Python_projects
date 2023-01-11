# Import the file to delete the code
import json
address=input("please enter the address of the code")
if(address.__contains__(".json")):
    with open('{address}', 'r') as handle:
        fixed_json = ''.join(line for line in handle if not line.startswith('//'))
        employee_data = json.loads(fixed_json)
    print(employee_data)