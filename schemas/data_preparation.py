import json
from jsonschema import validate


class ValidationJsonSchemas:
    @staticmethod
    def open_json_schema(data, schema_file):
        with open(schema_file) as f:
            read_json_schema = json.load(f)
        return validate(instance=data, schema=read_json_schema)

    @staticmethod
    def checking_json_schema(url):
        ValidationJsonSchemas.open_json_schema(url.json(), 'schemas/schema.json')

    @staticmethod
    def checking_json_schema_array(url):
        ValidationJsonSchemas.open_json_schema(url.json(), 'schemas/schema_array.json')
