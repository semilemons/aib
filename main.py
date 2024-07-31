import tkinter as tk
from get_metadata import get_metadata

def on_button_click():
    get_metadata()
    result_label.config(text="処理が完了しました")


if __name__ == "__main__":
    # GUIのセットアップ
    root = tk.Tk()
    root.title("Metadata GUI")
    root.geometry("300x200")

    # ボタンの作成
    button = tk.Button(root, text="スプレッドシートから情報取得", command=on_button_click)
    button.pack(pady=20)

    # ラベルの作成
    result_label = tk.Label(root, text="")
    result_label.pack(pady=20)

    # GUIのメインループを開始
    root.mainloop()

