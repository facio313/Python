from flask import Flask
from flask import request
from flask.templating import render_template
from flask.json import jsonify
from day10.dao_emp import Dao
    
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('hello.html')

@app.route('/ajax')
def ajax():
    de = Dao()
    list = de.selects()
    return jsonify(list = list)

@app.route('/ajax_one', methods=['POST'])
def ajax_one():
    de = Dao()
    data = request.get_json()
    one = de.select(data['e_id'])
    return jsonify(one = one)

@app.route('/ajax_add', methods=['POST'])
def ajax_add():
    de = Dao()
    data = request.get_json()
    
    cnt = 0
    
    try :
        cnt = de.insert(data['e_id'], data['e_name'], data['sex'], data['addr'])
    except Exception as e:
        print('예외가 발생했습니다.', e)
        cnt = 10000
    
    return jsonify(cnt = cnt)

@app.route('/ajax_edit', methods=['POST'])
def ajax_edit():
    de = Dao()
    data = request.get_json()
    
    cnt = 0
    
    try :
        cnt = de.update(data['e_id'], data['e_name'], data['sex'], data['addr'])
    except Exception as e:
        print('예외가 발생했습니다.', e)
        cnt = 10000
        
    return jsonify(cnt = cnt)

@app.route('/ajax_delete', methods=['POST'])
def ajax_delete():
    de = Dao()
    data = request.get_json()
    
    cnt = 0
    
    try :
        cnt = de.delete(data['e_id'])
    except Exception as e:
        print('예외가 발생했습니다.', e)
        cnt = 10000
        
    return jsonify(cnt = cnt)

if __name__ == '__main__':
    app.run()
