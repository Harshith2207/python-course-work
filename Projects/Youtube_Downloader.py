from pytube import YouTube
from urllib.parse import urlparse, parse_qs

def clean_youtube_url(url: str) -> str:
    """
    Cleans the YouTube URL by extracting the video ID and returning
    a canonical watch URL that pytube can handle.
    """
    parsed = urlparse(url)
    if 'youtu.be' in parsed.netloc:
        video_id = parsed.path.strip("/")
        return f"https://www.youtube.com/watch?v={video_id}"
    if 'youtube.com' in parsed.netloc:
        qs = parse_qs(parsed.query)
        video_id = qs.get('v', [None])[0]
        if video_id:
            return f"https://www.youtube.com/watch?v={video_id}"
    # fallback if input is already clean or just video ID
    return url

def download_video(url: str):
    try:
        clean_url = clean_youtube_url(url)
        print(f"Harshith's Downloader: Processing URL -> {clean_url}")

        yt = YouTube(clean_url)
        print(f"🎬 Title: {yt.title}")
        print("🚀 Starting download...")

        stream = yt.streams.get_highest_resolution()
        stream.download()

        print("✅ Download complete! Thanks for using Harshith's Downloader.")
    except Exception as e:
        print(f"❌ Oops! An error occurred: {e}")
        print("Make sure your pytube package is up to date by running:")
        print("   pip install --upgrade pytube")

if __name__ == "__main__":
    video_url = input("Enter YouTube URL: ").strip()
    download_video(video_url)
