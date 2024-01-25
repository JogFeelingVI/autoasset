/**
 * @Author: JogFeelingVI
 * @Date:   2024-01-25 20:54:21
 * @Last Modified by:   JogFeelingVI
 * @Last Modified time: 2024-01-25 21:35:36
 */
'use strict';
fetch('http://127.0.0.1:8080/handle')
.then(res => res.json())
.then(data => console.log(data))
console.log('hello is done')