import os
from google.genai import types


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Validates the file & directory, creating directories if needed, and writes input to the file in question",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file that is to be written",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content which shall be written to the file"
            )
        },
        required=["file_path", "content"]
    )
)


def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        absolute_working_dir = os.path.abspath(working_directory)
        absolute_file_path = os.path.normpath(os.path.join(absolute_working_dir, file_path))
        valid_target_dir = os.path.commonpath([absolute_working_dir, absolute_file_path]) == absolute_working_dir

        if not valid_target_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if os.path.isdir(absolute_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        os.makedirs(os.path.dirname(absolute_file_path), exist_ok=True)

        with open(absolute_file_path, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"