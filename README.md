# Blockchain Database API
Thin Database Architecture based on Blockchain technology


Background
---------------------------------------------
When we talk about Blockchain, we always relate it to peer-to-peer network and think that data must be distributed across the network. It will raise concern from people and think that Blockchain would breach the confidentiality of the data.
Actually, the data architecture of Blockchain itself already provides a good solution for securing the data from unauthorized manipulation, given that the server is protected by sufficient controls, such as access control, network and system security control, and better to be in an internal network. 

Therefore, I try to build an database based on the data architecture of Blockchain by using Python, Sqlite and RESTful API framework.

Objective
---------------------------------------------
Accountability, Confidentially and Integrity
When  the user create a transaction record, he encrypts the data with its private key and post the data to Blockchain Database API. Blockchain Database API will decrypt the data with the user’s public key.  In this process, the user’s identity has been confirmed. It achieves the objective of accountability and confidentially.
In the next step, Blockchain Database API will calculate the hash value for the transaction with nonce, i.e. random string, and the previous hash. Blockchain Database API will insert the transaction, nonce and hash to the database. 
To detect any unauthorized change, Blockchain Database API will re-calculate the hash value based on the information of the previous hash, transaction and nonce. If any change is made, the hash value will change and the API can be notified. Therefore, the integrity of the data will be ensured. 

Limitation
---------------------------------------------
Since it is in a centralized architecture, there is a possibility for the attacker, who obtains the administration right, to change  the entire database by recalculating the hash value again. 
This can be safeguarded by the following solutions:
- Clone the transaction to a secured log server  
- Back up the data incrementally (line by line transaction) rather than full backup



License
----------------------------------------------
MIT License

Copyright (c) 2017 Adam K.C. Chin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
