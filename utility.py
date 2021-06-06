def create_array(x_dim, y_dim=0):
    if y_dim > 0:
        return [[0 for col in range(y_dim)] for row in range(x_dim)]
    
    return [0 for row in range(x_dim)]


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
