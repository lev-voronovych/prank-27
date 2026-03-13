import tkinter as tk
from tkinter import ttk
import winsound
import random
import time
import threading
import math
import os
import sys
from datetime import datetime

# Глобальні змінні
all_windows = []
multiplying = False
cursor_window = None
shake_all_active = False
bsod_active = False
psod_active = False
rough_sound_active = False
glitch_active = False
matrix_active = False
chaos_mode = False
ad_window = None
ransomware_win = None
virus_start_time = None
VIRUS_DURATION = 60  # секунд
black_screen_win = None

# ==================== КРИНЖОВА РЕКЛАМА ====================

class CringeAd:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("🔥 HOT SINGLES 🔥")
        
        # Позиція - ПРАВИЙ нижній кут
        screen_w = self.window.winfo_screenwidth()
        screen_h = self.window.winfo_screenheight()
        self.window.geometry("300x250+{}+{}".format(screen_w - 320, screen_h - 300))
        self.window.configure(bg='#ff00ff')
        self.window.attributes('-topmost', True)
        self.window.overrideredirect(True)
        self.window.attributes('-alpha', 0.95)
        
        # Рамка з неоном
        frame = tk.Frame(self.window, bg='#ff00ff', relief='ridge', bd=4)
        frame.pack(expand=True, fill='both', padx=3, pady=3)
        
        # Миготливий заголовок
        self.header = tk.Label(frame, 
            text="🔥🔥🔥 HOT SINGLES 🔥🔥🔥",
            font=("Comic Sans MS", 14, "bold"),
            bg='#ff00ff', fg='yellow')
        self.header.pack(pady=5)
        
        # Кринжовий контент
        self.content = tk.Label(frame,
            text="💋 Твоя мама чекає! 💋\n\n😍 2 км від тебе! 😍\n\n👉 НАТИСНИ ЗАРАЗ! 👈",
            font=("Arial", 11, "bold"),
            bg='#ff00ff', fg='white',
            justify='center')
        self.content.pack(pady=10)
        
        # Фейкове фото
        self.photo = tk.Label(frame,
            text="👩‍🦰\n|  |\n/\\ /\\",
            font=("Arial", 32),
            bg='#ff00ff', fg='white')
        self.photo.pack(pady=5)
        
        # Кнопка "закрити" (фейкова)
        self.close_btn = tk.Button(frame,
            text="❌ ЗАКРИТИ ❌",
            font=("Arial", 10, "bold"),
            bg='red', fg='white',
            command=self.on_close_attempt)
        self.close_btn.pack(pady=5)
        
        # Лічильник "людей онлайн"
        self.online_label = tk.Label(frame,
            text="🔴 ONLINE: 6969",
            font=("Arial", 9),
            bg='#ff00ff', fg='#00ff00')
        self.online_label.pack(pady=2)
        
        self.running = True
        self.animate()
        self.update_online()
        self.auto_move()
    
    def animate(self):
        if not self.running or not self.window.winfo_exists():
            return
        
        try:
            self.header.config(fg=random.choice(['yellow', 'red', 'white']))
            self.content.config(fg=random.choice(['white', '#00ffff', '#ffff00']))
            self.window.config(bg=random.choice(['#ff00ff', '#ff69b4', '#ff1493']))
            new_size = random.randint(12, 16)
            self.header.config(font=("Comic Sans MS", new_size, "bold"))
        except:
            pass
        
        self.window.after(300, self.animate)
    
    def update_online(self):
        if not self.running or not self.window.winfo_exists():
            return
        
        try:
            online = random.randint(1000, 9999)
            self.online_label.config(text=f"🔴 ONLINE: {online}")
        except:
            pass
        
        self.window.after(2000, self.update_online)
    
    def auto_move(self):
        if not self.running or not self.window.winfo_exists():
            return
        
        try:
            screen_w = self.window.winfo_screenwidth()
            screen_h = self.window.winfo_screenheight()
            x = screen_w - 320 + random.randint(-3, 3)
            y = screen_h - 300 + random.randint(-3, 3)
            self.window.geometry(f"+{x}+{y}")
        except:
            pass
        
        self.window.after(100, self.auto_move)
    
    def on_close_attempt(self):
        for _ in range(3):
            new_ad = tk.Toplevel(self.window)
            new_ad.title("🔥")
            screen_w = new_ad.winfo_screenwidth()
            screen_h = new_ad.winfo_screenheight()
            x = random.randint(0, screen_w - 300)
            y = random.randint(0, screen_h - 250)
            new_ad.geometry(f"300x250+{x}+{y}")
            new_ad.configure(bg='#ff00ff')
            new_ad.attributes('-topmost', True)
            new_ad.overrideredirect(True)
            
            tk.Label(new_ad, text="😂 НЕ МОЖНА ВТЕКТИ! 😂",
                    font=("Arial", 16, "bold"), bg='#ff00ff', fg='white').pack(expand=True)
            
            new_ad.after(5000, new_ad.destroy)
        
        self.close_btn.config(text="❌ СПРОБУЙ ЩЕ ❌")
    
    def hide(self):
        self.running = False
        try:
            self.window.destroy()
        except:
            pass

