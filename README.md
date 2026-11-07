<!--
  PROFILE README — dán vào repo: geminiprocv-tech/geminiprocv-tech (repo PUBLIC, tên trùng username)
  Banner: mặc định dùng assets/banner.svg (nền tối, xanh nhạt làm điểm nhấn — hiển thị tốt ở cả dark & light mode)
          muốn nền sáng hoàn toàn thì đổi thành assets/banner-lite.svg
  Chỗ nào có <!-- EDIT --> là phải sửa theo dữ liệu thật.
-->

<p align="center">
  <img src="assets/banner.svg" alt="geminiprocv-tech — Embedded Systems, IoT, Edge AI" width="100%"/>
</p>

```console
geminiprocv@edge-node:~$ ./boot.sh
[    0.000] Booting geminiprocv-tech v1.0 ...................... OK
[    0.214] Mounting /skills ....................... 8 modules
[    0.402] Probing I2C bus 0 ......................... 3 devices found
[    0.611] Calibrating sensors ......................... stable
[    0.800] Loading model (int8, on-device) ............. 24 fps
[    1.000] Target profile: EMBEDDED · IoT · EDGE AI
[    1.002] Status: online — building, learning, shipping
```

<h3 align="center">I build small machines that sense the world, think locally, and talk over the wire.</h3>

<p align="center">
  <img src="https://img.shields.io/badge/FOCUS-firmware%20%C2%B7%20edge%20ai%20%C2%B7%20iot%20infra-8fd6ff?style=for-the-badge&labelColor=0b2130" alt="focus"/>
  <img src="https://img.shields.io/badge/BASE-da%20nang%2C%20vn-8fd6ff?style=for-the-badge&labelColor=0b2130" alt="location"/>
  <img src="https://img.shields.io/badge/OPEN%20TO-internship-8fd6ff?style=for-the-badge&labelColor=0b2130" alt="open to"/>
</p>

<p align="center">
  <img src="assets/divider.svg" alt="" width="100%"/>
</p>

## 🛰 Device status

| FIELD | VALUE |
|---|---|
| `DEVICE_ID` | **geminiprocv-tech** |
| `ROLE` | Computer Engineering student |
| `LOCATION` | Hoi An / Da Nang, Vietnam |
| `PRIMARY_BUS` | Embedded firmware · IoT systems · Edge AI |
| `CURRENT_MISSION` | Building an end-to-end sensor → edge AI → cloud system |
| `UPTIME` | learning since 2024 <!-- EDIT --> |
| `STATUS` | 🟢 online — open to internship & junior roles |

## ⚡ Bus topology — what I work with

**MCU / boards**
<br/>
<img src="https://img.shields.io/badge/STM32-8fd6ff?style=flat-square&labelColor=0b2130" alt="stm32"/>
<img src="https://img.shields.io/badge/ESP32-8fd6ff?style=flat-square&labelColor=0b2130" alt="esp32"/>
<img src="https://img.shields.io/badge/Raspberry%20Pi-8fd6ff?style=flat-square&labelColor=0b2130" alt="raspberry pi"/>
<img src="https://img.shields.io/badge/Jetson%20Nano-8fd6ff?style=flat-square&labelColor=0b2130" alt="jetson"/>
<img src="https://img.shields.io/badge/FPGA-8fd6ff?style=flat-square&labelColor=0b2130" alt="fpga"/>

**Languages**
<br/>
<img src="https://img.shields.io/badge/C-8fd6ff?style=flat-square&labelColor=0b2130" alt="c"/>
<img src="https://img.shields.io/badge/C%2B%2B-8fd6ff?style=flat-square&labelColor=0b2130" alt="cpp"/>
<img src="https://img.shields.io/badge/Python-8fd6ff?style=flat-square&labelColor=0b2130" alt="python"/>
<img src="https://img.shields.io/badge/Java-8fd6ff?style=flat-square&labelColor=0b2130" alt="java"/>
<img src="https://img.shields.io/badge/Bash-8fd6ff?style=flat-square&labelColor=0b2130" alt="bash"/>
<img src="https://img.shields.io/badge/SystemVerilog-8fd6ff?style=flat-square&labelColor=0b2130" alt="sv"/>

**Protocols**
<br/>
<img src="https://img.shields.io/badge/I2C-8fd6ff?style=flat-square&labelColor=0b2130" alt="i2c"/>
<img src="https://img.shields.io/badge/SPI-8fd6ff?style=flat-square&labelColor=0b2130" alt="spi"/>
<img src="https://img.shields.io/badge/UART-8fd6ff?style=flat-square&labelColor=0b2130" alt="uart"/>
<img src="https://img.shields.io/badge/MQTT-8fd6ff?style=flat-square&labelColor=0b2130" alt="mqtt"/>
<img src="https://img.shields.io/badge/BLE-8fd6ff?style=flat-square&labelColor=0b2130" alt="ble"/>
<img src="https://img.shields.io/badge/CAN-8fd6ff?style=flat-square&labelColor=0b2130" alt="can"/>

