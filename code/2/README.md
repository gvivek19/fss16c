#Week 2

##Active shooter exercise
###List two things *not to do* during an active shooter event.
1. Do not huddle. Spread out across the room.
2. Do not panic and shout.

###List two things *best to do* during an active shooter event.
1. Try to get away from the shooter, hide from the shooter or take down the shooter.
2. Know your surrounding and the exit routes and get out.

##ZeroR

The code for zeror predictor can be found [here](https://github.com/gvivek19/fss16c/blob/master/code/2/majorityPredictor.py).

The ZeroR and eg11 functions in ninja.rc:
```
zeror1() {
  python -B $Here/majorityPredictor.py $1 $2
}

eg11() {
    local data="data/jedit-4.1.arff"                    # edit this line to change the data
    local learners="j48 jrip nb rbfnet bnet zeror1"     # edit this line to change the leaners
    local goal=true                                     # edit this line to hunt for another goal
    
    local i="$Tmp/eg11"
    if [ -f "$i.pd" ]; then
       report pd "$i"
       report pf "$i"
    else
        crossval 5 5 "$data" $Seed $learners | grep $goal >"$i"
        gawk  '{print $2,$10}' "$i" > "$i.pd"
        gawk  '{print $2,$11}' "$i" > "$i.pf"
        eg11
   fi
}
```

The output of eg11
```
pd

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,       zeror1 ,       0  ,     0 (*              |              ), 0.00,  0.00,  0.00,  0.00,  0.00
   2 ,           nb ,      45  ,    18 (        ---   *| --           ),25.00, 36.00, 45.00, 53.00, 60.00
   2 ,       rbfnet ,      47  ,    20 (        ------ *   ---        ),25.00, 43.00, 47.00, 60.00, 67.00
   3 ,         bnet ,      60  ,    17 (             --|-- *  -       ),40.00, 55.00, 60.00, 67.00, 71.00
   3 ,         jrip ,      60  ,    23 (          -----|   *   ---    ),33.00, 50.00, 60.00, 71.00, 80.00
   4 ,          j48 ,      72  ,    16 (               |-----  *  --  ),50.00, 65.00, 72.00, 81.00, 87.00
pf

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,       zeror1 ,       0  ,     0 (*              |              ), 0.00,  0.00,  0.00,  0.00,  0.00
   2 ,          j48 ,       7  ,     6 (     --   *  --|---           ), 4.00,  5.00,  7.00,  9.00, 13.00
   2 ,           nb ,       7  ,     6 (     --   *   -|-             ), 4.00,  5.00,  7.00, 10.00, 12.00
   2 ,         jrip ,       9  ,    10 (  ---        * |------        ), 2.00,  4.00,  9.00, 11.00, 15.00
   2 ,       rbfnet ,       9  ,     5 (     -----   * |----          ), 4.00,  7.00,  9.00, 11.00, 14.00
   2 ,         bnet ,      11  ,     6 (        -----  |*   ------    ), 6.00,  9.00, 11.00, 14.00, 18.00
   ```

##Table Reader

Code can be found [here](https://github.com/gvivek19/fss16c/tree/master/code/2/tableReader)
To run the code, 
```
python table.py <dataset>
```

```
outlook
Mode : sunny    Entropy : 1.57740628285
temperature-
Mean : 73.5714285714    Standard Deviation : 6.57166745863
<humidity
Mean : 81.6428571429    Standard Deviation : 10.285218242
windy
Mode : FALSE    Entropy : 0.985228136034
>play
Mean : 1.07142857143    Standard Deviation : 0.997248963151
```
