#include <Arduino.h>

#include <FastLED.h>

// 定义 WS2812 灯带连接的 GPIO 引脚
#define LED_PIN     38
// 定义灯珠数量
#define NUM_LEDS    1

// 定义 FastLED 数组
CRGB leds[NUM_LEDS];

void setup() {
  // 初始化 FastLED
  FastLED.addLeds<WS2812, LED_PIN, GRB>(leds, NUM_LEDS);
}

void loop() {
  // 设置灯珠颜色为红色
  leds[0] = CRGB::Red;
  FastLED.show();
  delay(1000);

  // 设置灯珠颜色为绿色
  leds[0] = CRGB::Green;
  FastLED.show();
  delay(1000);

  // 设置灯珠颜色为蓝色
  leds[0] = CRGB::Blue;
  FastLED.show();
  delay(1000);
}