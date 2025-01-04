#!/usr/bin/env python
# coding: utf-8

# In[4]:


import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from fpdf import FPDF
from datetime import datetime, timedelta

class WeeklyPlannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Planejador Semanal")
        self.root.geometry("1200x850")

        self.activities = []
        self.schedule = []
        self.selected_day = None
        self.selected_time = None

        # Header
        header = tk.Label(root, text="Planejador Semanal - Organização de Atividades", font=("Helvetica", 16, "bold"), fg="white", bg="#4CAF50", pady=10)
        header.pack(fill="x")

        # Frame para os campos
        frame = tk.Frame(root, padx=10, pady=10)
        frame.pack(fill="both", expand=True)

        # Campo para Nome da Atividade
        tk.Label(frame, text="Atividade:", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w", pady=5)
        self.activity_entry = ttk.Entry(frame, width=30)
        self.activity_entry.grid(row=0, column=1, pady=5)

        # Botão para adicionar
        add_button = ttk.Button(frame, text="Adicionar Atividade", command=self.add_activity)
        add_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Grade de horários interativa
        self.days = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
        self.times = ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00"]

        self.schedule_frame = tk.Frame(root, padx=10, pady=10)
        self.schedule_frame.pack(fill="both", expand=True)

        tk.Label(self.schedule_frame, text="Planejamento da Semana", font=("Helvetica", 14, "bold")).grid(row=0, column=0, columnspan=len(self.days) + 1, pady=10)

        tk.Label(self.schedule_frame, text="Horários", font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", width=10).grid(row=1, column=0)
        for col, day in enumerate(self.days, start=1):
            tk.Label(self.schedule_frame, text=day, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", width=15).grid(row=1, column=col)

        self.schedule_buttons = {}
        for row, time in enumerate(self.times, start=2):
            tk.Label(self.schedule_frame, text=time, font=("Helvetica", 12), width=10).grid(row=row, column=0)
            for col, day in enumerate(self.days, start=1):
                btn = tk.Button(self.schedule_frame, text="Livre", font=("Helvetica", 10), bg="lightgray", width=15, command=lambda d=day, t=time: self.assign_schedule(d, t))
                btn.grid(row=row, column=col)
                self.schedule_buttons[(day, time)] = btn

        # Botões de ação
        export_button = ttk.Button(root, text="Exportar Planejamento para PDF", command=self.export_schedule_to_pdf)
        export_button.pack(pady=10)

    def add_activity(self):
        activity = self.activity_entry.get()

        if not activity:
            messagebox.showwarning("Atenção", "Preencha o nome da atividade antes de adicionar.")
            return

        self.activities.append(activity)
        messagebox.showinfo("Sucesso", "Atividade adicionada com sucesso!")

        # Limpar campos
        self.activity_entry.delete(0, tk.END)

    def assign_schedule(self, day, time):
        if not self.activities:
            messagebox.showwarning("Atenção", "Adicione pelo menos uma atividade antes de atribuir horários.")
            return

        activity = self.activities[-1]  # Pega a última atividade adicionada

        self.schedule.append({"day": day, "time": time, "activity": activity})
        btn = self.schedule_buttons[(day, time)]
        btn.config(text=activity, bg="#4CAF50", fg="white")

    def export_schedule_to_pdf(self):
        if not self.schedule:
            messagebox.showwarning("Atenção", "Nenhum planejamento foi preenchido para exportar.")
            return

        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="Planejamento Semanal", ln=True, align="C")

        pdf.set_font("Arial", size=10)
        pdf.cell(30, 10, "Horários", border=1, align="C")
        for day in self.days:
            pdf.cell(32, 10, day, border=1, align="C")
        pdf.ln()

        for time in self.times:
            pdf.cell(30, 10, time, border=1, align="C")
            for day in self.days:
                entries = [s for s in self.schedule if s["day"] == day and s["time"] == time]
                if entries:
                    cell_content = entries[0]['activity']
                else:
                    cell_content = "Livre"
                pdf.cell(32, 10, cell_content, border=1, align="C")
            pdf.ln()

        filename = "C:/Users/ppeli/OneDrive/Área de Trabalho/Horario/planejamento_semanal.pdf"
        pdf.output(filename)

        messagebox.showinfo("Sucesso", f"Planejamento exportado para {filename}!")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeeklyPlannerApp(root)
    root.mainloop()


# In[ ]:




