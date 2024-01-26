/**
 * @Author: JogFeelingVI
 * @Date:   2024-01-25 20:54:21
 * @Last Modified by:   JogFeelingVI
 * @Last Modified time: 2024-01-26 15:28:58
 */
'use strict';
console.log('hello is done')

fetch('/handle')
    .then(res => res.json())
    .then(data => console.log(data))

fetch('/handle_post', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        name: 'NLXY9291',
        lens: 50
    })
})
    .then(res => res.json())
    .then(data => {
        
        const formattedData = `<span class="lime-text lighten-5">${data.name}</span> was updated by <span class="lime-text lighten-3">${data.update}</span> lens <span>${data.lens}</spn>.`;
        document.getElementById('data').innerHTML = formattedData;
    })