# ==================== КРИПТОВІРУС (ЛІВИЙ ВЕРХНІЙ КУТ, НАЙВИЩЕ) ====================

def create_unclosable_ransomware():
    """Криптовірус у лівому верхньому куті, найвищий рівень, не можна закрити"""
    global ransomware_win
    
    if ransomware_win and ransomware_win.winfo_exists():
        return
    
    ransomware_win = tk.Toplevel()
    ransomware_win.title("💀 ВАШІ ФАЙЛИ ЗАШИФРОВАНІ 💀")
    
    # Фіксований розмір у лівому верхньому куті
    width = 450
    height = 550
    ransomware_win.geometry(f"{width}x{height}+0+0")
    
    ransomware_win.configure(bg='#1a0000')
    ransomware_win.attributes('-topmost', True)
    ransomware_win.overrideredirect(True)
    ransomware_win.protocol("WM_DELETE_WINDOW", lambda: None)
    
    # НАЙВИЩИЙ рівень - завжди зверху всіх
    def set_highest_level():
        if ransomware_win.winfo_exists():
            ransomware_win.lift()
            ransomware_win.attributes('-topmost', True)
            ransomware_win.after(50, set_highest_level)
    
    # Головна рамка
    main_frame = tk.Frame(ransomware_win, bg='#1a0000', relief='ridge', bd=3)
    main_frame.pack(expand=True, fill='both', padx=5, pady=5)
    
    # Заголовок з миготінням
    header = tk.Label(main_frame,
             text="⚠️⚠️⚠️ КРИТИЧНЕ ПОПЕРЕДЖЕННЯ ⚠️⚠️⚠️",
             font=("Arial", 13, "bold"),
             fg='#ff0000', bg='#1a0000')
    header.pack(pady=8)
    
    # Черепи
    skull_label = tk.Label(main_frame,
             text="💀💀💀",
             font=("Arial", 48),
             fg='#ff0000', bg='#1a0000')
    skull_label.pack(pady=10)
    
    # Текст БЕЗ ЦИФЕР
    txt = """ВАШ КОМП'ЮТЕР ЗАРАЖЕНО
Ryuk Crypto Virus

УСІ ВАШІ ФАЙЛИ ЗАШИФРОВАНО
НАЙСКЛАДНІШИМ АЛГОРИТМОМ

РОЗШИФРУВАТИ НЕМОЖЛИВО
БЕЗ УНІКАЛЬНОГО КЛЮЧА"""
    
    info_text = tk.Label(main_frame,
             text=txt,
             font=("Consolas", 10),
             fg='#ff6666', bg='#1a0000',
             justify='center')
    info_text.pack(pady=8)
    
    # Сума викупу БЕЗ ЦИФЕР
    btc_frame = tk.Frame(main_frame, bg='#330000', relief='sunken', bd=3)
    btc_frame.pack(pady=10, ipadx=20, ipady=10)
    
    tk.Label(btc_frame,
             text="ЗАПЛАТІТЬ ВИКУП:",
             font=("Arial", 11),
             fg='#ff6666', bg='#330000').pack()
    
    tk.Label(btc_frame,
             text="💰 БІТКОЇНИ 💰",
             font=("Arial", 24, "bold"),
             fg='#ffff00', bg='#330000').pack()
    
    tk.Label(btc_frame,
             text="(деталі в email)",
             font=("Arial", 9),
             fg='#ff6666', bg='#330000').pack()
    
    # Гаманець
    wallet_frame = tk.Frame(btc_frame, bg='#000000', relief='sunken', bd=2)
    wallet_frame.pack(pady=8, padx=10)
    
    wallet_label = tk.Label(wallet_frame,
             text="ГАМАНЕЦЬ НАДІСЛАНО\nНА ВАШ EMAIL",
             font=("Consolas", 9),
             fg='#44ff44', bg='#000000')
    wallet_label.pack(padx=5, pady=5)
    
    # Кнопка копіювання
    copy_btn = tk.Button(btc_frame,
             text="📋 ПЕРЕВІРИТИ EMAIL",
             font=("Arial", 9, "bold"),
             bg='#44ff44', fg='black',
             command=lambda: copy_btn.config(text="✅ ПЕРЕВІРЕНО!"))
    copy_btn.pack(pady=3)
    
    # Таймер БЕЗ ЦИФЕР
    timer_frame = tk.Frame(main_frame, bg='#1a0000')
    timer_frame.pack(pady=10)
    
    tk.Label(timer_frame,
             text="⏳ ЧАС ЙДЕ... ⏳",
             font=("Arial", 12, "bold"),
             fg='#ff4444', bg='#1a0000').pack()
    
    # Кольорові індикатори
    indicator_frame = tk.Frame(timer_frame, bg='#1a0000')
    indicator_frame.pack(pady=5)
    
    indicators = []
    for i in range(5):
        lbl = tk.Label(indicator_frame, text="●", font=("Arial", 20), fg='red', bg='#1a0000')
        lbl.pack(side='left', padx=2)
        indicators.append(lbl)
    
    # Статус файлів
    files_frame = tk.Frame(main_frame, bg='#0a0a0a', relief='sunken', bd=2)
    files_frame.pack(pady=8, padx=10, fill='x')
    
    files_label = tk.Label(files_frame,
             text="📁 ЙДЕ ШИФРУВАННЯ...\n✅ Особисті документи\n✅ Фотографії\n✅ Відео\n⏳ Робочі файли",
             font=("Consolas", 9),
             fg='#44ff44', bg='#0a0a0a',
             justify='left')
    files_label.pack(pady=5, padx=5)
    
    # Кнопка оплати
    pay_btn = tk.Button(main_frame,
              text="💰 Я СПЛАТИВ - РОЗШИФРУВАТИ",
              font=("Arial", 11, "bold"),
              bg='#ff0000', fg='white',
              bd=3, relief='raised',
              command=lambda: pay_btn.config(text="⛔ ПЕРЕВІРКА... ⛔", state='disabled'))
    pay_btn.pack(pady=8)
    
    # Попередження
    warning_label = tk.Label(main_frame,
             text="⚠️ НЕ ВИМИКАЙТЕ КОМП'ЮТЕР ⚠️\n⚠️ НЕ ЗАКРИВАЙТЕ ЦЕ ВІКНО ⚠️",
             font=("Arial", 10, "bold"),
             fg='yellow', bg='#1a0000')
    warning_label.pack(pady=5)
    
    # Анімація індикаторів
    def animate_indicators():
        if not ransomware_win.winfo_exists():
            return
        try:
            colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
            for lbl in indicators:
                lbl.config(fg=random.choice(colors))
            ransomware_win.after(300, animate_indicators)
        except:
            pass
    
    # Анімація заголовка
    def animate_header():
        if not ransomware_win.winfo_exists():
            return
        try:
            colors = ['#ff0000', '#ff4444', '#ff8888']
            current = header.cget('fg')
            next_color = colors[(colors.index(current) + 1) % len(colors)] if current in colors else colors[0]
            header.config(fg=next_color)
            ransomware_win.after(500, animate_header)
        except:
            pass
    
    # Фіксація позиції і фокус
    def force_focus():
        if ransomware_win.winfo_exists():
            ransomware_win.focus_force()
            ransomware_win.geometry(f"{width}x{height}+0+0")
            ransomware_win.after(50, force_focus)
    
    set_highest_level()
    animate_header()
    animate_indicators()
    force_focus()

