# 🖱️ Mouse Logger (Python)

**Mouse Logger** is a lightweight Python script that records mouse activity including movements, clicks, and scroll actions. It’s built using the `pynput` library and designed for educational, research, or testing purposes in a controlled environment.

---

## 📌 Features

- Logs mouse movement with real-time coordinates  
- Captures left/right/middle clicks and their locations  
- Records scroll wheel activity  
- Periodically writes logs to a file (`mouselog.txt`)  
- Customizable log interval and file name  

---

## 📂 How It Works

The logger uses the `pynput.mouse.Listener` class to monitor mouse events:

- `on_move`: Tracks cursor movement  
- `on_click`: Logs button presses and releases  
- `on_scroll`: Captures scroll events  

All logs are buffered and flushed to a file every 10 seconds by a background thread, ensuring minimal performance impact.

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3 installed. Then, install `pynput`:

```bash
pip install pynput
```

then Run the script

```bash
python mouse_logger.py
```

## ⚠️ Disclaimer

This tool is provided strictly for educational and ethical testing purposes only. Unauthorized use of surveillance software is illegal and may violate privacy laws. Do not run this tool on any system without explicit consent from the device owner.

!!I STILL HAVEN'T TESTED THE CODE!!



