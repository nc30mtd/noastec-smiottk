import sys
import qrcode

if __name__ == '__main__':
    args = sys.argv
    
    target_str = ''
    idx = 0

    if(len(args) > 2):
        target_str = args[1]
        export_filepath = args[2]
        outqrimg = qrcode.make(target_str)
        outqrimg.save(export_filepath+'.png')
    else:
        while(True):
            print("書き込む文字列を入力：")
            x = input()
            print("書き込む文字列：", x)
            outqrimg = qrcode.make(str(x))
            outqrimg.save('./'+str(idx)+'.png')
            print("書き出し完了")
            idx = idx + 1

    print('end')