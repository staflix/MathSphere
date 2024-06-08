import time

local_time = time.gmtime(time.time())
t = local_time[:5]
print(f'{str(t[2]).rjust(2, "0")}.{str(t[1]).rjust(2, "0")}.{t[0]} - {t[3]}:{t[4]} UTC')