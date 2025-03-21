import os, torch, cv2, numpy as np
from showtens import show_image,save_image
import pygame
import json

def launch_video(size,fps,fourcc='avc1'):
    """
        Returns Videowriter, ready to record and save the video.

        Parameters:
        size: (H,W) 2-uple size of the video
        fps: int, frames per second
        fourcc : Encoder, must work with .mp4 videos
    """
    os.makedirs('videos',exist_ok=True)
    fourcc = cv2.VideoWriter_fourcc(*fourcc)
    numvids = len(os.listdir('videos/'))
    vid_loc = f'videos/vid_{numvids}.mp4'
    return cv2.VideoWriter(vid_loc, fourcc, fps, (size[1], size[0]))

def add_frame(writer, worldsurface):
    worldmap = pygame.surfarray.array3d(worldsurface) # (W,H,3)

    frame = worldmap.transpose(1,0,2) # (H,W,3)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    writer.write(frame)

def print_screen(worldsurface):
    worldmap = pygame.surfarray.array3d(worldsurface) # (W,H,3)
    os.makedirs('images',exist_ok=True)
    numimgs = len(os.listdir('images/'))
    img_name = f'img_{numimgs}'
    save_image(torch.tensor(worldmap,dtype=float).permute(2,1,0)/255.,folder='images',name = img_name)

