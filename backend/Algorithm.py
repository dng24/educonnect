example = 'Leena Razzaq / 50 / 50 / 50 / 50 / 50 / Professor razzaq is good at answering piazza questions / professor razzaq is not a good lecturer'
user_inputs = {'lecture_frequency':50, 'lecture_importance':100, 'workload_handling_ability':50,
               'exam_ability':50, 'in_class_question_frequency':50, 'in_class_question_importance':50,
               'forum_question_frequency':50, 'forum_question_weight':50}
def get_compatibility(output_string, user_inputs):
    output_list = output_string.split(' / ')
    llm_outputs = {'lecture_quality':int(output_list[1]), 'workload_difficulty':int(output_list[2]),
                   'exam_heaviness':int(output_list[3]), 'in_class_question_quality':int(output_list[4]),
                   'forum_question_quality':int(output_list[5])}
    compatibility_score = 0
    #lectures
    compatibility_score += (abs(int(user_inputs['lecture_frequency']) - llm_outputs['lecture_quality'])
                            * 0.02 * int(user_inputs['lecture_importance']))
    #workload
    compatibility_score += abs(int(user_inputs['workload_handling_ability']) - llm_outputs['workload_difficulty'])
    #exams
    compatibility_score += abs(int(user_inputs['exam_ability']) - llm_outputs['exam_heaviness'])
    #in class questions
    compatibility_score += (abs(int(user_inputs['in_class_question_frequency']) - llm_outputs['in_class_question_quality'])
                            * 0.02 * int(user_inputs['in_class_question_importance']))
    #forum questions
    compatibility_score += (abs(int(user_inputs['forum_question_frequency']) - llm_outputs['forum_question_quality'])
                            * 0.02 * int(user_inputs['forum_question_weight']))
    return (output_list[0], 100 - compatibility_score/5, output_list[6], output_list[7])

if __name__ == "__main__":
    print(get_compatibility(example, user_inputs))
