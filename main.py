import tkinter as tk
from Backend import *

master = tk.Tk()
master.title("Cryptology Project-1 Deneesh & Arun")
# Have two labels and inputs for the user to key in the plaintext or ciphertext
tk.Label(master, text="Alphabet:").grid(row=0)
tk.Label(master, text="Plaintext:").grid(row=1)
tk.Label(master, text="Ciphertext:").grid(row=2)
tk.Label(master, text="Value \"a\" in the key:").grid(row=3)
tk.Label(master, text="Value \"b\" in the key").grid(row=4)

alphabet = tk.Entry(master)
plaintext = tk.Entry(master)
ciphertext = tk.Entry(master)
a_value = tk.Entry(master)
b_value = tk.Entry(master)

alphabet.grid(row=0, column=1)
plaintext.grid(row=1, column=1)
ciphertext.grid(row=2, column=1)
a_value.grid(row=3, column=1)
b_value.grid(row=4, column=1)


def encrypt():
    ciphertext.delete(0, len(ciphertext.get()))
    encrypted_text = AffineCipher.encryption(alphabet.get(), int(a_value.get()), int(b_value.get()), plaintext.get())
    ciphertext.insert(0, encrypted_text)
def decrypt():
    plaintext.delete(0, len(plaintext.get()))
    decrypted_text = AffineCipher.decryption(alphabet.get(), int(a_value.get()), int(b_value.get()), ciphertext.get())
    plaintext.insert(0, decrypted_text)


#Button creation
tk.Button(master, text='Quit', command=master.quit).grid(row=6, column=0, sticky=tk.W, pady=4)
tk.Button(master, text='Encrypt', command=encrypt).grid(row=6, column=1, sticky=tk.W, pady=4)
tk.Button(master, text='Decrypt', command=decrypt).grid(row=6, column=2, sticky=tk.W, pady=4)
