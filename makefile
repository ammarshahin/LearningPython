######################### Python makefile #####################
# Author : Ammar Shahin
# Date : 12/4/2020

############################### Variables #######################################

######### change The Files Name here ########
_EXC  = pong.py            # The Excutable File name 
#################################################################################
 
PYC = py
PYFLAGS = -u
SDIR = .\src\graphics

#******************************* Rules *******************************

all: printStartMsg app

printStartMsg: 
	@echo -------------Running...-------------

app:
	$(PYC) $(PYFLAGS) $(SDIR).\$(_EXC)

git:   # This rule is to automate a quick save to git 
	@echo -------------Quick Saving...-------------
	git add .
	git cm "Quick Save"

push:
	@echo -------------PushingToGithup...-------------
	git push origin master