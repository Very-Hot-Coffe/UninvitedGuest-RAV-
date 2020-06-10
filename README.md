# UninvitedGuest-RAV-
RAV - Remote access virus

## Protocol connection ##

### Philosofy
All packages  build to this structure:
1. 3 bytes - this request type , exemple (RTF) - read this file 
2. 10 bytes - size next part
3. to 9999999999 (10 sumbols) bytes or ~900 mb  - data from request

request exemple RTF0000000044C:\\config.txt 
