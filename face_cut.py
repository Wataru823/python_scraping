#Dlibで顔部分を切り抜き
import cv2, dlib, glob, pprint

#入力ディレクトリ指定
in_dir1="./images/figure0/"
in_dir2="./images/figure1/"

#出力ディレクトリ指定
out_dir1="./images/face0/"
out_dir2="./images/face1/"

#画像のID
fid=1000

#入力画像をリサイズするか
flag_resize=False

#Dlibを始める
detector=dlib.get_frontal_face_detector()

#顔画像を取得して保存
def get_face(fname, dout):
    global fid
    img=cv2.imread(fname)

    #サイズが大きければリサイズ
    if flag_resize:
        img=cv2.resize(img, None, fx=0.2, fy=0.2,)

    #顔検出
    dets=detector(img, 1)
    for k,d in enumerate(dets):
        pprint.pprint(d)
        x1=int(d.left())
        y1=int(d.top())
        x2=int(d.right())
        y2=int(d.bottom())
        im=img[y1:y2, x1:x2]
        #64x64にリサイズ
        try:
            im=cv2.resize(im, (64,64))
        except:
            continue

        #保存
        out=dout+"/"+str(fid)+".jpg"
        cv2.imwrite(out, im)
        fid+=1

#ファイルを列挙して繰り返し顔検出
in_dir_list = [in_dir1, out_dir1]
out_dir_list = [in_dir2, out_dir2]
dir_list = [in_dir_list, out_dir_list]


for l in dir_list:
    files=glob.glob(l[0]+"/*")
    for f in files:
        print(f)
        get_face(f, l[1])
    print("ok")