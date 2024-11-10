# XML Validation Project: FSA029 Schema

## Project Overview

This Python script validates XML files against the Bank of England's FSA029 Balance Sheet schema. It uses the `lxml` library for XML parsing and schema validation, the built-in python `os` and `sys` libraries for inputs and path manipulations respectively. The script is designed to check whether an XML submission complies with the FSA029 schema, which is essential for regulatory submissions in the financial industry.

## Requirements

- Python 3.x
- `lxml` library for XML parsing and schema validation

To install the required dependencies, use the following command:

- pip install -r requirements.txt

## Setup Instructions

1. Clone this repository or download the Projects folder.
   For cloning use the repository below:

   - https://github.com/DeenSooky/XML_Challenge.git

2. Navigate to the project directory, for example:

   - cd Folder1\Folder2\Projects\project_root

3. Create and activate a virtual environment:

   - python -m venv .venv
   - .venv\Scripts\activate # On Windows

4. Install the dependencies:
   - pip install -r requirements.txt

## How to Run the Script

- The script takes two arguments:

  - The path to the folder containing the FSA029 and CommonTypes schemas.
  - The path to the XML file you want to validate.

  Template example:

  - python script.py <schema_folder_path> <xml_data_path>

  Specific example:

  - python script.py Folder1\Folder2\Projects\project_root\schemas Folder1\Folder2\Projects\project_root\data\FSA029-v4-Samples\FSA029-Sample-Full.xml

## Code Explanation

- **SchemaResolver Class**: Handles dynamic schema paths, specifically resolving paths for CommonTypes-Schema.xsd.
- **validate_xml Function**: Validates an XML file against specified schemas, with distinct handling for validation vs. execution errors.
- **Command-Line Interface**: Accepts arguments for schema and XML file paths.

## Outputs

- **Valid data** should show "XML is valid according to the FSA029 schema"
- **Invalid data** should show "XML validation failed: {error message} within your sample data"
- **Excuction or general erros** should show "An error occurred: {error message}"

## Reflections

- **(a) What causes FSA029-Sample-Full.xml to fail schema validation? Why do you think the regulator has included a valid file in their examples?**

  - The failure of `FSA029-Sample-Full.xml` during schema validation is due to the presence of an unexpected element: PartnershipsSoleTraders. The error message indicates that this element is not expected at line 102 in the XML file.
    The issue arises because the XML file contains an element that does not conform to the structure or constraints defined in the schemas. In this case, it seems that the PartnershipsSoleTraders element in the `FSA029-Sample-Full.xml` does not conform to the structure of the schema's.
    The regulator likely includes a valid file in their examples to serve as a reference for developers and users, showing the expected format and structure that the XML data should adhere to.

- **(b) How would you fix the file to pass the schema validation?**

  - To fix the file, you would need to correct the data structure according to the schema’s requirements. In this case you would need to remove the PartnershipsSoleTraders element since the schemas don't expect this element.

- **(c) Why do you think the regulator includes an invalid file in their examples?**
  - The regulator includes invalid files to help developers understand common errors and test error handling.
