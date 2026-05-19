import os

def get_files_info(working_directory, directory="."):

    try:
        absolute_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(absolute_path, directory))
        valid_target_dir = os.path.commonpath([absolute_path, target_dir]) == absolute_path

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'


        dir_list = os.listdir(target_dir)
        item_list = []

        for item in dir_list:
            path = os.path.join(target_dir, item)
            file_size = os.path.getsize(path)
            is_dir = os.path.isdir(path)
            item_list.append(f"- {item}: file_size={file_size} bytes, is_dir={is_dir}")
        
        return "\n".join(item_list)   


    except Exception as e:
        return f"Error: {e}"


    
        