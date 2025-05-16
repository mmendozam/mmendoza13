# mmendoza13

# Windows commands

```batch
:: Map a network disk:
net use ${DRIVE} \\${SERVER}\${SHARE}
net use H: \\RP4-HOME\sdk1

:: Delete a mapped network drive
net use ${DRIVE}: /delete
net use H: /delete

:: Comparing 2 text files
fc "file1.txt" "file2.txt"

:: Comparing 2 binary files
fc \B "file1.bin" "file2.bin"

:: Syncing 2 directories
robocopy <source> <destination> [<file>[ ...]] [<options>]

robocopy C:\path\to\source E:\path\to\destination /S /Z /LOG:C:\Logs\Backup.log

robocopy /s /z /xc /xn /xo B:\NNLK_HOME\media\images F:\NNLK_HOME\media\images
```



# Linux commands

# Python

```python
import s
```

## Disks
