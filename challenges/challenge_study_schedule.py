def study_schedule(permanence_period, target_time):
    student_numbers = 0
    try:
        for in_time, out_time in permanence_period:
            if in_time <= target_time <= out_time:
                student_numbers += 1
        return student_numbers
    except TypeError:
        return None
