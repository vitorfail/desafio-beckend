import speech_recognition as sr

def transcrever_audio(nome_arquivo_audio):
    
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(nome_arquivo_audio) as source:
        audio = recognizer.record(source)
    
    try:
        texto = recognizer.recognize_sphinx(audio, language='pt-BR')
        print("Texto reconhecido: ", texto)
        
        # Escrever a letra da música em um arquivo de texto
        with open("letra_da_musica.txt", "w") as arquivo:
            arquivo.write(texto)
            print("Letra da música foi salva no arquivo 'letra_da_musica.txt'")
            
    except sr.UnknownValueError:
        print("Não foi possível reconhecer o áudio")
    except sr.RequestError as e:
        print("Erro ao acessar o serviço de reconhecimento de fala; {0}".format(e))

if __name__ == "__main__":
    nome_arquivo_audio = "j.wav"  # Substitua pelo caminho do arquivo de áudio da música
    transcrever_audio(nome_arquivo_audio)
