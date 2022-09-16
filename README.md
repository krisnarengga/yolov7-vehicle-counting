# yolov7-vehicle-counting
Demonstrating vehicles traffic counting using yolov7 and deepsort

This app is demonstrate simple vehicle counting on toll road or highway

This app is based on YOLOV7 object detection library engine from WongKinYiu repository on https://github.com/WongKinYiu/yolov7 and based on DeepSort object tracking implementation

Run this command to run the app
python detect_count_and_track.py --weights yolov7-tiny.pt --conf 0.55 --source traffic.mp4 --view-img --nosave --no-trace

Notes:
You can download yolov7-tiny or yolov7 weights from YOLOV7 assets repository https://github.com/WongKinYiu/yolov7/releases

App Demo:
https://youtu.be/KVj53FgF2ow

Sample Video:
https://drive.google.com/file/d/119FPTQ3FyK6J_16WZUzQUCD9R0PD9In-/view?usp=sharing
