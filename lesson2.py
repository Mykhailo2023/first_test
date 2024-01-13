'''def string_to_codes(string: str) -> dict:
    # Ініціалізація словника для зберігання кодів
    codes = {}  
    # Перебір кожного символу в рядку
    for ch in string:  
        # Перевірка, чи символ вже є в словнику
        if ch not in codes:
            # Додавання пари символ-код в словник  
            codes[ch] = ord(ch)  
    return codes

result = string_to_codes("Hello world test!")
print(result)'''

'''def say(message, times=1):
    print(message * times)

say('Привіт') 
say('Світ ', 5)

def example_function(*args, **kwargs):
    print("Позиційні аргументи:", args)
    print("Ключові аргументи:", kwargs)

example_function(1, 2, 3, name="Alice", age=25, khar="чудовий")'''
# гра камінь ножиці папір
player_1 = 'scissors'
player_2 = 'rock'

def game(player_1, player_2):
	# Визначення переможця
	if player_1 == player_2:
		return("It's a tie!")
	if (player_1 == 'rock' and player_2 == 'scissors') or (player_1 == 'scissors' and player_2 == 'paper') or (player_1 == 'paper' and player_2 == 'rock'):
		print("Player 1 wins!")
	else:
		return("Player 2 wins!")

print(game(player_1, player_2))