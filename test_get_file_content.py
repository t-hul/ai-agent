from functions.get_file_content import get_file_content

result = get_file_content("calculator", "lorem.txt")
content, message = result.split("[")
print(f"Length read from 'lorem.txt': {len(content)} characters")
print("Truncation message:")
print(f"[{message}")

result = get_file_content("calculator", "main.py")
print("Content of 'main.py':")
print(result)

result = get_file_content("calculator", "pkg/calculator.py")
print("Content of 'pkg/calculator.py':")
print(result)

result = get_file_content("calculator", "/bin/cat")
print("Content of '/bin/cat':")
print(result)

result = get_file_content("calculator", "pkg/does_not_exist.py")
print("Content of 'pkg/does_not_exist.py':")
print(result)
