"""
File: p1.py
Author: Jervon Drakes
Date: 02/11/2022
Lab Section: 32
Email:  jdrakes1@umbc.edu
Description:  This program prints various information as it relates to the attendance of various students
"""

''' ***** LEAVE THE LINES BELOW ALONE ***************                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
********* LEAVE THE LINES BELOW ALONE ***************                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
********* LEAVE THE LINES BELOW ALONE *************** '''
debug = False

from data_entry import fill_roster
from data_entry import fill_attendance_data

''' ***** LEAVE THE LINES ABOVE ALONE ***************                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
********* LEAVE THE LINES ABOVE ALONE ***************                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
********* LEAVE THE LINES ABOVE ALONE *************** '''

# minute constant set to a value of 60
MINUTE_CONSTANT = 60
# second constant set to a value of 60
SECOND_CONSTANT = 60


def list_students_not_in_class(roster, attend):
    """
  Compare the swipe log with the given course roster. Place those students that
  did not show up for class into a list.
  :param roster: A list of students
  :param attend: A list which includes attendance data for students
  :return: Students that did not show up to class
  """
    # sets an empty list for names
    names = []
    # sets another empty list for names
    names_2 = []
    # another empty list is created
    names_3 = []
    # loops through the roster list
    for name in roster:
        name = name.split(",")
        # the data within the roster list added to the list of names
        names.append(name)
    # loops through the attend list
    for name in attend:
        # splits the data within the list
        name = name.split(",")
        # adds the first two sets of information for the first two indexes to the names_2 list
        names_2.append(name[0:2])
    # loops through the list of names
    for name in names:
        # conditional to determine whether the values within names are in names_2
        if name not in names_2:
            name = ", ".join(name)
            # if the conditional is met the value is added to the list of names_3
            names_3.append(name)
    # values within names_3 are returned
    return names_3


def list_all_times_checking_in_and_out(student_name, data_attend):
    """
  Looking at the swiping log, this function will list all in and outs for a
  particular Student. Please note, as coded in the p1.py file given, this
  function was called three times with different student values.
  :param student_name: A list which includes the names of students
  :param data_attend: A list of the date and times for each student in attendance
  :return: The times a particular student swiped in and out
  """
    # empty list of attendance is created
    attendance = []
    # loops through the list of data_attend
    for data in data_attend:
        # conditional to determine whether the student is within the data
        if student_name in data:
            # if the conditional is met values are added to the attendance list
            attendance.append(data)
    # the attendance list is then returned
    return attendance


def list_all_times_checked_in(attendance_data):
    """
  This function returns a list of when all student(s) FIRST swipe in.
  :param attendance_data: A list of the specific attendance data attached to each student
  :return: The date and time as to when all students first swiped in
  """
    # an empty list for the first time students swiped in is created
    signed_in = list()
    # adds the first value in the attendance data list to the ]list of signed in students
    signed_in.append(attendance_data[0])
    # loops through the attendance data list
    for name in attendance_data:
        in_list = 0
        # loops through the signed in list to return all the first time each student swiped in
        for other_value in signed_in:
            if name.split(",")[0] == other_value.split(",")[0]:
                if name.split(",")[1] == other_value.split(",")[1]:
                    if name.split(",")[3] == other_value.split(",")[3]:
                        in_list += 1
        if in_list == 0:
            signed_in.append(name)
    # returns the students which signed in
    return signed_in


def list_students_late_to_class(late_time, attendance):
    """
   When given a timestamp string and the swipe log, a list of those records
   of students who swiped in late into the class is produced. This function
   returns a list of when all student(s) FIRST swipe in.
   :param late_time: List of students and the times they swiped in after which considers them late
   :param attendance: List of the attendance data for each student
   :return: The students who are arrived late
   """
    # sets an empty list of late comers
    late_comers = []
    # calls a function previous function that includes the times students first checked in
    signed_in_students = list_all_times_checked_in(attendance)
    # loops through signed in students
    for name in signed_in_students:
        # splits name and sets the variable time as the third value which would be the time stamps
        time = name.split(",")[2]
        # returns an integer for the hour portion of the time
        time_hour = int(time[0:3])
        # returns an integer for the minutes portion of the time
        time_minute = int(time[4:6])
        # returns an integer for the seconds portion of the time
        time_seconds = int(time[7:9])

        # the hours in each time is converted to seconds
        time_hour_conversion = time_hour * MINUTE_CONSTANT * SECOND_CONSTANT
        # the minutes in each time is converted to seconds
        time_minute_conversion = time_minute * SECOND_CONSTANT
        # the total seconds for each time is calculated
        time_total_seconds = time_hour_conversion + time_minute_conversion + time_seconds

        # the hours in the designated late time is returned as an integer
        time_late_hour = int(late_time[0:2])
        # the minutes in the designated late time is returned as an integer
        time_late_minutes = int(late_time[3:5])
        # the seconds in the designated late time is returned as an integer
        time_late_seconds = int(late_time[6:8])

        # the hours in the late time is converted to seconds
        time_late_hour_conversion = time_late_hour * MINUTE_CONSTANT * SECOND_CONSTANT
        # the minutes in the late time is converted to seconds
        time_late_minute_conversion = time_late_minutes * SECOND_CONSTANT
        # the total seconds for the late time is calculated
        time_late_total_seconds = time_late_hour_conversion + time_late_minute_conversion + time_late_seconds

        # conditional to determine if each time stamp's total seconds is greater than or equal to the late time's total seconds
        if time_total_seconds >= time_late_total_seconds:
            # once that is met the person and their information is added to the late comers list
            late_comers.append(name)
    # the late comers list is returned
    return late_comers


