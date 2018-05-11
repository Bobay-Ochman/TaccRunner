import multiprocessing
import sys
import os

print 'cpu count:', multiprocessing.cpu_count()
print 'my args:', str(sys.argv)
print 'hello World'

#now do all the things you dream of!
#Don't let your todo list stay memes!

prog = 'runner_multi.py'
scriptDir = '/work/03414/be4833/ConSpeciFix/databaseQuery/'
os.chdir(scriptDir)

print 'about to run ' + prog + ' with '+sys.argv[1] + ' '+sys.argv[2]
os.system('python ' + prog + ' ' +sys.argv[1] + ' '+sys.argv[2])
print 'finished! '+ prog + ' with '+sys.argv[1] + ' '+sys.argv[2]