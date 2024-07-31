# スプレッドシート連携画像ZIP化システム

このプロジェクトは、Google スプレッドシートと連携して、ローカルの画像ファイルをZIP圧縮するシンプルなGUIアプリケーションです。

## セットアップ手順

1. リポジトリのクローン:
   ```
   git clone https://github.com/yourusername/spreadsheet-image-zip.git
   cd spreadsheet-image-zip
   ```

2. 依存関係のインストール:
   ```
   pip install -r requirements.txt
   ```

3. credentials.jsonの設定:
   - `credentials-json-example.json` を `credentials.json` にコピーします。
   - Google Cloud Console で新しいプロジェクトを作成し、必要な認証情報を取得します。
   - `credentials.json` 内のプレースホルダーを実際の認証情報で置き換えます。

4. Google スプレッドシートの準備:
   - 新しいGoogle スプレッドシートを作成します。
   - スプレッドシートに画像ファイル名（拡張子なし）を列挙します。
   - スプレッドシートのURLからIDを取得します。
     (例: https://docs.google.com/spreadsheets/d/[このIDをコピー]/edit#gid=0)

5. スプレッドシートIDの設定:
   - `get_metadata.py` ファイルを開きます。
   - `SAMPLE_SPREADSHEET_ID` 変数を探し、その値を手順4で取得したスプレッドシートIDに置き換えます。
   例:
   ```python
   SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
   ```

6. ローカルフォルダの準備:
   - `workspace/images/` ディレクトリに、ZIP化したい画像ファイルを配置します。

## 使用方法

1. アプリケーションの実行:
   ```
   python main.py
   ```

2. Tkinterウィンドウが表示されます。

3. 表示されたボタンをクリックして処理を実行します。

4. ZIP化された画像ファイルが `workspace/zips/` ディレクトリに生成されます。

## ファイル構造

- `main.py`: アプリケーションのエントリーポイントとGUIロジック
- `get_metadata.py`: スプレッドシートからのデータ取得ロジック
- `credentials.json`: Google API認証用のクレデンシャル
- `token.json`: 認証トークン（自動生成）
- `workspace/`: 作業ディレクトリ
  - `images/`: 元の画像ファイルを配置
  - `zips/`: 生成されたZIPファイルの保存先

## 注意事項

- このシステムはテスト用であり、本番環境での使用は想定していません。
- `credentials.json` には機密情報が含まれるため、決して公開リポジトリにコミットしないでください。
- 使用前にGoogle Cloud ConsoleでGoogle Sheets APIとDrive APIを有効にしてください。
- スプレッドシートIDは `get_metadata.py` ファイル内で直接設定されます。セキュリティ上の理由から、本番環境では環境変数や設定ファイルを使用することをお勧めします。

## トラブルシューティング

- 認証エラーが発生した場合は、`credentials.json` の内容を確認し、必要に応じて `token.json` を削除して再認証を行ってください。
- 画像ファイルが見つからない場合は、`workspace/images/` ディレクトリ内のファイル名とスプレッドシートの内容が一致していることを確認してください。
- スプレッドシートからデータを取得できない場合は、`get_metadata.py` 内の `SAMPLE_SPREADSHEET_ID` が正しく設定されていることを確認してください。

