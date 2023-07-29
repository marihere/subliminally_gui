from librosa import *
from moviepy.editor import *


def video_creator(title, img_path):
    img = ImageClip(img_path).set_opacity(0.50)
    audio = AudioFileClip('subliminals/audios/' + title + '.wav')
    title_txt = TextClip(title, font='lib/.assets/akira_expanded_demo.otf', fontsize=70, color='white')
    watermark_txt = TextClip('\n\nmade with subliminally', font='lib/.assets/plank.otf', fontsize=20, color='white')

    clip = img.set_duration(audio.duration)
    video = clip.set_audio(audio)
    title_txt = title_txt.set_position('center').set_duration(audio.duration)
    video = CompositeVideoClip([video, title_txt])
    watermark_txt = watermark_txt.set_position('center').set_duration(audio.duration)
    video = CompositeVideoClip([video, watermark_txt])

    video.write_videofile('subliminals/videos/' + title + '.mp4', fps=10)

    return 'complete'

