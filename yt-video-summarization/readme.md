# YouTube Video Summarization

This project provides a tool to download YouTube videos, transcribe them, and generate summaries using advanced language models.

## Repository Structure

```
yt-video-summarization/
│
├── Data/                  # Directory to store downloaded videos and generated files
├── junk.ipynb             # Jupyter notebook for testing and experimentation
├── llama3_to_summarize.py # Script to summarize transcripts using LLaMA 3 model
├── main.py                # Main application script
├── transcript.py          # Script to generate transcript from audio
├── video_2_audio.py       # Script to convert video to audio
└── youtube_downloader.py  # Script to download YouTube videos
```

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/Pragateeshwaran/GenAi-Verse.git
   cd GenAi-Verse/yt-video-summarization
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Create a `.env` file in the root directory
   - Add your Hugging Face API token: `HUGGINGFACE_TOKEN=your_token_here`

## Usage

Run the main application script:

```
streamlit run main.py
```

This will start a Streamlit web application where you can enter a YouTube video URL to summarize.

## Demo 

![Demo Image](yt-video-summarization/Example.png)

## Features

- Download YouTube videos
- Convert video to audio
- Generate transcript from audio
- Summarize transcript using LLaMA 3 model
- Display summary and any code snippets found in the video

## Dependencies

- Python 3.8+
- Streamlit
- PyTube
- MoviePy
- Transformers
- Torch
- Torchaudio
- Hugging Face Hub

For a complete list of dependencies, see `requirements.txt`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

Pragateeshwaran - geniuspekka1808@gmail.com
Project Link: [https://github.com/Pragateeshwaran/GenAi-Verse](https://github.com/Pragateeshwaran/GenAi-Verse)

