from pytube import YouTube
from urllib.parse import urlparse, parse_qs
import re

def extract_video_id(url):
    parsed = urlparse(url)
    if 'youtube' in parsed.netloc or 'youtu.be' in parsed.netloc:
        if 'youtu.be' in parsed.netloc:
            return parsed.path.strip("/")
        query = parse_qs(parsed.query)
        return query.get('v', [None])[0]
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url)
    return match.group(1) if match else None

def download_youtube_video():
    try:
        url = input("Enter YouTube URL: ").strip()
        video_id = extract_video_id(url)
        if not video_id:
            raise ValueError("Invalid YouTube URL.")

        clean_url = f"https://www.youtube.com/watch?v={video_id}"
        yt = YouTube(clean_url)

        print(f"\nTitle: {yt.title}")
        print("Downloading video...")
        stream = yt.streams.get_highest_resolution()
        stream.download()
        print("✅ Download complete!")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    download_youtube_video()
