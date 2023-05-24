import scratchconnect, sys

user = ""

with open("./config/scratch.txt",'r') as scratchfile:
    lines =  scratchfile.readlines()
    username = lines[0].rstrip('\n')
    password = lines[1].rstrip('\n')
    user = scratchconnect.ScratchConnect(username, password)

async def set(args,message,self):
    project = args.pop(0)
    vartochange = args.pop(0).replace("="," ")

    variables = user.connect_project(project_id=int(project)).connect_cloud_variables()
    oldvalue = variables.get_cloud_variable_value(variable_name=vartochange,limit=1)
    variables.set_cloud_variable(variable_name=vartochange, value=args[0])
    return f"Updated var `{vartochange}` from `{oldvalue}` to `{' '.join(args)}`"