import os
from tweeter import main as download

def dump():
    os.system('cat outfile.txt >> old_outfile.txt ; rm outfile.txt;')

def main():
    dump()
    while 1:
        try:
            download()
        except (KeyboardInterrupt, SystemExit):
        	print('\n\nSaving current progress.')
        	dump()
        	print('done.')
        	break
        except:
            dump()

if __name__ == "__main__":
    main()
