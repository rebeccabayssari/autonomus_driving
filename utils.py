import os
import base64
import glob
import io
import numpy as np
from IPython.display import HTML, display
from stable_baselines3.common.vec_env import VecVideoRecorder, DummyVecEnv

def record_videos(env, model, video_length=500, prefix="", folder="videos/"):
    env = DummyVecEnv([lambda: env])
    env = VecVideoRecorder(
        env,
        folder,
        record_video_trigger=lambda x: x == 0,
        video_length=video_length,
        name_prefix=prefix,
    )
    obs = env.reset()
    for _ in range(video_length + 1):
        action, _ = model.predict(obs)
        obs, _, done, _ = env.step(action)
        if done:
            obs = env.reset()
    env.close()

def show_videos(folder="videos/"):
    mp4list = glob.glob(os.path.join(folder, "*.mp4"))
    if len(mp4list) > 0:
        for mp4 in mp4list:
            video = io.open(mp4, "r+b").read()
            encoded = base64.b64encode(video)
            display(
                HTML(
                    data=f'''
                <video alt="{mp4}" autoplay controls style="height: 400px;">
                <source src="data:video/mp4;base64,{encoded.decode("ascii")}" type="video/mp4"/>
                </video>'''
                )
            )
    else:
        print("No videos found")