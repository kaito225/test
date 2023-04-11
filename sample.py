""" ライブラリ読込 """
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from datasets import load_dataset
""" GPU設定 """
# GPUが利用できる場合はGPUを利用し、利用不可の場合はCPUを利用するための記述
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


""" (1)データの準備  """
iris=datasets.load_iris()
#iris=load_dataset("csv",data_files=["date/result/result.csv","sample.csv"])#pandasにあるデータを使用
X=iris.data.astype(np.float32)
Y=iris.target.astype(np.int64)
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.25,random_state=3)#test_sizeは全体のn％を利用して行う,random_stateはランダムなデータを固定化して偏りをなくす
X_train,X_test,Y_train,Y_test=torch.from_numpy(X_train).to(device),torch.from_numpy(X_test).to(device),torch.from_numpy(Y_train).to(device),torch.from_numpy(Y_test).to(device)
#学習データの説明変数
#X_train.shape=[105,4],Y=///[105]
print(X_train[:3])




""" (2)モデルクラスの登録 """
# nnクラスの関数(初期設定)を下記に記述
class lrisModel(nn.Module):
    
    # ユニット・層の数・活性化関数等ニューラルネットワークの模型となるものを下記に記述
    def __init__(self):
        super(lrisModel, self).__init__()
        self.model_info=nn.ModuleList([
            nn.Linear(4,6),nn.Sigmoid(),nn.Linear(6,3),
        ])
    #nn.linear(in_features, out_features, bias=True)
    #in各入力サンプルのサイズのこと
    # 順方向の計算処理の流れを下記に記述
    def forward(self,x):
        for i in range(len(self.model_info)):
            x=self.model_info[i](x)
        return x
    #ここに画像の下処理を行う関数を加える
  
      
""" (3)モデルとパラメータ探索アルゴリズムの設定 """
model     = lrisModel().to(device)  # モデルのインスタンス
optimizer =optim.SGD(model.parameters(),lr=0.05)                    # パラメータ探索アルゴリズム
criterion = nn.CrossEntropyLoss()                    # 損失関数



""" (4)モデル学習 """
data_size=len(X_train)
print(len(X_train))
mini_batch=int(data_size*3/4)
repeat = 1500     # 学習回数を設定(整数)

for epoch in range(repeat):
    dx=np.random.permutation(data_size)
    for num in range(0,data_size,mini_batch):  
        ex_var = X_train[dx[num:(num+mini_batch)if (num+mini_batch)<data_size else data_size]]  # 説明変数を作成
        target = Y_train[dx[num:(num+mini_batch)if (num+mini_batch)<data_size else data_size]]  # 目的変数を作成
        # モデルのforward関数を用いた順伝播の予測(モデルの出力値算出)
        output = model(ex_var) 
        # 上記出力値(output)と教師データ(target)を損失関数に渡し、損失関数を計算
        loss = criterion(output, target)
        # 勾配を初期化
        optimizer.zero_grad()
        # 損失関数の値から勾配を求め誤差逆伝播による学習を実行
        loss.backward()
        # 学習結果に基づきパラメータを更新
        optimizer.step()


""" (5) モデルを保存/呼び出し """
torch.save(model.state_dict(), "sample.model")     # モデル保存する場合
model.load_state_dict(torch.load("sample.model"))  # モデルを呼び出す場合


model.eval()
with torch.no_grad():
    # 性能評価
    pred_model=model(X_test)
    pred_result=torch.argmax(pred_model,1)
    print("正解率"+str(round(((Y_test==pred_result).sum()/len(pred_result)).item(),3))+"[%]")