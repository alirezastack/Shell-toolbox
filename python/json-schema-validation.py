# install jsonschema with pip
# schema is used to check whether provided data is valid or not
schema = {
	"type": "object",
	"properties": {
	    	"number": {
	    		"type": "string"
		},
		"expire_date": {
			"type": "string"
		},
		"owner_id": {
                        "type": "string"
		},
		"user": {
                        "type": "object",
		}
	},
	"required": [
		"number",
		"expire_date",
		"owner_id",
		"user"
	]
}
jsonschema.validate(json_input_data, schema)
