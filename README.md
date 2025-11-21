# 📚 DragonFlyBot - Hướng Dẫn Sử Dụng

## 📋 Yêu cầu hệ thống
- Python 3.8+
- Windows/Mac/Linux
- 4GB RAM (tối thiểu)
- 2GB disk space

---

## 🚀 Hướng dẫn cài đặt & chạy

### **Bước 1: Clone/Tải project**
```bash
cd /đường/dẫn/thư/mục
# Hoặc tải file zip và giải nén
```

### **Bước 2: Tạo Virtual Environment**
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python -m venv .venv
source .venv/bin/activate
```

### **Bước 3: Cài đặt Dependencies**
```bash
pip install --upgrade pip
pip install torch transformers datasets flask flask-cors
```

### **Bước 4: Kiểm tra file data.txt**
- Đảm bảo file data.txt có format đúng:
```
User: Câu hỏi 1?
Bot: Câu trả lời 1

User: Câu hỏi 2?
Bot: Câu trả lời 2
```

---

## 💬 Chạy Chatbot (2 cách)

### **Cách 1: Chat trực tiếp trong Terminal (Đơn giản)**
```bash
python chatbot.py
```
**Cách dùng:**
- Gõ câu hỏi → Enter
- Bot sẽ trả lời
- Gõ `exit` hoặc `thoát` để thoát

**Ví dụ:**
```
Bạn: Trường Duy Tân ở đâu?
Bot: Cơ sở chính của Duy Tân nằm ở 254 Nguyễn Văn Linh, Đà Nẵng...

Bạn: thoát
```

---

### **Cách 2: Chạy API Server (Cho ứng dụng)**

**Bước 1: Chạy server**
```bash
python server.py
```
Bạn sẽ thấy:
```
 * Running on http://0.0.0.0:5000
```

**Bước 2: Kiểm tra server hoạt động**

Mở terminal khác:
```bash
python test_api.py
```

**Bước 3: Gọi từ Android app**

Gửi HTTP POST request:
```
URL: http://your-ip:5000/chat
Method: POST
Header: Content-Type: application/json

Body:
{
  "message": "Trường Duy Tân ở đâu?"
}
```

**Response:**
```json
{
  "success": true,
  "reply": "Cơ sở chính của Duy Tân nằm ở 254 Nguyễn Văn Linh, Đà Nẵng...",
  "found": true
}
```

---

## 📁 Cấu trúc File

| File | Mục đích |
|------|---------|
| chatbot.py | Chat trực tiếp với bot |
| server.py | API server cho Android/Web |
| data.txt | **Kiến thức của bot** (quan trọng nhất) |
| train_gpt2.py | Train model (chạy 1 lần) |
| train_vietnamese.py | Train model Vietnamese (tuỳ chọn) |

---

## ⚙️ Tùy chỉnh

### Thay đổi độ chính xác trả lời

Sửa trong chatbot.py dòng:
```python
def find_best_match(user_input, threshold=0.70):
```

- `threshold=0.70` → Bot chỉ trả lời khi 70% chắc chắn
- `threshold=0.60` → Dễ dàng trả lời hơn
- `threshold=0.80` → Khó trả lời hơn, ít sai

### Thêm câu hỏi/trả lời mới

Mở data.txt và thêm:
```
User: Câu hỏi mới?
Bot: Câu trả lời mới

```

Lưu file → Bot sẽ sử dụng ngay (không cần restart)

---

## 🔗 API Endpoints (cho server.py)

| Endpoint | Method | Mô tả |
|----------|--------|-------|
| `/` | GET | Kiểm tra server hoạt động |
| `/health` | GET | Kiểm tra sức khỏe hệ thống |
| `/info` | GET | Thông tin bot |
| `/chat` | POST | Chat với bot |

**Ví dụ gọi `/info`:**
```bash
curl http://localhost:5000/info
```

Response:
```json
{
  "name": "DragonFlyBot",
  "version": "1.0",
  "qa_count": 108,
  "language": "Vietnamese"
}
```

---

## 🐛 Xử lý lỗi

### Lỗi: `ModuleNotFoundError: No module named 'transformers'`
```bash
pip install transformers
```

### Lỗi: `FileNotFoundError: data.txt not found`
- Đảm bảo file data.txt tồn tại trong thư mục project

### Lỗi: Port 5000 đã được sử dụng
```bash
# Sửa trong server.py dòng:
app.run(host="0.0.0.0", port=5001, debug=True)  # Đổi sang 5001
```

### Bot trả lời không chính xác
- Tăng số lượng Q&A trong data.txt
- Thay đổi `threshold` từ 0.70 → 0.75

---

## 📱 Tích hợp Android

**Sửa URL trong Android app:**
```java
String url = "http://192.168.1.x:5000/chat";  // Thay x = IP của server
```

**Gửi message:**
```java
JSONObject json = new JSONObject();
json.put("message", "Trường Duy Tân ở đâu?");
```

---

## ✅ Kiểm tra hoạt động

```bash
# 1. Mở terminal 1
python server.py

# 2. Mở terminal 2
python test_api.py

# 3. Nếu thấy response JSON → Hoạt động OK ✅
```

---

## 💡 Tips

- 📌 **Quan trọng nhất:** Cập nhật data.txt với nhiều Q&A chính xác
- 🔄 Không cần retrain model, chỉ cần edit data.txt
- 🌐 Để chạy server trên máy khác, dùng IP thực tế thay `localhost`
- 📊 Càng nhiều Q&A trong data.txt → Bot càng thông minh

---

## 📞 Hỗ trợ

Nếu có lỗi:
1. Kiểm tra terminal output
2. Đảm bảo data.txt format đúng
3. Cài đặt lại dependencies: `pip install -r requirements.txt`

Chúc bạn thành công! 🚀
