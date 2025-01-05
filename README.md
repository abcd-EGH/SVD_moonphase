# SVD_moonphase
**Stable Video Diffusion Fine-Tuning Code for Moon Phases Video w/ LoRA**

**As part of the AITAP lecture at Hanyang University, we fine tune SVD with reference to the github:** [SVD_Xtend](https://github.com/pixeli99/SVD_Xtend)

## Project Overview
The primary objective of this project was to fine-tune the Stable Video Diffusion model. Initially, the model was unable to display the phases of the moon even when given images of the moon as input. However, **after fine-tuning, the model successfully generates outputs that visually represent the changing phases of the moon over time** when provided with moon imagery as input.

## Colab Notebook
The fine-tuning process was conducted using Google Colab. You can access the notebook via the following link:  
[Colab Notebook](https://colab.research.google.com/drive/1V4vTzM4T6fcK8TMWbKIFkBw8Q2rZVGYX?usp=sharing)  
**GPU Used:** NVIDIA A100

## Training Video Sources & Dataset
The fine-tuning dataset was prepared using the following videos: 
https://svs.gsfc.nasa.gov/5415/

Specially, we need the moon phase video like this: 
https://svs.gsfc.nasa.gov/5415/#media_group_376356

1. To prepare the dataset, create an `original` folder containing one or more `.mp4` video files in the same directory as `videoframe.py`. (It's okay if there's only one video)
```bash
videoframe.py
original
    ├── video_name1.mp4
    ├── video_name2.mp4
    ├── ...
```

2. When you run `videoframe.py`, frames from each video will be extracted and stored in the `finetuning` folder. (By default, frames are extracted at an interval of 10, which can be adjusted using the `FRAME_INTERVAL` variable in `videoframe.py`.)
```bash
videoframe.py
original
    ├── video_name1.mp4
    ├── video_name2.mp4
    ├── ...
finetuning
    ├── video_name1
    │   ├── video_frame1
    │   ├── video_frame2
    │   ...
    ├── video_name2
    │   ├── video_frame1
    │   ├── ...
```
3. Create a `finetuning.zip` file as shown and save it to Google Drive.
```bash
finetuning.zip
    ├── finetuning
    │   ├── video_name1
    │   │   ├── video_frame1
    │   │   ├── video_frame2
    │   │   ├── ...
    │   ├── video_name2
    │   │   ├── video_frame1
    │   │   ├── ...
```

4. Share the zip file to generate a shareable link, and modify the link as shown below to include it in the `.ipynb` file for downloading in Colab.
```bash
# share link: https://drive.google.com/file/d/{file_id}/view?usp=sharing

!gdown https://drive.google.com/uc?id={file_id}
!unzip /content/finetuning.zip -d /content
```

## Results
### Comparison by fine tuning
| Init Image | Before Fine-tuning | After Fine-tuning |
|------------|--------------------|-------------------|
|<img src=".asset\moon1_frame_10.png" width="256" height="160">|<img src=".asset\output.gif" width="256" height="160">|<img src=".asset\output_finetuning.gif" width="256" height="160">|

### Comparison by Train Step (Total steps: 5,000)
| 1,000 Steps | 2,000 Steps | 3,000 Steps |
|-------------|-------------|-------------|
|<img src=".asset\step_1000_val_img_0.gif" width="256" height="160">|<img src=".asset\step_2000_val_img_0.gif" width="256" height="160">|<img src=".asset\step_3000_val_img_0.gif" width="256" height="160">|

## Limitations and Improvements
### 1. Training Video Size and Step Restrictions
Due to usage limitations in Colab, the training video size was set to `width=512`, `height=320`, and `step=5000`. Increasing the size and step values could result in higher resolution and better performance.

### 2. Limited Dataset
Only two moon videos were used as the dataset. Expanding the dataset with more diverse videos could improve the model's generalization performance.

##  TODO List
- [x] Update README.md
- [ ] Upload fine-tuned model to the HuggingFace

## Acknowledgement
This project is related to [Diffusers](https://github.com/huggingface/diffusers), [Stability AI](https://github.com/Stability-AI/generative-models) and [SVD_Xtend](https://github.com/pixeli99/SVD_Xtend). Thanks for their great work.
