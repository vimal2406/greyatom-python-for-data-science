# --------------
#Code starts here

#Function to read file
def read_file(path):
    
    #Opening of the file located in the path in 'read' mode
    file = open(path,'r')
    #Reading of the first line of the file and storing it in a variable
    sentence = file.readline()
    file.close()
    return sentence
sample_message = read_file(file_path)
print(sample_message)
message_1 = read_file(file_path_1)
message_2 = read_file(file_path_2)
print(message_1)
print(message_2)

def fuse_msg(message_a , message_b):
    quotient = int(message_b) // int(message_a)
    return str(quotient)
secret_msg_1 = fuse_msg(message_1,message_2)
message_3 = read_file(file_path_3)

def substitute_msg(message_c):
    sub=""
    if message_c == 'Red':
        sub = 'Army Genral'
    elif message_c == 'Green':
        sub = 'Data Scientist'
    elif message_c == 'Blue':
        sub = 'Marine Biologist'
    return sub
secret_msg_2 = substitute_msg(message_3)
message_4 = read_file(file_path_4)
message_5 = read_file(file_path_5)
print(message_4)
print(message_5)
#Function to compare message

def compare_msg(message_d,message_e):
    a_list = message_d.split(" ")
    b_list = message_e.split(" ")
    c_list = []
    c_list = [i for i in a_list if i not in b_list]
    final_msg = " ".join(c_list)
    return final_msg
secret_msg_3 = compare_msg(message_4 , message_5)
print(secret_msg_3)
message_6 = read_file(file_path_6)
print(message_6)
   
def extract_msg(message_f):
    a_list = message_f.split(" ")
    even_word = lambda x:len(x)%2==0
    b_list = filter(even_word,a_list)
    final_msg = " ".join(b_list)
    return final_msg
secret_msg_4 = extract_msg(message_6)   
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]
secret_msg = " ".join(message_parts)
# define the path where you 
final_path= user_data_dir + '/secret_message.txt'
#Function to write inside a file
def write_file(secret_msg,path):
    file_path = open(path,'a+')
    file_path.write(secret_msg)
    file_path.close()
write_file(secret_msg,final_path)
print(secret_msg)



