# This simple code is created to automate the boring
# task of moving files from Transport folder to the
# respective client folders based on matching the
# the files to be moved with the respective
# subfolders based on the client's surname and name.

import os, shutil, re

def getFolderNamelist(clientFoldersPath):
    clientFolderList = [entry for entry in os.listdir(clientFoldersPath) if os.path.isdir(os.path.join(clientFoldersPath, entry))]
    #print(clientFolderList)
    return clientFolderList

def getFileNamelist(clientFilesPath):
    clientFileList = [entry for entry in os.listdir(clientFilesPath) if os.path.isfile(os.path.join(clientFilesPath, entry))]
    #print(clientFileList)
    return clientFileList

def fileRedirector(clientFoldersPath, clientFilesPath):
    folderList = getFolderNamelist(clientFoldersPath)
    fileList = getFileNamelist(clientFilesPath)
    clientNameList = ['The list of all clients for whom at least one file was moved']
    file = open(clientFoldersPath + '\\\\clientFileList.txt', 'w') 
    print("The list of all clients for whom at least one file was moved : ", file.name)
    file.close()
    for Folder in folderList:
        folderName = re.compile(Folder)
        for fileName in fileList:
            if folderName.search(fileName):
                shutil.move(clientFilesPath + '\\\\' + fileName, clientFoldersPath + '\\\\' + Folder)
                if (Folder in clientNameList) == False:
                    clientNameList.append(Folder)
    print(clientNameList)

    # write the file header including the current date
    with open(clientFoldersPath + '\\\\clientFileList.txt', "a") as file:
        for Client in clientNameList:
            file.write(Client)
            file.write("\n")



#getFolderNamelist('C:\\Users\\filax\OneDrive\\Desktop\\Code-repository\\2025-08-03-Investcon-file-redirector\\clientDatabase')

#getFileNamelist('C:\\Users\\filax\\OneDrive\\Desktop\\Code-repository\\2025-08-03-Investcon-file-redirector\\clientFilesTransport')

fileRedirector('C:\\Users\\filax\\OneDrive\\Desktop\\Code-repository\\2025-08-03-Investcon-file-redirector\\clientDatabase',
               'C:\\Users\\filax\\OneDrive\\Desktop\\Code-repository\\2025-08-03-Investcon-file-redirector\\clientFilesTransport')
