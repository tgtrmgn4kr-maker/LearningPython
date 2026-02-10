import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-d',
                    '--sum',
                    nargs='+',
                    type=int,
                    required=True,
                    help='計算加總',
                    action='store'
                    )
                    #短參數=>快捷鍵
                    #長參數=>程式碼使用的名字
                    #程式內永遠用長參數對應的屬性
                    #argparse 只會建立 一個屬性名稱，而這個名稱來自長參數（--sum）
"""
                    #Optional short parameter (one minus sign)
                    #Optional long parameter (two minus sign)
                    #nargs:number of parameter(+:At least one)(All parameters are packaged into a list)
                    #Set the parameter as a required one
                    #It shows when you execute 'python argparse_parameters_setting.py -h'
                    #Optional. The default is "store" 
"""
                               
args = parser.parse_args()

print('sum arguments list ', args.sum)

total = sum(args.sum)

print('Total sum: ',total)
print(args.sum)

"""
The following four input is equivalent:
python script.py --sum 1 3 5 7
python script.py -d 1 3 5 7
python script.py --sum 1
python script.py -d 1
"""
"""
--sum  \
        → args.sum
-d     /
"""


