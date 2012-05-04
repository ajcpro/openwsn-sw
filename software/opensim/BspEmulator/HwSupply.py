#!/usr/bin/python

import HwModule

class HwSupply(HwModule.HwModule):
    '''
    \brief Emulates the mote's power supply
    '''
    
    def __init__(self,motehandler):
        
        # store params
        self.motehandler = motehandler
        
        # local variables
        self.moteOn = False
        
        # initialize the parent
        HwModule.HwModule.__init__(self,'HwSupply')
    
    #======================== public ==========================================
    
    def switchOn(self):
        
        # log the activity
        self.log.debug('switchOn')
        
        # filter error
        if self.moteOn:
            raise RuntimeError('mote already on')
        
        # change local variable
        self.moteOn = True
        
        # send command to mote
        self.motehandler.sendCommand(self.motehandler.commandIds['OPENSIM_CMD_supply_on'])
    
    def switchOff(self):
        
        # log the activity
        self.log.debug('switchOff')
        
        # filter error
        if not self.moteOn:
            raise RuntimeError('mote already off')
        
        # change local variable
        self.moteOn = False
        
    def isOn(self):
        return self.moteOn
    
    #======================== private =========================================