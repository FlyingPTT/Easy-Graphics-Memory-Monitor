import time
import random
import pyttsx3
import pynvml

pynvml.nvmlInit()
handle = pynvml.nvmlDeviceGetHandleByIndex(1)

engine = pyttsx3.init()

has_reminded_low = False
has_reminded_high = False
start_time = time.time()

while True:
    info = pynvml.nvmlDeviceGetMemoryInfo(handle)
    current_usage = info.used / (1024 * 1024 * 1024)

    elapsed_time = time.time() - start_time
    formatted_time = time.strftime('%H:%M:%S', time.gmtime(elapsed_time))

    if current_usage < 10 and not has_reminded_low:
        engine.say("显存占用小于 10GB！")
        engine.runAndWait()
        has_reminded_low = True
        has_reminded_high = False
    elif current_usage >= 10 and not has_reminded_high:
        engine.say("显存占用超过 10GB！")
        engine.runAndWait()
        has_reminded_high = True
        has_reminded_low = False

    print(f"\r已运行时间：{formatted_time}，当前显存占用：{current_usage:.2f}GB", end='')
    time.sleep(5)