def get_first_student_to_enter(earliest_attend):
    """
   Simply, this function returns the student that swiped in first. Note,
   the order of the data entered into the swipe log as not the earliest
   student to enter.
   :param earliest_attend: List of students and their attendance data
   :return: The student who swiped in first
   """

    # empty list of time stamps created
    time_stamps = []
    # calls a function previous function that includes the times students first checked in
    signed_in_students = list_all_times_checked_in(earliest_attend)
    # loops through the list of signed in students
    for name in signed_in_students:
        # splits name and sets the variable time as the third value which would be the time stamps
        time = name.split(',')[2]

        # returns integers for the hour portion of each time stamps
        time_hour = int(time[0:3])
        # returns integers for the minutes portion of each time stamps
        time_minute = int(time[4:6])
        # returns integers for the seconds portion of each time stamps
        time_seconds = int(time[7:9])

        # converts hours to seconds
        time_hour_conversion = time_hour * MINUTE_CONSTANT * SECOND_CONSTANT
        # converts minutes to seconds
        time_minute_conversion = time_minute * SECOND_CONSTANT
        # returns the total seconds
        time_total_seconds = time_hour_conversion + time_minute_conversion + time_seconds
        # adds each value to the time stamps list
        time_stamps.append(time_total_seconds)

    # sets the earliest time as the first value in the time stamps list
    earliest_time = time_stamps[0]
    earliest_student = ""

    # loops through the time stamps list to return the earliest student
    for i in range(len(time_stamps)):
        # condition to determine the earliest time
        if time_stamps[i] < earliest_time:
            earliest_time = time_stamps[i]
            # assigns the student information attached to the lowest time stamp to the earliest student
            earliest_student = earliest_attend[i]
            # splits all the information
            earliest_student = earliest_student.split(",")
            # assigns the earliest student as the student's first and last name
            earliest_student = earliest_student[0:2]
            earliest_student = ", ".join(earliest_student)
    # returns earliest student
    return earliest_student


def printList(list_print):
    """
   Simply prints the list. The function should not be able to change any
   values of that list passed in.
   :param list_print: list of the values of returned
   :return: The list of all the values returned prior.
   """
    # loops through the list of list print
    for element in list_print:
        # prints each value
        print(element)
    print()


''' ***** LEAVE THE LINES BELOW ALONE ***************                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
********* LEAVE THE LINES BELOW ALONE ***************                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
********* LEAVE THE LINES BELOW ALONE *************** '''

if __name__ == '__main__':
    # Example, Dr. NIcholas, 9am class

    # load class roster here into a list
    classRoster = fill_roster()

    # figure out which attendance data file to load here

    # load data
    attendData = fill_attendance_data()

    # use different tests
    # make sure roster was filled
    # printList(classRoster)
    # make sure attendance data was loaded
    # printList(attendData)

    # list all those missing
    print("****** Students missing in class *************")
    printList(list_students_not_in_class(classRoster, attendData))
    # list signin/out times for a student
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Lupoli, Shawn", attendData))
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Allgood, Nick", attendData))
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Arsenault, Al", attendData))
    # display when students first signed in (and in attendance)
    print("****** Check in times for all students who attended***")
    printList(list_all_times_checked_in(attendData))
    # display all of those students late to class
    print("****** Students that arrived late ********************")
    printList(list_students_late_to_class("09:00:00", attendData))
    # display first student to enter class
    print("******* Get 1st student to enter class ****************")
    print(get_first_student_to_enter(attendData))

''' ***** LEAVE THE LINES ABOVE ALONE ***************                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
********* LEAVE THE LINES ABOVE ALONE ***************                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
********* LEAVE THE LINES ABOVE ALONE *************** '''
