# To map a network drive

# HOME
NET USE H: \\RP4-HOME\sdk1

# PLEX
NET USE P: \\Rpi4-plex\tsb_plex

# NNLK
NET USE N: \\Rpi4-cloud\max_nnlk
NET USE Q: \\Rpi4-nnlk\sdk_nnlk
NET USE R: \\Rpi4-cloud\pny_02
NET USE S: \\Rpi4-plex\pny_03
NET USE T: \\Rpi3-dev\sdk_dev

# To delete a mapped network drive
NET USE ${DRIVE}: /delete
NET USE H: /delete

# File comparison Windows CLI
fc file1.txt file2.txt

# ############################
# Notes
# 1. LAPTOP NNLK is fully sync'd with TSB_BACKUP
#   1.1. TSB_BACKUP contains TOKYOMOTION files that LAPTOP does not

# 1 - Scan directories
python scanner.py $PATH_TO_SCAN [$OUTPUT_FILE]
python scanner.py "C:\ZWOLF_HOME\_Nanalka" "laptop"
python scanner.py "F:\ZWOLF_HOME\_Nanalka" "tsb-backup"

# 2 - Analize a single file
python analyzer.py laptop

# 3 - Compare 2 drives
python analyzer.py "laptop" "tsb-backup"

# 3.1 Comparing 2 text files
FC "file1.txt" "file2.txt"

# 3.2 Comparing 2 binary files
FC \B "file1.bin" "file2.bin"

# 4 - Check reports

# laptop_vs_tsb-backup_diff
\ZWOLF_HOME\_Nanalka\info\nnlk.links.sh
\ZWOLF_HOME\_Nanalka\info\afreecatv\afreecatv.info.sh
\ZWOLF_HOME\_Nanalka\info\voyeur-house\voyeur-house.tv.sh
\ZWOLF_HOME\_Nanalka\info\voyeur-house\voyeur-house.tv.xlsx
\ZWOLF_HOME\_Nanalka\media\videos\Instagram\instablog9ja\instablog9ja - Cg8h7aYDIIQ - 2.jpg
\ZWOLF_HOME\_Nanalka\media\videos\Instagram\instablog9ja\instablog9ja - Cg8h7aYDIIQ.info.json

# 5 Copy missing files
#   5.1 Add list of files to '2copy.txt'
#   5.2 Run
python copier.py







# Scan all
python scanner.py "C:\ZWOLF_HOME" "laptop" & python scanner.py "F:\ZWOLF_HOME" "tsb-backup" & python scanner.py "O:\ZWOLF_HOME" "tsb-cloud"

python scanner.py "C:\ZWOLF_HOME" "laptop"
python scanner.py "F:\ZWOLF_HOME" "tsb-backup"
python scanner.py "O:\ZWOLF_HOME" "tsb-cloud"

python analyzer.py "laptop" "tsb-backup"
python analyzer.py "laptop" "tsb-cloud"
python analyzer.py "tsb-cloud" "tsb-backup"

# NNLK

# no content
# python scanner.py "O:\ZWOLF_HOME\_Nanalka" "tsb-cloud.nnlk"

# Scan
python scanner.py "C:\ZWOLF_HOME\_Nanalka" "laptop.nnlk"
python scanner.py "F:\ZWOLF_HOME\_Nanalka" "tsb-backup.nnlk"
python scanner.py "N:\ZWOLF_HOME\_Nanalka" "max.nnlk"

python scanner.py "C:\ZWOLF_HOME\_Nanalka" "laptop.nnlk" & python scanner.py "F:\ZWOLF_HOME\_Nanalka" "tsb-backup.nnlk" & python scanner.py "N:\ZWOLF_HOME\_Nanalka" "max.nnlk"


# Analyzer

python analyzer.py "laptop.nnlk" "tsb-backup.nnlk" # OK - [tokyomotion]            not in 'laptop'
python analyzer.py "laptop.nnlk" "max.nnlk"        # OK - [tokyomotion, afreecatv] not in 'laptop'
python analyzer.py "tsb-backup.nnlk" "max.nnlk"    # OK - [tokyomotion, afreecatv] not in 'tsb-backup'

# afreecatv (890 GB) only in 'max.nnlk'
# tokyomotion distributed between 'tsb-backup' and 'max-nnlk'









