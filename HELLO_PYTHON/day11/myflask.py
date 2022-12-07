from flask import Flask
from flask import request
from flask.templating import render_template
from day11.dao_member import MemberDao
    
app = Flask(__name__)

@app.route('/')
@app.route('/member_list')
def member_list():
    de = MemberDao()
    
    list = de.selects()
    return render_template('member_list.html', list = list)

@app.route('/member_detail')
def member_detail():
    de = MemberDao()
    
    id = request.args.get('m_id')
    one = de.select(id)
    return render_template('member_detail.html', one = one)

@app.route('/member_edit')
def member_edit():
    de = MemberDao()
    
    id = request.args.get('m_id')
    one = de.select(id)
    return render_template('member_edit.html', one = one)
    
@app.route('/member_edit_act', methods=['POST'])
def member_edit_act():
    de = MemberDao()
    
    id = request.form['m_id']
    name = request.form['m_nm']
    tel = request.form['tel']
    ymd = request.form['ymd']
    
    cnt = ""
    
    try :
        cnt = de.update(id, name, tel, ymd)
    except Exception as e:
        print('예외가 발생했습니다.', e)
        cnt = 10000
    
    return render_template('member_edit_act.html', cnt = cnt)
    # if cnt > 0 :
    #     list = de.selects()
    #     return render_template('member_list.html', list = list)
    # else :
    #     one = de.select(id)
    #     msg = "수정 실패"
    #     return render_template('edit.html', one = one , msg = msg)

@app.route('/member_delete', methods=['POST'])
# @app.route('/member_delete')
def member_delete():
    de = MemberDao()
    
    id = request.form['m_id']
    # id = request.args.get('m_id')
    
    cnt = ""
    
    try :
        cnt = de.delete(id)
    except Exception as e:
        print('예외가 발생했습니다.', e)
        cnt = 10000
    
    return render_template('member_delete_act.html', cnt = cnt)
    
    # if cnt > 0:
    #     list = de.selects()
    #     return render_template('member_list.html', list = list)
    # else :
    #     one = de.select(id)
    #     msg = "삭제 실패"
    #     return render_template('member_detail.html', one = one, msg = msg )
    
@app.route('/member_add')
def member_add():
    return render_template('member_add.html')
    
@app.route('/member_add_act', methods=['POST'])
def member_add_act():
    de = MemberDao()
    
    id = request.form['m_id']
    name = request.form['m_nm']
    tel = request.form['tel']
    ymd = request.form['ymd']
    
    cnt = ""
     
    try : 
        cnt = de.insert(id, name, tel, ymd)
    except Exception as e:
        print('예외가 발생했습니다.', e, e.pgcode)
        cnt = 10000
        
    return render_template('member_add_act.html', cnt = cnt)
    
    # if cnt > 0 :
    #     list = de.selects()
    #     return render_template('member_list.html', list = list)
    # else :
    #     msg = "추가 실패"
    #     return render_template('member_add.html', msg = msg)
    
if __name__ == '__main__':
    app.run()