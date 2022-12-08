from flask import Flask
from flask import request
from flask.templating import render_template
from flask.json import jsonify
from day13.dao_student import Dao
    
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('hello.html')

@app.route('/ajax')
def ajax():
    ds = Dao()
    list = ds.selects()
    return jsonify(list = list)

@app.route('/ajax_one', methods=['POST'])
def ajax_one():
    ds = Dao()
    data = request.get_json()
    one = ds.select(data['s_id'])
    return jsonify(one = one)

@app.route('/ajax_add', methods=['POST'])
def ajax_add():
    ds = Dao()
    data = request.get_json()
    
    cnt = 0
    
    try :
        cnt = ds.insert(data['s_id'], data['s_name'], data['mobile'], data['address'])
    except Exception as e:
        print('예외가 발생했습니다.', e)
        cnt = 10000
    
    return jsonify(cnt = cnt)

@app.route('/ajax_edit', methods=['POST'])
def ajax_edit():
    ds = Dao()
    data = request.get_json()
    
    cnt = 0
    
    try :
        cnt = ds.update(data['s_id'], data['s_name'], data['mobile'], data['address'])
    except Exception as e:
        print('예외가 발생했습니다.', e)
        cnt = 10000
        
    return jsonify(cnt = cnt)

@app.route('/ajax_delete', methods=['POST'])
def ajax_delete():
    ds = Dao()
    data = request.get_json()
    
    cnt = 0
    
    try :
        cnt = ds.delete(data['s_id'])
    except Exception as e:
        print('예외가 발생했습니다.', e)
        cnt = 10000
        
    return jsonify(cnt = cnt)

if __name__ == '__main__':
    app.run()
