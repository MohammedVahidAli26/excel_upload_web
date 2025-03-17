from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    table_data = None
    left_headers = []
    right_headers = []
    
    if request.method == 'POST':
        file = request.files['file']
        left_headers = request.form.get('left_headers', '').split(',')
        right_headers = request.form.get('right_headers', '').split(',')
        
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            
            df = pd.read_excel(filepath)
            
            if all(h in df.columns for h in left_headers):
                left_data = df[left_headers].astype(str).agg(' ', axis=1)
            else:
                left_data = []
                left_headers = []
            
            if all(h in df.columns for h in right_headers):
                right_data = df[right_headers].astype(str).agg(' ', axis=1)
            else:
                right_data = []
                right_headers = []
            
            table_data = list(zip(left_data, right_data))
    
    return render_template('index.html', table_data=table_data, left_headers=left_headers, right_headers=right_headers)

if __name__ == '__main__':
    app.run(debug=True)
