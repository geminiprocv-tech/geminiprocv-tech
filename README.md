<!--
  ============================================================
  PROFILE README v2 — BẢN CHUYÊN NGHIỆP (khuyên dùng)
  Dán vào repo: geminiprocv-tech/geminiprocv-tech (Public, tên trùng username)
  Upload kèm thư mục assets/ (banner.svg + divider.svg)

  Khác bản v1: bỏ badge wall, bỏ snake, bỏ 3 stats card, bỏ emoji heading.
  Mỗi chỗ <!-- EDIT --> là phải sửa theo dữ liệu thật.
  Nguyên tắc: 1 màn hình, 1 stats widget, 4 repo pin.
  ============================================================
-->

<p align="center">
  <img src="assets/banner.svg" alt="geminiprocv-tech — Embedded Systems · IoT · Edge AI" width="100%"/>
</p>

**Computer Engineering student building low-power sensor nodes and on-device inference.**
I work from firmware up: hand-written drivers, RTOS task sets, quantized models, and the
infrastructure that keeps the whole thing observable. Looking for an **embedded / edge-AI internship**
in Da Nang or remote.

### Now

- Building **sensor-node** — bare-metal STM32 with FreeRTOS, MQTT uplink, 42 µA sleep current.
- Learning FreeRTOS internals and INT8 quantization on Jetson.
- Next milestone: end-to-end system (node → on-device model → cloud dashboard).

<!-- EDIT: cập nhật 3 gạch đầu dòng này mỗi 2–4 tuần. Đây là phần duy nhất cho thấy profile còn sống. -->

### Selected work

**sensor-node** — Battery-powered sensor node for indoor climate monitoring.
Bare-metal STM32 with a hand-written I2C driver (no HAL), FreeRTOS task set, MQTT uplink,
flash buffer that survives network loss. Runs 9 days on a single 18650 at 42 µA sleep.
`C` · `FreeRTOS` · `STM32` · `MQTT` → [repo](https://github.com/geminiprocv-tech) <!-- EDIT -->

**edge-vision** — On-device people counting for a fixed power budget.
INT8-quantized YOLOv8n on Jetson Nano: 24 FPS (from 9), 6.1 MB model, 1.2% mAP cost.
The interesting part was not accuracy — it was the size/latency trade-off.
`Python` · `PyTorch` · `TensorRT` · `OpenCV` → [repo](https://github.com/geminiprocv-tech) <!-- EDIT -->

**iot-dashboard** — API and dashboard for a small device fleet.
14 endpoints, time-series ingestion at 1.2 M rows/day, p95 85 ms. Built to keep reads cheap
while writes grow.
`Java` · `Spring Boot` · `PostgreSQL` → [repo](https://github.com/geminiprocv-tech) <!-- EDIT -->

<!-- EDIT: nếu chưa có project 3–4 thì XOÁ dòng đó. 3 dòng thật > 5 dòng mẫu. -->

### Numbers I can defend

| Metric | Value | How it was measured |
|---|:--:|---|
| Sleep current | **42 µA** | multimeter in series, STM32 stop mode |
| Battery life | **9 days** | 18650 3000 mAh ÷ average draw |
| On-device throughput | **24 FPS** | INT8 TensorRT, Jetson Nano, 640×640 |
| API latency (p95) | **85 ms** | load test, 12 devices, 7-day window |

> Nhà tuyển dụng nhúng **sẽ hỏi** "đo bằng gì". Bảng này là để bạn trả lời được ngay — và cũng là
> lý do đừng điền số khi chưa đo.

### Stack

**Firmware:** C, C++, bare-metal, FreeRTOS, STM32, ESP32, I²C / SPI / UART / CAN
**Device AI:** PyTorch, OpenCV, TensorRT, ONNX, INT8 quantization
**Backend:** Java, Spring Boot, PostgreSQL, REST, MQTT
**Infra:** Linux, Docker, GitHub Actions, Prometheus, Git

<!-- Không dùng badge wall. 4 dòng text này đọc nhanh hơn 25 cái badge và không bị coi là filler. -->

### Reach

[Email](mailto:YOUR@EMAIL.COM) · [LinkedIn](https://www.linkedin.com/in/YOUR-HANDLE) · [CV](cv.pdf) <!-- EDIT -->

<br/>

<sub>Da Nang, Vietnam (GMT+7) · open to internship from 2027</sub>
<!-- EDIT -->

<p align="center">
  <img src="assets/divider.svg" alt="" width="100%"/>
</p>

<!--
  TUỲ CHỌN — ĐÚNG MỘT stats widget. Bỏ comment nếu muốn. Đừng thêm cái thứ hai.
  <p align="center">
    <img height="150" src="https://github-readme-stats.vercel.app/api?username=geminiprocv-tech&show_icons=true&hide_border=true&hide_title=true&bg_color=0b2130&title_color=8fd6ff&text_color=a8c6d4&icon_color=8fd6ff" alt="GitHub stats"/>
  </p>
-->

<!--
  TUỲ CHỌN — nếu bạn vẫn thích motif terminal, cho vào <details> để không chiếm màn hình.
  <details>
    <summary>boot log</summary>

  ```console
  [ 0.000] probing I2C bus 0 ......... 3 devices
  [ 1.000] profile: EMBEDDED · IoT · EDGE AI
  [ 1.002] status: online
  ```

  </details>
-->
