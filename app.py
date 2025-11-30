import streamlit as st
import cv2
import tempfile
from ultralytics import YOLO
import imageio
import os

# ---------------- YOLO Model ----------------
st.title("🚀 Real-Time YOLOv8 Video Detection")
model = YOLO("yolov8n.pt")  # Fast lightweight model

# ---------------- Function to Process Video ----------------
def detect_objects_in_video(video_path):
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS)) or 25

    # Temporary output file
    temp_output = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    output_path = temp_output.name
    temp_output.close()

    writer = imageio.get_writer(output_path, fps=fps, codec="libx264")

    progress_text = st.empty()
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    processed_frames = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, imgsz=640, conf=0.3)  # smaller imgsz = faster
        annotated_frame = results[0].plot()

        writer.append_data(cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB))

        # Progress bar update
        processed_frames += 1
        progress_text.text(f"⚡ Processing frame {processed_frames}/{total_frames}")

    cap.release()
    writer.close()

    # Read video as bytes for Streamlit
    with open(output_path, "rb") as f:
        video_bytes = f.read()

    try:
        os.remove(output_path)
    except PermissionError:
        pass

    return video_bytes

# ---------------- Streamlit UI ----------------
st.write("Upload a short video to see YOLOv8 detections 🔍")

uploaded_file = st.file_uploader("🎬 Choose a video file", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    # Save uploaded video to temp file
    temp_input = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    temp_input.write(uploaded_file.read())
    temp_input.close()

    st.subheader("▶️ Original Video")
    st.video(temp_input.name)

    st.write("🛠️ Running YOLOv8… please wait")
    video_bytes = detect_objects_in_video(temp_input.name)

    st.subheader("✅ Processed Output")
    st.video(video_bytes)

    # Optional: download button
    st.download_button(
        label="📥 Save Processed Video",
        data=video_bytes,
        file_name="yolo_output.mp4",
        mime="video/mp4"
    )

    # Cleanup
    try:
        os.remove(temp_input.name)
    except PermissionError:
        pass
