a = int(input("請輸入星星數:"))

num = int((a+1)/2)

for i in range(1,num+1):
        print(' '*(num-i)+'*'*(2*i-1))

for j in range(num-1,0,-1):
        print(' '*(num-j)+'*'*(2*j-1))
