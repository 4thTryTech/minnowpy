import time


stopped = False


def calc_time_diff(current_time, start_time):
    time_diff = current_time - start_time
    # print(time_diff)
    return time_diff

def add_time(time1, time2):
    time_sum = time1 + time2
    # print("time sum: " + str(time_sum))
    return time_sum

def time_ms():
    # nanoseconds in a millisecond: 1000000
    # print("current time: " + str(time.time_ns() / 1000000))
    return time.time_ns() / 1000000

def executor(delay, task):
    # delay is in milliseconds and this function is expected to run in milliseconds
    now = time_ms()
    scheduled_time = add_time(now, delay)
    # print("now: " + str(now))
    # print("scheduled time: " + str(scheduled_time))
    while stopped is not True:
        if calc_time_diff(scheduled_time, now) == 0:
            # if it is the scheduled time, run the command
            print("Right at time!")
            task()
            scheduled_time = add_time(now, delay)
        elif calc_time_diff(scheduled_time, now) < 0:
            # if it is past the scheduled time, note the scheduler ran behind and run the task
            print("Oops, running late, tell task to run faster!")
            task()
            #set the time of the next event
            #note: should this calculate based on the previous event or the current time?
            #       in case the processor is running behind, making the cycke run longer than it should
            scheduled_time = add_time(now, delay)
        now = time_ms()


def task():
    # just a dummy task for testing
    print("hello world!")

def run_task():
    executor(3000, task)

def stop():
    stopped = True

run_task()