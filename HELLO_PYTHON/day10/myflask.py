from flask import Flask
from flask import request
from flask.templating import render_template
from day10.dao_emp import Dao
    
app = Flask(__name__)

@app.route('/')
@app.route('/emp_list')
def emp_list():
    de = Dao()
    
    list = de.selects()
    return render_template('emp_list.html', list = list)

@app.route('/emp_detail')
def emp_detail():
    de = Dao()
    
    id = request.args.get('e_id')
    one = de.select(id)
    return render_template('emp_detail.html', one = one)

@app.route('/emp_edit')
def emp_edit():
    de = Dao()
    
    id = request.args.get('e_id')
    one = de.select(id)
    return render_template('emp_edit.html', one = one)
    
@app.route('/emp_edit_act', methods=['POST'])
def emp_edit_act():
    de = Dao()
    
    id = request.form['e_id']
    name = request.form['e_name']
    sex = request.form['sex']
    addr = request.form['addr']
    
    cnt = ""
    
    try :
        cnt = de.update(id, name, sex, addr)
    except Exception as e:
        print('예외가 발생했습니다.', e)
        cnt = 10000
    
    return render_template('emp_edit_act.html', cnt = cnt)
    # if cnt > 0 :
    #     list = de.selects()
    #     return render_template('emp_list.html', list = list)
    # else :
    #     one = de.select(id)
    #     msg = "수정 실패"
    #     return render_template('edit.html', one = one , msg = msg)

@app.route('/emp_delete', methods=['POST'])
# @app.route('/emp_delete')
def emp_delete():
    de = Dao()
    
    id = request.form['e_id']
    # id = request.args.get('e_id')
    
    cnt = ""
    
    try :
        cnt = de.delete(id)
    except Exception as e:
        print('예외가 발생했습니다.', e)
        cnt = 10000
    
    return render_template('emp_delete_act.html', cnt = cnt)
    
    # if cnt > 0:
    #     list = de.selects()
    #     return render_template('emp_list.html', list = list)
    # else :
    #     one = de.select(id)
    #     msg = "삭제 실패"
    #     return render_template('emp_detail.html', one = one, msg = msg )
    
@app.route('/emp_add')
def emp_add():
    return render_template('emp_add.html')
    
@app.route('/emp_add_act', methods=['POST'])
def emp_add_act():
    de = Dao()
    
    id = request.form['e_id']
    name = request.form['e_name']
    sex = request.form['sex']
    addr = request.form['addr']
    
    cnt = ""
     
    try : 
        cnt = de.insert(id, name, sex, addr)
    except Exception as e:
        print('예외가 발생했습니다.', e, e.pgcode)
        cnt = 10000
        
    return render_template('emp_add_act.html', cnt = cnt)
    
    # if cnt > 0 :
    #     list = de.selects()
    #     return render_template('emp_list.html', list = list)
    # else :
    #     msg = "추가 실패"
    #     return render_template('emp_add.html', msg = msg)
    
if __name__ == '__main__':
    app.run()