# ==================== ЧОРНИЙ ЕКРАН (ПІД КРИПТОВІРУСОМ, АЛЕ ВИЩЕ ВІКОН) ====================

def show_black_screen():
    """Чорний екран з повідомленням про відновлення – на першому плані"""
    global black_screen_win

    # Закриваємо криптовірус, якщо він ще є
    global ransomware_win
    if ransomware_win and ransomware_win.winfo_exists():
        ransomware_win.destroy()
        ransomware_win = None

    black_screen_win = tk.Toplevel()
    black_screen_win.attributes('-fullscreen', True)
    black_screen_win.configure(bg='#000000')
    black_screen_win.overrideredirect(True)
    black_screen_win.attributes('-topmost', True)   # НА ПЕРШОМУ ПЛАНІ
    black_screen_win.focus_force()

    # Текст посередині
    label = tk.Label(black_screen_win,
                     text="💀 ВІДНОВЛЕННЯ СИСТЕМИ... 💀\n\nЗачекайте, будь ласка...",
                     font=("Arial", 32, "bold"),
                     fg='#ffffff', bg='#000000')
    label.place(relx=0.5, rely=0.5, anchor='center')

    # Прогрес-бар
    progress = ttk.Progressbar(black_screen_win, length=400, mode='indeterminate')
    progress.place(relx=0.5, rely=0.6, anchor='center')
    progress.start(10)

    # Через 5 секунд відновлюємо браузер
    black_screen_win.after(5000, restore_browser)

# ==================== ТАЙМЕР ВІРУСУ ====================

def start_virus_timer():
    global virus_start_time
    virus_start_time = time.time()
    
    def check_time():
        elapsed = time.time() - virus_start_time
        remaining = VIRUS_DURATION - elapsed
        
        if remaining <= 0:
            show_black_screen()
        else:
            try:
                root.title(f"💀 SYSTEM BREACH - {int(remaining)}s 💀")
            except:
                pass
            root.after(1000, check_time)
    
    check_time()

def restore_browser():
    """Повне відновлення браузера до початкового стану з рекламою"""
    global black_screen_win, ransomware_win, ad_window
    
    # 1. Закриваємо чорний екран
    if black_screen_win:
        try:
            black_screen_win.destroy()
        except:
            pass
        black_screen_win = None
    
    # 2. Закриваємо криптовірус
    if ransomware_win:
        try:
            ransomware_win.destroy()
        except:
            pass
        ransomware_win = None
    
    # 3. Зупиняємо ВСІ ефекти
    stop_all_effects()
    
    # 4. Повне очищення і відновлення GUI
    full_reset_gui()

def stop_all_effects():
    """Зупиняє всі ефекти"""
    global multiplying, shake_all_active, rough_sound_active, chaos_mode
    
    multiplying = False
    shake_all_active = False
    rough_sound_active = False
    chaos_mode = False
    
    # Закриваємо всі вікна вірусів
    for virus in all_windows[:]:
        try:
            virus.window.destroy()
        except:
            pass
    all_windows.clear()
    
    # Закриваємо курсори
    global cursor_window
    if cursor_window:
        try:
            cursor_window.destroy()
        except:
            pass
        cursor_window = None

