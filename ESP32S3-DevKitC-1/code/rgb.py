import machine
import neopixel
import time

# 定义 WS2812 连接的 GPIO 引脚和灯珠数量
pin = 38
num_pixels = 1  # 假设只有一个灯珠，可根据实际情况修改

# 初始化 neopixel 对象
np = neopixel.NeoPixel(machine.Pin(pin), num_pixels)

try:
    while True:
        # 设置灯珠颜色为红色
        np[0] = (255, 0, 0)
        np.write()
        time.sleep(1)

        # 设置灯珠颜色为绿色
        np[0] = (0, 255, 0)
        np.write()
        time.sleep(1)

        # 设置灯珠颜色为蓝色
        np[0] = (0, 0, 255)
        np.write()
        time.sleep(1)

except KeyboardInterrupt:
    # 当按下 Ctrl+C 时，关闭所有灯珠
    for i in range(num_pixels):
        np[i] = (0, 0, 0)
    np.write()