import qrcode

if __name__ == '__main__':
    idx = 0
    while(True):
        print("書き込む文字列を入力：")
        x = input()
        print("書き込む文字列：", x)
        outqrimg = qrcode.make(str(x))
        outqrimg.save('./'+str(idx)+'.png')
        print("書き出し完了")
        idx = idx + 1

    print('end')