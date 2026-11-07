# NOW — 90 ngày đầu (07/11/2026 → 05/02/2027)

> Đây là kế hoạch đứng sau bảng "What I am working toward" trong profile.
> Điều duy nhất khiến profile này đáng tin: **bạn thật sự làm đúng file này.**
> Ngân sách: **15 giờ/tuần** (theo lộ trình học đã chốt). 13 tuần ≈ 195 giờ.

**Sprint hiện tại:** `1/13` — **C: pointers & memory**

---

## Định nghĩa "xong" của 90 ngày này

Không phải "học xong C". Cụ thể là:

- [ ] Viết được **một driver I²C cho STM32 không dùng HAL** — tự cấu hình thanh ghi, tự xử lý START/STOP/ACK
- [ ] Giải thích được **`volatile` làm gì** và tại sao bỏ nó ra thì ISR hỏng
- [ ] Đọc được **nhiệt độ + độ ẩm từ 1 cảm biến thật**, in ra UART, không dùng thư viện mẫu copy trên mạng
- [ ] Đo được **dòng tiêu thụ ở chế độ ngủ bằng đồng hồ vạn năng**, và **ghi lại con số đầu tiên** (chưa cần đẹp)
- [ ] Repo `stm32-sensor-node` công khai, README có **3 lệnh chạy** + **1 đoạn trade-off**

Đủ 5 dòng đó là bạn có thứ đầu tiên đáng để pin lên profile.
**Chưa đủ thì chưa đổi `fw_projects = 0`.** Đó là luật.

---

## 13 tuần

| Tuần | Nội dung | Giờ | Sản phẩm nhìn thấy được |
|:--:|---|:--:|---|
| 1 | C: con trỏ, mảng, quan hệ `a[i]` ↔ `*(a+i)`. Viết lại các bài tập cũ bằng con trỏ. | 12 | 10 bài tập trong `c-foundations/` |
| 2 | C: cấp phát động, `malloc/free`, lỗi rò rỉ. Chạy `valgrind` trên Linux. | 12 | 1 bài "tại sao chương trình này crash" có before/after |
| 3 | C: bit manipulation — `& | ^ ~ << >>`, đọc/ghi thanh ghi giả lập | 12 | Hàm `set_bit/clear_bit/toggle_bit` + test |
| 4 | C: `struct`, `union`, `volatile`, `const`. Viết **buffer vòng** cho UART RX | 15 | `ringbuf.c` có unit test |
| 5 | **Checkpoint 1.** Đọc datasheet STM32F4 chương GPIO + RCC. Bật LED bằng thanh ghi, không HAL | 15 | Video 15s LED nhấp nháy + giải thích từng dòng |
| 6 | Clock tree, SysTick, delay không dùng `HAL_Delay` | 15 | `delay_ms()` viết tay |
| 7 | UART: cấu hình, `printf` redirect, dùng buffer vòng tuần 4 | 15 | Log ra terminal, ảnh chụp |
| 8 | **Checkpoint 2.** I²C: hiểu START/ADDR/ACK/DATA. **Tự viết driver**, không HAL | 18 | `i2c.c` chạy được ở 100 kHz |
| 9 | Cảm biến thật (AHT20/BME280/SHT3x — chọn loại có datasheet rõ). Đọc nhiệt độ + độ ẩm | 15 | Số liệu thật hiện ra UART |
| 10 | Sleep mode: `WFI`, tắt clock ngoại vi. **Đo dòng bằng đồng hồ vạn năng** | 15 | **Con số µA đầu tiên** — ghi vào README |
| 11 | Viết README repo theo template (`templates/REPO-README.md`): demo, kiến trúc, pinout, 3 lệnh chạy, trade-off | 12 | Repo công khai, pin lên profile |
| 12 | Đo lại dòng, tính tuổi thọ pin, ghi sai số đo. Dọn code, tách file | 12 | Bảng số thật thay dòng `fw_projects = 0` |
| 13 | **Checkpoint 3.** Viết 1 bài blog/journal: "cái gì khó nhất khi bỏ HAL". Cập nhật `now.json` | 12 | 1 bài viết + profile tự cập nhật |

**Tổng: 178–195 giờ.** Đúng ngân sách 15h/tuần.

---

## Nhịp mỗi tuần (đừng học kiểu cảm hứng)

| Khi nào | Việc | Giờ |
|---|---|:--:|
| T2–T6, mỗi tối | 1h30 đọc + gõ lại ví dụ. **Không copy-paste** | 7.5 |
| T7 sáng | 3h làm bài tập/bật board | 3 |
| T7 chiều | 1h30 viết lại điều đã hiểu vào `notes/` | 1.5 |
| CN | 2h đệm — bù bài trượt, hoặc nghỉ nếu đã xong | 2 |
| **Cộng** | | **14–15** |

> MMO / việc làm thêm: **giữ dưới 4–6h/tuần** và phải sau 15h này, không phải thay vào.

---

## Checkpoint — tự chấm, không tự lừa

| | Câu hỏi | Đạt khi |
|:--:|---|---|
| **CP1** (tuần 5) | Bỏ HAL rồi, bạn còn bật được LED không? | giải thích được từng dòng ghi thanh ghi, không nhìn mẫu |
| **CP2** (tuần 8) | Driver I²C của bạn có tự viết không? | trả lời được "nếu thiết bị không ACK thì bạn thấy gì trên scope" |
| **CP3** (tuần 13) | Có **một con số đo được** chưa? | có số µA, có cách đo, có ảnh/ảnh chụp đồng hồ |

Trượt checkpoint → **cắt việc, không cắt deadline**: bỏ phần "hay ho" (RTOS, MQTT, edge AI) và làm cho xong phần lõi.

---

## Những thứ CỐ TÌNH không học trong 90 ngày này

Mỗi thứ dưới đây đều hấp dẫn và đều là bẫy ở giai đoạn này:

- ❌ **FreeRTOS** — chỉ có nghĩa khi đã viết được code chạy được trên bare-metal
- ❌ **MQTT / ESP32** — mạng che lấp lỗi firmware; xong I²C rồi hẵng lên mạng
- ❌ **TensorFlow Lite / edge AI** — đúng hướng nhưng là việc của năm 3–4
- ❌ **PCB design** — KiCad để dành khi đã hiểu peripheral
- ❌ **Chứng chỉ online** — 90 ngày này không có chỗ cho Coursera
- ❌ **Học thêm ngôn ngữ mới** — C chưa xong thì Python/JS/Rust đều là trốn việc

---

## Cách nộp bằng chứng (để profile không nói suông)

Mỗi tuần, đúng 1 commit vào `c-foundations/` hoặc `stm32-sensor-node/`:

```
w03: bit manipulation — set/clear/toggle + 8 test cases
w08: i2c driver, 100kHz, no HAL — START/ADDR/ACK handled manually
w10: sleep mode → 640 µA (down from 12 mA), measured with UT61E
```

Commit message có nội dung = lịch sử học của bạn. Recruiter mở tab Commits là thấy bạn học thật hay không. **Đây là lý do không cần badge nào cả.**

---

## Sau 90 ngày (05/02/2027)

1. Cập nhật `now.json`: `fw_projects` 0 → 1, `sprint` → sprint 2 (FreeRTOS hoặc MQTT)
2. Action tự chạy, README tự đổi. Không sửa tay.
3. Chuyển sang giai đoạn tiếp theo của `../career/LO-TRINH-HOC-4-PLAN.md`
