# Scraping

スクレイピングについてのコードを動かせるようにエラー修正などした。

## 機械学習で顔分類するためにスクレイピングで画像収集


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

### 参考記事

[齋藤飛鳥と玉森裕太の顔分類 WEB アプリ開発](https://qiita.com/shota_seki/items/c8cf40f9c7764f43496c)

[dlibと呼ばれる画像処理ライブラリを使ってみた](https://nonbiri-tereka.hatenablog.com/entry/2016/07/11/150106)

[【python】ImportError: No module named '***'の対処法](https://www.haya-programming.com/entry/2018/09/09/202711)

[Pillow (Python Imaging Library)でPNGファイルを扱う時の注意](https://ugcj.com/pillow-python-imaging-library%E3%81%A7png%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%82%92%E6%89%B1%E3%81%86%E6%99%82%E3%81%AE%E6%B3%A8%E6%84%8F/)

[【Python】画像の破損をチェックするコード例【Pillow】](https://srbrnote.work/archives/5717)

