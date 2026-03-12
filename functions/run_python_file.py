import os
import subprocess

from google.genai import types


def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        file_path_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))

        is_valid_file_path = (
            os.path.commonpath([working_dir_abs, file_path_abs]) == working_dir_abs
        )
        if not is_valid_file_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(file_path_abs):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", file_path_abs]
        if args is not None:
            command.extend(args)
        result = subprocess.run(
            command, cwd=working_dir_abs, capture_output=True, text=True, timeout=30
        )

        output = ""
        if result.returncode != 0:
            output += f"Process exited with code {result.returncode}"
        if result.stdout == "" and result.stderr == "":
            output += "No output produced"
        if result.stdout != "":
            output += f"STDOUT: {result.stdout}"
        if result.stderr != "":
            output += f"STDERR: {result.stderr}"
        return output

    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute a python file specified by a file_path relative to the working directory. Returns the STDOUT and/or STDERR of the process or any error message that was raised",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path of the file to execute, relative to the working directory. Has to be a .py file",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="List of STRING arguments that will be added to the call of the python file",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
        required=["file_path"],
    ),
)
