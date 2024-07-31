import os
import zipfile
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SPREADSHEET_ID = '1nsB2fSKAYU4Bsblm1m8dZoJMOZOX_ovvcBuLsKmhOYk'
image_folder = './workspace/images'
output_zip = './workspace/zips/output.zip'

def get_spreadsheet_data():
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    # C列の4行目から最後までのデータを取得
    RANGE_NAME = '商品説明!C4:C'

    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])

    return [row[0] for row in values if row]  # 空の行を除外

def create_zip_from_local_images(product_names, image_folder, output_zip):
    with zipfile.ZipFile(output_zip, 'w') as zipf:
        for product in product_names:
            image_name = f"{product}.png"  # 画像ファイル名
            image_path = os.path.join(image_folder, image_name)
            
            if os.path.exists(image_path):
                zipf.write(image_path, image_name)
            else:
                print(f"警告: {image_name} が見つかりません。")

    print(f"ZIPファイルが作成されました: {output_zip}")

def get_metadata():
    product_names = get_spreadsheet_data()
    print(product_names)
    create_zip_from_local_images(product_names, image_folder, output_zip)
    
if __name__ == "__main__":
    get_metadata()