/**
 * @Author: JogFeelingVI
 * @Date:   2024-01-25 20:54:21
 * @Last Modified by:   JogFeelingVI
 * @Last Modified time: 2024-01-31 11:06:43
 */

document.addEventListener("DOMContentLoaded", (event) => {
    console.log("DOM fully loaded and parsed");
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems, '');
});

window.onload = function () {
    const filterv3 = document.getElementById('filterv3');
    fetch('/filter_all_name')
        .then(res => res.json())
        .then(data => {
            let html = ''
            for (let i = 0; i < data.list.length; i++) {
                if (data.checked.indexOf(data.list[i]) != -1) {
                    html += `<label class="switch"><input type="checkbox" checked="checked"/><span>${data.list[i]}</span></label>`
                } else {
                    html += `<label class="switch"><input type="checkbox"/><span>${data.list[i]}</span></label>`
                }
            }
            filterv3.innerHTML = html
        })
};

function loadInsxRego() {
    const save = document.getElementById('insxrego')
    fetch('/load_insx_rego')
        .then(res => res.json())
        .then(data => {
            const save = document.getElementById('insxrego')
            save.value = data.insxd
            M.textareaAutoResize(save);
        })    
};

function saveInsxRego() {
    const save = document.getElementById('insxrego').value
    save_json = {"insxd": save}
    fetch('/save_insx_rego', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(save_json)
    })
        .then(res => res.json())
        .then(data => {
            console.log(data)
        })
};

function upgradeClicked() {
    fetch('/handle')
        .then(res => res.json())
        .then(data => {
            const formattedData = `${data.message}, ${data.time}.`;
            document.getElementById('upgrade').innerHTML = formattedData;
        })
};

function doneClicked() {
    const rego = document.getElementById('rego')
    const filterv3 = document.getElementById('filterv3');
    const labels = filterv3.getElementsByTagName('label');
    const onoff = rego.getElementsByTagName('input')[0]
    const checkboxStates = { 'rego': onoff.checked }
    for (let i = 0; i < labels.length; i++) {
        ckb = labels[i].getElementsByTagName('input')[0];
        span = labels[i].getElementsByTagName('span')[0];
        if (ckb.checked) {
            checkboxStates[span.innerHTML] = ckb.checked
        }
    }
    const json = JSON.stringify(checkboxStates);
    PostJson(json)
};

function PostJson(JSONA) {
    document.getElementById('navigation').innerHTML = `<p>json data has been sent waiting for server response.</p>`    
    fetch('/handle_post', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(JSONA)
    })
        .then(res => res.json())
        .then(data => {
            const jsdata = JSON.parse(data)
            let item = ''
            for (var it in jsdata) {
                let ix = jsdata[it]
                item += `<div class="message"><span class="red-text darken-3">${ix[0]}</span><span class="blue-text darken-4">${ix[1]}</span></div>`
            }
            document.getElementById('navigation').innerHTML = item;
        })
};


