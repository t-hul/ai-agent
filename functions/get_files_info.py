import os


def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        is_valid_target_dir = (
            os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        )
        if not is_valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        content_str = ""
        dir_items = os.listdir(target_dir)
        for item_name in dir_items:
            item_path = os.path.join(target_dir, item_name)
            size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)

            content_str += f"- {item_name}: file_size={size} bytes, is_dir={is_dir}\n"
        return content_str
    except Exception as e:
        return f"Error: {e}"
