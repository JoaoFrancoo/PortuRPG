import tkinter as tk
from tkinter import messagebox

# Estado inicial
hp = 100
enemy_hp = 100
dano = 10
dano_inimigo = 10

def atacar():
    global enemy_hp, hp
    enemy_hp -= dano
    hp -= dano_inimigo
    atualizar_labels()

    if hp <= 0:
        messagebox.showinfo("Game Over", "Perdeste 😵")
        root.quit()
    elif enemy_hp <= 0:
        messagebox.showinfo("Vitória", "Ganhaste lil homie! 🏆")
        root.quit()

def escolher_item():
    global dano, dano_inimigo
    escolha = item_input.get().lower()

    if escolha == "espada":
        dano = 20
        status_label["text"] = "Usaste a espada! Dano aumentado."
    elif escolha == "escudo":
        dano_inimigo = 5
        status_label["text"] = "Usaste o escudo! Dano do inimigo reduzido."
    elif escolha == "vassoura":
        dano = 50
        status_label["text"] = "Pegaste na vassoura mágica! 💥"
    else:
        status_label["text"] = "Item inválido."

def atualizar_labels():
    hp_label["text"] = f"Teu HP: {hp}"
    enemy_label["text"] = f"HP do inimigo: {enemy_hp}"

root = tk.Tk()
root.title("PortuRPG")

hp_label = tk.Label(root, text=f"Teu HP: {hp}")
hp_label.pack()

enemy_label = tk.Label(root, text=f"HP do inimigo: {enemy_hp}")
enemy_label.pack()

btn_atacar = tk.Button(root, text="Atacar", command=atacar)
btn_atacar.pack(pady=5)


item_input = tk.Entry(root)
item_input.pack()

btn_item = tk.Button(root, text="Usar item", command=escolher_item)
btn_item.pack(pady=5)


status_label = tk.Label(root, text="")
status_label.pack(pady=10)

root.mainloop()
