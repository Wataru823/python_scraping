#画像ファイルを読んでNumpy形式に変換
#画像にラベルをつけて保存
import numpy as np
from PIL import Image
import glob, random

#保存ファイル名
outfile="./images/dataset.npz"
#利用する画像枚数
max_photo=200
#画像サイズ
photo_size=64
#画像データ
x=[]
#ラベルデータ
y=[]

def main():
    #各画像フォルダを読む
    glob_files("./images/face0/", 0)
    glob_files("./images/face1/", 1)

    #ファイルへ保存
    np.savez(outfile, x=x, y=y)
    print("データセットの作成完了："+outfile, len(x))


#path以下の画像を読み込む
def glob_files(path, label):
    #画像ファイルを読む
    files=glob.glob(path+"/*.jpg")
    random.shuffle(files)

    #各ファイルを処理
    num=0
    for f in files:
        if num>=max_photo: break
        num+=1

        #画像ファイルを読む
        img=Image.open(f)
        #色空間をRGB
        img=img.convert("RGB")
        #サイズ変更
        img=img.resize((photo_size, photo_size))
        img=np.asarray(img)
        img=img/255
        x.append(img)
        y.append(label)

if __name__=='__main__':
    main()