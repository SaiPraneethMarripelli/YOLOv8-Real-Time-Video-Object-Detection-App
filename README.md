# 🚀 YOLOv8 Real-Time Video Object Detection App  
### *Streamlit + YOLOv8 + OpenCV + ImageIO*

This project is a **real-time video object detection application** built using the **YOLOv8** deep learning model.  
Users can upload any short video and get a **processed output video** with bounding boxes, labels, and confidence scores drawn on detected objects — all displayed interactively in a **Streamlit web app**.

---

## 📌 Project Overview  
Object detection is a core computer vision task with applications in surveillance, autonomous driving, robotics, and more.  
This project demonstrates how to:

✔ Run YOLOv8 inference on videos  
✔ Process frames in real-time  
✔ Display and download annotated videos  
✔ Build a user-friendly Streamlit interface  

The app uses the lightweight **YOLOv8n** model for fast processing.

---

## 🧠 Features  
### 🔍 Key Features
- Upload any video (`mp4`, `avi`, `mov`)  
- Process video with YOLOv8 object detection  
- Real-time frame-by-frame annotation  
- Progress indicator during processing  
- Live preview of original vs processed video  
- Download final YOLO output video  
- Automatically handles temporary file cleanup  

---

## 🛠 Tech Stack  
| Component | Technology |
|----------|------------|
| Frontend | Streamlit |
| Object Detection | YOLOv8n (Ultralytics) |
| Video Processing | OpenCV, ImageIO |
| Programming Language | Python |
| Dependencies | ultralytics, cv2, imageio, streamlit |

---

## 📁 Project Structure  

```
YOLO-Video-Detection/
│── app.py                    # Main Streamlit App
│── requirements.txt          # Project dependencies
│── README.md                    # Documentation
```

---

## ▶ How to Run the Project Locally  

### 1️⃣ Clone the Repository  
```
git clone https://github.com/SaiPraneethMarripelli/yolo-video-detection.git
cd yolo-video-detection
```

### 2️⃣ Install Dependencies  
```
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App  
```
streamlit run app.py
```

---

## 🎬 Usage  

1. Launch the Streamlit app  
2. Upload a short video file  
3. Wait for YOLOv8 to process  
4. View original & processed videos  
5. Download output if needed  

---

## 🚀 Future Enhancements  
- Add webcam support  
- Allow choosing different YOLOv8 models  
- GPU acceleration support  
- Add visualization dashboard  
- Per-class filtering  

---

## 👤 Author  
**Sai Praneeth Marripelli**  
📧 Email: saipraneethmarripelli@gmail.com  
🔗 LinkedIn: www.linkedin.com/in/saipraneeth-marripelli-2003sai

---

## ⭐ Support  
If this project helped you, please ⭐ star the repository!
