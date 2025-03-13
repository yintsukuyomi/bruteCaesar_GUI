import tkinter as tk
from tkinter import messagebox

def caesar_brute_force(ciphertext, alphabet='abcdefghijklmnopqrstuvwxyz'):
    results = []
    for shift in range(len(alphabet)):
        decrypted_text = ''
        for char in ciphertext:
            if char.isalpha():
                shift_index = alphabet.index(char.lower()) - shift
                decrypted_char = alphabet[shift_index % len(alphabet)]
                if char.isupper():
                    decrypted_text += decrypted_char.upper()
                else:
                    decrypted_text += decrypted_char
            else:
                decrypted_text += char
        results.append(f"Shift {shift}: {decrypted_text}")
    return results

def on_decrypt():
    ciphertext = entry_ciphertext.get()
    alphabet_choice = var_alphabet.get()

    if not ciphertext:
        messagebox.showwarning("Input Error", "Please enter a ciphertext.")
        return

    if alphabet_choice == 'tr':
        alphabet = 'abcçdefgğhıijklmnoöprsştuüvyz'
    else:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

    entry_ciphertext.config(state=tk.DISABLED)
    radio_english.config(state=tk.DISABLED)
    radio_turkish.config(state=tk.DISABLED)
    button_decrypt.config(state=tk.DISABLED)

    results = caesar_brute_force(ciphertext, alphabet)

    entry_ciphertext.config(state=tk.NORMAL)
    radio_english.config(state=tk.NORMAL)
    radio_turkish.config(state=tk.NORMAL)
    button_decrypt.config(state=tk.NORMAL)

    result_text.delete(1.0, tk.END)
    for result in results:
        result_text.insert(tk.END, result + "\n")

root = tk.Tk()
root.title("Caesar Cipher Brute Force")
root.geometry("500x400")
root.config(bg="#E3F2FD")

header_label = tk.Label(root, text="Caesar Cipher Brute Force", font=("Helvetica", 16, "bold"), bg="#E3F2FD", fg="#1976D2")
header_label.pack(pady=10)

label_ciphertext = tk.Label(root, text="Enter Ciphertext:", font=("Helvetica", 12), bg="#E3F2FD", fg="#1976D2")
label_ciphertext.pack(pady=5)

entry_ciphertext = tk.Entry(root, width=50, font=("Helvetica", 12))
entry_ciphertext.pack(pady=5)

label_alphabet = tk.Label(root, text="Choose Alphabet (English or Turkish):", font=("Helvetica", 12), bg="#E3F2FD", fg="#1976D2")
label_alphabet.pack(pady=5)

var_alphabet = tk.StringVar(value='en')
radio_english = tk.Radiobutton(root, text="English", variable=var_alphabet, value='en', font=("Helvetica", 12), bg="#E3F2FD", fg="#1976D2", activebackground="#E3F2FD", activeforeground="#1976D2")
radio_english.pack(pady=3)
radio_turkish = tk.Radiobutton(root, text="Turkish", variable=var_alphabet, value='tr', font=("Helvetica", 12), bg="#E3F2FD", fg="#1976D2", activebackground="#E3F2FD", activeforeground="#1976D2")
radio_turkish.pack(pady=3)

button_decrypt = tk.Button(root, text="Decrypt", font=("Helvetica", 12), bg="#1976D2", fg="white", command=on_decrypt)
button_decrypt.pack(pady=20)

result_label = tk.Label(root, text="Decryption Results:", font=("Helvetica", 12), bg="#E3F2FD", fg="#1976D2")
result_label.pack(pady=5)

result_text = tk.Text(root, height=10, width=60, font=("Helvetica", 12), wrap=tk.WORD, bd=2, relief="sunken", bg="#BBDEFB", fg="#1976D2")
result_text.pack(pady=10)

root.mainloop()
