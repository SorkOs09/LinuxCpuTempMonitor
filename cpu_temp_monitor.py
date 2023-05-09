from subprocess import check_output as subprocess_check_output
from subprocess import Popen        as subprocess_popen


from time import sleep     as time_sleep
from time import localtime as time_localtime

from os      import getcwd as os_getcwd 
from os.path import join   as os_join

from sys import argv

from termcolor import colored







def draw_line():
    print_and_save("_______________________")



def print_and_save(string):
    global args_save_log
    global log_file
    global args_show_cpu_mhz

    print(string)

    if args_save_log:
        log_file.write("\n"+string)




def get_time():

    lcl_time = time_localtime()
    time     = ''

    for i in (3, 4, 5):
        
        time += {False: "", True: "0"}[lcl_time[i] < 10] + str(lcl_time[i]) 
        time += ':'
    
    return time[:-1]




def get_cpu_MHz():
    out = str(subprocess_check_output(["cat", "/proc/cpuinfo"]))

    cpu_mhz_list = []
    
    while True:
        cpu_mhz_line_find = out.find('cpu MHz')
        
        if cpu_mhz_line_find == -1:
            break
        
        out = out[cpu_mhz_line_find+7:]
        out = out[out.find(' '):]

        cpu_mhz_line_find = out.find('.')

        cpu_mhz_list.append(int(out[:cpu_mhz_line_find]))

    return cpu_mhz_list




def get_cpu_MHz_stat():
    

    cpu_mhz_list = get_cpu_MHz()
    rtrn_line    = "No info about CPU MHz"
    
    if len(cpu_mhz_list):
        rtrn_line  = "MHz"
        rtrn_line += ", min: "
        rtrn_line += str(min(cpu_mhz_list))
        rtrn_line += ", max: "
        rtrn_line += str(max(cpu_mhz_list))
        rtrn_line += ", avg: "
        rtrn_line += str(int(sum(cpu_mhz_list)/len(cpu_mhz_list)))
        
        

    return rtrn_line



def bye():
    print_and_save("Bye!")
    draw_line()











####################################################


args_stress_test  = False
args_save_log     = False
args_show_cpu_mhz = False


def check_args():
    global args_stress_test
    global args_save_log
    global args_show_cpu_mhz
    global log_file
    global log_file_cwd
    for i in argv:
        if i == "-help":
            print_and_save("-stress      CPU stress test.")
            print_and_save("-save_log    Save all information to log file.")
            print_and_save("-mhz         Show processor cores frequency in mhz.")
            if len(argv) == 2:
                return -1
            else:
                draw_line()

        elif i == "-mhz":
            args_show_cpu_mhz = True
        
        elif i == "-stress":
            args_stress_test     = True
            number_of_cores = len(get_cpu_MHz())

            print_and_save(get_time() + ", CPU stress test started on " + str(number_of_cores) + " cores.")
            
            subprocess_popen(["stress", "--cpu", str(number_of_cores)])
        elif i == "-save_log":
            args_save_log = True
            
            log_file_cwd = os_join(os_getcwd(), "log.txt")
            
            log_file = open(log_file_cwd, 'a')
            
            log_file.write("\n" + get_time() + ", A new session has been launched.")

            print_and_save(get_time() + ', All information is will be saved in "' + log_file_cwd + '"')
            


def main():
    global args_stress_test
    global args_save_log
    global log_file
    global log_file_cwd


    while True:
        out = str(subprocess_check_output(["sensors"]))
        
        if args_stress_test:
            cpu_mhz_text = " STRESS TEST! "
            cpu_mhz      = " " + colored(cpu_mhz_text, "red", "on_white") + " "

        else:
            cpu_mhz_text = ""
            cpu_mhz      = ""   

        temp_line = out[out.find("Tctl:"):]
        temp_line = temp_line[temp_line.find("+"):]
        temp_line = temp_line[:temp_line.find(".")]
        temp_line = int(temp_line)

        if temp_line < 50:
            cr = 'green'
        elif temp_line < 70:
            cr = 'cyan'
        elif temp_line < 85:
            cr = 'yellow'
        else:
            cr = 'red'

        if args_show_cpu_mhz:
            mhz_tmp       = " MHz: " + str(get_cpu_MHz()) 
            cpu_mhz_text += mhz_tmp
            cpu_mhz      += mhz_tmp

        time_and_temp = get_time() + ", " + str(temp_line) + "°C "

        
        
        terminal_size  = int(subprocess_check_output(["stty", "size"]).split()[1]) 
        terminal_size -= len(time_and_temp)
        terminal_size -= len(cpu_mhz_text)+2
        



        #if terminal_size >= 100:
        #    temp_line_multiply = 1.0
        
        if terminal_size > 0:
            temp_line_multiply = terminal_size/100.0
        else:
            temp_line_multiply = 0
        
        temp_line_tmp = int(temp_line*temp_line_multiply)



        colored_space = colored("*"*temp_line_tmp, cr)
        if temp_line_multiply < 50:
            empty_space = str("*"*int((100.0*temp_line_multiply)-temp_line_tmp))
        else:
            empty_space = ""
        




        print_and_save(time_and_temp + colored_space + empty_space + cpu_mhz)
        time_sleep(1)


if __name__ == '__main__':
    args = check_args()
    try:
        if args != -1:
            main()
        raise RuntimeError()
    except Exception as error:
        print_and_save(error)
    finally:
        if args_save_log:
            print_and_save('\nSave log information to the "' + log_file_cwd + '" file...')
            bye()
            log_file.close()
        elif args != -1:
            bye()
