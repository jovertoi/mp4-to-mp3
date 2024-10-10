import os
from moviepy.editor import VideoFileClip

def convert_mp4_to_mp3(input_file, output_file):
    try:
        video = VideoFileClip(input_file)
        audio = video.audio
        audio.write_audiofile(output_file)
        audio.close()
        video.close()
        return True
    except Exception as e:
        print(f"Conversion failed: {str(e)}")
        return False

def error_handling():
    print("An error occurred during conversion.")
    return input("Do you want to try again? (yes/no): ").lower().strip() == 'yes'

def main():
    while True:
        input_file = input("Enter the path to the MP4 file: ")
        if not os.path.exists(input_file):
            print("File not found. Please check the path and try again.")
            continue

        output_file = input("Enter the path for the output MP3 file: ")

        print("Converting MP4 to MP3...")
        success = convert_mp4_to_mp3(input_file, output_file)

        if success:
            print("Conversion completed successfully.")
            break
        else:
            if not error_handling():
                print("Conversion process terminated.")
                break

if __name__ == "__main__":
    main()
