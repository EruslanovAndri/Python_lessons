from pytube import YouTube

def download_video_to_the_folder(user_link,path_to_folder):
    your_tube_video = YouTube(user_link)
    your_tube_video.streams.get_highest_resolution().download(path_to_folder)
    print('Download was complited')

def download_audio(link, path):
    your_tube_audio = YouTube(link)
    t=your_tube_audio.streams.filter(only_audio=True).first()
    t.download(path, filename='first_audio.mp3')
    print("Аудио успешно загружено")



