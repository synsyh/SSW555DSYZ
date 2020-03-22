**SSW555 Agile Methods For Software Development Group Project**  
**Group Members:**
- Danping Cai
- Siteng Fan
- Yuning Sun
- Zihao Kang  

Get individuals and families:  
  
`geddata.get_inds_fams(ged_file_path)  `

For example
```Python
import geddata

inds, fams = geddata.get_inds_fams('res/valid.ged')  
for ind in inds: 
    # print every individual's age
    print(ind['age'])
    # or
    print(ind['age'].value)
    # print age line in ged file
    print(ind['age'].line)
```
Data structure:  
>fams {list}
>>age {GEDAttribute}
>>>value {int or str}  
>>>line {int}
>
>birt {GEDAttribute}
>>>value {int or str}  
>>>line {int}
>>chil {list}
>
>chil {list}
>>0 {GEDAtribute}
>>>value {int or str}  
>>>line {int}


File description:  
>./res/:  
US26_1.ged: Individual has no corresponding family entry.  
US26_0.ged: Individual in family has no corresponding individual entry.  
US27.ged: Individual has no birthday information so that has no age information.  