import sys

def main(args):
    cmd_parser = argparse.ArgumentParser(description='Parse arguments to log parser', prog='logparse')
    cmd_parser.add_argument('file_input', type=str)
    opts = cmd_parser.parse_args(args)
    f = open(opts.file_input)

if __name__ == '__main__':    
    main(sys.argv[1:])