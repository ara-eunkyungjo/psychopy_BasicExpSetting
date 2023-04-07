#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.1),
    on Sat Apr  8 00:39:46 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.1'
expName = 'test'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/jo-eunkyung/Documents/psychopyTest/intro-consent-text-slider/intro-consent-text-slider_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1470, 956], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "intro" ---
instructionText = visual.TextStim(win=win, name='instructionText',
    text="Example of instruction text here.\n\nPress 'y' key to proceed.\n\nPress 'n' key to exit.",
    font='Open Sans',
    pos=(0, 0), height=0.045, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
inst_resp = keyboard.Keyboard()

# --- Initialize components for Routine "consent" ---
consentText = visual.TextStim(win=win, name='consentText',
    text="Read consent form presented below.\nBy pressing 'y' key, you agree to the consent form.\n\nPress 'n' if you disagree with the consent form then the experiment will be finished.",
    font='Open Sans',
    pos=(0, 0), height=0.045, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
consRes = keyboard.Keyboard()

# --- Initialize components for Routine "stimuli" ---
stimuliText = visual.TextStim(win=win, name='stimuliText',
    text='',
    font='Open Sans',
    pos=(0, 0.3), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
slider = visual.Slider(win=win, name='slider',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.25), units=win.units,
    labels=['strongly disagree', 'disagree', 'neutral', 'agree', 'strongly agree'], ticks=(1, 2, 3, 4, 5), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, ori=0.0, depth=-1, readOnly=False)
rateText = visual.TextStim(win=win, name='rateText',
    text='Rate how much blame should the agent receive?',
    font='Open Sans',
    pos=(0, -0.15), height=0.03, wrapWidth=None, ori=0.0, 
    color=[1.0000, 1.0000, -0.1294], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "bye" ---
byeText = visual.TextStim(win=win, name='byeText',
    text='Thank you for participating!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "intro" ---
continueRoutine = True
# update component parameters for each repeat
inst_resp.keys = []
inst_resp.rt = []
_inst_resp_allKeys = []
# keep track of which components have finished
introComponents = [instructionText, inst_resp]
for thisComponent in introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "intro" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructionText* updates
    
    # if instructionText is starting this frame...
    if instructionText.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        instructionText.frameNStart = frameN  # exact frame index
        instructionText.tStart = t  # local t and not account for scr refresh
        instructionText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructionText.started')
        # update status
        instructionText.status = STARTED
        instructionText.setAutoDraw(True)
    
    # if instructionText is active this frame...
    if instructionText.status == STARTED:
        # update params
        pass
    
    # *inst_resp* updates
    waitOnFlip = False
    
    # if inst_resp is starting this frame...
    if inst_resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        inst_resp.frameNStart = frameN  # exact frame index
        inst_resp.tStart = t  # local t and not account for scr refresh
        inst_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inst_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'inst_resp.started')
        # update status
        inst_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(inst_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(inst_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if inst_resp.status == STARTED and not waitOnFlip:
        theseKeys = inst_resp.getKeys(keyList=['y','n'], waitRelease=False)
        _inst_resp_allKeys.extend(theseKeys)
        if len(_inst_resp_allKeys):
            inst_resp.keys = _inst_resp_allKeys[-1].name  # just the last key pressed
            inst_resp.rt = _inst_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "intro" ---
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if inst_resp.keys in ['', [], None]:  # No response was made
    inst_resp.keys = None
thisExp.addData('inst_resp.keys',inst_resp.keys)
if inst_resp.keys != None:  # we had a response
    thisExp.addData('inst_resp.rt', inst_resp.rt)
thisExp.nextEntry()
# Run 'End Routine' code from introCode
if inst_resp.keys == 'y':
    consentReps = 1
    skip_consent = False
    skip_stimuli = False
elif inst_resp.keys == 'n':
    skip_consent = True
    skip_stimuli = True
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
consentloop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='consentloop')
thisExp.addLoop(consentloop)  # add the loop to the experiment
thisConsentloop = consentloop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisConsentloop.rgb)
if thisConsentloop != None:
    for paramName in thisConsentloop:
        exec('{} = thisConsentloop[paramName]'.format(paramName))

for thisConsentloop in consentloop:
    currentLoop = consentloop
    # abbreviate parameter names if possible (e.g. rgb = thisConsentloop.rgb)
    if thisConsentloop != None:
        for paramName in thisConsentloop:
            exec('{} = thisConsentloop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "consent" ---
    continueRoutine = True
    # update component parameters for each repeat
    consRes.keys = []
    consRes.rt = []
    _consRes_allKeys = []
    # Run 'Begin Routine' code from consentCode
    if skip_consent:
        continueRoutine = False
    # keep track of which components have finished
    consentComponents = [consentText, consRes]
    for thisComponent in consentComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "consent" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *consentText* updates
        
        # if consentText is starting this frame...
        if consentText.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            consentText.frameNStart = frameN  # exact frame index
            consentText.tStart = t  # local t and not account for scr refresh
            consentText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(consentText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'consentText.started')
            # update status
            consentText.status = STARTED
            consentText.setAutoDraw(True)
        
        # if consentText is active this frame...
        if consentText.status == STARTED:
            # update params
            pass
        
        # *consRes* updates
        waitOnFlip = False
        
        # if consRes is starting this frame...
        if consRes.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            consRes.frameNStart = frameN  # exact frame index
            consRes.tStart = t  # local t and not account for scr refresh
            consRes.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(consRes, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'consRes.started')
            # update status
            consRes.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(consRes.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(consRes.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if consRes.status == STARTED and not waitOnFlip:
            theseKeys = consRes.getKeys(keyList=['y','n'], waitRelease=False)
            _consRes_allKeys.extend(theseKeys)
            if len(_consRes_allKeys):
                consRes.keys = _consRes_allKeys[-1].name  # just the last key pressed
                consRes.rt = _consRes_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in consentComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "consent" ---
    for thisComponent in consentComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if consRes.keys in ['', [], None]:  # No response was made
        consRes.keys = None
    consentloop.addData('consRes.keys',consRes.keys)
    if consRes.keys != None:  # we had a response
        consentloop.addData('consRes.rt', consRes.rt)
    # Run 'End Routine' code from consentCode
    if consRes.keys == 'y':
        stimuliReps = 1
    elif consRes.keys == 'n':
        skip_stimuli = True
    # the Routine "consent" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'consentloop'


# set up handler to look after randomisation of conditions etc
stimuliloop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.xlsx'),
    seed=None, name='stimuliloop')
thisExp.addLoop(stimuliloop)  # add the loop to the experiment
thisStimulusloop = stimuliloop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisStimulusloop.rgb)
if thisStimulusloop != None:
    for paramName in thisStimulusloop:
        exec('{} = thisStimulusloop[paramName]'.format(paramName))

for thisStimulusloop in stimuliloop:
    currentLoop = stimuliloop
    # abbreviate parameter names if possible (e.g. rgb = thisStimulusloop.rgb)
    if thisStimulusloop != None:
        for paramName in thisStimulusloop:
            exec('{} = thisStimulusloop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "stimuli" ---
    continueRoutine = True
    # update component parameters for each repeat
    stimuliText.setText(text)
    slider.reset()
    # Run 'Begin Routine' code from stimuliCode
    if skip_stimuli:
        continueRoutine = False
    # keep track of which components have finished
    stimuliComponents = [stimuliText, slider, rateText]
    for thisComponent in stimuliComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "stimuli" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimuliText* updates
        
        # if stimuliText is starting this frame...
        if stimuliText.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            stimuliText.frameNStart = frameN  # exact frame index
            stimuliText.tStart = t  # local t and not account for scr refresh
            stimuliText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuliText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'stimuliText.started')
            # update status
            stimuliText.status = STARTED
            stimuliText.setAutoDraw(True)
        
        # if stimuliText is active this frame...
        if stimuliText.status == STARTED:
            # update params
            pass
        
        # *slider* updates
        
        # if slider is starting this frame...
        if slider.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            slider.frameNStart = frameN  # exact frame index
            slider.tStart = t  # local t and not account for scr refresh
            slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider.started')
            # update status
            slider.status = STARTED
            slider.setAutoDraw(True)
        
        # if slider is active this frame...
        if slider.status == STARTED:
            # update params
            pass
        
        # Check slider for response to end routine
        if slider.getRating() is not None and slider.status == STARTED:
            continueRoutine = False
        
        # *rateText* updates
        
        # if rateText is starting this frame...
        if rateText.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            rateText.frameNStart = frameN  # exact frame index
            rateText.tStart = t  # local t and not account for scr refresh
            rateText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rateText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'rateText.started')
            # update status
            rateText.status = STARTED
            rateText.setAutoDraw(True)
        
        # if rateText is active this frame...
        if rateText.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimuliComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "stimuli" ---
    for thisComponent in stimuliComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    stimuliloop.addData('slider.response', slider.getRating())
    stimuliloop.addData('slider.rt', slider.getRT())
    # the Routine "stimuli" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'stimuliloop'


# --- Prepare to start Routine "bye" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
byeComponents = [byeText]
for thisComponent in byeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "bye" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *byeText* updates
    
    # if byeText is starting this frame...
    if byeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        byeText.frameNStart = frameN  # exact frame index
        byeText.tStart = t  # local t and not account for scr refresh
        byeText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(byeText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'byeText.started')
        # update status
        byeText.status = STARTED
        byeText.setAutoDraw(True)
    
    # if byeText is active this frame...
    if byeText.status == STARTED:
        # update params
        pass
    
    # if byeText is stopping this frame...
    if byeText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > byeText.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            byeText.tStop = t  # not accounting for scr refresh
            byeText.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'byeText.stopped')
            # update status
            byeText.status = FINISHED
            byeText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in byeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "bye" ---
for thisComponent in byeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
