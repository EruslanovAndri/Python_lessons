from pytube import YouTube

def user_input_link():
    link  = input('Add your URL-link => ')
    # link = 'https://www.youtube.com/watch?v=ZwQxlBoTZto'
    user_link = link
    return user_link


def get_path_to_folder_download_video():
    path_to_folder = input('Choose a folder to downlad => ')
    # path_to_folder = '/Users/eruslanovandrey/Python_lessons/Home_Work_Lesson9_Project2/src/download_video'
    return path_to_folder


def download_video_to_the_folder(user_link,path_to_folder):
    your_tube_video = YouTube(user_link)
    your_tube_video.streams.get_highest_resolution().download(path_to_folder)
    print('Download was complited')


download_video_to_the_folder(user_input_link(),get_path_to_folder_download_video())