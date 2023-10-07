#JSON Operator to take multiple input paths

import json

class JSONOperator:
    def __init__(self, json_string):
        self.json_data = json.loads(json_string)

    def extract_values(self, paths):
        results = []
        for path in paths:
            result = self.extract_value(path)
            results.append(result)
        return results

    def extract_value(self, path):
        # Implement your logic to extract the value at the given path
        # This can be done using recursive traversal of the JSON data
        # and handling nested keys or indices as needed.
        # For simplicity, here's a basic example assuming a flat structure:
        keys = path.split('.')
        current_data = self.json_data
        for key in keys:
            if key in current_data:
                current_data = current_data[key]
            else:
                return None  # Path not found
        return current_data

# Example usage:
json_string = '{"name": "John", "age": 30, "address": {"city": "New York", "zipcode": "10001"}}'
json_operator = JSONOperator(json_string)
paths = ["name", "address.city"]
values = json_operator.extract_values(paths)
print(values)  # Output: ['John', 'New York']
