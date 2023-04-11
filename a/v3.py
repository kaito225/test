import itertools

N = int(input())

digits = ["123456789"] + ["0123456789"] * 5
#*digitsリストからとりだす
six = tuple(itertools.product(*digits))
#sixは全ての通りを小銃んから生じ
A, B, C, D, E, F = six[N - 1]
#()の中の値だから上のように引き出せる
ANS = "".join((A, A, B, C, D, D, E, F, E))
#空白なしに上の順でくっつけていって下さい。
print(ANS)