def full_reset_gui():
    """Повне відновлення GUI браузера як при старті"""
    global ad_window
    
    # Відновлюємо властивості вікна
    try:
        root.title("Super Browser 2024")
        root.configure(bg='#1e1e2e')
        root.geometry("1000x650")
        
        # Відновлюємо кнопки навігації
        search_btn.config(text='🔍 Пошук', bg='#4ade80', state='normal')
        close_btn.config(text='✕', bg='#f87171', state='normal')
        help_btn.config(text='?', bg='#60a5fa', state='normal')
        back_btn.config(state='normal')
        forward_btn.config(state='normal')
        refresh_btn.config(state='normal')
        
        # Відновлюємо URL
        url.delete(0, tk.END)
        url.insert(0, "https://www.google.com")
        
        # Відновлюємо поле пошуку
        search_entry.delete(0, tk.END)
        search_entry.insert(0, "Введіть пошуковий запит...")
        
        # Відновлюємо статус
        for widget in status_frame.winfo_children():
            if isinstance(widget, tk.Label):
                if 'Безпечне' in widget.cget('text'):
                    widget.config(text="✅ Безпечне з'єднання", fg='#4ade80')
        
        # Запускаємо рекламу знову (як при старті)
        ad_window = CringeAd(root)
        
        # Показуємо повідомлення про відновлення
        recovery = tk.Toplevel()
        recovery.title("✅")
        recovery.geometry("400x200")
        recovery.configure(bg='black')
        recovery.attributes('-topmost', True)
        
        tk.Label(recovery, 
                text="✅ СИСТЕМА ВІДНОВЛЕНА ✅\n\nВірус було видалено\nВсі файли в безпеці\nБраузер працює нормально",
                font=("Arial", 14, "bold"), 
                fg='#00ff00', 
                bg='black').pack(expand=True)
        
        recovery.after(3000, recovery.destroy)
        
    except Exception as e:
        print(f"Помилка відновлення: {e}")

# ==================== ІНШІ ФУНКЦІЇ ====================

def screen_glitch():
    global glitch_active
    if glitch_active:
        return
    glitch_active = True
    
    def glitch_effect():
        original_geometry = root.geometry()
        for _ in range(20):
            try:
                x_offset = random.randint(-100, 100)
                y_offset = random.randint(-50, 50)
                root.geometry(f"+{root.winfo_x() + x_offset}+{root.winfo_y() + y_offset}")
                root.configure(bg=random.choice(['red', 'blue', 'green', 'black', 'white']))
                
                for widget in root.winfo_children():
                    try:
                        if isinstance(widget, tk.Label):
                            widget.config(fg=random.choice(['#ff0000', '#00ff00', '#0000ff']))
                    except:
                        pass
                
                time.sleep(0.05)
            except:
                break
        
        try:
            root.geometry(original_geometry)
            root.configure(bg='#1e1e2e')
        except:
            pass
        glitch_active = False
    
    threading.Thread(target=glitch_effect, daemon=True).start()

class ReverseCursor:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.attributes('-alpha', 0.7, '-topmost', True)
        self.window.overrideredirect(True)
        self.window.geometry("50x50")
        self.window.configure(bg='black')
        self.window.attributes('-transparentcolor', 'black')
        
        self.label = tk.Label(self.window, text="🖱️", font=("Segoe UI", 24), bg='black', fg='red')
        self.label.pack(expand=True)
        
        self.x = random.randint(100, 800)
        self.y = random.randint(100, 600)
        self.window.geometry(f"+{self.x}+{self.y}")
        
        self.running = True
        self.move_away()
    
    def move_away(self):
        if not self.running:
            return
        
        try:
            mouse_x = self.window.winfo_pointerx()
            mouse_y = self.window.winfo_pointery()
            
            dx = self.x - mouse_x
            dy = self.y - mouse_y
            distance = math.sqrt(dx**2 + dy**2)
            
            if distance < 200 and distance > 0:
                speed = 15
                self.x += int((dx/distance) * speed)
                self.y += int((dy/distance) * speed)
                
                screen_w = self.window.winfo_screenwidth()
                screen_h = self.window.winfo_screenheight()
                self.x = max(0, min(screen_w-50, self.x))
                self.y = max(0, min(screen_h-50, self.y))
                
                self.window.geometry(f"+{self.x}+{self.y}")
            
            self.window.after(50, self.move_away)
        except:
            pass
    
    def stop(self):
        self.running = False
        try:
            self.window.destroy()
        except:
            pass

