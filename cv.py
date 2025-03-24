from tkinter import *

HEADER_BG = "#54788e"
HEADER_FG = "#FFFFFF"
BODY_BG = "#FFFFFF"
TEXT_FG = "#000000"

root = Tk()
root.title("Životopis - Daniel Šoltys")
root.geometry("750x750")
root.configure(bg=BODY_BG)

header = Frame(root, bg=HEADER_BG, height=100)
header.pack(fill="x")

name_label = Label(header, text="Daniel Šoltys", font=("Arial", 20, "bold"), bg=HEADER_BG, fg=HEADER_FG)
name_label.pack(anchor="w", padx=10, pady=10)

contact_label = Label(header, text="Branka u Opavy, 74741 | Tel: +420 605 583 329 | Email: soltys.dan@seznam.cz", 
                      font=("Arial", 12), bg=HEADER_BG, fg=HEADER_FG)
contact_label.pack(anchor="w", padx=10, pady=(0, 10))

content_frame = Frame(root, bg=BODY_BG)
content_frame.pack(fill="both", expand=True, padx=20, pady=20)

def add_section(title, items):
    title_label = Label(content_frame, text=title, font=("Arial", 14, "bold"), bg=BODY_BG, fg=TEXT_FG)
    title_label.pack(anchor="w")

    for item, details in items:
        content_label = Label(content_frame, text=item, font=("Arial", 11, "bold"), bg=BODY_BG, fg=TEXT_FG, justify="left")
        content_label.pack(anchor="w", padx=10)

        if details:
            for detail in details:
                detail_label = Label(content_frame, text=f"• {detail}", font=("Arial", 10), bg=BODY_BG, fg=TEXT_FG, justify="left")
                detail_label.pack(anchor="w", padx=20, pady=2)

    separator = Frame(content_frame, height=1, bg=TEXT_FG)
    separator.pack(fill="x", pady=(10, 10))

add_section("Vzdělání", [
    ("2019 - 2023\t\tStřední odborná škola dopravy a cestovního ruchu", 
     ["Obor: Ekonomika a podnikání"]),
    ("2023 - současnost\t\tVŠB-TU Ostrava - Fakulta Elektrotechniky a Informatiky", 
     ["Obor: Informatika"]),
    ("2024 - současnost\t\tSlezská univerzita Opava - Filozoficko-přírodovědecká fakulta", 
     ["Obor: Moderní informatika"])
])

add_section("Pracovní zkušenosti", [
    ("červen 2024 - březen 2025\tLetiště Leoše Janáčka", 
     ["Práce na pozici Bezpečnostní pracovník", "Zodpovědnost za kontrolu a bezpečnost cestujících a personálu"])
])

add_section("Jazyky", [
    ("Angličtina", ["Úroveň: C1, plynulá komunikace v mluvené i psané podobě"])
])

add_section("Dovednosti", [
    ("Programování", 
     ["C, C++, Python, C#"]),
    ("Další dovednosti", 
     ["Základy práce s databázemi (SQL), tvorba webových stránek pomocí HTML a CSS"])
])


root.mainloop()
