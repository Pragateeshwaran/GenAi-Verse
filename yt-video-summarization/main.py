import streamlit as st
from youtube_downloader import download_yt_video
from transcript import Transcript
from video_2_audio import video_to_audio
from llama3_to_summarize import summarize
import re

def extract_code_snippets(text):
    code_snippets = []
    pattern = r'```python\n(.*?)\n```'
    matches = re.findall(pattern, text, re.DOTALL)
    for match in matches:
        code_snippets.append(match.strip())
    return code_snippets

def main():
    st.title("YouTube Video Summarization")
    video_url = st.text_input("Enter YouTube video URL:")

    if st.button("Summarize Video"):
        if video_url:
            # Download the video
            download_yt_video(video_url)

            # Convert video to audio
            video_to_audio(r'F:\works\A-important\A-neurals\GenAi-Verse\yt-video-summarization\Data\my_video.mp4',
                            r'F:\works\A-important\A-neurals\GenAi-Verse\yt-video-summarization\Data\my_audio.mp3')

            # Generate transcript from audio
            Transcript()

            # Summarize the transcript
            summarize()

            # Display the summary
            with open(r'F:\works\A-important\A-neurals\GenAi-Verse\yt-video-summarization\Data\my_file.txt', 'r') as f:
                transcript = f.read()
            st.write("Explanation:")
            st.text_area("", transcript, height=300)

            # Display code snippets with highlighting
            code_snippets = extract_code_snippets(transcript)
            if code_snippets:
                st.write("Code Snippets:")
                for snippet in code_snippets:
                    st.code(snippet, language="python")

if __name__ == "__main__":
    main()