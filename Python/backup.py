import platform
import os

# Backup would be stored in a hidden directory under Home
bkpFolderPath='~' # Specifies Home directory
bkpFolderName='/.ControlYourselfConfig'
# Caution: Make include spaces inside the above strings

def backup():
    if platform.system()=='Linux':
        try:
            os.system('mkdir '+bkpFolderPath+bkpFolderName)
            os.system('sudo cp /etc/hosts '+bkpFolderPath+bkpFolderName)
            print('File successfully backed up')
        except:
            print('Something went wrong')
    elif platform.system()=='Windows':
        try:
            os.system('md '+bkpFolderPath+bkpFolderName)
            os.system('copy C:\\Windows\\System32\\drivers\\etc\\hosts '+bkpFolderPath+bkpFolderName)
            print('File successfully backed up')
        except:
            print('Something went wrong')
    else:
        print('An error occurred while detecting the OS')

def restore():
    if platform.system()=='Linux':
        try:
            os.system('sudo cp '+bkpFolderPath+bkpFolderName+' /etc/')
            print('File successfully restored')
        except:
            print('Something went wrong')
    elif platform.system()=='Windows':
        try:
            os.system('copy '+bkpFolderPath+bkpFolderName+' C:\\Windows\\System32\\drivers\\etc\\')
            print('File successfully restored')
        except:
            print('Something went wrong')
    else:
        print('An error occurred while detecting the OS')

def clearBackup():
    if platform.system()=='Linux':
        try:
            os.system('sudo rm -r '+bkpFolderPath+bkpFolderName) # try not use the force flag
            print('Custom back directory removed')
        except:
            print('Something went wrong')
    elif platform.system()=='Windows':
        try:
            os.system('del '+bkpFolderPath+bkpFolderName)
            print('Custom back directory removed')
        except:
            print('Something went wrong')


# Driver Program
if __name__=="__main__":
    print('-----------------------')
    print('Detected OS: ',platform.system())
    print('-----------------------')
    print('1. Backup')
    print('2. Restore')
    print('3. Clear Backup')
    inp=int(input('Enter choice '))
    if inp==1:
        backup()
    elif inp==2:
        restore()
    elif inp==3:
        clearBackup()
    else:
        print('Option missmatched')
