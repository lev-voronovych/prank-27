import ctypes
import time
import winsound
import threading
import random
import tkinter as tk
from tkinter import messagebox, font as tkfont

# для звуків
import wave
import struct
import math
import tempfile
import os

# pygame використовується для мікшування й одночасного відтворення
try:
    import pygame
    PYGAME_AVAILABLE = True
except Exception:
    PYGAME_AVAILABLE = False

stop_event = threading.Event()

# ------------------------------- ЗВУКОВИЙ ГЕНЕРАТОР (вбудований) ------------------------------- #
def synth_wav_sine(path, freq=440.0, duration=0.5, volume=0.8, samplerate=44100):
    """Генерує простий синусоїдальний WAV."""
    n_samples = int(samplerate * duration)
    with wave.open(path, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 16-bit
        wf.setframerate(samplerate)
        for i in range(n_samples):
            t = i / samplerate
            val = int(volume * 32767.0 * math.sin(2.0 * math.pi * freq * t))
            wf.writeframes(struct.pack('<h', val))

def synth_wav_siren(path, f_low=200.0, f_high=1200.0, duration=1.2, volume=0.9, samplerate=44100):
    """Генерує сиреноподібний звук зі змінною частотою."""
    n_samples = int(samplerate * duration)
    with wave.open(path, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(samplerate)
        for i in range(n_samples):
            t = i / samplerate
            # плавний підйом/спад частоти (sine sweep)
            frac = i / n_samples
            freq = f_low + (f_high - f_low) * (0.5 - 0.5 * math.cos(math.pi * 2 * frac))  # cos ease
            val = int(volume * 32767.0 * math.sin(2.0 * math.pi * freq * t))
            # додаємо невеликий шум для агресивності
            noise = int((random.random() - 0.5) * 2000)
            wf.writeframes(struct.pack('<h', max(-32768, min(32767, val + noise))))

def synth_wav_glitch(path, duration=0.7, volume=0.9, samplerate=44100):
    """Генерує короткі 'глітч' сплески (випадкові хвилі та шум)."""
    n_samples = int(samplerate * duration)
    with wave.open(path, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(samplerate)
        for i in range(n_samples):
            t = i / samplerate
            # комбінація синусів різних частот з випадковою фазою
            val = int(volume * 32767.0 * (
                0.4 * math.sin(2.0 * math.pi * 350 * t + random.random()) +
                0.3 * math.sin(2.0 * math.pi * 700 * t + random.random()) +
                0.3 * math.sin(2.0 * math.pi * 1200 * t + random.random())
            ))
            # сильні інтермедіатні імпульси
            if random.random() < 0.02:
                val = int(val * (1 + random.uniform(2.0, 6.0)))
            # кидок шуму
            if random.random() < 0.01:
                val = int((random.random() - 0.5) * 32767 * 0.9)
            wf.writeframes(struct.pack('<h', max(-32768, min(32767, val))))

def make_temp_sounds():
    """Створює набір тимчасових WAV-файлів зі страшними ефектами. Повертає список шляхів."""
    temp_paths = []
    try:
        # rumble (низький гул, довгий)
        f1 = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
        f1.close()
        synth_wav_sine(f1.name, freq=70.0, duration=2.2, volume=0.9)
        temp_paths.append(f1.name)

        # siren (підйом)
        f2 = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
        f2.close()
        synth_wav_siren(f2.name, f_low=250.0, f_high=1400.0, duration=1.4, volume=0.95)
        temp_paths.append(f2.name)

        # glitch (короткі сплески)
        f3 = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
        f3.close()
        synth_wav_glitch(f3.name, duration=0.9, volume=0.95)
        temp_paths.append(f3.name)

        # високий пронизливий сигнал
        f4 = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
        f4.close()
        synth_wav_sine(f4.name, freq=2200.0, duration=0.35, volume=1.0)
        temp_paths.append(f4.name)

        return temp_paths
    except Exception as e:
        # при помилці намагаємось очистити створені тимчасові файли
        for p in temp_paths:
            try: os.remove(p)
            except: pass
        raise e

# ------------------------------- ДОДАТКОВІ ЕФЕКТИ ------------------------------- #

def flicker_screen():
    """Червоне мерехтіння екрана як при вірусній інфекції"""
    try:
        root = tk.Tk()
        root.attributes('-fullscreen', True)
        root.attributes('-topmost', True)
        root.config(bg="black")
        root.overrideredirect(True)

        for i in range(12):
            if stop_event.is_set():
                break
            color = random.choice(["#330000", "#220000", "#550000", "#000000"])
            root.config(bg=color)
            root.update()
            time.sleep(0.08)

        root.destroy()
    except:
        pass

def kernel_panic(duration=10):
    """Ефект kernel panic перед BSOD — страшно виглядає"""
    try:
        root = tk.Tk()
        root.attributes('-fullscreen', True)
        root.attributes('-topmost', True)
        root.configure(bg='black')

        font_big = tkfont.Font(family="Consolas", size=16)
        label = tk.Label(root, fg="#00FF00", bg="black", font=font_big, justify='left')
        label.pack(anchor='nw')

        panic_text = [
            "[!] Kernel Panic - not syncing: Fatal exception",
            "CPU: 0 PID: 0 Comm: swapper/0",
            "Hardware name: UNKNOWN",
            "Call Trace:",
            " [<ffffffff8101234a>] panic+0x200/0x21f",
            " [<ffffffff8104567f>] do_exit+0x555/0x890",
            " [<ffffffff81089abc>] do_group_exit+0x45/0xa0",
            "SYSTEM FAILURE: SEGMENTATION FAULT",
            "u fuck'n idiot"
        ]

        for line in panic_text:
            label.config(text=label.cget("text") + line + "\n")
            root.update()
            time.sleep(0.4)

        time.sleep(duration)
        root.destroy()

    except Exception as e:
        print("[Kernel Panic ERROR]:", e)


# ------------------------------- ПОПАПИ ------------------------------- #

def error_popup():
    try:
        while not stop_event.is_set():
            w = random.randint(220, 420)
            h = random.randint(120, 280)

            x = random.randint(0, ctypes.windll.user32.GetSystemMetrics(0) - w)
            y = random.randint(0, ctypes.windll.user32.GetSystemMetrics(1) - h)

            root = tk.Tk()
            root.overrideredirect(True)
            root.attributes('-topmost', True)
            root.geometry(f"{w}x{h}+{x}+{y}")

            root.config(bg="#111")

            lbl = tk.Label(root, fg="red", bg="#111",
                           font=("Consolas", 12),
                           wraplength=w - 20,
                           justify="left")
            lbl.pack(expand=True, fill='both')

            msgs = [
                "!!! CRITICAL SYSTEM ERROR !!!",
                "Файли системи REACT OS пошкоджені",
                "BIOS CORRUPTED: CHECKSUM INVALID",
                "Виявлено несанкціонований доступ!",
                "PROCESS MEMORY DAMAGED",
                "ROOTKIT DETECTED",
                "Загроза рівня RED LEVEL"
            ]

            lbl.config(text=random.choice(msgs))
            root.after(random.randint(700, 1300), root.destroy)
            root.mainloop()

            time.sleep(random.uniform(0.15, 0.35))
    except:
        pass


# ------------------------------- ПСЕВДО-ФОРМАТ ------------------------------- #

def fake_format_window():
    try:
        root = tk.Tk()
        root.overrideredirect(True)
        root.attributes('-topmost', True)

        w, h = 420, 240
        x = random.randint(0, ctypes.windll.user32.GetSystemMetrics(0) - w)
        y = random.randint(0, ctypes.windll.user32.GetSystemMetrics(1) - h)
        root.geometry(f"{w}x{h}+{x}+{y}")

        root.config(bg="black")

        text = tk.Label(root, text="Форматування диска C: …",
                        fg="white", bg="black", font=("Consolas", 14))
        text.pack(pady=10)

        progress = tk.Label(root, fg="lime", bg="black", font=("Consolas", 22))
        progress.pack(pady=20)

        def loop(i=0):
            if stop_event.is_set() or i > 100:
                root.destroy()
                return
            progress.config(text=f"{i}%")
            root.after(60, loop, i + 1)

        loop()
        root.mainloop()
    except:
        pass


# ------------------------------- BSOD ------------------------------- #

def show_blue_screen(duration_seconds=20):
    try:
        root = tk.Tk()
        root.attributes('-fullscreen', True)
        root.configure(bg='#0078d7')
        root.attributes('-topmost', True)

        font_big = tkfont.Font(family="Lucida Console", size=16)

        text = """
:( На вашому ПК сталася критична помилка, і його потрібно перезавантажити.
Ми збираємо деякі відомості про помилку. 

Код зупинки: SYSTEM_THREAD_EXCEPTION_NOT_HANDLED
"""

        percent = tk.Label(root, fg='white', bg='#0078d7',
                           font=font_big, justify='left',
                           text=text)
        percent.place(relx=0.12, rely=0.2)

        p = tk.Label(root, fg='white', bg='#0078d7',
                     font=tkfont.Font(size=48),
                     text=":(")
        p.place(relx=0.5, rely=0.4, anchor='center')

        def anim(i=0):
            if i > 100:
                time.sleep(1)
                root.destroy()
                return
            percent.config(text=text + f"\n{ i }% завершено")
            root.after(70, anim, i + 1)

        anim()
        root.mainloop()

    except:
        pass


# ------------------------------- ГОЛОВНЕ ------------------------------- #

def main_attack():
    # ефект зараження
    flicker_screen()
    time.sleep(0.4)
    flicker_screen()

    # запуск звуків
    threading.Thread(target=play_sounds, daemon=True).start()

    # попапи
    for _ in range(6):
        threading.Thread(target=error_popup, daemon=True).start()

    # фейкове форматування
    for _ in range(3):
        threading.Thread(target=fake_format_window, daemon=True).start()

    # 20 сек хаосу
    time.sleep(20)

    stop_event.set()
    time.sleep(1)

    # kernel panic
    kernel_panic()

    # BSOD
    show_blue_screen(duration_seconds=60)

    # фінальне повідомлення
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("ваш комп'ютер ушкоджений! GG WP")
    root.destroy()


# ------------------------------- SOUND (вбудований) ------------------------------- #

def play_sounds():
    """
    Створює тимчасові страшні WAV і програє їх хаотично.
    Використовує pygame якщо доступний, інакше winsound (файловий шлях).
    """
    temp_files = []
    mixer_sounds = []
    try:
        temp_files = make_temp_sounds()

        if PYGAME_AVAILABLE:
            try:
                pygame.mixer.init()
                # завантажуємо всі звуки як pygame.Sound
                for p in temp_files:
                    snd = pygame.mixer.Sound(p)
                    mixer_sounds.append(snd)

                # додаємо довгий низький гул на фон (loop)
                bg = mixer_sounds[0]
                bg_channel = bg.play(loops=-1)
                bg.set_volume(0.6)

                # хаотично програємо інші звуки зверху
                while not stop_event.is_set():
                    # випадкові накладки: інколи сирена, інколи глітч, інколи пронизливий сигнал
                    choice = random.choice([1, 2, 3, 3, 1, 2, 3, 1, 3])
                    snd = mixer_sounds[choice]
                    snd.set_volume(random.uniform(0.5, 1.0))
                    snd.play()
                    # коротка пауза, щоб ефекти не перетворилися в шум
                    time.sleep(random.uniform(0.08, 0.5))

                # зупинити bg
                if bg_channel:
                    try:
                        bg_channel.stop()
                    except:
                        pass

            except Exception as e:
                print("[pygame sound error]:", e)
                # fallback до winsound
                for p in temp_files:
                    while not stop_event.is_set():
                        winsound.PlaySound(p, winsound.SND_FILENAME | winsound.SND_ASYNC)
                        time.sleep(random.uniform(0.08, 0.4))

        else:
            # якщо pygame немає — просто намагаємось по черзі програвати файли через winsound
            while not stop_event.is_set():
                p = random.choice(temp_files)
                winsound.PlaySound(p, winsound.SND_FILENAME | winsound.SND_ASYNC)
                time.sleep(random.uniform(0.08, 0.45))

    except Exception as e:
        print("[play_sounds ERROR]:", e)

    finally:
        # видаляємо тимчасові файли
        for p in temp_files:
            try:
                os.remove(p)
            except:
                pass


if __name__ == "__main__":
    main_attack()
