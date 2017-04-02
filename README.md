# Keyboard_Recorder 
## English 英文
### This program allows you to  record keyboard input and the windows title when you have input. It save a .txt file on the target PC, and record all data. 
 The V1 is an un encryped version, using unencrypted text saving in an text file. 
#### UPDATE LOG -V1
 Add in the record of mouse event, keyboard event and mouse event in the same windows will be record together
 
 e.g.

---------
WindowName: Keyboard-Recorder/README.md at master · cyankw/Keyboard-Recorder - Mozilla Firefox 132440

Time:2017-04-02 22:42:23.001000 
        Click:mouse left up(921, 53)22:42:23
        
     Key:K-22:42:24  
     Key:E-22:42:24  
     Key:Y-22:42:25  
     Key:B-22:42:25  
     Key:O-22:42:25  
     Key:A-22:42:25  
     Key:R-22:42:26  
     Key:D-22:42:26  
     Key:Return-22:42:26  
---------
WindowName: keyboard_百度搜索 - Mozilla Firefox 132440

Time:2017-04-02 22:42:30.884000
        Click:mouse left up(921, 51)22:42:30
        
     Key:K-22:42:32  
     Key:Y-22:42:35  
     Key:B-22:42:35  
     Key:D-22:42:35  
     
        Click:mouse left up(921, 52)22:42:37
        Click:mouse left up(921, 52)22:42:38
        
     Key:R-22:42:39  
     Key:C-22:42:39  
     Key:D-22:42:40  
     Key:E-22:42:41  
     Key:R-22:42:41  
     
        Click:mouse left up(922, 51)22:42:42
        Click:mouse left up(922, 50)22:42:43


 The V2 is an encrypted one,which is THE FINAL WORK (Using base64 and url encode, with several other [.replace()] ) you can use the unencrypter.py to get it readable.
#### Analyzer.py in both path allows you to create an excel table with elected data for other future analyzes.
 However, support in Chinese isn't good enough, still working on it. Other function like sending the .txt file to mail box and delet the local record file, are still in developing. 
 
 ---
## 中文 Chinese
### 本程序可以用于进行键盘记录，并在键盘有输入的时候记录当前窗口的标题. 程序将在本地计算机上建立一个.txt文件并记录文档
 V1 是明文版本 将记录直接写入txt文档
#### UPDATE LOG -V1
 增添鼠标点击记录，同一个窗口下的键盘输入和鼠标点击将被记录在一起
 
e.g.

---------
WindowName: Keyboard-Recorder/README.md at master · cyankw/Keyboard-Recorder - Mozilla Firefox 132440

Time:2017-04-02 22:42:23.001000 
        Click:mouse left up(921, 53)22:42:23
        
     Key:K-22:42:24  
     Key:E-22:42:24  
     Key:Y-22:42:25  
     Key:B-22:42:25  
     Key:O-22:42:25  
     Key:A-22:42:25  
     Key:R-22:42:26  
     Key:D-22:42:26  
     Key:Return-22:42:26  
---------
WindowName: keyboard_百度搜索 - Mozilla Firefox 132440

Time:2017-04-02 22:42:30.884000
        Click:mouse left up(921, 51)22:42:30
        
     Key:K-22:42:32  
     Key:Y-22:42:35  
     Key:B-22:42:35  
     Key:D-22:42:35  
     
        Click:mouse left up(921, 52)22:42:37
        Click:mouse left up(921, 52)22:42:38
        
     Key:R-22:42:39  
     Key:C-22:42:39  
     Key:D-22:42:40  
     Key:E-22:42:41  
     Key:R-22:42:41  
     
        Click:mouse left up(922, 51)22:42:42
        Click:mouse left up(922, 50)22:42:43


 V2 是加密版本 使用base64 和 url 加密 （并使用多组.replace()替换部分字符串，防止直接被解码 ) 你可以使用encrypter.py进行解码
#### 两个目录中的Analyzer.py 可以生成相应版本的数据excel表格，方便后续的分析
 中文支持尚且不够完善，努力中。定期发送至邮箱并清理本地文件的功能也在开发中
