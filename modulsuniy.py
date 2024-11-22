from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Modelni yuklash
with open('/home/shohruh/Downloads/model.pkl', 'rb') as f:
    model = pickle.load(f)

# Asosiy sahifa
@app.route('/')
def home():
    return render_template('index.html')

# Bashorat qilish uchun endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = float(request.form['age'])
        sex = int(request.form['sex'])
        bp = float(request.form['bp'])
        cholesterol = int(request.form['cholesterol'])
        na_to_k = float(request.form['na_to_k'])

        features = [age, sex, bp, cholesterol, na_to_k]
        prediction = model.predict([features])

        return render_template('index.html', prediction=f"Bashorat natijasi: {int(prediction[0])}")
    except Exception as e:
        return render_template('index.html', prediction=f"Xato yuz berdi: {e}")

if __name__ == "__main__":
    app.run(debug=True, port=5005)
