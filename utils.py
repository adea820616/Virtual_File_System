import sys

def check_format(name): 
    if not name.isalnum():
        print(f"Error: The '{name}' contains invalid characters, case-insensitive alpha and numeric only.", file=sys.stderr)
        return False
    else:
        return True