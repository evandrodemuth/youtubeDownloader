from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()

    except:
        print("🔴 Houve um erro ao realizar o download do seu video! 🥹")
    print('✅ Vídeo baixado com sucesso!!')

if __name__ == "__main__":
    link = input("Informe a url do vídeo que você deseja baixar:")
    Download(link)

