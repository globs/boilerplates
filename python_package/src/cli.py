
import getopt
import sys
from CHANGEME_PACKAGE_NAME.common.test import add_one



def usage():
    print("""
    udb -m (--mode) [mode] -f (--csvpath) [csvfilepath] -o (--outformat) [outformat]
    -m --mode: choose to tool you want to interact with: secret, connection, csvutils
    -s --secret: use to input secret name for action
    -a --action:
    * mode secret : list, create, update, delete
    * mode connection: connect, execute
    examples 
    udb -m secret -a list
    udb -m secret -a create -i "{\"name\":\"cloudbd2-1\", \"type\":\"db\", \"model\":\"db2\", \"vendor\":\"IBM\",\"login_mode\":\"direct\",\"host\":\"159.8.82.250\",\"port\":\"50000\", \"user\":\"db2inst1\", \"password\":\"ChangeMe@2023\", \"db\":\"testdb\", \"schema\":\"\" }"

    udb -m connection -a connect -s cloudbd2-1

    """)



def handle_actions(run_config):
    add_one(1)
    pass
            



def main():
    """ Main entry point of the client"""
    #TODO initialize logging
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hm:s:a:i:f:v", ["help", "mode", "secret", "action", "input", "file"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    config_exec = {}
    for o, a in opts:
        print(f"Parsing opt: option {o} , argument {a}")
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-s", "--secret"):
            config_exec['secret'] = a
        elif o in ("-a", "--action"):
            config_exec['action'] = a
        elif o in ("-i", "--input"):
            config_exec['input'] = a
        elif o in ("-f", "--file"):
            config_exec['inputfile'] = a
        elif o in ("-m", "--mode"):
            config_exec['mode'] = a    
        else:
            raise Exception(f"Error: unhandled option {a}")
            sys.exit(2)
    handle_actions(config_exec)
    print('Finished')


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()