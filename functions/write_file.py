import os


def write_file(working_directory, file_path, content):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        file_path_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))

        is_valid_file_path = (
            os.path.commonpath([working_dir_abs, file_path_abs]) == working_dir_abs
        )
        if not is_valid_file_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(file_path_abs):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        os.makedirs(os.path.dirname(file_path_abs), exist_ok=True)

        chars_written = 0
        with open(file_path_abs, "w") as f:
            chars_written = f.write(content)

        if chars_written == len(content):
            return f'Successfully wrote to "{file_path}" ({chars_written} characters written)'
        return f'Error: only {chars_written} of {len(content)} characters written to "{file_path}"'

    except Exception as e:
        return f"Error: {e}"
