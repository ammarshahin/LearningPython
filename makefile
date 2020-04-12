######################### Python makefile #####################
# Author : Ammar Shahin
# Date : 12/4/2020

############################### Variables #######################################

######### change The Files Name here ########
_DEPS =                          # 
_EXC  = app.exe                  # The Excutable File name 
#################################################################################
 
PYC = py
PYFLAGS = -u
SDIR = .\src

#******************************* Rules *******************************
#all: git clean printStartMsg app run

all: git printStartMsg app

printStartMsg: 
	@echo -------------Building...-------------

app:
	$(PYC) $(CXXFLAGS) $(SDIR).\*.py

git:                      # This rule is to automate aquick save to the VCS git 
	@echo -------------Quick Saving...-------------
	git add .
	git commit -a -m "Quick Save" 

run:
	@echo -------------running...-------------
	@$(_EXC)

.PHONY: clean

clean:
	@echo -------------Cleaning...-------------
	del *.exe $(ODIR).\*.o