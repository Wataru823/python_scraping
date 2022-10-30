from icrawler.builtin import BingImageCrawler
from PIL import Image
import glob


# 画像を収集するメソッド
# 引数は画像を保存するパスpath、検索ワードkeyword、収集する枚数num

def scraping(path, keyword, num):

    bing_crawler=BingImageCrawler(
    downloader_threads=4,
    storage={'root_dir': path}
    )

    #検索ワードにkeywordを入れたときに得られる画像をnum枚収集
    bing_crawler.crawl(
        keyword=keyword,
        max_num=num
    )
    print(f'{keyword}: scraping completed!')


#ファイルの形式はjpegなので、ファイル名には必ず拡張子.jpgがつく
asuka_path='./images/figure0/*.jpg'
tama_path='./images/figure1/*.jpg'

keywords=['平野紫耀','テテ']
num=600

scraping('./images/figure0/', keywords[0], num)
scraping('./images/figure1/', keywords[1], num)

# """
# 画像をリサイズするメソッド
# 引数は保存したいパスpath=フォルダ名+フォーマット名、変更後のサイズの幅と高さw,h
#
# *リサイズしたい画像はパスで指定される
# """

def resize_image(path, w, h):
    img_paths=glob.glob(path)

    for img_path in img_paths:
        try:
            #画像ファイルに変換
            img=Image.open(img_path).convert('RGB')
            #指定したサイズでリサイズをする
            img_resized=img.resize((w,h))

            #リサイズした画像を上書き保存、同じパスを指定
            img_resized.save(img_path)
            img.close()
        except Exception as e:
            print("Error:", img_path)
            # e に msg 属性があれば取得、無ければ None にしておきました。
            msg = getattr(e, 'msg', None)
            print(f'(message) {msg}')
        else:
            # エラーは検出できなかった。
            print('ok!', img_path)
    print(f'{path}: resized!')

#サイズは300x300で指定
width=300
height=300

resize_image(asuka_path, width, height)
resize_image(tama_path, width, height)