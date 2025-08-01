from pytube import YouTube

try:
    url = input("Enter YouTube URL: ").strip()
    
    # If a playlist URL is given, extract only video part
    if "&" in url:
        url = url.split("&")[0]  # take only the video link

    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    print("Downloading...")
    stream.download()
    print("Download complete!")

except Exception as e:
    print(f"Error: {e}")
