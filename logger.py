import os

log = ''
message = []
# file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_files', 'test.png')
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '/home/seeam/Desktop/test-logger/test-log')

a = 'first message'
message.append(a)
b = 'second message'
message.append(b)
c = 'third message'
message.append(c)

log = '\n'.join(message)

target = open(file_path, 'a')
# target.truncate()
target.write("\n\n%s" % log)
target.close()

# You can also use this method directly
def write_error_log(Error):
    """
Error parameter should contains the string of the error message when the file could not open.
    :param Error:
    """
    target = open("Error_log.txt", 'a')
    target.write(Error)
    target.close()
