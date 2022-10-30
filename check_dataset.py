#画像とそのラベルの確認
import matplotlib.pyplot as plt
import numpy as np

#画像データ読み込み
photos=np.load("./images/dataset.npz")
x=photos['x']
y=photos['y']

#開始インデックス ここを変更することで他の画像も確認可能
idx=350

#pyplotで出力
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5, 5, i+1)
    plt.title(y[i+idx])
    plt.axis('off')
    plt.imshow(x[i+idx])
plt.show()
