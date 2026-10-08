import yt_dlp
from threading import Thread
from pathlib import Path
import json

pasta_caminho = Path(__file__).parent / "videos"

def salvar_url_json(url):
    with open(Path(__file__).parent / "urls.json", "r") as file_json:
        urls = json.load(file_json)
        if "url" not in urls:
            urls["url"] = []
        urls["url"].append(url)
    with open(Path(__file__).parent / "urls.json", "w") as file_json:
        
        json.dump(urls, file_json)



def baixar_video_thread(url, ydl_opts):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def baixar_video(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': str(pasta_caminho / "%(title).100B [%(id)s].%(ext)s"),
    }
    thread = Thread(target=baixar_video_thread, args=(url, ydl_opts))
    thread.start()


if __name__ == "__main__":
    url = input("Digite a URL do vídeo do YouTube: ")
    baixar_video(url)        