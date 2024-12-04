import flet as ft
from pytubefix import YouTube

def main(page: ft.Page):
    page.title = "YouTube Video Downloader"
    page.vertical_alignment = ft.MainAxisAlignment.START

    search_query = ft.TextField(label="Search for YouTube videos", autofocus=True)
    search_button = ft.ElevatedButton("Search", on_click=search_videos)
    video_list = ft.Column()

    def search_videos(e):
        # Clear the video list before new search
        video_list.controls.clear()

        query = search_query.value.strip()
        if not query:
            return

        # Use PyTubeFix to search YouTube
        results = search_on_youtube(query)
        for video in results:
            video_button = ft.ElevatedButton(
                f"{video['title']} ({video['duration']})",
                on_click=lambda e, url=video['url']: download_video(url),
            )
            video_list.controls.append(video_button)

        page.update()

    def search_on_youtube(query):
        # Search YouTube and get the results
        yt = YouTube(search=query)
        videos = yt.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').desc()
        return [
            {"title": video.title, "url": video.url, "duration": video.length // 60}  # Duration in minutes
            for video in videos
        ]

    def download_video(url):
        # Download the video from YouTube
        try:
            yt = YouTube(url)
            stream = yt.streams.filter(progressive=True, file_extension="mp4").first()
            stream.download()
            page.add(ft.Text(f"Downloaded: {yt.title}"))
        except Exception as e:
            page.add(ft.Text(f"Error downloading video: {str(e)}"))
        page.update()

    page.add(search_query, search_button, video_list)

ft.app(target=main)
