import tkinter as tk
from tkinter import ttk
import json

class Benzin:
    def __init__(self, qiymetler):
        self.qiymetler = qiymetler
        self.secilmis_nov = None

    def sec(self, nov):
        self.secilmis_nov = nov

    def qiymet(self):
        return self.qiymetler.get(self.secilmis_nov, 0)

class Kafe:
    def __init__(self):
        self.mehsullar = {
            "Hotdog": {"qiymet": 4.00, "var": False, "miqdar": 0},
            "Hamburger": {"qiymet": 5.40, "var": False, "miqdar": 0},
            "Fri": {"qiymet": 7.20, "var": False, "miqdar": 0},
            "Coca-Cola": {"qiymet": 4.40, "var": False, "miqdar": 0},
        }

    def yenile(self, mehsul, var, miqdar):
        if mehsul in self.mehsullar:
            self.mehsullar[mehsul]["var"] = var
            self.mehsullar[mehsul]["miqdar"] = miqdar

    def cem(self):
        return sum(m["qiymet"] * m["miqdar"] for m in self.mehsullar.values() if m["var"])

class FileHandler:
    @staticmethod
    def save_data(data, filename):
        with open(filename, 'w') as file:
            json.dump(data, file)
    
    @staticmethod
    def load_data(filename):
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.title("BestOil")

        self.benzin = Benzin({
            "A-92": 6.40,
            "A-95": 7.10,
            "A-98": 7.70,
            "Dizel": 6.20
        })

        self.kafe = Kafe()

        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        benzin_frame = tk.LabelFrame(self, text="LoolOil", padx=10, pady=10)
        benzin_frame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

        tk.Label(benzin_frame, text="Benzin").grid(row=0, column=0, sticky="w")
        self.benzin_combobox = ttk.Combobox(benzin_frame, values=list(self.benzin.qiymetler.keys()))
        self.benzin_combobox.bind("<<ComboboxSelected>>", self.benzin_secilib)
        self.benzin_combobox.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(benzin_frame, text="Qiymət").grid(row=1, column=0, sticky="w")
        self.secilmis_qiymet = tk.StringVar(value="0.00")
        tk.Label(benzin_frame, textvariable=self.secilmis_qiymet).grid(row=1, column=1, sticky="w")

        tk.Label(benzin_frame, text="Miqdar").grid(row=2, column=0, sticky="w")
        self.litr_girisi = tk.Entry(benzin_frame)
        self.litr_girisi.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(benzin_frame, text="Cəm").grid(row=3, column=0, sticky="w")
        self.benzin_cemi_labeli = tk.Label(benzin_frame, text="0.00 AZN")
        self.benzin_cemi_labeli.grid(row=3, column=1, sticky="w")

        kafe_frame = tk.LabelFrame(self, text="Mini-Kafe", padx=10, pady=10)
        kafe_frame.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")

        self.kafe_vars = {}
        for i, (mehsul, details) in enumerate(self.kafe.mehsullar.items()):
            var = tk.IntVar()
            self.kafe_vars[mehsul] = var
            tk.Checkbutton(kafe_frame, text=f"{mehsul} ({details['qiymet']} AZN)", variable=var, command=lambda m=mehsul: self.update_kafe(m)).grid(row=i, column=0, sticky="w")
            girisi = tk.Entry(kafe_frame, width=5)
            girisi.grid(row=i, column=1)
            self.kafe.mehsullar[mehsul]["girisi"] = girisi

        tk.Label(kafe_frame, text="Kafe Cəmi:").grid(row=len(self.kafe.mehsullar), column=0, sticky="w")
        self.kafe_cemi_labeli = tk.Label(kafe_frame, text="0.00 AZN")
        self.kafe_cemi_labeli.grid(row=len(self.kafe.mehsullar), column=1, sticky="w")

        self.hesabla_button = tk.Button(self, text="Ümumi Hesabla", command=self.umumi_hesabla)
        self.hesabla_button.grid(row=1, column=0, columnspan=2, pady=10)

        tk.Label(self, text="Ümumi Cəm:").grid(row=2, column=0, sticky="e")
        self.umumi_labeli = tk.Label(self, text="0.00 AZN")
        self.umumi_labeli.grid(row=2, column=1, sticky="w")

    def benzin_secilib(self, event):
        secilmis_benzin = self.benzin_combobox.get()
        self.benzin.sec(secilmis_benzin)
        self.secilmis_qiymet.set(f"{self.benzin.qiymet():.2f}")

    def update_kafe(self, mehsul):
        var = self.kafe_vars[mehsul].get()
        miqdar = int(self.kafe.mehsullar[mehsul]["girisi"].get() or 0)
        self.kafe.yenile(mehsul, var, miqdar)

    def umumi_hesabla(self):
        try:
            benzin_miqdari = float(self.litr_girisi.get()) if self.litr_girisi.get() else 0
            benzin_qiymeti = self.benzin.qiymet()
            kafe_cemi = self.kafe.cem()

            benzin_cemi = benzin_miqdari * benzin_qiymeti
            self.benzin_cemi_labeli.config(text=f"{benzin_cemi:.2f} AZN")
            self.kafe_cemi_labeli.config(text=f"{kafe_cemi:.2f} AZN")
            self.umumi_labeli.config(text=f"{benzin_cemi + kafe_cemi:.2f} AZN")
            self.save_data()
        except ValueError:
            self.umumi_labeli.config(text="Yanlış giriş!")

    def save_data(self):
        data = {
            "benzin": self.benzin.secilmis_nov,
            "kafe": {mehsul: {"var": details["var"], "miqdar": details["miqdar"]} for mehsul, details in self.kafe.mehsullar.items()}
        }
        FileHandler.save_data(data, "data.json")

    def load_data(self):
        data = FileHandler.load_data("data.json")
        if data:
            if "benzin" in data:
                self.benzin_combobox.set(data["benzin"])
                self.benzin.sec(data["benzin"])
            if "kafe" in data:
                for mehsul, details in data["kafe"].items():
                    if mehsul in self.kafe.mehsullar:
                        self.kafe_vars[mehsul].set(details["var"])
                        self.kafe.mehsullar[mehsul]["girisi"].delete(0, tk.END)
                        self.kafe.mehsullar[mehsul]["girisi"].insert(0, details["miqdar"])

if __name__ == "__main__":
    app = Application()
    app.mainloop()
