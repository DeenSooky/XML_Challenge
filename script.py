from lxml import etree  # For parsing and validating XML data
import sys  # For command line arguments
import os  # For path manipulations

# Custom resolver class to manage schema locations
class SchemaResolver(etree.Resolver):
    def __init__(self, schema_folder):
        self.schema_folder = schema_folder

    def resolve(self, url, public_id, context):
        # If the URL is for the CommonTypes schema, adjust the path to the local schema folder
        if 'CommonTypes-Schema.xsd' in url:
            # Constructing the full path for CommonTypes-Schema.xsd within schema_folder
            url = os.path.join(self.schema_folder, "CommonTypes-Schema.xsd")
            
        # Return the resolved filename
        return self.resolve_filename(url, context)

def validate_xml(schema_folder, xml_path):
    # Defining schema file paths based on the schema_folder provided
    fsa_schema_file = os.path.join(schema_folder, "FSA029-Schema.xsd")
    commonTypes_file = os.path.join(schema_folder, "CommonTypes-Schema.xsd")

    # Initializing the custom resolver to help the parser locate schema files
    resolver = SchemaResolver(schema_folder)

    try:
        # Creating XML parser that can resolve schemas
        parser = etree.XMLParser(resolve_entities=True)
        parser.resolvers.add(resolver)

        # Loading and parsing the CommonTypes schema for validation setup
        commonTypes_doc = etree.parse(commonTypes_file, parser)
        commonTypes_schema = etree.XMLSchema(commonTypes_doc)

        # Loading and parsing the FSA029 schema for validation setup
        fsa_schema_doc = etree.parse(fsa_schema_file, parser)
        fsa_schema = etree.XMLSchema(fsa_schema_doc)

        # Loading the XML file to validate it against the FSA029 schema
        with open(xml_path, "rb") as xml_file:
            doc = etree.parse(xml_file, parser)

            # Validating the parsed XML document against the FSA029 schema
            fsa_schema.assertValid(doc)
            print("XML is valid according to the FSA029 schema.")
            
    except etree.DocumentInvalid as error:
        print("XML validation failed:", error, "within your sample data")  # Specific error for schema validation failure
    except Exception as error:
        print("An error occurred:", error)  # General error for execution or unexpected errros

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Invalid arguments.")
        print("To run this script, provide:")
        print("1. The path to the folder containing the FSA029 and CommonTypes schemas.")
        print("2. The path to the XML file you want to validate.")
        print("\nFor example:")
        print("python script.py <schema_folder_path> <xml_data_path>")
    else:
        print("Starting the XML validation script...")
        # Get the schema folder and XML path from command-line arguments
        schema_folder = sys.argv[1]
        xml_path = sys.argv[2]
        
        # Run the validate_xml function
        validate_xml(schema_folder, xml_path)
