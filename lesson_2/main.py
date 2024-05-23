def steganography_encrypt(text):
    encrypted_text = ''
    for char in text:
        encrypted_text += char + ' '  # добавляем пробел после каждого символа
    return encrypted_text

def steganography_decrypt(text):
    decrypted_text = ''
    text_list = text.split()
    for i in range(0, len(text_list), 2):
        decrypted_text += text_list[i]  # берем только каждый нечетный символ
    return decrypted_text

# Пример текста для шифрования
original_text = "Скрывайте информацию в межсимвольных интервалах"

# Зашифровываем текст
encrypted_text = steganography_encrypt(original_text)
print("Зашифрованный текст:", encrypted_text)

# Расшифровываем текст
decrypted_text = steganography_decrypt(encrypted_text)
print("Расшифрованный текст:", decrypted_text)