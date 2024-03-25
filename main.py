import os
import subprocess
import time

N2NEXE = "N2N\\edge.exe"
groupName = "GDJAY1"
serverAddress = "52.192.105.70:3000"
localAddress = "192.168.5.1"

if __name__ == '__main__':
    print("hello world")
    ret = subprocess.Popen(f"{N2NEXE} -c {groupName} -a {localAddress} -l {serverAddress}",
    stdout = subprocess.PIPE,stdin = subprocess.PIPE,stderr = subprocess.PIPE)

    time.sleep(3)
    print("here")

    # handle = msvcrt.get_osfhandle(ret.stdout.fileno())
    # read, avail_count, msg = _winapi.PeekNamedPipe(handle, 0)
    # while avail_count > 0:
    #     data , errcode = _winapi.ReadFile(handle, avail_count)
    #     print(data)

    # info = ret.stdout.read(2).decode("utf8")
    # while info!="":
    #     print(info,end="")
    #     info = ret.stdout.read(2)
    #     if info is None:
    #         break
    #     else:
    #         info = info.decode("utf8")

    os.system("pause")
    os.system(f"taskkill /f /pid {ret.pid}")


    # while True:
    #     info = ret.read(2)
    #     if info != "":
    #         print(info,end="")