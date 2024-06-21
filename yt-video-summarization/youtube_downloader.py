from pytube import YouTube

# Enter the URL of the YouTube video you want to download
def download_yt_video(video_url):
    # Create a YouTube object
    yt = YouTube(video_url)

    # Get the highest resolution video stream
    video_stream = yt.streams.get_highest_resolution()
    # Download the video
    print(f"Downloading '{yt.title}'...")
    video_stream.download(output_path = r'Data', filename="my_video.mp4")
    print("Download complete!")
    