MOCK_USERS = [{"email": "test@example.com",
               "salt": "8Fb23mMNHD5Zb8pr2qWA3PE9bH0=",
               "hashed":"1736f83698df3f8153c1fbd6ce2840f8aace4f200771a46672635374073cc876cf0aa6a31f780e576578f791b5555b50df46303f0c3a7f2d21f91aa1429ac22e",
               "user_id": 1}]

MOCK_MEETINGS = [{"meeting_id": 1,
                  "title": "1/15/2018",
                  "date": "2018-01-15",
                  "user_id": 1}]

MOCK_QUESTIONS = [{"question_id": 3,
                   "title": "Can we make a program for students who are looking for internships?",
                   "status": "No",
                   "meeting_id": 1,
                   "user_id": 1},
                  {"question_id": 2,
                   "title": "Should we remove the president?",
                   "status": "Yes",
                   "meeting_id": 1,
                   "user_id": 1},
                  {"question_id": 1,
                   "title": "Should we protest on weekends only?",
                   "status": "Yes",
                   "meeting_id": 1,
                   "user_id": 1}
                  ]

MOCK_VOTING = []

class MockDBHelper:

    def get_user(self, email):
        for user in MOCK_USERS:
            user_email = user.get("email")
            if email == user_email:
                return user
        return None

    def add_user(self, email, salt, hashed):
        MOCK_USERS.append({"email": email, "salt": salt, "hashed":hashed})

    def get_meetings(self):
        return MOCK_MEETINGS

    def get_meeting(self, meeting_id):
        for meeting in MOCK_MEETINGS:
            if meeting_id == meeting.get('meeting_id'):
                return meeting

    def add_meetings(self, meeting_id, title, date, user_id):
        MOCK_MEETINGS.append({"meeting_id": meeting_id,
                  "title": title,
                  "date": date,
                  "user_id": user_id})

    def get_questions(self, meeting_id):
        meeting_q = []
        for question in MOCK_QUESTIONS:
            if question.get('meeting_id') == meeting_id:
                meeting_q.append(question)

        return meeting_q

    def add_questions(self, question_id, title, status, meeting_id, user_id):
        MOCK_QUESTIONS.append({"question_id": question_id,
                              "title": title,
                              "status": status,
                              "meeting_id": meeting_id,
                              "user_id": user_id})

    def add_votings(self, voting_id, choice, question_id, user_id):
        MOCK_VOTING.append({ "voting_id": voting_id,
                              "choice": choice,
                              "question_id": question_id,
                              "user_id": user_id})

    def has_voted(self, question_id, user_id):
        for voting in MOCK_VOTING:
            if voting.get('question_id') == question_id and voting.get('user_id') == user_id:
                return True
        return False


if __name__ == '__main__':
    DB = MockDBHelper()
    print DB.get_questions(1)
    print DB.get_meeting(1)