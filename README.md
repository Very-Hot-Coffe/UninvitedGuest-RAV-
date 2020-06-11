# UninvitedGuest-RAV
RAV - Remote access virus

### Linqs
* [Requests]:https://github.com/Very-Hot-Coffe/UninvitedGuest-RAV-#request-types
* [Answers](https://github.com/Very-Hot-Coffe/UninvitedGuest-RAV-#answer-types)

## Protocol connection ##

### Philosofy
All packages  build to this structure:
1. 3 bytes - this request type , exemple (RTF) - read this file 
2. 10 bytes - size next part
3. to 9999999999 (10 sumbols) bytes or ~900 mb  - data from request

request exemple RTF0000000044C:\\config.txt 

### Request types
1. RTF - read file text in file 
    data : C:\\Config.txt
2. WTF - Write text file
    data: C:\\Config.txt __\n__ blablabla

### Answer types
1. TXT - text (usually server answer return string)
    data : some text...
2. ERR - error
    data : Ooops
