import tkinter as tk
from tkinter import ttk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.entryBoxes = []
        self.hours = 0
        self.mins = 0
        self.secs = 0
        self.msecs = 0
        self.master = master
        self.master.title("Tic Tac Toe")
        self.master.resizable(True, True)
        self.master.geometry("430x295")  # automatic size
        self.master.attributes("-topmost", True)
        self.pack(fill="both", expand=True)

        self.window()

    def window(self):
        self.top_panel()
        self.main_features()

        self.grid_columnconfigure(0, weight=1)

    def top_panel(self):
        topPanel = tk.Frame(self, bg="#000000")
        topPanel.grid(row=0, column=0, sticky="nsew")

        tittle = tk.Label(topPanel, text="AUTO CLICKER", bg="#000000", height=1, font=("Berlin Sans FB Demi", 30),
                          fg="#03DAC6")
        tittle.grid(row=0, column=0, rowspan=3, sticky="nsew")

        createdBy = tk.Label(topPanel, text="HALOW ™️", bg="#000000", height=1, font=("Berlin Sans FB Demi", 15),
                             fg="#FFFFFF")
        createdBy.grid(row=1, column=1, sticky="nsew")

        topPanel.grid_columnconfigure(0, weight=1)
        topPanel.grid_columnconfigure(1, weight=1)

    def main_features(self):
        mainFeatures = tk.Frame(self, bg="White")
        mainFeatures.grid(row=1, column=0, sticky="nsew")

        self.click_interval(mainFeatures)
        self.click_progress(mainFeatures)
        self.parameters(mainFeatures)

        mainFeatures.grid_columnconfigure(0, weight=1)

    def click_interval(self, parent):
        clickInterval = tk.Frame(parent, bg="#FFFFFF")
        clickInterval.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        labelNumber = 0

        hourTime = tk.Label(clickInterval, text="HOUR", bg="#FFFFFF", height=1, font=("Berlin Sans FB Demi", 10),
                            fg="#000000")
        hourTime.grid(row=0, column=0, sticky="nsew")

        minTime = tk.Label(clickInterval, text="MINUITE", bg="#FFFFFF", height=1, font=("Berlin Sans FB Demi", 10),
                           fg="#000000")
        minTime.grid(row=0, column=2, sticky="nsew")

        secTime = tk.Label(clickInterval, text="SECOND", bg="#FFFFFF", height=1, font=("Berlin Sans FB Demi", 10),
                           fg="#000000")
        secTime.grid(row=0, column=4, sticky="nsew")

        msecTime = tk.Label(clickInterval, text="MILI SECOND", bg="#FFFFFF", height=1, font=("Berlin Sans FB Demi", 10),
                            fg="#000000")
        msecTime.grid(row=0, column=6, sticky="nsew")

        for i in range(1, 8):
            if i % 2 != 0:
                entryBox = tk.Entry(clickInterval, bg="#FFFFFF", fg="#000000", font=("impact", 30), relief="flat",
                                    justify=tk.CENTER)
                entryBox.insert(0, "00")
                entryBox.bind("<KeyRelease>", lambda event: self.validate_input1())
                entryBox.bind("<FocusOut>", lambda event: self.validate_input2())
                entryBox.grid(row=1, column=(i - 1), sticky="ew")
                self.entryBoxes.append(entryBox)

            elif i % 2 != 1:
                if labelNumber <= 2:
                    labelNumber += 1
                    label = tk.Label(clickInterval, text="-", bg="#FFFFFF", font=("Berlin Sans FB Demi", 30))
                    label.grid(row=1, column=(i - 1))

        for i in range(0, 8, 2):
            clickInterval.grid_columnconfigure(i, weight=1)

    def validate_input1(self):
        for entryBox in self.entryBoxes:
            text = entryBox.get()
            cleaned_text = ''.join(filter(str.isdigit, text))
            cleaned_text = cleaned_text[-2:]
            entryBox.delete(0, tk.END)
            entryBox.insert(0, cleaned_text)

    def validate_input2(self):
        for entryBox in self.entryBoxes:
            fixed_text = entryBox.get()
            if len(fixed_text) == 0:
                fixed_text = "00"
            elif len(fixed_text) == 1:
                fixed_text = "0" + fixed_text
            entryBox.delete(0, tk.END)
            entryBox.insert(0, fixed_text)

    def click_progress(self, parent):
        progress = tk.Frame(parent, bg="#FFFFFF")
        progress.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

        style = ttk.Style()
        style.theme_use('default')
        style.configure("custom.Horizontal.TProgressbar", troughcolor="#707070", borderwidth=0, bordercolor="#FFFFFF",
                        background="#03DAC6")
        progressBar = ttk.Progressbar(progress, orient="horizontal", mode="determinate", value=50,
                                      style="custom.Horizontal.TProgressbar")
        progressBar.grid(row=3, column=0, columnspan=6, sticky="nsew")

        progress.grid_columnconfigure(0, weight=1)

    def parameters(self, parent):
        parameters = tk.Frame(parent, bg="#FFFFFF")
        parameters.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)

        start = tk.Button(parameters, bg="#383838", text="START", fg="#FFFFFF", font=("Berlin Sans FB Demi", 15),
                          width=3, relief="flat", padx=20)
        start.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        stop = tk.Button(parameters, bg="#707070", text="STOP", fg="#FFFFFF", font=("Berlin Sans FB Demi", 15),
                         width=3, relief="flat", padx=20, state="disabled", disabledforeground="#FFFFFF")
        stop.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

        settings = tk.Button(parameters, bg="#383838", text="SETTING", fg="#FFFFFF", font=("Berlin Sans FB Demi", 15),
                             width=3, relief="flat", padx=20, command=self.open_settings_window)
        settings.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

        quit = tk.Button(parameters, bg="#383838", text="QUIT", fg="#FFFFFF", font=("Berlin Sans FB Demi", 15),
                         width=3, relief="flat", padx=20)
        quit.grid(row=2, column=2, sticky="nsew", padx=5, pady=5)

        parameters.grid_columnconfigure(0, weight=1)
        parameters.grid_columnconfigure(2, weight=1)

    def open_settings_window(self):
        settings_window = tk.Toplevel(self.master)
        settings_window.title("Settings")
        settings_window.geometry("450x450")
        settings_window.grab_set()
        settings_window.attributes("-topmost", True)
        settings_window.columnconfigure(0, weight=1)
        self.setting_window(settings_window)

    def setting_window(self, parent):
        settingWindow = tk.Frame(parent, bg="#707070", pady=5, padx=5)
        settingWindow.grid(row=0, column=0, sticky="nsew")

        self.click_type(settingWindow)
        self.click_repeat(settingWindow)
        self.cursor_position(settingWindow)
        self.hotkey_setting(settingWindow)
        self.setting_parameter(settingWindow)

        settingWindow.columnconfigure(0, weight=1)
        settingWindow.columnconfigure(1, weight=1)

    def click_type(self, parent):
        clickType = tk.Frame(parent, bg="#FFFFFF", pady=10, padx=10)
        clickType.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

        mouseButtonLabel = tk.Label(clickType, text="MOUSE BUTTON", bg="#FFFFFF", height=1,
                                    font=("Berlin Sans FB Demi", 15), fg="#000000")
        mouseButtonLabel.grid(row=0, column=0, columnspan=5, sticky="w")

        radioStyle = ttk.Style()

        radioStyle.configure("TRadiobutton", padding=4, relief="flat", background="#FFFFFF", foreground="#707070",
                             font=("Berlin Sans FB Demi", 10), borderwidth=0, sticky="w")

        radioStyle.map("TRadiobutton", background=[("selected", "#FFFFFF")], foreground=[("selected", "#03DAC6")])

        radioStyle.map("TRadiobutton", focuscolor=[("", "")], focusthickness=[("", 0)])

        mouseButtonOption = tk.StringVar()

        leftClick = ttk.Radiobutton(clickType, text="LEFT", variable=mouseButtonOption, value="Left")
        leftClick.grid(row=1, column=0, sticky="w", pady=6)

        rightClick = ttk.Radiobutton(clickType, text="RIGHT", variable=mouseButtonOption, value="Right")
        rightClick.grid(row=2, column=0, sticky="w")

        middleClick = ttk.Radiobutton(clickType, text="MIDDLE", variable=mouseButtonOption, value="Middle")
        middleClick.grid(row=3, column=0, sticky="w", pady=6)

        mouseButtonOption.set("Left")

        clickTypeLabel = tk.Label(clickType, text="CLICK TYPE", bg="#FFFFFF", height=1,
                                  font=("Berlin Sans FB Demi", 15), fg="#000000")
        clickTypeLabel.grid(row=0, column=5, columnspan=5, sticky="w")

        clickTypeOption = tk.StringVar()

        singleClick = ttk.Radiobutton(clickType, text="SINGLE", variable=clickTypeOption, value="Single")
        singleClick.grid(row=1, column=5, sticky="w")

        doubleClick = ttk.Radiobutton(clickType, text="DOUBLE", variable=clickTypeOption, value="Double")
        doubleClick.grid(row=2, column=5, sticky="w")

        clickTypeOption.set("Single")

        clickType.columnconfigure(1, weight=1)
        clickType.columnconfigure(5, weight=1)

    def click_repeat(self, parent):
        clickRepeat = tk.Frame(parent, bg="#FFFFFF", pady=10, padx=10)
        clickRepeat.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        clickRepeatLabel = tk.Label(clickRepeat, text="REPEAT TYPE", bg="#FFFFFF", height=1,
                                    font=("Berlin Sans FB Demi", 15), fg="#000000")
        clickRepeatLabel.grid(row=0, column=0, columnspan=5, sticky="w")

        clickRepeatOption = tk.StringVar()

        repeat1 = ttk.Radiobutton(clickRepeat, text="REPEAT", variable=clickRepeatOption, value="Repeat1")
        repeat1.grid(row=1, column=0, sticky="w", pady=6)

        spinbox = tk.Spinbox(clickRepeat, bg="#FFFFFF", fg="#000000", font=("impact", 10), relief="flat", width=5,
                             justify=tk.CENTER)
        spinbox.grid(row=1, column=1)

        repeat1Label = tk.Label(clickRepeat, text="TIMES", bg="#FFFFFF", height=1,
                                font=("Berlin Sans FB Demi", 10), fg="#383838")
        repeat1Label.grid(row=1, column=2, columnspan=5, sticky="w")

        repeat2 = ttk.Radiobutton(clickRepeat, text="REPEAT UNTIL STOPPED", variable=clickRepeatOption, value="Repeat2")
        repeat2.grid(row=2, column=0, columnspan=5, sticky="w")

        clickRepeatOption.set("Repeat2")

    def hotkey_setting(self, parent):
        hotkeySetting = tk.Frame(parent, bg="#FFFFFF", pady=10, padx=10)
        hotkeySetting.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

        hotkeySettingLabel = tk.Label(hotkeySetting, text="HOTKEY SETTING", bg="#FFFFFF", height=1,
                                      font=("Berlin Sans FB Demi", 15), fg="#000000")
        hotkeySettingLabel.grid(row=0, column=0, columnspan=6, sticky="w")

        hotkeyShortcut = tk.Entry(hotkeySetting, bg="#FFFFFF", fg="#000000", font=("Impact", 13), relief="flat",
                                  justify=tk.CENTER, width=10)
        hotkeyShortcut.grid(row=2, column=0, pady=6)

        pickLocationButton = tk.Button(hotkeySetting, text="START / STOP", bg="#383838", fg="#FFFFFF",
                                       font=("Berlin Sans FB Demi", 13), width=10, relief="flat")
        pickLocationButton.grid(row=4, column=0)

        hotkeySetting.columnconfigure(0, weight=1)
        hotkeySetting.rowconfigure(3, weight=1)

    def cursor_position(self, parent):
        cursorPosition = tk.Frame(parent, bg="#FFFFFF", pady=10, padx=10)
        cursorPosition.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

        cursorPositionLabel = tk.Label(cursorPosition, text="CURSOR POSITION", bg="#FFFFFF", height=1,
                                       font=("Berlin Sans FB Demi", 15), fg="#000000")
        cursorPositionLabel.grid(row=0, column=0, columnspan=6, sticky="w")

        cursorPositionOption = tk.StringVar()

        currentLocation = ttk.Radiobutton(cursorPosition, text="CURRENT LOCATION", variable=cursorPositionOption,
                                          value="currentLocation")
        currentLocation.grid(row=1, column=0, columnspan=6, sticky="w")

        pickLocation = ttk.Radiobutton(cursorPosition, text="", variable=cursorPositionOption,
                                       value="pickLocation")
        pickLocation.grid(row=1, column=8, sticky="w")

        pickLocationButton = tk.Button(cursorPosition, text="PICK LOCATION",bg="#383838", fg="#FFFFFF", font=("Berlin Sans FB Demi", 10),
                                       relief="flat")
        pickLocationButton.grid(row=1, column=9)

        pickLocationXLabel = tk.Label(cursorPosition, text="X", bg="#FFFFFF", height=1,
                                      font=("Berlin Sans FB Demi", 10), fg="#000000")
        pickLocationXLabel.grid(row=1, column=10, sticky="w")

        pickLocationX = tk.Entry(cursorPosition, bg="#FFFFFF", fg="#000000", font=("Impact", 13), relief="flat",
                                 justify=tk.CENTER, width=3)
        pickLocationX.grid(row=1, column=11)

        pickLocationYLabel = tk.Label(cursorPosition, text="Y", bg="#FFFFFF", height=1,
                                      font=("Berlin Sans FB Demi", 10), fg="#000000")
        pickLocationYLabel.grid(row=1, column=12, sticky="w")

        pickLocationY = tk.Entry(cursorPosition, bg="#FFFFFF", fg="#000000", font=("Impact", 13), relief="flat",
                                 justify=tk.CENTER, width=3)
        pickLocationY.grid(row=1, column=13)

        cursorPositionOption.set("currentLocation")

        for i in range(14):
            cursorPosition.columnconfigure(i, weight=1)

    def setting_parameter(self, parent):
        settingParameter = tk.Frame(parent, bg="#707070", padx=10, pady=10)
        settingParameter.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

        save = tk.Button(settingParameter, bg="#383838", text="START", fg="#FFFFFF", font=("Berlin Sans FB Demi", 15),
                         width=3, relief="flat", padx=20)
        save.grid(row=0, column=1, sticky="nsew", padx=5)

        cancel = tk.Button(settingParameter, bg="#383838", text="STOP", fg="#FFFFFF", font=("Berlin Sans FB Demi", 15),
                           width=3, relief="flat", padx=20)
        cancel.grid(row=0, column=3, sticky="nsew", padx=5)

        for i in range(5):
            settingParameter.columnconfigure(i, weight=1)


root = tk.Tk()

app = Application(master=root)

app.mainloop()