def hacker_terminal():
    term = tk.Toplevel()
    term.title("root@kali:~#")
    term.geometry("800x500")
    term.configure(bg='#0c0c0c')
    term.attributes('-topmost', True)
    
    text = tk.Text(term, bg='#0c0c0c', fg='#00ff00', font=('Consolas', 11),
                   insertbackground='#00ff00', relief='flat')
    text.pack(expand=True, fill='both', padx=5, pady=5)
    
    commands = [
        "nmap -sS -O 192.168.1.0/24",
        "hydra -l admin -P /usr/share/wordlists/rockyou.txt ssh://192.168.1.105",
        "msfconsole -q -x 'use exploit/windows/smb/ms17_010_eternalblue'",
        "sqlmap -u 'http://target.com/page.php?id=1' --dbs",
        "airodump-ng wlan0mon",
        "john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt",
        "nc -lvnp 4444",
        "python -c 'import pty; pty.spawn(\"/bin/bash\")'",
        "chmod +x /tmp/backdoor && /tmp/backdoor &",
        "rm -rf / --no-preserve-root 2>/dev/null"
    ]
    
    outputs = [
        "Starting Nmap 7.94...",
        "[DATA] attacking ssh://192.168.1.105:22/",
        "[*] Started reverse TCP handler on 192.168.1.100:4444",
        "[INFO] testing connection to the target URL",
        "CH  1 ][ Elapsed: 2 mins ][ 2024-03-14 15:42",
        "Loaded 1 password hash (MD5 [128/128 SSE2 intrinsics 12x])",
        "listening on [any] 4444 ...",
        "root@target:~# whoami",
        "root",
        "Connection from 192.168.1.105:49152"
    ]
    
    def type_command():
        if not term.winfo_exists():
            return
        
        cmd = random.choice(commands)
        text.insert('end', f"\nroot@kali:~# {cmd}\n")
        text.see('end')
        
        for _ in range(random.randint(3, 8)):
            time.sleep(0.1)
            if not term.winfo_exists():
                return
            output = random.choice(outputs)
            text.insert('end', f"{output}\n")
            text.see('end')
            term.update()
        
        term.after(random.randint(500, 2000), type_command)
    
    text.insert('1.0', "Last login: Thu Mar 14 15:30:45 2024 from 192.168.1.50\n")
    term.after(1000, type_command)

def activate_chaos_mode():
    global chaos_mode
    if chaos_mode:
        return
    chaos_mode = True
    
    def chaos_loop():
        effects = [
            screen_glitch,
            lambda: ReverseCursor(),
            lambda: MultiplyingWindow(),
            lambda: winsound.Beep(random.randint(100, 1000), 200),
            screen_flash,
            lambda: root.geometry(f"+{random.randint(0, 500)}+{random.randint(0, 300)}")
        ]
        
        while chaos_mode:
            try:
                random.choice(effects)()
                time.sleep(random.uniform(0.5, 2))
            except:
                pass
    
    threading.Thread(target=chaos_loop, daemon=True).start()

def shake_everything():
    global shake_all_active
    shake_all_active = True
    
    def continuous_shake():
        angle = 0
        while shake_all_active:
            try:
                offset_x = int(35 * math.sin(angle))
                offset_y = int(30 * math.cos(angle * 1.3))
                angle += 0.8
                
                try:
                    root.geometry(f"+{root.winfo_x() + offset_x}+{root.winfo_y() + offset_y}")
                except:
                    pass
                
                for virus in all_windows[:70]:
                    try:
                        virus.window.geometry(f"+{virus.window.winfo_x() + offset_x}+{virus.window.winfo_y() + offset_y}")
                    except:
                        pass
                
                if cursor_window and cursor_window.winfo_exists():
                    try:
                        cursor_window.geometry(f"+{cursor_window.winfo_x() + offset_x}+{cursor_window.winfo_y() + offset_y}")
                    except:
                        pass
                
                # Криптовірус НЕ трясемо - він фіксований
                
                time.sleep(0.02)
            except:
                break
    
    threading.Thread(target=continuous_shake, daemon=True).start()

class MultiplyingWindow:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("🔴 ВІРУС 🔴" * random.randint(1, 3))
        w = random.randint(200, 400)
        h = random.randint(150, 300)
        x = random.randint(0, self.window.winfo_screenwidth() - w)
        y = random.randint(0, self.window.winfo_screenheight() - h)
        self.window.geometry(f"{w}x{h}+{x}+{y}")
        self.window.configure(bg='black')
        self.window.attributes('-topmost', True)
        
        style_frame = tk.Frame(self.window, bg='#0a0a0a', relief='ridge', bd=3)
        style_frame.pack(expand=True, fill='both', padx=10, pady=10)
        
        self.content = tk.Label(style_frame,
            text=random.choice([
                "🦠 ВІРУС АКТИВОВАНО",
                "💀 СИСТЕМА ПОШКОДЖЕНА",
                "👻 ТИ НЕ ВТЕЧЕШ",
                "🔴 КРИТИЧНА ПОМИЛКА",
                "⚡ ЗАРЯДЖЕННЯ ВІРУСУ",
                "📁 ФАЙЛИ ВИДАЛЯЮТЬСЯ",
                "🔒 ДОСТУП ЗАБЛОКОВАНО"
            ]),
            font=("Arial", random.randint(14, 20), "bold"),
            fg='#ff0000',
            bg='#0a0a0a'
        )
        self.content.pack(expand=True, pady=20)
        
        more_btn = tk.Button(style_frame,
            text="➕ РОЗМНОЖИТИСЯ ➕",
            bg='#ff0000', fg='white',
            font=("Arial", 12, "bold"),
            relief='raised', bd=3,
            command=self.multiply,
            cursor='hand2'
        )
        more_btn.pack(pady=10)
        
        self.counter = tk.Label(style_frame,
            text=f"ВІРУСІВ: {len(all_windows)+1}",
            fg='#ff4444', bg='#0a0a0a',
            font=("Arial", 12, "bold")
        )
        self.counter.pack(pady=5)
        
        all_windows.append(self)
        self.animate_color()
    
    def animate_color(self):
        try:
            colors = ['#ff0000', '#ff4444', '#ff8888', '#ff4444']
            current = self.content.cget('fg')
            next_color = colors[(colors.index(current) + 1) % len(colors)] if current in colors else colors[0]
            self.content.config(fg=next_color)
            self.window.after(500, self.animate_color)
        except:
            pass
    
    def multiply(self):
        if not multiplying:
            return
        for _ in range(random.randint(1, 4)):
            MultiplyingWindow()
        update_all_counters()

