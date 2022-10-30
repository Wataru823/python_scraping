# Scraping

スクレイピングについてのコードを動かせるようにエラー修正などした。

## 機械学習で顔分類

参考記事

[齋藤飛鳥と玉森裕太の顔分類 WEB アプリ開発](https://qiita.com/shota_seki/items/c8cf40f9c7764f43496c)

同じ人だとつまらないから、平野紫耀と BTS のテテで画像収集した。

### Google の検索結果を元に 300×300 のサイズで画像を取得

```
python scraping.py
```

### dlib を用いて顔の部分を抽出

dlib は画像処理ライブラリ。リアルタイムで顔検知できたり、軽くて精度もいい感じがする。

```
python face_cut.py
```

### その他

データセット作成の make_dataset.py や作成した npz ファイルを確認する check_dataset.py がある。
