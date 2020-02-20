from time import *
from datetime import *

now = ctime()
cnvtime = strptime(now)
nowTime = print(strftime("%H:%M", cnvtime))

dt1 = datetime(year=1970, month=1, day=1)
dt_now = datetime.now()
elapsed_time = dt_now - dt1
print(elapsed_time.days)

dt2 = datetime(year=1970, month=1, day=2)
elapsed_time1 = dt2 - dt1
#print(elapsed_time1.days)

"""   このプログラムは、入力した日時との偏差を出し、経過日数を表示する。
    このままの状態で実行すれば、dt1と現在までの経過日数を表示する。
    直観的に分かると思うけど、例えば、1980/01/01から現在までの経過日数を出したかったら、8行目を
    dt1 = datatime(year=1980, month=1, day=1)にする
    ある地点からある地点までを表示させたい時は、11行目をコメントアウトし、
    15行目の#を消して、dt1とdt2を使う。ただし、dt2 > dt1
    """