from jsonschema import validate, Draft7Validator
from itertools import islice


request_json = { "done" :True, "id" : 1, "description" : "i"}

update_task = Draft7Validator({ "type" : "object",
            "properties" : {
            "id": {
                "type": "integer",
                "description": "Id of the task to be modified",
            },
            "description": {
                "type": "string",
                "description": "Description of the task to be modified",
                "minLength": 3,
                "maxLength": 64,
            },
            "done": {
                "type": "boolean",
                "description": "Current statuts of the task",
            },
            "title": {
                "type": "string",
                "description": "Title of the task to be modified",
                "minLength": 3,
                "maxLength": 256,
            },},
            
       
        "required": ["id", "done"],
    })

def iterate_properties_updatetask(request_json: dict,):
    """
    Returns a small selection of the errors encountered, or an empty list if no errors encountered
    """

    errors = []
    
    errors += islice(
        update_task.iter_errors(request_json), 3
    )
    return errors

pitu= iterate_properties_updatetask(request_json)
print(pitu[0])