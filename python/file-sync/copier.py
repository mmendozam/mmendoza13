from pathlib import Path
import shutil

FROM_DRIVE = 'C:'
TO_DRIVE = 'F:'

errors = []
copied = []

copy_list = []
with open('2copy.txt', 'r', encoding='utf-8') as f:
    copy_list = f.read().splitlines()

counter = 0
total = len(copy_list)
for file in copy_list:
    # file = '/ZWOLF_HOME/_Nanalka/media/images/dfncvnp-d6a7a417-a544-4a1e-9869-f963e5868d8a.jpg'
    source_path = Path(f'{FROM_DRIVE}{file}')
    source_file = str(source_path)
    counter += 1
    
    print(f'[{counter} / {total}]')
    print(f'{FROM_DRIVE} => {TO_DRIVE}')
    print(f'Copying: {file}')
    if not source_path.exists() or not source_path.is_file():
        print(f'Invalid source file: {source_file}')
        errors.append(source_file)
    else:
        try:
            destiny_path = Path(f'{TO_DRIVE}{file}')
            destiny_file = str(destiny_path)
            if not destiny_path.parent.exists():
                print(f'Creating missing folder: {str(destiny_path.parent)}')
                destiny_path.parent.mkdir(parents=True)
            shutil.copy2(source_file, destiny_file)
        except Exception as e:
            print(e)
            errors.append(source_file)
        else:
            copied.append(source_file)
    print('-------------------------')

with open(f'copier.errors.txt', 'w', encoding='utf-8') as out:
    for error in errors:
        out.write(f'{error}\n')

with open(f'copier.copied.txt', 'w', encoding='utf-8') as out:
    for d in copied:
        out.write(f'{d}\n')

print('')
print(f'{len(copied)} files copied')
print(f'{len(errors)} errors')
