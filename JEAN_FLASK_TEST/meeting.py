from flask import request, render_template
from flask_login import login_required
from mockdbhelper import MockDBHelper as DBHelper

DB = DBHelper()

@login_required
def meeting():
    meeting_id = int(request.form.get('meeting_id'))
    questions = DB.get_questions(meeting_id)
    current_meeting = DB.get_meeting(meeting_id)
    title = current_meeting.get('title')
    return render_template("meeting.html", questions=questions, meeting_title=title)