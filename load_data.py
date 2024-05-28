import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from dotenv import load_dotenv
import pandas as pd

def load_data(file_name, sep=','):
    # load environment variables from .env file, get path to client_secrets.json from environment variable
    load_dotenv()
    client_secrets_path = os.getenv('GOOGLE_CLIENT_SECRETS')

    if client_secrets_path is None:
        raise ValueError("The environment variable GOOGLE_CLIENT_SECRETS is not set.")

    # PyDrive client for OAuth 2.0 authentication
    gauth = GoogleAuth()
    gauth.LoadClientConfigFile(client_secrets_path)

    # Load credentials
    gauth.LoadCredentialsFile("mycreds.txt")
    if gauth.credentials is None:
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()
    gauth.SaveCredentialsFile("mycreds.txt")

    drive = GoogleDrive(gauth)
    search_query = f"title = '{file_name}' and trashed=false"
    file_list = drive.ListFile({'q': search_query}).GetList()

    if not file_list:
        print("No files found matching the query.")
        return None
    else:
        for file in file_list:
            print(f'Title: {file["title"]}, ID: {file["id"]}')
            file_id = file['id']
            file = drive.CreateFile({'id': file_id})
            file.GetContentFile(file_name)
            print('File downloaded successfully!')
        df = pd.read_csv(file_name, sep=sep)
    return df
