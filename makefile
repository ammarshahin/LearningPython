######################### Python makefile #####################
# Author : Ammar Shahin
# Date : 12/4/2020

############################### Variables #######################################

######### change The Files Name here ########
_DEPS =                          # 
_EXC  = FindtheRunner-UpScore.py            # The Excutable File name 
#################################################################################
 
PYC = py
PYFLAGS = -u
SDIR = .\Hakerrank

#******************************* Rules *******************************

all: git printStartMsg app

build:	printStartMsg app

printStartMsg: 
	@echo -------------Building...-------------

app:
	$(PYC) $(CXXFLAGS) $(SDIR).\$(_EXC)

git:                      # This rule is to automate aquick save to the VCS git 
	@echo -------------Quick Saving...-------------
	git add .
	git commit -a -m "Quick Save"

push:
	@echo -------------PushingToGithup...-------------
	git push origin master