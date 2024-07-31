function downloadImagesAsZipNewFolder() {
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet(); // 現在のスプレッドシートを取得
  var descriptionSheet = spreadsheet.getSheetByName("商品説明"); // "商品説明"シートを取得
  var folderId = '1t1-vA45fNEFf573bJ4o2pgc6ySPVv6cc'; // 画像があるフォルダのID
  var folder = DriveApp.getFolderById(folderId); // フォルダを取得
  var startRow = 4; // 開始行（C4から始まるため）
  var range = descriptionSheet.getRange(startRow, 3, descriptionSheet.getLastRow() - startRow + 1); // C列の範囲を取得
  var values = range.getValues(); // C列の値（商品名）を取得

  var zipFiles = []; // ZIP化するファイルのリスト
  for (var i = 0; i < values.length; i++) {
    var fileName = values[i][0] + '.png'; // 商品名 + .png
    var files = folder.getFilesByName(fileName); // ファイルを検索
    while (files.hasNext()) {
      var file = files.next();
      zipFiles.push(file.getBlob().setName(fileName)); // ZIPリストに追加
    }
  }

  if (zipFiles.length > 0) {
    var zip = Utilities.zip(zipFiles, 'images.zip'); // ZIPファイル作成
    var zipFile = DriveApp.createFile(zip); // Driveにファイル作成

    var destinationFolder = DriveApp.getFolderById('1H4vyXzNhgKB3LI4bubsVlLh8cmNaXjW2'); // 保存先フォルダ
    zipFile.moveTo(destinationFolder); // ZIPファイルを移動

    var url = 'https://drive.google.com/uc?export=download&id=' + zipFile.getId(); // ダウンロードURL作成
    descriptionSheet.getRange('D4').setValue(url); // D4セルにURLを設定
  } else {
    descriptionSheet.getRange('D4').setValue("No files found to zip"); // ファイルがない場合のメッセージ
  }
}