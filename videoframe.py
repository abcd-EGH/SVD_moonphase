import cv2
import os
import glob

# Directory containing the original video files
video_dir = 'img2vid_dataset/original'
path_dir = './'
video_path = os.path.join(path_dir, video_dir)
MAX_SAVED_FRAMES = 1e+10  # Maximum number of frames to save
FRAME_INTERVAL = 10       # Interval between frames to save
width_resize, height_resize = 1024, 576  # Resized image dimensions

# Output directory for finetuning
output_base_dir = os.path.join(path_dir, 'img2vid_dataset', 'finetuning')

# Check if the directory containing the original videos exists
if not os.path.exists(video_path):
    print(f"Video directory does not exist: {video_path}")
    exit(1)

# Create the output directory for finetuning if it doesn't exist
os.makedirs(output_base_dir, exist_ok=True)

# Get the list of .mp4 files
file_list = glob.glob(os.path.join(video_path, '*.mp4'))

if not file_list:
    print(f"No .mp4 files found in: {video_path}")
    exit(1)

for file in file_list:
    print(f"Processing file: {file}")
    vidcap = cv2.VideoCapture(file)
    
    # Check if the video file was successfully opened
    if not vidcap.isOpened():
        print(f"Error opening video file: {file}")
        continue
    
    # Print video information
    total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    width = int(vidcap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(f"Total Frames: {total_frames}, FPS: {fps}, Resolution: {width}x{height}")
    
    # Extract the base name of the file (without extension)
    file_base = os.path.splitext(os.path.basename(file))[0]
    
    # Set the output directory for each video file
    output_dir = os.path.join(output_base_dir, file_base)
    os.makedirs(output_dir, exist_ok=True)
    
    frame_count = 0  # Count of all frames processed
    saved_count = 0  # Count of frames saved
    
    while True:
        success, image = vidcap.read()
        if not success:
            if frame_count == 0:
                print("There is no frame to read or the video is empty.")
            else:
                print("End of video reached.")
            break
        
        if image is None:
            print("Read a frame but it's None.")
            break
        
        # Frame number (starting from 1)
        frame_number = frame_count + 1
        
        # Save every FRAME_INTERVAL-th frame (e.g., 5, 10, 15, ...)
        if frame_number % FRAME_INTERVAL == 0:
            if saved_count >= MAX_SAVED_FRAMES:
                print(f"Reached maximum saved frames ({MAX_SAVED_FRAMES}). Stopping frame extraction.")
                break  # Stop the loop if the maximum number of frames to save is reached
            
            # Attempt to resize the image while preserving data type
            try:
                image_resized = cv2.resize(image, (width_resize, height_resize), interpolation=cv2.INTER_AREA)
            except Exception as e:
                print(f"Error resizing frame {frame_number}: {e}")
                break
            
            # Set the save path
            title = os.path.join(output_dir, f"{file_base}_frame_{frame_number}.png")
            try:
                cv2.imwrite(title, image_resized)
                saved_count += 1
            except Exception as e:
                print(f"Error saving frame {frame_number}: {e}")
                break
        
        frame_count += 1
    
    vidcap.release()  # Release resources
    print(f"Finished processing {file}, total frames saved: {saved_count}\n")