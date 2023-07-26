def intro_1():
    global name ; global career ;global technical_skills #making variables as global so can also access them outside of function
    name="Usama"
    career="DevOps engineer"
    technical_skills=["RHCSA", "Bash Scripting", "Docker", "git & github"]
name="Ali"
career="Senior DevOps engineer"
technical_skills=["RHCSA", "Bash Scripting", "Docker", "git & github", "Teraform", "Ansible", "CI/CD pipelines"]
intro_1()
print(f"{name}\n{career}\n{technical_skills}")   