import argparse
import adduser
import real_time

def get_float(x):
    try:
        x = float(x)
    except ValueError:
        raise argparse.ArgumentTypeError('%r is not a floating-point number'%(x,))
    
    if x<0.0 or x>1.0:
        raise argparse.ArgumentTypeError('%r not in range (0,1)'%(x,))
    return x

parser = argparse.ArgumentParser(prog='run')

parser.add_argument('-r', '--run', type = get_float, help="starts taking the attendance")
parser.add_argument('-a', '--add', help="adds new user to the list of known faces")
args = parser.parse_args()

if(args.run):
    real_time.main(args.run)
if(args.add):
    adduser.main(args.add)