#! /usr/bin/env
# randomQuizGenerator.py -- create 35 different quizzes from a collection of 50 quizzes in random order

import random

# the quiz collection
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New\
Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West\
Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quiz in range(35):
    # create the quiz and the answers files
    quizFO = open('QuizNumber%s.txt' %(quiz + 1), 'w')
    answerFO = open('AnswerNumber%s.txt' %(quiz + 1), 'w')
    # write the header of thte quiz
    quizFO.write('Firstname :\nLastname :\n\n')
    quizFO.write(('*' * 20) + 'Capital quiz number %s' %(quiz + 1))
    # shuffle the order of the states.  
    states = list(capitals.keys())
    random.shuffle(states)
    # loop through all the states and make a question for each.
    for question in range(50):
        # Get the right answers
        correctAnswer = capitals[states[question]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        quizFO.write('\n%s. What is the capital of %s?\n' %(question + 1, states[question]))
        for i in range(4):
            quizFO.write('    %s.%s\n' %('ABCD'[i], answerOptions[i]))
        quizFO.write('\n')
        answerFO.write('%s.%s\n' %(question + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

    quizFO.close()
    answerFO.close()
        # FO stands for 'file object'
