from sys import argv

script, user_name = argv
prompt = '>'

print "script = %s, user_name = %s" %(user_name , script)
print "Do U like me?"
likes = raw_input(prompt)