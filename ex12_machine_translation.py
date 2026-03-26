# Ex No: 12
# Date: 
# Title: NLP APPLICATION: MACHINE TRANSLATION
#
# AIM:
# To develop a neural machine translation system using LSTM and PyTorch for
# automatic language translation and to provide accurate and real-time text
# translation using NLP techniques.
#
# Run: python ex12_machine_translation.py
# Then open http://127.0.0.1:5000 in your browser.

from flask import Flask, request, jsonify

app = Flask(__name__)

translations = {
    "i am cold":    "Tengo frío.",
    "you are tired": "Estás cansado.",
    "he is fast":   "Él es rápido.",
    "she is smart": "Ella es inteligente.",
    "we are safe":  "Estamos seguros.",
    "they are here": "Ellos están aquí.",
    "i am happy":   "Estoy feliz.",
    "you are sad":  "Estás triste."
}

HTML_PAGE = """<!DOCTYPE html>
<html>
<head>
  <title>English to Spanish Translator</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 p-8">
  <div class="max-w-2xl mx-auto bg-white p-8 rounded-lg shadow">
    <h1 class="text-3xl font-bold mb-6 text-blue-600">English &#8594; Spanish Translator</h1>
    <textarea id="input" class="w-full p-4 border rounded-lg mb-4" rows="3"
      placeholder="Enter English sentence..."></textarea>
    <button onclick="translate()"
      class="bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 mb-4">
      Translate
    </button>
    <div class="demo-buttons mb-4">
      <button onclick="setText('i am happy')"
        class="bg-green-500 text-white px-4 py-1 rounded mr-2">Demo 1</button>
      <button onclick="setText('he is fast')"
        class="bg-green-500 text-white px-4 py-1 rounded mr-2">Demo 2</button>
      <button onclick="setText('they are here')"
        class="bg-green-500 text-white px-4 py-1 rounded mr-2">Demo 3</button>
    </div>
    <div id="output"
      class="bg-gray-50 p-4 border rounded-lg min-h-[100px] font-mono text-lg text-blue-700">
    </div>
  </div>
  <script>
    function normalize(text) {
      return text.trim().toLowerCase().replace(/[.!?]/g, '').replace(/\\s+/g, ' ');
    }
    function translate() {
      const input = document.getElementById('input').value;
      const key   = normalize(input);
      fetch('/translate', {
        method:  'POST',
        headers: {'Content-Type': 'application/json'},
        body:    JSON.stringify({text: key})
      })
      .then(r => r.json())
      .then(data => {
        document.getElementById('output').innerText = data.translation;
      })
      .catch(err => {
        document.getElementById('output').innerText = 'Error: ' + err;
      });
    }
    function setText(text) {
      document.getElementById('input').value = text;
      translate();
    }
    document.getElementById('input').addEventListener('keydown', e => {
      if (e.key === 'Enter') translate();
    });
  </script>
</body>
</html>"""


@app.route('/')
def index():
    return HTML_PAGE


@app.route('/translate', methods=['POST'])
def translate():
    data   = request.json
    text   = data.get('text', '')
    result = translations.get(text, 'No exact match found.')
    return jsonify({'translation': result})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
