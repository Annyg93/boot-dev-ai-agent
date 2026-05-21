import os
from agent.config import MAX_CHARS


def get_file_content(working_directory, file_path):

    try:
        absolute_working_dir = os.path.abspath(working_directory)
        absolute_file_path = os.path.normpath(os.path.join(absolute_working_dir, file_path))
        valid_target_dir = os.path.commonpath([absolute_working_dir, absolute_file_path]) == absolute_working_dir

        if not os.path.isfile(absolute_file_path):
            return f'Error: File not found or it is not a regular file: "{file_path}"'
        
        if not valid_target_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        

        with open(absolute_file_path, "r") as f:
            content = f.read(MAX_CHARS)

            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return content

    except Exception as e:
        return f"Error: {e}"