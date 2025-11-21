

# **DragonFlyBot – User Guide**

## **System Requirements**

* Python 3.8+
* Windows / macOS / Linux
* Minimum 4GB RAM
* At least 2GB of free disk space

---

## **Installation and Setup**

### **Step 1: Download or Clone the Project**

```bash
cd /path/to/your/folder
# Or download the ZIP file and extract it
```

### **Step 2: Create a Virtual Environment**

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
python -m venv .venv
source .venv/bin/activate
```

### **Step 3: Install Dependencies**

```bash
pip install --upgrade pip
pip install torch transformers datasets flask flask-cors
```

### **Step 4: Verify data.txt Format**

Make sure the file follows this structure:

```
User: Question 1?
Bot: Answer 1

User: Question 2?
Bot: Answer 2
```

---

## **Running the Chatbot**

### **Method 1: Run Direct Chat in Terminal**

```bash
python chatbot.py
```

**Usage:**

* Type your question → press Enter
* Type `exit` or `quit` to stop

**Example:**

```
You: Where is Duy Tan University?
Bot: The main campus is located at 254 Nguyen Van Linh, Da Nang.

You: exit
```

---

### **Method 2: Run the API Server (for Android or Web Apps)**

**Start the server:**

```bash
python server.py
```

Expected output:

```
 * Running on http://0.0.0.0:5000
```

**Test the API:**

```bash
python test_api.py
```

**Calling from Android (POST request):**

```
URL: http://your-ip:5000/chat
Method: POST
Content-Type: application/json

Body:
{
  "message": "Where is Duy Tan University?"
}
```

**Response Example:**

```json
{
  "success": true,
  "reply": "The main campus is located at 254 Nguyen Van Linh, Da Nang.",
  "found": true
}
```

---

## **Project Structure**

| File                | Description                         |
| ------------------- | ----------------------------------- |
| chatbot.py          | Terminal-based chatbot interface    |
| server.py           | Flask API server                    |
| data.txt            | Bot knowledge base                  |
| train_gpt2.py       | Train model (run once)              |
| train_vietnamese.py | Optional Vietnamese training script |

---

## **Configuration**

### Adjust Answer Accuracy

Inside `chatbot.py`:

```python
def find_best_match(user_input, threshold=0.70):
```

* `0.70` → balanced
* `0.60` → more flexible
* `0.80` → more strict

### Adding New Q&A

Edit `data.txt`:

```
User: New question?
Bot: New answer
```

Save the file — the bot will immediately use the new data.

---

## **API Endpoints**

| Endpoint  | Method | Description                    |
| --------- | ------ | ------------------------------ |
| `/`       | GET    | Check if the server is running |
| `/health` | GET    | System health check            |
| `/info`   | GET    | Bot information                |
| `/chat`   | POST   | Send a message to the bot      |

**Example:**

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

## **Troubleshooting**

### Error: `ModuleNotFoundError: No module named 'transformers'`

```bash
pip install transformers
```

### Error: `data.txt not found`

Make sure the file exists inside the project folder.

### Port 5000 is already in use

Edit in `server.py`:

```python
app.run(host="0.0.0.0", port=5001, debug=True)
```

### Bot inaccurate

* Add more Q&A to `data.txt`
* Adjust threshold (e.g., 0.75)

---

## **Android Integration**

**Update URL:**

```java
String url = "http://192.168.1.x:5000/chat";
```

**Send request:**

```java
JSONObject json = new JSONObject();
json.put("message", "Where is Duy Tan University?");
```

---

## **Verification Checklist**

```bash
python server.py      # Terminal 1
python test_api.py    # Terminal 2
```

If JSON appears → API is working correctly.

---

## **Tips**

* The most important file is `data.txt`
* No need to retrain after updating Q&A
* Use real IP instead of `localhost` when accessing from another device
* More Q&A = better bot performance

---


