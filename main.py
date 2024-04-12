import tkinter as tk
from typing import Any
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Comic Sans MS"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✓"
reps = 0
working = False
timer: Any = None


def main() -> None:
    def appear_on_top() -> None:
        """Make main window pop up to the top."""
        pomodoro_app.attributes("-topmost", True)
        pomodoro_app.attributes("-topmost", False)

    # ---------------------------- TIMER RESET ------------------------------- #
    def reset_timer() -> None:
        """Cancel current active timer and reset displayed time."""
        global reps
        reps = 0
        pomodoro_app.after_cancel(timer)
        checkmarks["text"] = ""
        tomato.itemconfig(timer_txt, text="00:00")
        label["text"] = "Timer"
        start_btn.config(state="normal")

    # ---------------------------- TIMER MECHANISM ------------------------------- #
    def start_timer() -> None:
        """Start timer and update displayed time."""
        start_btn.config(state="disabled")
        global reps
        reps += 1

        work_sec: int = WORK_MIN * 60
        short_break_sec: int = SHORT_BREAK_MIN * 60
        long_break_sec: int = LONG_BREAK_MIN * 60

        if reps % 8 == 0:
            label.config(text="Long Break", fg=RED)
            countdown(long_break_sec)
            appear_on_top()
        elif reps % 2 == 0:
            label.config(text="Short Break", fg=PINK)
            countdown(short_break_sec)
            appear_on_top()
        else:
            label.config(text="Work", fg=GREEN)
            countdown(work_sec)

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
    def countdown(count: int) -> None:
        """Start countdown and display time left on the canvas."""
        global timer

        count_minute: int = count // 60
        count_sec: int = count % 60
        # string format :02 -> 2 as many trailing 0s required to satisfy the minimum length of 2
        count_sec: str = f"{count_sec:02}"

        tomato.itemconfig(timer_txt, text=f"{count_minute}:{count_sec}")
        if count > 0:
            timer = pomodoro_app.after(1000, countdown, count - 1)
        else:
            start_timer()
            marks: str = ""
            print(reps)
            work_sessions: int = reps // 2
            for _ in range(work_sessions):
                marks += CHECKMARK
            checkmarks.config(text=marks)

    # ---------------------------- UI SETUP ------------------------------- #
    pomodoro_app = tk.Tk()
    pomodoro_app.title("Pomodoro app")
    pomodoro_app.geometry("600x500")
    pomodoro_app.config(bg=YELLOW, padx=100, pady=40)

    label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 36, "bold"))
    label.grid(column=1, row=0)

    tomato_img = tk.PhotoImage(file="tomato.png")

    tomato = tk.Canvas(width=300, height=250, bg=YELLOW, highlightthickness=0)
    tomato.create_image(150, 125, image=tomato_img)
    tomato.grid(column=1, row=1)
    timer_txt = tomato.create_text(150, 150, text="00:00", font=(FONT_NAME, 18, "bold"), fill="white")

    start_btn = tk.Button(text="Start", font=(FONT_NAME, 16), borderwidth=0.5, command=start_timer)
    start_btn.grid(column=0, row=2)

    reset_btn = tk.Button(text="Reset", font=(FONT_NAME, 16), borderwidth=0.5, command=reset_timer)
    reset_btn.grid(column=2, row=2)

    checkmarks = tk.Label(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
    checkmarks.grid(column=1, row=3)

    pomodoro_app.mainloop()


if __name__ == "__main__":
    main()
