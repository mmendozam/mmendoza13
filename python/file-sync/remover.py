from pathlib import Path
import sys

errors = []
deleted = []

delete_list = []
with open('2delete.txt', 'r', encoding='utf-8') as f:
    delete_list = f.read().splitlines()

if not delete_list:
    print('No files to remove.')
    sys.exit(0)

drive = input('Drive (C:, F:, O:) ').upper()

# Confirmation
print(f'About to remove {len(delete_list)} files from drive {drive}')
answer = input('Are you sure? (yes/no) ')
if answer.lower() != 'yes':
    print('Exiting without deleting')
    sys.exit(0)

for file in delete_list:
    path = Path(f'{drive}{file}')
    path_str = str(path)
    
    if not path.exists() or not path.is_file():
        print(f'Invalid file: {path_str}')
        errors.append(path_str)
    else:
        print(f'Deleting: {path_str}')
        try:
            path.unlink()
        except:
            errors.append(path_str)
        else:
            deleted.append(path_str)

with open(f'remover.errors.txt', 'w', encoding='utf-8') as out:
    for error in errors:
        out.write(f'{error}\n')

with open(f'remover.deleted.txt', 'w', encoding='utf-8') as out:
    for d in deleted:
        out.write(f'{d}\n')

print('')
print(f'{len(deleted)} files deleted')
print(f'{len(errors)} errors')
