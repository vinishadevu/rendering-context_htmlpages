from flask import Flask,render_template

FAI=Flask(__name__)

@FAI.route('/first')
def first():
    return render_template('first.html')
@FAI.route('/data_render')
def data_render():
    return render_template('data_render.html',name='vinisha',age=10)

if __name__=='__main__':
    FAI.run(debug=True)