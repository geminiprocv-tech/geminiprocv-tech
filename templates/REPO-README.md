<!-- MẪU README CHO REPO DỰ ÁN IoT/NHÚNG — copy vào repo dự án, xoá comment hướng dẫn -->

# 🛰 sensor-node — low-power IoT sensor node

> Node đo nhiệt–ẩm gửi dữ liệu qua MQTT, chạy pin **9 ngày** ở chế độ sleep **42 µA**.

<p align="center">
  <img src="docs/demo.gif" alt="demo" width="70%"/>
</p>

| | |
|---|---|
| **MCU** | STM32F411 (bare-metal + FreeRTOS, driver tự viết) |
| **Sensor** | SHT31 (I2C), pin VEML7700 |
| **Link** | WiFi (ESP-AT) → MQTT → broker |
| **Power** | 18650 · **42 µA** sleep · **9 ngày** liên tục |
| **Status** | v1.0 — hoạt động ổn định |

## 1. Vấn đề & giải pháp
- **Vấn đề:** (1–2 câu — bài toán thực tế, càng cụ thể càng tốt)
- **Giải pháp:** (cách bạn giải quyết, và **tại sao chọn cách này** thay vì cách khác)

## 2. Kiến trúc
```
[STM32] --I2C--> [SHT31]
   |                   
   |--UART--> [ESP8266] --MQTT--> [Broker] --> [Dashboard]
   |
   +-- [RTC wake 60s] [Flash buffer khi mất mạng]
```
> Sơ đồ khối vẽ bằng tay/Excalidraw cũng được — quan trọng là có, và giải thích được tại sao chia block như vậy.

## 3. Pinout
| Pin | Chức năng | Ghi chú |
|---|---|---|
| PA9/PA10 | USART1 TX/RX | debug + ESP-AT |
| PB6/PB7 | I2C1 SCL/SDA | 100 kHz, pull-up 4.7k |
| PC13 | LED status | active low |
| PA0 | Wake (EXTI) | nút nhấn |

## 4. BOM
| Linh kiện | SL | Giá | Nguồn |
|---|:--:|:--:|---|
| STM32F411 Black Pill | 1 | 95k | Shopee |
| SHT31 module | 1 | 60k | ... |

## 5. Metrics (đo thật, có số)
| Chỉ số | Giá trị | Cách đo |
|---|:--:|---|
| Sleep current | **42 µA** | multimeter nối tiếp, đo ở `stop mode` |
| Active current | 38 mA | trong lúc truyền |
| Battery life | **9 ngày** | 18650 3000mAh / dòng trung bình |
| Uptime liên tục | **11 ngày** | log timestamp |
| Latency end-to-end | 240 ms | `millis()` từ sample → ack |

## 6. Chạy lại (3 lệnh)
```bash
make flash          # build + nạp qua ST-Link
make monitor        # xem log UART 115200
docker compose up   # broker + dashboard
```

## 7. Bug khó nhất đã fix
> Mô tả 1 bug thật: triệu chứng → giả thuyết → cách tìm ra → root cause → fix.
> **Đây là phần nhà tuyển dụng đọc kỹ nhất.** Nó chứng minh bạn thật sự làm, không copy.

## 8. Hướng phát triển
- [ ] OTA firmware
- [ ] Thêm BME280 đo áp suất
- [ ] Sơ đồ mạch + PCB

## Tech
`C` `STM32` `FreeRTOS` `I2C` `MQTT` `low-power` `Makefile`