**Infra & tools**
<br/>
<img src="https://img.shields.io/badge/Linux-8fd6ff?style=flat-square&labelColor=0b2130" alt="linux"/>
<img src="https://img.shields.io/badge/Docker-8fd6ff?style=flat-square&labelColor=0b2130" alt="docker"/>
<img src="https://img.shields.io/badge/GitHub%20Actions-8fd6ff?style=flat-square&labelColor=0b2130" alt="actions"/>
<img src="https://img.shields.io/badge/PostgreSQL-8fd6ff?style=flat-square&labelColor=0b2130" alt="postgres"/>
<img src="https://img.shields.io/badge/PyTorch-8fd6ff?style=flat-square&labelColor=0b2130" alt="pytorch"/>
<img src="https://img.shields.io/badge/OpenCV-8fd6ff?style=flat-square&labelColor=0b2130" alt="opencv"/>
<img src="https://img.shields.io/badge/Git-8fd6ff?style=flat-square&labelColor=0b2130" alt="git"/>

<p align="center">
  <img src="assets/divider.svg" alt="" width="100%"/>
</p>

## 📡 Active nodes — projects

> Mỗi dòng = một thiết bị trong mạng. Thay bằng dự án thật (xóa dòng mẫu khi đã có).
> **Quy tắc kể:** nêu *số đo được* — dòng điện sleep, FPS, độ trễ, kích thước model, uptime.

| NODE | STACK | TELEMETRY | STATUS |
|---|---|:--:|:--:|
| [**sensor-node**](https://github.com/geminiprocv-tech) <!-- EDIT --> | `C` `STM32` `I2C` `MQTT` | sleep **42 µA**, battery **9 days** | 🟢 done |
| [**edge-vision**](https://github.com/geminiprocv-tech) <!-- EDIT --> | `Python` `YOLOv8n` `TensorRT` | **24 FPS** after INT8, model **6.1 MB** | 🟡 wip |
| [**iot-dashboard**](https://github.com/geminiprocv-tech) <!-- EDIT --> | `Java` `Spring` `PostgreSQL` | p95 **85 ms**, **1.2 M** rows/day | 🟡 wip |
| [**node-infra**](https://github.com/geminiprocv-tech) <!-- EDIT --> | `Docker` `CI/CD` `Prometheus` | deploy **1 command**, pipeline **92 s** | 🔵 planned |

<p align="center">
  <img src="assets/divider.svg" alt="" width="100%"/>
</p>

## 📈 Telemetry

<p align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=geminiprocv-tech&show_icons=true&hide_border=true&bg_color=0b2130&title_color=8fd6ff&text_color=a8c6d4&icon_color=8fd6ff&include_all_commits=true&count_private=true" alt="GitHub stats"/>
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=geminiprocv-tech&layout=compact&hide_border=true&bg_color=0b2130&title_color=8fd6ff&text_color=a8c6d4&langs_count=8" alt="Top languages"/>
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=geminiprocv-tech&bg_color=0b2130&color=8fd6ff&line=4fb8e8&point=cdeeff&area=true&hide_border=true" alt="activity graph" width="100%"/>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/geminiprocv-tech/geminiprocv-tech/output/github-snake-dark.svg" alt="contribution snake" width="100%"/>
</p>

<p align="center">
  <img src="assets/divider.svg" alt="" width="100%"/>
</p>

## 🔌 Pinout — get in touch

| PIN | SIGNAL |
|:--:|---|
| `TX` | [![LinkedIn](https://img.shields.io/badge/LinkedIn-8fd6ff?style=flat-square&labelColor=0b2130)](https://www.linkedin.com/in/YOUR-HANDLE) <!-- EDIT --> |
| `RX` | [![Email](https://img.shields.io/badge/Email-8fd6ff?style=flat-square&labelColor=0b2130)](mailto:YOUR@EMAIL.COM) <!-- EDIT --> |
| `GND` | Da Nang, Vietnam (GMT+7) |
| `3V3` | Open to **internship** & **junior embedded / edge AI** roles |

<br/>

<p align="center">
  <i>"If it doesn't have a debug LED and a log line, it doesn't exist."</i>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=geminiprocv-tech&label=node%20visits&color=8fd6ff&style=flat-square" alt="profile views"/>
</p>
