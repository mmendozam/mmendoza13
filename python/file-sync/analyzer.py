import sys
import pandas

"""100 MB"""
LARGE_FILE_SIZE = 1024 * 1024 * 100

SPOT_EXTS = ['.db', '.part', '.tmp', '.temp', '.unknown_video']
SPOT_DIRECTORIES = ['.metadata', '.settings']

# Headers
FULL_PATH = 'FULL_PATH'
DIRECTORY = 'DIRECTORY'
FILENAME = 'FILENAME'
EXTENSION = 'EXTENSION'
SIZE = 'SIZE'
STATUS = 'STATUS'
ACTION = 'ACTION'

DEFAULT_SORT = [DIRECTORY, FILENAME]

# Merge statuses
BOTH = 'both'
LEFT_ONLY = 'left_only'
RIGHT_ONLY = 'right_only'
DIFF = 'DIFF'

# ###########################################

def main(argv: list[str]) -> None:
    argv_len = len(argv)
    if not argv or argv_len == 0:
        # TODO print usage
        raise Exception('Missing parameters :(')
    elif len(argv) == 1:
        single_file(argv[0])
    elif argv_len == 2:
        compare(argv[0], argv[1])
    else:
        print('Invalid arguments :(')


def single_file(filename: str) -> None:
    df = pandas.read_csv(f'{filename}.csv', encoding='utf8')

    # filtering directories
    # df = df[ ~df[DIRECTORY].str.startswith('/ZWOLF_HOME/_Albums') ]
    df = df[ ~df[DIRECTORY].str.startswith('/ZWOLF_HOME/tmp') ]

    all_extensions = df[EXTENSION].unique()
    same_size = df[df.duplicated(SIZE, keep=False)].sort_values(by=SIZE)
    same_name = df[df.duplicated(FILENAME)].sort_values(by=DEFAULT_SORT)
    zero_size = df[df[SIZE] == 0].sort_values(by=DEFAULT_SORT) # TODO Skip folders
    large_files = df[df[SIZE] > LARGE_FILE_SIZE].sort_values(by=SIZE, ascending=True)
    # TODO spot files with long names

    #  Spotting files
    spot_exts = df[EXTENSION].isin(SPOT_EXTS)
    spot_no_ext = df[EXTENSION].isnull()
    spot_long_ext = df[EXTENSION].str.len() > 5
    # spot_tilde = df[FILENAME].str.startswith('~')
    spot_equals = df[FILENAME].str.contains('=')
    # spot_copied = df[FILENAME].str.match('.*\([0-9]*\)')
    # TODO Spot files with long names (255 chars max)
    spotted = df[spot_exts | spot_no_ext | spot_long_ext | spot_equals].sort_values(by=DEFAULT_SORT)

    # size of files under a given folder
    # s = df[df['DIRECTORY'].str.startswith('/ZWOLF_HOME/_Nanalka/media/videos/tokyomotion')]['SIZE'].sum()
    # s / (1024 * 1024)                 # MB
    # s / (1024 * 1024 * 1024)          # GB
    # s / (1024 * 1024 * 1024 * 1024)   # TB
    
    print('all_extensions')
    print(all_extensions)
    print('same_size')
    print(same_size)
    print('same_name')
    print(same_name)
    print('zero_size')
    print(zero_size)
    print('large_files')
    print(large_files)
    print('spotted')
    print(spotted)
    
    print('Exporting spotted to file')
    spotted.to_csv(f'{filename}.spotted.csv', index=False)


def compare(left_name: str, right_name: str):
    left_df = pandas.read_csv(f'{left_name}.csv', encoding='utf8')
    right_df = pandas.read_csv(f'{right_name}.csv', encoding='utf8')

    # Merging left and right
    merged = left_df.merge(right_df, indicator=STATUS, how='outer').sort_values(by=DEFAULT_SORT)
    merged.replace({STATUS: LEFT_ONLY}, {STATUS: left_name.upper()}, inplace=True)
    merged.replace({STATUS: RIGHT_ONLY}, {STATUS: right_name.upper()}, inplace=True)
    merged[ACTION] = None

    # filtering directories
    # merged = merged[ ~merged[DIRECTORY].str.startswith('/ZWOLF_HOME/_Albums') ]
    # merged = merged[ ~merged[DIRECTORY].str.startswith('/ZWOLF_HOME/_Nanalka') ]
    merged = merged[ ~merged[DIRECTORY].str.startswith('/ZWOLF_HOME/tmp') ]

    # Files with different size
    diff = merged[merged.duplicated(FULL_PATH)].copy()
    if len(diff) == 0:
        print('No files out of sync found :)')
    else:
        print('Files out of sync found')
        diff[STATUS] = DIFF
        diff.to_csv(f'{left_name}_vs_{right_name}_changes.csv', index=False)

    # Files missing on either side
    sync = merged[merged[STATUS] != BOTH].sort_values(by=DEFAULT_SORT)
    if len(sync) == 0:
        print('Directories are in sync :)')
    else:
        print('Directories out of sync')
        sync.to_csv(f'{left_name}_vs_{right_name}_missing.csv', index=False)


if __name__ == "__main__":
    main(sys.argv[1:])
