# kod z użyciem frameworku Flask, dla ułatwienia obsługi http.

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Tworzenie tabeli - tworze kursor, tabele, zatwierdzam zmiany i koncze polaczenie. 
def create_table():
    conn = sqlite3.connect('dane.db') # Tworzy połączenie z bazą danych 
    c = conn.cursor() # Tworzę obiekt kursora 'c'
    c.execute('''CREATE TABLE IF NOT EXISTS Dane (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT)''') # polecenie tworzenia tabeli z 3 kolumnami
    conn.commit() # zatwierdzam zmiany
    conn.close() # zamykam połączenie z bazą SQL

# Główna strona
@app.route('/') # nastepna funkcja 'index' zostanie wywyłana gdy Flask otrzyma żądanie http dla ścieżki głownej - Poprawił mi to chat gpt w kodzie ktory nie działał
def index():
    return render_template('index.html') # funkcja Flask do renderowania szablonów html z folderu templates

# Obsługa formularza
@app.route('/submit', methods=['POST']) # Flask, funkcja submit będzię obsługiwać żądania html typu Post wwysłane do adresu /submit
def submit():
    if request.method == 'POST':
        name = request.form['name'] # pobieranie danych z formularza
        email = request.form['email']
        
        conn = sqlite3.connect('dane.db') # tworzenie połączenia z bazą danych + kursor do wykonywania poleceń na tej bazie
        c = conn.cursor()
        c.execute("INSERT INTO Dane (name, email) VALUES (?, ?)", (name, email)) # (?, ?) - zapewnia bezpieczeństwo operacji w bazie
        conn.commit()
        conn.close()
        
        return 'Dane zapisane!'
    return 'Błąd zapisu danych.'

if __name__ == '__main__': 
    create_table()
    app.run(debug=True) # uruchamia Flask
