import os

def get_files_info(working_directory, directory="."):

    try:
        absolute_working_dir = os.path.abspath(working_directory)
        absolute_file_path = os.path.normpath(os.path.join(absolute_working_dir, directory))
        valid_target_dir = os.path.commonpath([absolute_working_dir, absolute_file_path]) == absolute_working_dir

        if not os.path.isdir(absolute_file_path):
            return f'Error: "{directory}" is not a directory'
        
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'


        dir_list = os.listdir(absolute_file_path)
        item_list = []

        for item in dir_list:
            path = os.path.join(absolute_file_path, item)
            file_size = os.path.getsize(path)
            is_dir = os.path.isdir(path)
            item_list.append(f"- {item}: file_size={file_size} bytes, is_dir={is_dir}")
        
        return "\n".join(item_list)   


    except Exception as e:
        return f"Error: {e}"


    
        