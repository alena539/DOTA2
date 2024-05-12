from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

uploaded_files = []


@app.route('/')
def index():
    with open('your_file.txt', 'r') as file:
        lines = file.readlines()
    first_words = [line.split()[0] for line in lines]

    uploaded_lines = []
    for uploaded_file in uploaded_files:
        with open(uploaded_file, 'r') as uploaded:
            uploaded_lines.extend(uploaded.readlines())

    first_word = [line.split()[0] for line in uploaded_lines]

    return render_template('index.html', first_words=first_words, lines=lines, first_word=first_word)


@app.route('/line/<int:index>')
def show_line(index):
    with open('your_file.txt', 'r') as file:
        lines = file.readlines()
    line = lines[index - 1]
    first_word = line.split()[0]
    return render_template('line.html', line=line, image_url=url_for('static', filename=f'images/{first_word}.jpg'))


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save(f'upload_{len(uploaded_files)+1}.txt')
    uploaded_files.append(f'upload_{len(uploaded_files)+1}.txt')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
