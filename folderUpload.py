import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        # enumerate local files recursively 
        for root, dirs, files in os.walk(file_from): 
            for filename in files: 
                # construct the full local path 
                local_path = os.path.join(root, filename) 
                # construct the full Dropbox path 
                relative_path = os.path.relpath(local_path, file_from) 
                dropbox_path = os.path.join(file_to, relative_path) 
        # upload the file 
        with open(local_path, 'rb') as f: 
            dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BF97JQVvXAOLeiYGhxpSKJ363RC0vySJ4KMH96CKT6RHg75he6Y40HeivjsXbS23sZVe4YiEVDgWBobiWCkuOMIBzyAL5mXm2W5Qy8jOAfLSOOPrOEpPSSNrDKDThLrPoGZRqVk'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")

if __name__ == '__main__':
    main()