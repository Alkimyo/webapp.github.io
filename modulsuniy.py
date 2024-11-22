from flask import Flask, request, jsonify
import pickle

# Flask ilovasini yaratish
app = Flask(__name__)

# Modelni yuklash
with open('/home/shohruh/Downloads/model.pkl', 'rb') as f:
    model = pickle.load(f)

# Asosiy sahifa
@app.route('/')
def home():
    return "Bosh sahifa: Ushbu dastur model yordamida bashorat qiladi."

# Bashorat qilish uchun endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Foydalanuvchi kiritgan qiymatlarni olish
        age = float(request.form['age'])
        sex = int(request.form['sex'])
        bp = float(request.form['bp'])
        cholesterol = int(request.form['cholesterol'])
        na_to_k = float(request.form['na_to_k'])

        # Model uchun xususiyatlar
        features = [age, sex, bp, cholesterol, na_to_k]
        
        # Modeldan bashorat qilish
        prediction = model.predict([features])
        
        # Bashorat natijasini qaytarish
        return f"Bashorat natijasi: {int(prediction[0])}"
    except Exception as e:
        return f"Xato yuz berdi: {e}"

# Flask ilovasini ishga tushirish
if __name__ == "__main__":
    app.run(debug=True, port=5005)
