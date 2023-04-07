# psychopy_BasicExpSetting
This is an example of experiment setting, consisted of introduction, consent, stimuli (vignette-Likert), and ending routines.<br><br>

## How to Start
1. Download files in the same folder.<br>
2. If you want to work on the builder, run Psychopy and open 'intro-consent-text-slider.psyexp.'<br>
3. You can also work on '---.py' file if you are familiar to python code.<br>
<br><br>

## Procedure at a Glance

<img src="./images/procedure.png" width="700">

<img src="./images/1.png" width="500">

<img src="./images/2.png" width="500">

<img src="./images/3.png" width="500">

<img src="./images/4.png" width="500">

<img src="./images/5.png" width="500">
<br><br>

## Notes: Branch, Condition, Jump to the Last Routine <br>
#### Branch<br>
With loop function, different routines will be presented depending on the participants' answer to the previous routine.<br>
Please check the 'Code' element in each routines.<br>
#### Condition<br>
(1) With xlsX file, you can present the stimulus in randomized order. The xlsx file should be uploaded in the 'stimuliloop' window (Conditions section).<br>
(2) Stimulus are presented in random order (loopType = 'random').<br>
#### Jump to the Last Routine<br>
Codes were added to skip 'consent' and/or 'stimuli' routine and directly go to the last ('bye') routine.<br>