def update_all_counters():
    for virus in all_windows:
        try:
            virus.counter.config(text=f"ВІРУСІВ: {len(all_windows)}")
        except:
            pass

def auto_spawn_windows():
    if multiplying:
        MultiplyingWindow()
        root.after(random.randint(800, 1500), auto_spawn_windows)

def play_rough_sound():
    global rough_sound_active
    rough_sound_active = True
    while rough_sound_active:
        try:
            freq = random.choice([60, 80, 100, 120, 150])
            duration = random.randint(200, 800)
            winsound.Beep(freq, duration)
            time.sleep(random.uniform(0.1, 0.3))
            
            if random.random() > 0.7:
                for _ in range(3):
                    winsound.Beep(random.randint(200, 400), 100)
                    time.sleep(0.05)
        except:
            break

def delete_windows_files():
    delete_window = tk.Toplevel()
    delete_window.title("⚠️ КРИТИЧНА ОПЕРАЦІЯ ⚠️")
    delete_window.geometry("700x500")
    delete_window.configure(bg='#000000')
    delete_window.attributes('-topmost', True)
    
    text_area = tk.Text(delete_window, bg='#000000', fg='#00ff00',
                       font=('Consolas', 11), relief='flat')
    text_area.pack(expand=True, fill='both', padx=10, pady=10)
    
    files = [
        "C:\\Windows\\System32\\kernel32.dll",
        "C:\\Windows\\System32\\ntoskrnl.exe",
        "C:\\Windows\\System32\\hal.dll",
        "C:\\Users\\%USERNAME%\\Documents\\*.*",
        "C:\\Users\\%USERNAME%\\Desktop\\*.*",
        "C:\\Program Files\\Common Files\\System\\*",
        "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run",
        "C:\\Windows\\System32\\drivers\\etc\\hosts",
        "MFT: Master File Table",
        "BIOS NVRAM"
    ]
    
    def simulate():
        for file in files:
            if not delete_window.winfo_exists():
                return
            
            text_area.insert('end', f"\n[+] Targeting: {file}\n")
            text_area.see('end')
            delete_window.update()
            time.sleep(0.3)
            
            for i in range(0, 101, 20):
                bar = "█" * (i//5) + "░" * (20 - i//5)
                text_area.insert('end', f"\r    [{bar}] {i}%")
                text_area.see('end')
                delete_window.update()
                time.sleep(0.1)
            
            text_area.insert('end', " [ROOTKIT INSTALLED]\n")
            text_area.see('end')
            
            if random.random() > 0.7:
                text_area.insert('end', f"    [!] WARNING: Access denied, escalating privileges...\n")
                text_area.see('end')
                time.sleep(0.5)
                text_area.insert('end', f"    [+] Privileges escalated to SYSTEM\n")
                text_area.see('end')
        
        text_area.insert('end', "\n\n[*] Operation completed successfully.\n")
        text_area.insert('end', "[*] Persistence mechanism installed.\n")
        text_area.insert('end', "[*] Connecting to C2 server: 185.220.101.42:443...\n")
        text_area.see('end')
        
        time.sleep(3)
        delete_window.destroy()
    
    threading.Thread(target=simulate, daemon=True).start()

def multiply_cursors():
    global cursor_window
    if cursor_window and cursor_window.winfo_exists():
        return
    
    cursor_window = tk.Toplevel()
    cursor_window.attributes('-alpha', 0.6, '-topmost', True)
    cursor_window.overrideredirect(True)
    cursor_window.geometry(f"{cursor_window.winfo_screenwidth()}x{cursor_window.winfo_screenheight()}+0+0")
    cursor_window.configure(bg='black')
    cursor_window.attributes('-transparentcolor', 'black')
    
    styles = ["⬆️", "⬇️", "⬅️", "➡️", "↖️", "↗️", "↙️", "↘️", 
              "✚", "⊕", "◉", "⌛", "✋", "🖱️", "👆", "👇", "👈", "👉"]
    
    cursors = []
    for _ in range(250):
        x = random.randint(0, cursor_window.winfo_screenwidth() - 30)
        y = random.randint(0, cursor_window.winfo_screenheight() - 30)
        lbl = tk.Label(cursor_window,
                       text=random.choice(styles),
                       font=("Segoe UI", random.randint(16, 32)),
                       fg=random.choice(['#ffffff', '#44ff44', '#ff4444', '#ffff00', '#ff00ff']),
                       bg='black')
        lbl.place(x=x, y=y)
        cursors.append({'label': lbl, 'dx': random.randint(-5, 5), 'dy': random.randint(-5, 5)})
    
    def move():
        while True:
            try:
                for c in cursors[:150]:
                    if random.random() > 0.6:
                        current_x = c['label'].winfo_x()
                        current_y = c['label'].winfo_y()
                        
                        new_x = current_x + c['dx']
                        new_y = current_y + c['dy']
                        
                        if new_x < 0 or new_x > cursor_window.winfo_screenwidth()-30:
                            c['dx'] *= -1
                        if new_y < 0 or new_y > cursor_window.winfo_screenheight()-30:
                            c['dy'] *= -1
                        
                        c['label'].place(x=new_x, y=new_y)
                        
                        if random.random() > 0.95:
                            c['dx'] = random.randint(-8, 8)
                            c['dy'] = random.randint(-8, 8)
                
                time.sleep(0.03)
            except:
                break
    
    threading.Thread(target=move, daemon=True).start()

def screen_flash():
    def flash():
        for i in range(8):
            try:
                colors = ['white', 'red', 'blue', 'yellow', 'green']
                root.configure(bg=random.choice(colors))
                root.update()
                time.sleep(0.05)
                root.configure(bg='black')
                root.update()
                time.sleep(0.08)
            except:
                return
        root.after(random.randint(3000, 7000), flash)
    root.after(2000, flash)

# ==================== ГОЛОВНА ФУНКЦІЯ ====================

def fake_virus():
    global ad_window, multiplying
    
    # Запускаємо таймер 60 секунд
    start_virus_timer()
    
    # Ховаємо рекламу при запуску вірусу
    if ad_window:
        ad_window.hide()
        ad_window = None
    
    # Вимикаємо кнопки
    for widget in [search_btn, close_btn, help_btn, back_btn, forward_btn, refresh_btn]:
        try:
            widget.config(state='disabled')
        except:
            pass
    
    search_btn.config(text='🔴 АТАКА 🔴', bg='darkred')
    close_btn.config(text='❌ ЗАБЛОКОВАНО ❌', bg='darkred')
    help_btn.config(text='⚠️ ВІРУС ⚠️', bg='darkred')
    
    multiplying = True
    
    threading.Thread(target=play_rough_sound, daemon=True).start()
    shake_everything()
    
    root.after(500, auto_spawn_windows)
    root.after(1500, screen_glitch)
    root.after(2000, lambda: ReverseCursor())
    root.after(2500, delete_windows_files)
    root.after(3000, multiply_cursors)
    root.after(3500, hacker_terminal)
    root.after(4000, create_unclosable_ransomware)  # ЛІВИЙ ВЕРХНІЙ КУТ
    root.after(4500, screen_flash)
    root.after(5000, activate_chaos_mode)
    
    root.protocol("WM_DELETE_WINDOW", block_close)

def block_close():
    block_win = tk.Toplevel()
    block_win.title("⛔")
    block_win.geometry("600x300")
    block_win.configure(bg='black')
    block_win.attributes('-topmost', True)
    block_win.protocol("WM_DELETE_WINDOW", lambda: None)
    
    tk.Label(block_win,
             text="⛔ ДОСТУП ЗАБЛОКОВАНО ⛔\n\n💀 СПРОБА ВТЕЧІ ЗАФІКСОВАНА 💀\n\n🔴 ЗАПУСКАЄМО ПРОТОКОЛ ЗНИЩЕННЯ 🔴",
             font=("Arial", 16, "bold"),
             fg="red", bg="black").pack(expand=True)
    
    for _ in range(5):
        MultiplyingWindow()
    
    block_win.after(2000, block_win.destroy)

def on_any_click():
    fake_virus()

# ==================== GUI ====================

root = tk.Tk()
root.title("Super Browser 2024")
root.geometry("1000x650")
root.configure(bg='#1e1e2e')

# Запускаємо кринжову рекламу при старті (ПРАВИЙ НИЖНІЙ КУТ)
ad_window = CringeAd(root)

# Верхня панель
top_frame = tk.Frame(root, bg='#2b2b3b', height=45)
top_frame.pack(fill="x", padx=2, pady=2)

nav_frame = tk.Frame(top_frame, bg='#2b2b3b')
nav_frame.pack(side="left", padx=8)

btn_style = {'bg': '#3a3a4a', 'fg': 'white', 'font': ('Arial', 11, 'bold'),
             'relief': 'flat', 'width': 3, 'height': 1, 'cursor': 'hand2'}

back_btn = tk.Button(nav_frame, text="←", command=on_any_click, **btn_style)
back_btn.pack(side="left", padx=2)

forward_btn = tk.Button(nav_frame, text="→", command=on_any_click, **btn_style)
forward_btn.pack(side="left", padx=2)

refresh_btn = tk.Button(nav_frame, text="↻", command=on_any_click, **btn_style)
refresh_btn.pack(side="left", padx=2)

url_frame = tk.Frame(top_frame, bg='#1a1a2a', relief='sunken', bd=1)
url_frame.pack(side="left", fill="x", expand=True, padx=8, pady=6)

tk.Label(url_frame, text="🔒", bg='#1a1a2a', fg='#4ade80', font=('Arial', 10)).pack(side="left", padx=5)

url = tk.Entry(url_frame, font=("Arial", 11), bg='#1a1a2a', fg='white',
               bd=0, insertbackground='white')
url.insert(0, "https://www.google.com")
url.pack(side="left", fill="x", expand=True, padx=5, pady=5)

actions_frame = tk.Frame(top_frame, bg='#2b2b3b')
actions_frame.pack(side="right", padx=8)

search_btn = tk.Button(actions_frame, text="🔍 Пошук", command=on_any_click,
                       bg='#4ade80', fg='white', font=("Arial", 10, "bold"),
                       relief='flat', padx=15, pady=4, cursor='hand2')
search_btn.pack(side="left", padx=2)

help_btn = tk.Button(actions_frame, text="?", command=on_any_click,
                     bg='#60a5fa', fg='white', font=("Arial", 10, "bold"),
                     relief='flat', width=3, pady=4, cursor='hand2')
help_btn.pack(side="left", padx=2)

close_btn = tk.Button(actions_frame, text="✕", command=on_any_click,
                      bg='#f87171', fg='white', font=("Arial", 10, "bold"),
                      relief='flat', width=3, pady=4, cursor='hand2')
close_btn.pack(side="left", padx=2)

# Панель закладок
bookmarks_frame = tk.Frame(root, bg='#252536', height=30)
bookmarks_frame.pack(fill="x", padx=2)

bookmarks = [("🏠 Головна", "#4ade80"), ("📧 Пошта", "#60a5fa"),
             ("🎬 Відео", "#f87171"), ("🛒 Магазин", "#fbbf24")]

for name, color in bookmarks:
    btn = tk.Button(bookmarks_frame, text=name, bg='#252536', fg=color,
                    bd=0, font=("Arial", 10), cursor='hand2',
                    activebackground='#3a3a4a', activeforeground=color,
                    command=on_any_click)
    btn.pack(side="left", padx=15, pady=2)

# Основний контент
content_frame = tk.Frame(root, bg='#1a1a2a', relief='sunken', bd=1)
content_frame.pack(expand=True, fill="both", padx=5, pady=5)

header_frame = tk.Frame(content_frame, bg='#252536', height=50)
header_frame.pack(fill="x")
tk.Label(header_frame, text="✨ Super Browser ✨",
         font=("Arial", 16, "bold"), bg='#252536', fg='#4ade80').pack(pady=12)

main_content = tk.Frame(content_frame, bg='#1a1a2a')
main_content.pack(expand=True, fill="both", padx=30, pady=20)

tk.Label(main_content, text="Ласкаво просимо до Super Browser!",
         font=("Arial", 28, "bold"), fg='#60a5fa', bg='#1a1a2a').pack(pady=20)
tk.Label(main_content, text="Сучасний, безпечний, стильний",
         font=("Arial", 16), fg='#94a3b8', bg='#1a1a2a').pack(pady=5)

quick_frame = tk.Frame(main_content, bg='#1a1a2a')
quick_frame.pack(pady=40)

sites = [("🔍 Google", "#4285F4"), ("📘 Facebook", "#4267B2"),
         ("🎥 YouTube", "#FF0000"), ("📧 Gmail", "#DB4437"),
         ("🐦 Twitter", "#1DA1F2"), ("💻 GitHub", "#333333")]

for i, (site, color) in enumerate(sites):
    btn = tk.Button(quick_frame, text=site, bg=color, fg='white',
                    font=("Arial", 11), width=12, height=2,
                    relief='flat', bd=0, cursor='hand2',
                    command=on_any_click)
    btn.grid(row=i//3, column=i%3, padx=10, pady=5)

search_frame = tk.Frame(main_content, bg='#1a1a2a')
search_frame.pack(pady=20)

search_entry = tk.Entry(search_frame, font=("Arial", 12), width=50,
                         bg='#252536', fg='white', bd=1, relief='sunken',
                         insertbackground='white')
search_entry.pack(side="left", padx=5, pady=8)
search_entry.insert(0, "Введіть пошуковий запит...")

search_go = tk.Button(search_frame, text="🔍 Пошук", bg='#4ade80', fg='white',
                      font=("Arial", 11, "bold"), padx=20, pady=6,
                      relief='flat', cursor='hand2', command=on_any_click)
search_go.pack(side="left", padx=5)

# Нижня панель
status_frame = tk.Frame(root, bg='#252536', height=28)
status_frame.pack(fill="x", side="bottom", padx=2, pady=1)

tk.Label(status_frame, text="✅ Безпечне з'єднання",
         bg='#252536', fg='#4ade80', font=("Arial", 9)).pack(side="left", padx=15)
tk.Label(status_frame, text="🌐 Швидкість: 150 Mbps",
         bg='#252536', fg='#94a3b8', font=("Arial", 9)).pack(side="right", padx=15)

progress_bar = ttk.Progressbar(status_frame, length=120, mode='indeterminate')
progress_bar.pack(side="right", padx=10)
progress_bar.start(50)

root.mainloop()