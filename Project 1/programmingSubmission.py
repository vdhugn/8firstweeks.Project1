from datetime import datetime

def process_submission_data(submission_data):
    submissions = []
    for line in submission_data:
        user, problem, time_point, status, point = line.split()
        submissions.append({"user": user, "problem": problem, "status": status, "point": int(point), "time_point": time_point})
    return submissions

def total_number_submissions(submissions):
    return len(submissions)

def number_error_submission(submissions):
    sum = 0
    for submission in submissions:
        if submission["status"] == "ERR":
            sum += 1
    return sum

def number_error_submission_of_user(submissions, user):
    sum = 0
    for submission in submissions:
        if submission["user"] == user and submission["status"] == "ERR":
            sum += 1
    return sum

def total_point_of_user(submissions, user):
    user_points = {}
    
    for sub in submissions:
        if sub["user"] == user:
            key = sub["problem"]
            if key not in user_points or sub["point"] > user_points[key]:
                user_points[key] = sub["point"]

    return sum(user_points.values())

def number_submission_period(submissions, from_time_point, to_time_point):
    start_time = datetime.strptime(from_time_point, "%H:%M:%S")
    end_time = datetime.strptime(to_time_point, "%H:%M:%S")
    return sum(1 for submission in submissions if start_time <= datetime.strptime(submission["time_point"], "%H:%M:%S") <= end_time)

# Read input data
submission_data = []
while True:
    line = input().strip()
    if line == "#":
        break
    submission_data.append(line)

query_data = []
while True:
    line = input().strip()
    if line == "#":
        break
    query_data.append(line)

# Process submission data
submissions = process_submission_data(submission_data)

# Process queries
for query in query_data:
    if query == "?total_number_submissions":
        print(total_number_submissions(submissions))
    elif query == "?number_error_submision":
        print(number_error_submission(submissions))
    elif query.startswith("?number_error_submision_of_user"):
        _, user = query.split()
        print(number_error_submission_of_user(submissions, user))
    elif query.startswith("?total_point_of_user"):
        _, user = query.split()
        print(total_point_of_user(submissions, user))
    elif query.startswith("?number_submission_period"):
        _, from_time_point, to_time_point = query.split()
        print(number_submission_period(submissions, from_time_point, to_time_point))
