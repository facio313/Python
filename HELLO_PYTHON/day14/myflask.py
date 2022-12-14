from flask import Flask
from flask import request
from flask.templating import render_template
from flask.json import jsonify
from day14.dao_teacher import Dao
    
app = Flask(__name__)

@app.route('/')
@app.route('/teacher')
def teacher():
    return render_template('teacher.html')

@app.route('/ajax_teacher_list', methods=['POST'])
def ajax_teacher_list():
    dt = Dao()
    list = dt.selects()
    return jsonify(list = list)

@app.route('/ajax_teacher_one', methods=['POST'])
def ajax_teacher_one():
    dt = Dao()
    data = request.get_json()
    one = dt.select(data['t_id'])
    return jsonify(one = one)

@app.route('/ajax_teacher_add', methods=['POST'])
def ajax_teacher_add():
    dt = Dao()
    data = request.get_json()
    
    cnt = 0
    
    try :
        cnt = dt.insert(data['t_name'], data['mobile'], data['addr'])
    except Exception as e:
        print('예외가 발생했습니다.', e)
        cnt = 10000
    
    return jsonify(cnt = cnt)

@app.route('/ajax_teacher_edit', methods=['POST'])
def ajax_teacher_edit():
    dt = Dao()
    data = request.get_json()
    
    cnt = 0
    
    try :
        cnt = dt.update(data['t_id'], data['t_name'], data['mobile'], data['addr'])
    except Exception as e:
        print('예외가 발생했습니다.', e)
        cnt = 10000
        
    return jsonify(cnt = cnt)

@app.route('/ajax_teacher_del', methods=['POST'])
def ajax_teacher_del():
    dt = Dao()
    data = request.get_json()
    
    cnt = 0
    
    try :
        cnt = dt.delete(data['t_id'])
    except Exception as e:
        print('예외가 발생했습니다.', e)
        cnt = 10000
        
    return jsonify(cnt = cnt)

if __name__ == '__main__':
    app.run()
