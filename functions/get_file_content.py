import os

def get_file_content(working_directory, file_path):

    try:
        absolute_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(absolute_path, file_path))
        valid_target_dir = os.path.commonpath([absolute_path, target_dir]) == absolute_path

        if not os.path.isfile(file_path):
            return f'Error: File not found or it is not a regular file: "{file_path}"'
        
        if not valid_target_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        

        





    except Exception as e:
        return f"Error: {e}"