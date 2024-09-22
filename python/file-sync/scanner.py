import sys
from pathlib import Path


class FileSync:
    def __init__(self, directory: str, name: str, extension: str, size: int) -> None:
        self.directory = directory
        self.name = name
        self.extension = extension.lower()
        self.size = size

    def __str__(self) -> str:
        return f'{self.directory} {self.name} ({self.size})'

    def to_csv(self) -> str:
        return f'"{self.directory}/{self.name}","{self.directory}","{self.name}","{self.extension}","{self.size}"'


FILES: list[FileSync] = []

# IGNORE_DIRECTORIES: list[str] = ['/ZWOLF_HOME/_Nanalka/media/images', '/ZWOLF_HOME/_Nanalka/media/videos/PLAYLISTS', '/ZWOLF_HOME/_Nanalka/dev/dlss', '/ZWOLF_HOME/_Nanalka/media/videos/tokyomotion']
# IGNORE_DIRECTORIES: list[str] = ['/ZWOLF_HOME/_Nanalka', '/ZWOLF_HOME/_Albums']
# IGNORE_DIRECTORIES: list[str] = ['/ZWOLF_HOME/_Nanalka/media/videos/tokyomotion', '/ZWOLF_HOME/_Nanalka/media/videos/afreecatv', '/ZWOLF_HOME/_Nanalka/media/videos/PLAYLISTS']
# IGNORE_DIRECTORIES: list[str] = ['/ZWOLF_HOME/_Nanalka', '/ZWOLF_HOME/_Albums', '/ZWOLF_HOME/tmp']

IGNORE_DIRECTORIES: list[str] = []


def print_usage() -> None:
    print('Usage: python scanner.py "C:\path\to\folder" "label"')


def isExcludeDirectory(directory: str) -> bool:
    for ignore_directory in IGNORE_DIRECTORIES:
        if directory.startswith(ignore_directory):
            return True
    return False


def process_file(path: Path) -> None:
    parent = path.parent
    directory = str(parent.as_posix()).replace(parent.drive, '', 1)
    if isExcludeDirectory(directory):
        return
    file_sync = FileSync(directory, path.name, path.suffix, path.stat().st_size)
    FILES.append(file_sync)


def process_folder(path: Path) -> None:
    directory = str(path.as_posix()).replace(path.drive, '', 1)
    if isExcludeDirectory(directory):
        return
    file_sync = FileSync(directory, '', '<FOLDER>', 0)
    FILES.append(file_sync)


def main(argv: list[str]) -> None:
    if not argv or len(argv) < 2:
        print('Missing parameters :(')
        print_usage()
        return

    path = Path(argv[0])
    label = argv[1]
    
    if not path.exists() or not path.is_dir():
        raise Exception('Invalid path :(')

    folder_counter = 0
    file_counter = 0
    for p in path.rglob('*'):
        if p.is_dir():
            folder_counter += 1
            print(f'  [{folder_counter}] {str(p)}')
            process_folder(p)
        elif p.is_file():
            file_counter += 1
            process_file(p)

    print(f'----------------------------')
    print(f'{folder_counter} scanned folders, {file_counter} scanned files.')
    print(f'----------------------------')

    output_file = f'{label}.csv'
    print(f'Exporting to file: {output_file}')
    with open(output_file, 'w', encoding='utf-8') as out:
        out.write('"FULL_PATH","DIRECTORY","FILENAME","EXTENSION","SIZE"\n')
        for f in FILES:
            out.write(f'{f.to_csv()}\n')


if __name__ == "__main__":
    main(sys.argv[1:])
