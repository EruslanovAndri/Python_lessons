from pytube import YouTube


link = 'https://www.youtube.com/watch?v=ZwQxlBoTZto'
path_to_folder = '/Users/eruslanovandrey/Python_lessons/Home_Work_Lesson9_Project2/src/download_video'

def user_input_link(link:str):
    user_link = link
    return user_link

print(f'Input user link => ',user_input_link(link))

def get_path_to_folder_download_video(path:str):
    path_to_folder = path
    return path_to_folder

print(f'Path to folder for collecting video => ',get_path_to_folder_download_video(path_to_folder))

def download_video_to_the_folder(link,path:str):
    you_tube_video = YouTube(link)
    
    you_tube_video.streams.get_highest_resolution().download(path)
    print('Download was complited')

download_video_to_the_folder(link,path_to_folder)
